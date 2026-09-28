from flask import Flask, request, jsonify, g
from pymongo import MongoClient
import numpy as np
from sklearn.ensemble import IsolationForest
from datetime import datetime, timedelta
import time
import math

app = Flask(__name__)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 9 — Rate limiting guiado por anomalia (Aulas 2, 4, 6 e 8/A09):
        A própria API vira fonte de dados: registre cada requisição no MongoDB, 
        extraia o comportamento de cada IP e use IsolationForest para bloquear anomalias.
'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Memória volátil da API para bloqueio rápido
ips_bloqueados = set()
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def _conectar_mongo():
    ''' Retorna a conexão com o MongoDB. '''
    client = MongoClient("mongodb://localhost:27017/")
    return client["seguranca"]

# -----------------------------------------------------------------------------
# OS HOOKS DA API (A Geração de Dados)
# -----------------------------------------------------------------------------

@app.before_request
def _registrar_entrada():
    '''
    Interceptor de Entrada.
    Verifica a lista de bloqueios (Rate Limit) e inicia o registro de auditoria.
    '''
    ip = request.remote_addr
    
    # 5. IP anômalo recebe 429 nas próximas requisições
    if ip in ips_bloqueados:
        resposta = jsonify({"erro": "muitas requisições"})
        resposta.status_code = 429
        resposta.headers['Retry-After'] = '60'
        return resposta

    try:
        db = _conectar_mongo()
        # Gravando {ip, rota, metodo, timestamp}
        registro = {
            "ip": ip,
            "rota": request.path,
            "metodo": request.method,
            # No laboratório real usaríamos datetime.now(), mas permitimos 
            # que a simulação sobrescreva o tempo para o teste funcionar.
            "timestamp": request.environ.get('SIMULACAO_TIMESTAMP', datetime.now())
        }
        
        resultado = db["acessos"].insert_one(registro)
        # Salva o ID do MongoDB no contexto global da requisição (Flask 'g')
        g.log_id = resultado.inserted_id
        
    except Exception as e:
        print("Falha na auditoria de entrada: {}".format(e))


@app.after_request
def _registrar_saida(resposta):
    '''
    Interceptor de Saída.
    Recupera o ID do log salvo na entrada e injeta o status code da resposta.
    '''
    if hasattr(g, 'log_id'):
        try:
            db = _conectar_mongo()
            db["acessos"].update_one(
                {"_id": g.log_id},
                {"$set": {"status_code": resposta.status_code}}
            )
        except Exception as e:
            print("Falha na auditoria de saída: {}".format(e))
            
    return resposta

# -----------------------------------------------------------------------------
# ROTAS DE TESTE
# -----------------------------------------------------------------------------

@app.route('/api/dados', methods=['GET'])
def _rota_valida():
    return jsonify({"dados": "acesso concedido"}), 200

# -----------------------------------------------------------------------------
# O CÉREBRO: Detecção de Anomalias (Machine Learning)
# -----------------------------------------------------------------------------

