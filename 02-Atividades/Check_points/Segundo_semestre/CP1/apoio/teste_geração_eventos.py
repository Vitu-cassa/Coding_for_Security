# from datetime import datetime
# import random

# def gerar_data_aleatoria():
#     dia = random.randint(10, 28)
#     hora = random.randint(0, 23)
#     minuto = random.randint(0, 59)
#     segundo = random.randint(0, 59)
#     return datetime(2025, 2, dia, hora, minute=minuto, second=segundo)

# MULTIPLICADOR = 3  # Exemplo: vai gerar 69 logs no total (23 * 3)

# base_logs = [
#     {"tipo": "FAIL", "usuario": "admin", "ip": "185.220.101.1"},
#     {"tipo": "FAIL", "usuario": "root", "ip": "185.220.101.1"},
#     {"tipo": "OK",   "usuario": "carlos", "ip": "192.168.1.10"},
#     {"tipo": "FAIL", "usuario": "admin", "ip": "91.240.118.172"},
#     {"tipo": "FAIL", "usuario": "test", "ip": "185.220.101.1"},
#     {"tipo": "FAIL", "usuario": "admin", "ip": "185.220.101.1"},
#     {"tipo": "OK",   "usuario": "ana", "ip": "192.168.1.45"},
#     {"tipo": "FAIL", "usuario": "root", "ip": "91.240.118.172"},
#     {"tipo": "FAIL", "usuario": "admin", "ip": "45.33.32.156"},
#     {"tipo": "FAIL", "usuario": "admin", "ip": "185.220.101.1"},
#     {"tipo": "FAIL", "usuario": "root", "ip": "185.220.101.1"},
#     {"tipo": "FAIL", "usuario": "guest", "ip": "91.240.118.172"},
#     {"tipo": "FAIL", "usuario": "admin", "ip": "185.220.101.1"},
#     {"tipo": "OK",   "usuario": "bruno", "ip": "10.0.0.5"},
#     {"tipo": "FAIL", "usuario": "sa", "ip": "185.220.101.1"},
#     {"tipo": "FAIL", "usuario": "admin", "ip": "91.240.118.172"},
#     {"tipo": "FAIL", "usuario": "root", "ip": "185.220.101.1"},
#     {"tipo": "FAIL", "usuario": "test", "ip": "45.33.32.156"},
#     {"tipo": "FAIL", "usuario": "admin", "ip": "185.220.101.1"},
#     {"tipo": "FAIL", "usuario": "root", "ip": "185.220.101.1"},
#     {"tipo": "OK",   "usuario": "diana", "ip": "192.168.1.20"},
#     {"tipo": "FAIL", "usuario": "admin", "ip": "91.240.118.172"},
#     {"tipo": "FAIL", "usuario": "oracle", "ip": "45.33.32.156"}
# ]

# # Dicionário final que receberá os dados
# dicionario_eventos = {}
# contador_id = 100

# # O LOOP FOR que gera, multiplica e preenche o dicionário
# for _ in range(MULTIPLICADOR):
#     for log in base_logs:
#         # Cria a linha com os dados estruturados e a data aleatória
#         linha_evento = {
#             "data": gerar_data_aleatoria(),
#             "tipo": log["tipo"],
#             "usuario": log["usuario"],
#             "ip": log["ip"]
#         }
        
#         # Preenche o dicionário mapeando o ID sequencial para o evento gerado
#         dicionario_eventos[contador_id] = linha_evento
#         contador_id += 1

# # --- Teste de Visualização ---
# print(f"Total de chaves geradas no dicionário: {len(dicionario_eventos)}")
# print("\nExemplo das duas primeiras chaves preenchidas:")
# print(f"Chave 1: {dicionario_eventos[1]}")
# print(f"Chave 2: {dicionario_eventos[2]}")

ips = [
    "185.220.101.1",
    "91.240.118.172",
    "45.33.32.156",
    "192.168.1.10"
]


# # Gera 1000 eventos
# eventos = []

# for i in range(1000):
#     evento = {
#         "id_evento": i + 1,
#         "ip": ips[i % 4],
# "tipo": ("ACESSO" if i % 2 == 0 elif "CONSULTA")
#     }

#     eventos.append(evento)

# # print(eventos)

# from datetime import datetime, timedelta
# import random

# ips = ["185.220.101.1", "91.240.118.172", "45.33.32.156", "192.168.1.10"]
# eventos = []

# # Ponto de partida para a geração das datas (Ex: Agora)
# data_base = datetime.now()

# for i in range(1000):
#     # Gera uma variação aleatória de minutos e segundos para os logs não ficarem iguais
#     minutos_aleatorios = random.randint(1, 10000)
#     segundos_aleatorios = random.randint(0, 59)
#     data_evento = data_base - timedelta(minutes=minutos_aleatorios, seconds=segundos_aleatorios)

#     evento = {
#         "id_evento": i + 1,
#         "ip": ips[i % 4],
#         "tipo": "ACESSO" if i % 2 == 0 else "CONSULTA",
#         # Adicionando o índice com o objeto de data formatado
#         "atualizado_em": data_evento
#     }
#     eventos.append(evento)

# # Visualizando um exemplo do resultado
# print("Exemplo do primeiro evento gerado:")
# print(eventos)

from datetime import datetime, timedelta
import random

# Função auxiliar para verificar se um número é primo
def eh_primo(n):
    if n < 2:
        return False
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            return False
    return True

# Nova função que encapsula todo o processo de geração
def geraEventos(quantidade=1000):
    ips = ["185.220.101.1", "91.240.118.172", "45.33.32.156", "192.168.1.10"]
    eventos_gerados = []
    data_base = datetime.now()

    for i in range(quantidade):
        # Lógica da data aleatória
        minutos_aleatorios = random.randint(1, 10000)
        segundos_aleatorios = random.randint(0, 59)
        data_evento = data_base - timedelta(minutes=minutos_aleatorios, seconds=segundos_aleatorios)

        # Determina o Tipo (Verifica primo primeiro)
        if eh_primo(i):
            tipo_evento = "SUSPEITO"
        else:
            tipo_evento = "ACESSO" if i % 2 == 0 else "CONSULTA"

        # Monta o dicionário do evento
        evento = {
            "id_evento": i + 1,
            "ip": ips[i % 4],
            "tipo": tipo_evento,
            "status": "OK" if i % 2 == 0 else "NOK",
            "atualizado_em": data_evento
        }
        eventos_gerados.append(evento)
        
    return eventos_gerados

# --- Exemplo de como usar a função na sua aplicação ---
# Chama a função para gerar os 1000 registros
meus_eventos = geraEventos(1000)

print(f"Sucesso! Gerados {len(meus_eventos)} eventos.")
print("Primeiro evento:", meus_eventos[0])
