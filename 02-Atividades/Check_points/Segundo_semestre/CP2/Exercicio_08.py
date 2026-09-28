from flask import Flask, request, jsonify
from pymongo import MongoClient
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix
import random
from datetime import datetime
import time

app = Flask(__name__)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 8 — Modelo de ML servido por API, com métricas auditáveis:
        Treine um classificador de risco e exponha-o. A entrada do modelo precisa 
        ser rigorosamente validada antes de ser processada. Toda previsão é gravada 
        no MongoDB para auditoria futura.
'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Variáveis Globais de Estado (Memória do Servidor)
modelo_ml = None
metricas_globais = {}
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def _conectar_mongo():
    ''' Retorna a conexão com o banco de dados de auditoria NoSQL. '''
    client = MongoClient("mongodb://localhost:27017/")
    return client["seguranca"]

def _forjar_modelo_e_metricas():
    '''
    Gera dados sintéticos, treina uma Random Forest em memória e 
    calcula as métricas contra a base de teste antes de liberar a API.
    '''
    global modelo_ml, metricas_globais
    
    print("Gerando dataset sintético de SOC...")
    X, y = [], []
    
    # Gerando eventos "Baixo Risco" (Classe 0)
    # [falhas_login, portas_distintas, bytes_saida, hora_do_dia]
    for _ in range(800):
        X.append([random.randint(0, 2), random.randint(1, 3), random.randint(100, 5000), random.randint(8, 18)])
        y.append(0)
        
    # Gerando eventos "Alto Risco / Ataque" (Classe 1)
    for _ in range(200):
        X.append([random.randint(5, 15), random.randint(5, 20), random.randint(50000, 200000), random.randint(0, 5)])
        y.append(1)
        
    X = np.array(X)
    y = np.array(y)
    
    print("Separando treino/teste e forjando a Floresta Aleatória...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    modelo = RandomForestClassifier(n_estimators=50, random_state=42)
    modelo.fit(X_train, y_train)
    
    print("Aferindo métricas do modelo...")
    y_pred = modelo.predict(X_test)
    
    # A Mágica das Métricas - Transformamos para tipos nativos do Python (.item(), .tolist()) para o JSON aceitar
    metricas_globais = {
        "precisao": round(precision_score(y_test, y_pred).item(), 4),
        "recall": round(recall_score(y_test, y_pred).item(), 4),
        "f1": round(f1_score(y_test, y_pred).item(), 4),
        "matriz": confusion_matrix(y_test, y_pred).tolist(),
        "aviso": (
            "A acurácia (accuracy) foi omitida de propósito. Em cibersegurança, datasets são "
            "altamente desbalanceados (ex: 99% de tráfego bom). Um modelo inútil que classifique "
            "tudo como 'seguro' teria 99% de acurácia, mas pegaria 0 ataques. Focamos em Precisão e Recall."
        )
    }
    
    modelo_ml = modelo

def _validar_features(payload):
    '''
    A Sentinela de Entrada. Impede que lixo ou ataques matemáticos 
    derrubem o motor de inferência.
    '''
    if not payload or 'features' not in payload:
        return None, "corpo da requisição vazio ou sem a chave 'features'"
        
    features = payload['features']
    
    if not isinstance(features, list):
        return None, "features deve ser uma lista (array)"
        
    if len(features) != 4:
        return None, "esperadas 4 features, recebidas {}".format(len(features))
        
    for f in features:
        if not isinstance(f, (int, float)) or isinstance(f, bool):
            return None, "features devem ser estritamente numéricas"
            
    return features, None

def _auditar_previsao(features, risco, confianca):
    ''' Salva o racional da decisão no MongoDB (A08 / A09). '''
    try:
        db = _conectar_mongo()
        colecao = db["previsoes"]
        
        registro = {
            "entrada_features": features,
            "saida_risco": risco,
            "confianca": confianca,
            "criado_em": datetime.now()
        }
        
        colecao.insert_one(registro)
    except Exception as e:
        # Em um SOC real, falha de log gera alerta. Aqui apenas imprimimos.
        print("Falha na auditoria MongoDB: {}".format(e))

# -----------------------------------------------------------------------------
# ROTAS DA API
# -----------------------------------------------------------------------------

@app.route('/api/triagem', methods=['POST'])
def _classificar_evento():
    try:
        payload = request.get_json(silent=True)
    except Exception:
        payload = None

    features_seguras, erro = _validar_features(payload)
    
    if erro:
        return jsonify({"erro": erro}), 400
        
    try:
        # Prepara a entrada no formato que o scikit-learn espera (Array 2D)
        X_inferencia = np.array([features_seguras])
        
        # O modelo cospe 0 (baixo) ou 1 (alto)
        previsao_bruta = modelo_ml.predict(X_inferencia)[0]
        risco = "alto" if previsao_bruta == 1 else "baixo"
        
        # Captura o grau de confiança da árvore de decisão
        probabilidades = modelo_ml.predict_proba(X_inferencia)[0]
        confianca = round(probabilidades[previsao_bruta].item(), 4)
        
        # Auditoria (Log) da decisão
        _auditar_previsao(features_seguras, risco, confianca)
        
        return jsonify({"risco": risco, "confianca": confianca}), 200
        
    except Exception as e:
        return jsonify({"erro_interno": "Falha na inferência: {}".format(e)}), 500


@app.route('/api/modelo/metricas', methods=['GET'])
def _exibir_metricas():
    return jsonify(metricas_globais), 200


if __name__ == '__main__':
    print("Iniciando Forja de Inteligência Artificial...")
    time.sleep(1)
    
    # Treina o modelo antes de subir a guarita
    _forjar_modelo_e_metricas()
    
    # Limpa o banco de auditoria antigo para os testes atuais
    try:
        db = _conectar_mongo()
        db["previsoes"].drop()
        print("Coleção de previsões limpa no MongoDB.")
    except Exception as e:
        print("Aviso: Falha ao limpar o Mongo - {}".format(e))
        
    time.sleep(1)
    print("Guarita MLOps rodando na porta 5000!")
    
    try:
        app.run(port=5000, debug=True)
    except Exception as e:
        print("Falha severa ao iniciar o servidor: {}".format(e))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
RESPOSTA TEÓRICA (Entregável do Exercício):
Para testar, instale o scikit-learn (pip install scikit-learn).
Rode o script e teste os payloads da matriz no terminal via curl (ou no VS Code Thunder Client).

O aviso na rota de métricas evidencia o erro mais amador de Data Science na área 
de Segurança: olhar para o número errado. O modelo gravar no banco a `entrada_features` 
junto com a `confianca` nos permite fazer auditoria de "Data Drift": se os ataques 
mudarem e o modelo começar a dar confiança de "0.51", nós saberemos lendo o banco 
que o modelo ficou obsoleto e precisa de retreinamento.
'''