contas = [(1, "Alice", 1000), (2, "Bob", 500)]

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 5 — Transação com rollback:
        Simule uma transferência entre duas "contas" no MySQL (debita de uma,
        credita em outra). Se a segunda operação falhar (ex: conta inexistente),
        faça rollback e prove que o saldo da primeira conta não mudou.

        # Tabela: contas(id, titular, saldo)
        contas = [(1, "Alice", 1000), (2, "Bob", 500)]

        # Cenário de teste:
        # Transferir 200 de Alice para Bob      -> commit, saldos: Alice=800, Bob=700
        # Transferir 100 de Alice para conta 99 -> rollback, saldos INALTERADOS: Alice=800

        # Saída esperada:
        # Transferência 1 OK. Alice=800, Bob=700
        # Transferência 2 FALHOU (conta destino inexistente). Rollback. Alice=800
'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import mysql.connector
from mysql.connector import Error

# Conecta com o banco
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

    # Cria a tabela de contas

    print("Criando tabela de contas...")
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contas(
                    id INT PRIMARY KEY UNIQUE,
                    nome VARCHAR(50),
                    saldo DECIMAL(10,2),
                    atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
        """)
    except Exception as e:
        print("Tabela não criada: {}".format(e))

    # Insere as contas na tabela
    print("Inserindo contas...")
    try:
        cursor.executemany(
            "INSERT INTO contas (id, nome, saldo) \
            VALUES (%s, %s, %s)", contas
            )
        conexao.commit()
    except Exception as e:
        print("Contas não adicionadas: {}".format(e))

    # consultado contas e saldos atuais
    print("Consultando contas...")
    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM contas"
        )
        for conta in cursor.fetchall():
            print("Cliente: {0[nome]:<10} | saldo: R$ {0[saldo]}".format(conta))
        conexao.commit()
    except Exception as e:
        print("Consulta não executada: {}".format(e))

    # Realiza teste de transferência com rollback
    print("Realizando transferências por Picles...")
    try:
        # Transferências de Alice para bob
        cursor.execute(
            "UPDATE contas SET saldo = saldo - 200 WHERE id = 1"
        )
        cursor.execute(
            "UPDATE contas SET saldo = saldo + 200 WHERE id = 2"
        )
        Trânsferencias de alice para ID desconhecido
        cursor.execute(
            "UPDATE contas SET saldo = saldo - 100 WHERE id = 1"
        )
        cursor.execute(
            "UPDATE contas SET saldo = saldo + 200 WHERE id = 99"
        )
        conexao.commit()

    except Exception as e:
        conexao.rollback()
        print("Transferência não realizada: {}".format(e))
        print("Realizando RollBack...")

        # Consulta a tabela para verificar status da conta após rollback
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM contas"
        )
        for conta in cursor.fetchall():
            print("Cliente: {0[nome]:<10} | saldo: R$ {0[saldo]}".format(conta))

    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
