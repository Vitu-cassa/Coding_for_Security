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
        "cve_id": "CVE-2026-CP1", "tipo": "teste", 
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
    for vuln in vulnerabilidades.find({"severidade": "critica"}):
        print(vuln)
except Exception as e:
    print("Falha na consulta multipla: {}".format(e))

# Realiza a inserção de varias vulnerabilidades (lista do exercicio)
# Serão inseridas toda vez que o teste é executado.
print("Inserindo novas vulnerabilidades...")
try:
    vulnerabilidades.insert_many(vulns)
except Exception as e:
    print("Falha na inserção: {}".format(e))

# Realiza consulta das vulnerabilidades da lista
print("Consultando vulnerabilidades do exercicio...")
try:
    for vuln in vulnerabilidades.find({"cve_id": {"$regex": "CVE-2024-*"}}):
        print(vuln)
except Exception as e:
    print("Falha na consulta completa: {}".format(e))

# Realização do Update do banco (Update da CVE de teste)
print("Realizando update...")
try:
    vulnerabilidades.update_many({"tipo": "Teste"}, {"$set": {"corrigida": True}})
    vulnerabilidades.update_one({"cve_id": "CVE-2024-001"},{"$set": {"corrigida": True}})
    for vuln in vulnerabilidades.find({}):
            print("CVE {0[cve_id]} está: {1}".format(vuln, "Corrigida" if vuln.get("corrigida") else "Pendente"))
except Exception as e:
    print("Atualização não ralizada: {}".format(e))


# Removendo "teste" da coleção
print("Removendo vulnerabilidade de teste...")
try:
    vulnerabilidades.delete_many({"tipo": "Teste" })
    for vuln in vulnerabilidades.find({}):
        print("ID: {0[cve_id]} tipo: {0[tipo]}".format(vuln))
except Exception as e:
    print("Vulnerabilidade não removida: {}".format(e))
