
def _parseador():
    # Substitua 'seus_logs.txt' pelo caminho real do arquivo no seu diretório
    caminho_arquivo = "auth.log"
    logs_normalizados = []

    print("Iniciando a normalização do arquivo...")

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha_limpa = linha.strip()
                
                # Ignora linhas vazias acidentais
                if not linha_limpa:
                    continue
                
                # 1. Primeira quebra por espaços em branco
                # Resultado esperado: ['2025-02-20', '08:15:01', 'FAIL', 'usuario=admin', 'ip=185.220.101.1']
                partes = linha_limpa.split()
                
                if len(partes) == 5:
                    # Junta a data e a hora em uma única string
                    data_str = f"{partes[0]} {partes[1]}"
                    tipo = partes[2].upper()  # Garante caixa alta para o tipo (FAIL/OK)
                    
                    # 2. Segunda quebra usando .split("=") para isolar os valores brutos
                    usuario = partes[3].split("=")[1].lower()  # Pega o valor e força minúsculo
                    ip = partes[4].split("=")[1].strip()       # Pega o IP limpo
                    
                    # 3. Monta o dicionário estruturado e normalizado
                    log_dicionario = {
                        "data": datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S"),
                        "tipo": tipo,
                        "usuario": usuario,
                        "ip": ip
                    }
                    
                    logs_normalizados.append(log_dicionario)
                    
        print(f"Sucesso! {len(logs_normalizados)} linhas foram normalizadas e estruturadas.")
        
        # # Exibe os 3 primeiros apenas para validação visual
        # print("\n--- Amostra dos Dados Normalizados ---")
        # for log in logs_normalizados[:3]:
        #     print(log)
        return logs_normalizados
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro no pipeline: {e}")


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''Exercício 10 (Desafio) — Mini-pipeline SIEM:
        log → MongoDB → ML: Integre tudo.
        (1) Leia o auth.log (formato da GS do 1º semestre) e normalize
        cada linha em umdocumento.
        (2) Insira todos no MongoDB.
        (3) Para cada IP, calcule via agregação a contagem de FAILs.
        (4) Monte um dataset simples [qtd_fails] e rotule IP como suspeito
        (1) se ≥ 5 falhas, senão 0.
        (5) Treine um classificador e preveja o rótulo de um IP novo com 8 falhas.

        # auth.log (23 linhas, formato: TIMESTAMP TIPO usuario=NOME ip=IP)
        # 2025-02-20 08:15:01 FAIL usuario=admin ip=185.220.101.1
        # ... (use o arquivo da GS)

        # Contagem esperada (agregação):
        # 185.220.101.1 -> 10 FAILs (suspeito=1)
        # 91.240.118.172 -> 5 FAILs (suspeito=1)
        # 45.33.32.156  -> 3 FAILs (suspeito=0)

        # Saída esperada:
        # Eventos inseridos no MongoDB: 23
        # Dataset de treino: [[10],[5],[3], ...] rótulos [1,1,0, ...]
        # Previsão para IP com 8 falhas -> Suspeito (1)
'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from datetime import datetime
from pymongo import MongoClient
from datetime import datetime, timezone
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

apagar = input("Quer remover coleções anteriores? [S]im/[N]ão ")

# configurando conexão
client = MongoClient("mongodb://localhost:27017/")
db = client["seguranca"]
logs_db = db["logs"]

print(client.admin.command("ping"))
print("Conectado ao Mongo!")

if apagar == "S":
    # Limpando coleções antigas no banco
    print("Limpando todas as coleções antigas...")
    try:
        # Busca a lista com o nome de todas as coleções ativas no banco
        for nome_colecao in db.list_collection_names():
            # Exclui a coleção inteira
            db[nome_colecao].drop()
            print(f"Coleção '{nome_colecao}' removida com sucesso.")
            
        print("Banco de dados resetado com sucesso!")

    except Exception as e:
        print(f"Erro ao limpar o banco: {e}")

novos_logs = _parseador()

# Adicionando eventos á coleção
print("Inserindo novos eventos...")
try:
    logs_db.insert_many(novos_logs)
    print("{} novos logs catalogados.".format(logs_db.count_documents({})))
except Exception as e:
    print("Falha na inserção: {}".format(e))

# Criando um index simples para IP.
print("Indexando...")
try:
    logs_db.create_index("ip")
except Exception as e:
    print("Indexação falhou: {}".format(e))

# Verifica eventos, utilizando pipeline para contagem de eventos
print("Verificando quantidade de eventos e organizando por IP...")
try:
    dataset_treino = []
    rotulo = []

    pipeline = [
        {"$match": {"tipo": "FAIL"}},
        {"$group": {"_id": "$ip", "total": {"$sum":1}}},
        {"$sort": {"total": -1}}
    ]
    for evento in logs_db.aggregate(pipeline):
        print("eventos do IP {0[_id]}: {0[total]}".format(evento))
        rotulo.append(1 if evento["total"] >=5 else 0)
        dataset_treino.append(evento["total"])

except Exception as e:
    print("Falha na contagem de eventos: {}".format(e))

print("Preparando o aprentizado de maquina...")
try:
    # preparando o modelo de machine learning
    # formatando os dados
    x = np.array(dataset_treino)
    y = np.array(rotulo)

    # divisões de treino
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=42)

    # importantdo modelo e passando parametros de treino
    avaliador = RandomForestClassifier(n_estimators=100, random_state=42)
    avaliador.fit(x_train, y_train)

    # Previsoes
    # previsoes = avaliador.predict(x_test)
    # print("\nAcurácia: {:.2f}".format(accuracy_score(y_test, previsoes)))
    # print("{}".format(classification_report(y_test, previsoes)))

except Exception as e:
    print("Modelo falhou: {}".format(e))
