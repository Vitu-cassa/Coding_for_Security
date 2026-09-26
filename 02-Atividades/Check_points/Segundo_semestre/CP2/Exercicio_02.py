
ativos  = [(1,"SRV-WEB01","192.168.1.10","alta"), (2,"PC-RH03","192.168.1.45","baixa")]
alertas = [(1,1,"BRUTE_FORCE","critica"), (2,1,"PORT_SCAN","alta"), (3,2,"XSS","media")]

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 2 — Migração relacional → documentos (Aulas 1, 2 e 3):
        O cadastro está normalizado em MySQL (ativos 1—N alertas). Migre para o
        MongoDB no modelo de documentos, aninhando os dados do ativo dentro de
        cada alerta, e prove que nada se perdeu no caminho.

        # MySQL (crie e popule):
        # ativos(id PK, nome, ip UNIQUE, criticidade ENUM('baixa','media','alta'))
        # alertas(id PK, ativo_id FK, tipo, severidade, criado_em)

        ativos  = [(1,"SRV-WEB01","192.168.1.10","alta"), (2,"PC-RH03","192.168.1.45","baixa")]
        alertas = [(1,1,"BRUTE_FORCE","critica"), (2,1,"PORT_SCAN","alta"), (3,2,"XSS","media")]

        # 1. Leia com um JOIN parametrizado.
        # 2. Monte documentos assim e insira com insert_many:
        # {"tipo":"BRUTE_FORCE","severidade":"critica",
        #  "ativo":{"nome":"SRV-WEB01","ip":"192.168.1.10","criticidade":"alta"}}
        # 3. Verifique a migração: conte no MySQL e no Mongo e compare.

        # Saída esperada:
        # MySQL: 3 alertas | MongoDB: 3 documentos -> MIGRAÇÃO ÍNTEGRA
        # Consulta sem JOIN: db.alertas.find({"ativo.criticidade":"alta"}) -> 2 documentos
        # Comentário (2 linhas): o que se ganha (leitura sem JOIN) e o que se perde
        #                        (duplicação: renomear o ativo exige update_many).
'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# importa módulos para o programa

import mysql.connector
from mysql.connector import Error
from pymongo import MongoClient
from pymongo.errors import PyMongoError # Tentei usar isso mas não gostei
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

def _criaTabelaSQL():
    '''
    cria as tabelas para exercicio
        MySQL (crie):
        ativos(id PK, nome, ip UNIQUE, criticidade ENUM('baixa','media','alta'))

    '''
    # Cria tabela
    try:
        print("Demolindo tabelas antigas...")
        cursor.execute("DROP TABLE IF EXISTS ativos")
        cursor.execute("DROP TABLE IF EXISTS alertas")
        conexao.commit()

        print("Criando Tabelas novas")
        cursor.execute("""
            CREATE TABLE ativos(
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        nome VARCHAR(20),
                        ip VARCHAR(25) UNIQUE,
                        criticidade ENUM('baixa', 'media', 'alta'),
                        criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        )
        """)

        cursor.execute("""
            CREATE TABLE alertas(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    ativo_id INT,
                    FOREIGN KEY (ativo_id) REFERENCES ativos(id),
                    tipo VARCHAR(20),
                    Severidade VARCHAR(20),
                    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
        """)

    except Error as e:
        print("Tabela não criada: {}".format(e))
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
try:
    conexao = mysql.connector.connect(
        host="localhost", user="root",
        password="senha", database="seguranca"
    )
    if conexao.is_connected():
        print("Conectado ao MySQL!")
except Error as e:
    print(f"Erro de conexão: {e}")

finally:
    cursor = conexao.cursor()
    _criaTabelaSQL()