vulns = [
            {"cve_id": "CVE-2024-001", "tipo": "SQL Injection", "severidade": "Alta",  "corrigida": False},
            {"cve_id": "CVE-2024-002", "tipo": "XSS",           "severidade": "Media", "corrigida": True},
            {"cve_id": "CVE-2024-003", "tipo": "Path Traversal","severidade": "Critica","corrigida": False},
        ]
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''Exercício 2 — CRUD com PyMongo: 
        Conecte ao MongoDB e implemente as quatro operações sobre uma coleção 
        vulnerabilidades. Insira, busque por severidade, atualize corrigida 
        para True e delete por cve_id.

        vulns = [
            {"cve_id": "CVE-2024-001", "tipo": "SQL Injection", "severidade": "Alta",  "corrigida": False},
            {"cve_id": "CVE-2024-002", "tipo": "XSS",           "severidade": "Media", "corrigida": True},
            {"cve_id": "CVE-2024-003", "tipo": "Path Traversal","severidade": "Critica","corrigida": False},
        ]

        # Saída esperada:
        # Buscar severidade='Alta'      -> CVE-2024-001: SQL Injection
        # update corrigida=True em 001  -> "1 documento modificado"
        # count corrigida=False         -> 1 (só a CVE-2024-003 restou aberta)

'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from pymongo import MongoClient
from pymongo.errors import PyMongoError # Tentei usar isso mas não gostei
from datetime import datetime, timezone
from datetime import date
from zoneinfo import ZoneInfo

agora = datetime.now(ZoneInfo("America/sao_paulo")) # Tentativa de colocar uma data

# configurando conexão
client = MongoClient("mongodb://localhost:27017/")
db = client["seguranca"]
vulnerabilidades = db["vulnerabilidades"]

print(client.admin.command("ping"))
print("Conectado ao Mongo!")

# Insere uma vuln de teste (será inserida uma nova toda vez que o teste for executado)
print("Inserindo uma vulnerabilidade...")
try:
    vulnerabilidade = {
        "cve_id": "CVE-2026-CP1", "tipo": "Teste", 
        "severidade": "critica",  "corrigida": False, "timestamp": datetime.now(timezone.utc)
    }

    res = vulnerabilidades.insert_one(vulnerabilidade)
    print(res.inserted_id)
except Exception as e:
    print("Falha na atualização da coleção: {}".format(e))

# Realiza leitura de um item da coleção
print("Consultando Vulnerabilidade...")
try:
    vuln = vulnerabilidades.find_one({"severidade": "critica"})
    print(vuln)
except Exception as e:
    print("Falha na consulta unitária: {}".format(e))

# Realiza a consulta de toda a coleção
print("Consultando mais de uma vulnerabilidade cadastradas...")
try:
    for vulns in vulnerabilidades.find({"severidade": "critica"}):
        print(vulns)
except Exception as e:
    print("Falha na consulta completa: {}".format(e))

# Realiza a inserção de varias vulnerabilidades (lista do exercicio)