# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''Exercício 6 — Índice e desempenho:
        Crie uma coleção com 1000 eventos gerados em laço, crie um índice no
        campo ip e demonstre uma consulta por IP. Explique em 2 linhas
        (comentário no código) por que o índice importa quando a coleção cresce.

        # Dica: gere eventos com um for e insert_many; use create_index("ip").
        # Consulte um IP específico e conte quantos eventos retornaram.

        # Saída esperada (exemplo):
        # 1000 eventos inseridos.
        # Índice criado em 'ip'.
        # Eventos do IP 185.220.101.1: 250
        # Comentário: sem índice a busca seria O(n) (varre tudo); com índice ~O(log n).
'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from pymongo import MongoClient
from datetime import datetime
from datetime import datetime, timedelta
import random

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Criando carga para coleção de eventos.
# Gerado por vibe coding, a partir de um loop simples enviado para a IA.
# Logica dos prompts em "miscelanea/duvidas.md".
# Função auxiliar para verificar se um número é primo

def eh_primo(n):
    if n < 2:
        return False
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            return False
    return True

# Nova função que encapsula todo o processo de geração de eventos
def geraEventos(quantidade=1000):
    '''
    funçao gera uma quantidade de eventos semi-aleatorios para aplicar na coleçã,
    os valores de alguns indices variam de acordo com a validação de "i".
    data e hora também são aleatorios. (Ao menos espero que sejam)
    '''
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
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

apagar = input("Quer remover coleções anteriores? [S]im/[N]ão ")

# configurando conexão
client = MongoClient("mongodb://localhost:27017/")
db = client["seguranca"]
eventos_db = db["eventos"]

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

eventos = geraEventos(1000)

# dicionando eventos á coleção
print("Inserindo novos eventos...")
try:
    eventos_db.insert_many(eventos)
    print("{} novos eventos catalogados.".format(eventos_db.count_documents({})))
except Exception as e:
    print("Falha na inserção: {}".format(e))

# Criando um index simples para IP.
print("Indexando...")
try:
    eventos_db.create_index("ip")
except Exception as e:
    print("Indexação falhou: {}".format(e))

# Verifica eventos, utilizando pipeline para contagem de eventos
print("Verificando quantidade de eventos do ip 185.220.101.1...")
try:
    pipeline = [
        {"$match": {"ip": "185.220.101.1"}},
        {"$group": {"_id": "$ip", "total":{"$sum": 1}}},
        ]
    for evento in eventos_db.aggregate(pipeline):
        print("eventos do IP {0[_id]}: {0[total]}".format(evento))
except Exception as e:
    print("Falha na contagem de eventos: {}".format(e))

'''
Uma consulta por index é mais rapida, pois direciona a busca para uma chave
especifica. Utilizazndo o exemplo do material, funciona como um indice de livro.
Sem o index, a busca em um banco muito grande pode ser demara, pos a aplicação
realiza uma vistoria linear em todos os dados da coleção.

NOTA: Estou verificando, por hora, uma maneira de mostrar que essa consulta
foi realizada por index, e não linearmente.
'''