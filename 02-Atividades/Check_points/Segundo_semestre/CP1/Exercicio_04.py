usuarios = [
    ("admin","admin@x.com"), 
    ("ana","ana@x.com"), 
    ("bruno","bruno@x.com")
    ]
entrada = "' OR '1'='1"

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''Exercício 4 — Query parametrizada (defesa contra SQL Injection): 
        Escreva duas funções de busca por nome de usuário: uma insegura 
        (concatenando) e uma segura (parametrizada). Demonstre com a entrada 
        ' OR '1'='1 que a insegura vaza todos os registros e a segura não 
        retorna nada.

        usuarios = [("admin","admin@x.com"), ("ana","ana@x.com"), ("bruno","bruno@x.com")]
        entrada = "' OR '1'='1"

        # Saída esperada:
        # [INSEGURO] entrada=' OR '1'='1  -> 3 usuários (VAZAMENTO)
        # [SEGURO]   entrada=' OR '1'='1  -> 0 usuários (defesa OK)
        ⚠️ Exercício defensivo — rode apenas no banco local de laboratório.
'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import mysql.connector
from mysql.connector import Error

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

    # Cria tabela de usuarios
    try:
        print("Criando tabela...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(50),
                    email VARCHAR(45) UNIQUE,
                    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
        """)
    except Error as e:
        print("Tabela não criada: {}".format(e))
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()

    # Insere os usuários da atividade
    print("Inserindo usuários da lista...")

    try:
        cursor.executemany(
        "INSERT INTO users (nome, email) \
         VALUES (%s, %s,)", usuarios
         )
        conexao.commit()
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()
    except Error as e:
        print("Usuários não cadastrados: {}".format(e))

