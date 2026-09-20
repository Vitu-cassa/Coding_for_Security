eventos = [
            {"tipo": "FAIL", "ip": "185.220.101.1"}, {"tipo": "FAIL", "ip": "185.220.101.1"},
            {"tipo": "OK",   "ip": "192.168.1.10"},  {"tipo": "FAIL", "ip": "91.240.118.172"},
            {"tipo": "FAIL", "ip": "185.220.101.1"}, {"tipo": "FAIL", "ip": "91.240.118.172"},
            {"tipo": "FAIL", "ip": "45.33.32.156"},  {"tipo": "FAIL", "ip": "185.220.101.1"},
        ]
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''Exercício 3 — Agregação: Top IPs:
        Insira uma lista de eventos no MongoDB e use um aggregation pipeline 
        para retornar os 3 IPs com mais eventos do tipo FAIL, ordenados de 
        forma decrescente.

        eventos = [
            {"tipo": "FAIL", "ip": "185.220.101.1"}, {"tipo": "FAIL", "ip": "185.220.101.1"},
            {"tipo": "OK",   "ip": "192.168.1.10"},  {"tipo": "FAIL", "ip": "91.240.118.172"},
            {"tipo": "FAIL", "ip": "185.220.101.1"}, {"tipo": "FAIL", "ip": "91.240.118.172"},
            {"tipo": "FAIL", "ip": "45.33.32.156"},  {"tipo": "FAIL", "ip": "185.220.101.1"},
        ]

        # Dica: pipeline = [{"$match":{"tipo":"FAIL"}}, {"$group":{"_id":"$ip","total":{"$sum":1}}},
        #                   {"$sort":{"total":-1}}, {"$limit":3}]

        # Saída esperada:
        # 185.220.101.1 -> 4
        # 91.240.118.172 -> 2
        # 45.33.32.156  -> 1

'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import pymongo
from pymongo import MongoClient
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

# configurando conexão
client = MongoClient("mongodb://localhost:27017/")
db = client["seguranca"]
eventosDb = db["eventos"]

print(client.admin.command("ping"))
print("Conectado ao Mongo!")

# Realiza a inserção dos evnetos (lista do exercicio)
# Serão inseridas toda vez que o teste é executado.
print("Inserindo novos eventos...")
try:
    eventosDb.insert_many(eventos)
    print("Visualisando eventos:")

    for event in eventosDb.find({}):
        print("IP: {0[ip]:<16} | tipo: {0[tipo]}".format(event))
except Exception as e:
    print("Falha na inserção: {}".format(e))

# Realizando o pipeline
print("Ordenando pipeline...")
try:
    pipeline = [
        {"$match": {"tipo": "FAIL"}},
        {"$group": {"_id": "$ip", "total": {"$sum":1}}},
        {"$sort": {"total": -1}}, 
        {"$limit": 3}
    ]
    print("Top 3 IPs com mais falhas registradas:")
    for evento in eventosDb.aggregate(pipeline):
        print("{0[_id]:<16} -> {0[total]} falhas".format(evento))

except Exception as e:
    print("Erro ao rankear os IPs: {}".format(e))