def _analisar_acessos():
    '''
    Extrai comportamento por IP, cria as features e treina a Floresta de Isolamento.
    Atualiza a lista negra em tempo real.
    '''
    try:
        db = _conectar_mongo()
        
        # 3. Agregação no MongoDB -> features por IP
        pipeline = [
            {"$group": {
                "_id": "$ip",
                "total_reqs": {"$sum": 1},
                "primeiro_acesso": {"$min": "$timestamp"},
                "ultimo_acesso": {"$max": "$timestamp"},
                "erros_4xx": {
                    "$sum": {"$cond": [{"$and": [{"$gte": ["$status_code", 400]}, {"$lt": ["$status_code", 500]}]}, 1, 0]}
                },
                "rotas_unicas": {"$addToSet": "$rota"}
            }}
        ]
        
        resultados = list(db["acessos"].aggregate(pipeline))
        
        if len(resultados) < 2:
            print("Dados insuficientes para rodar Isolation Forest.")
            return

        features = []
        estatisticas = []

        for r in resultados:
            ip = r["_id"]
            total = r["total_reqs"]
            
            # Calcula a janela de tempo em minutos (mínimo de 1/60 minuto para evitar divisão por zero)
            delta_tempo = r["ultimo_acesso"] - r["primeiro_acesso"]
            minutos = delta_tempo.total_seconds() / 60.0
            if minutos <= 0: minutos = 1.0 / 60.0
            
            # Montagem das Features Matemáticas
            req_por_minuto = total / minutos
            taxa_4xx = r["erros_4xx"] / total
            rotas_distintas = len(r["rotas_unicas"])
            
            features.append([req_por_minuto, taxa_4xx, rotas_distintas])
            estatisticas.append({
                "ip": ip, 
                "rpm": req_por_minuto, 
                "taxa_4xx": taxa_4xx, 
                "rotas": rotas_distintas
            })

        # 4. Treinamento do IsolationForest
        X = np.array(features)
        modelo = IsolationForest(contamination=0.2, random_state=42)
        previsoes = modelo.fit_predict(X)

        print("\n# === Análise de acessos ===")
        ips_bloqueados.clear()

        # -1 significa Anomalia, 1 significa Normal
        for i, pred in enumerate(previsoes):
            est = estatisticas[i]
            ip_alvo = est["ip"]
            
            if pred == -1:
                status = "ANOMALIA -> bloqueado"
                ips_bloqueados.add(ip_alvo)
            else:
                status = "normal"
                
            print("# {:<15} [ {:>5.1f} req/min | 4xx {:.2f} | {} rotas]  -> {}".format(
                ip_alvo, est["rpm"], est["taxa_4xx"], est["rotas"], status
            ))
            
    except Exception as e:
        print("Falha na análise de Machine Learning: {}".format(e))

# -----------------------------------------------------------------------------
# MOTOR DE SIMULAÇÃO (Para gerar a saída exigida pelo laboratório)
# -----------------------------------------------------------------------------

def _simular_trafego_de_teste():
    ''' Roda internamente um script de requisições disparando contra a própria API. '''
    print("\nLimpando MongoDB para nova simulação...")
    db = _conectar_mongo()
    db["acessos"].drop()
    
    cliente = app.test_client()
    tempo_base = datetime.now()
    
    print("Simulando IP normal: 5 requisições espaçadas (192.168.1.10)")
    for i in range(5):
        # Espaçadas em 2 minutos cada
        tempo_fake = tempo_base + timedelta(minutes=(i*2))
        cliente.get('/api/dados', environ_base={'REMOTE_ADDR': '192.168.1.10', 'SIMULACAO_TIMESTAMP': tempo_fake})
        
    print("Simulando IP hostil: 60 requisições em 10s, 40 invalidas (185.220.101.1)")
    for i in range(60):
        # 60 requisições disparadas na mesma janela de 10 segundos
        tempo_fake = tempo_base + timedelta(seconds=(i % 10))
        rota = '/api/dados' if i < 20 else '/api/inexistente_{}'.format(i)
        cliente.get(rota, environ_base={'REMOTE_ADDR': '185.220.101.1', 'SIMULACAO_TIMESTAMP': tempo_fake})

    # Aciona o modelo para classificar os dados recém-inseridos
    _analisar_acessos()
    
    print("\nTestando o bloqueio 429 na prática:")
    resposta_bloqueio = cliente.get('/api/dados', environ_base={'REMOTE_ADDR': '185.220.101.1'})
    print("# Próxima requisição de 185.220.101.1 -> {} {}".format(resposta_bloqueio.status_code, resposta_bloqueio.get_json()))
    print("#                                        Retry-After: {}".format(resposta_bloqueio.headers.get('Retry-After')))


if __name__ == '__main__':
    # Roda a simulação antes de prender o terminal com o servidor Flask
    _simular_trafego_de_teste()
    
    print("\nGuarita Inteligente armada na porta 5000!")
    try:
        app.run(port=5000, debug=True)
    except Exception as e:
        print("Falha severa ao iniciar o servidor: {}".format(e))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
RESPOSTA TEÓRICA (Entregável do Exercício):
Comentário: Qual é o risco de bloquear por anomalia em vez de regra fixa?

R: Modelos de ML são matemáticos, não têm contexto de negócio. Um pico legítimo de tráfego 
(ex: script da equipe de marketing, ou uma promoção sazonal que gera muito acesso em rotas novas) 
mudará bruscamente a distribuição estatística. O modelo considerará a operação legítima como uma 
anomalia e bloqueará usuários reais (Falso Positivo gerando negação de serviço autoinfligida).
'''