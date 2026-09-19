ativos = [
            ("SRV-WEB01", "192.168.1.10", "servidor", "alta",  "ativo"),
            ("PC-RH03",   "192.168.1.45", "estacao",  "baixa", "ativo"),
            ("SW-CORE01", "192.168.1.1",  "switch",   "media", "inativo"),
            ]
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 1 — Modelagem e CRUD SQL:
        Crie a tabela ativos no MySQL e escreva os comandos para inserir,
        listar filtrando por tipo, atualizar o status e remover.
        Use ENUM para o campo criticidade e UNIQUE no IP.

        # Schema esperado:
            ativos(
                    id PK AUTO_INCREMENT, nome, ip UNIQUE, tipo, criticidade
                    ENUM('baixa','media','alta'), status
                    )

        # Dados iniciais:
            ativos = [
                ("SRV-WEB01", "192.168.1.10", "servidor", "alta",  "ativo"),
                ("PC-RH03",   "192.168.1.45", "estacao",  "baixa", "ativo"),
                ("SW-CORE01", "192.168.1.1",  "switch",   "media", "inativo"),
            ]

        # Saída esperada:
            Listar tipo='servidor' -> SRV-WEB01 | 192.168.1.10 | alta | ativo
            Após UPDATE status de SW-CORE01 para 'ativo' -> "1 registro atualizado"
            Inserir IP duplicado (192.168.1.10) -> erro de UNIQUE tratado
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

    # Cria tabela
    try:
        print("tomara que esteja criando a tabela...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ativos(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(50),
                    ip VARCHAR(45) UNIQUE,
                    tipo VARCHAR(50),
                    criticidade ENUM('baixa', 'media', 'alta'),
                    status ENUM('ativo', 'inativo') DEFAULT 'ativo', 
                    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
        """)
    except Error as e:
        print("Tabela não criada: {}".format(e))

    # Insere um ativo
    print("inserindo apenas um dado...")
    try:
        cursor.execute(
            "INSERT INTO ativos (nome, ip, tipo, criticidade, status) \
            VALUES ('teste', '1.1.1.1', 'maquininha', 'baixa', 'ativo')")
        conexao.commit()
    except Error as e:
        print("Ativo não cadastrado: {}".format(e))

    # Insere os ativos da atividade
    print("Inserindo ativos da lista...")
    try:
        cursor.executemany(
        "INSERT INTO ativos (nome, ip, tipo, criticidade, status) \
         VALUES (%s, %s, %s, %s, %s)", ativos
         )
        conexao.commit()
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()
    except Error as e:
        print("Ativo não cadastrado: {}".format(e))

    # Realiza consulta na tabela por status "ativo"
    print("Realinzando consultas...")

    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(
        "SELECT * FROM ativos WHERE status = %s", ("ativo",)
        )
        for row in cursor.fetchall():
            print(f"[{row['status']}] {row['nome']} {row['ip']} {row['tipo']}")
        conexao.commit()

        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()
    except Error as e:
        print("Consulta não realizada: {}".format(e))

    # Realiza o update de "CORE" para ativo
    print("Atualizando servidores inativos...")

    try:

        print(conexao.is_connected())
        cursor.execute(
            "UPDATE ativos SET status = %s WHERE status = %s", ('ativo', 'inativo')
        )
        conexao.commit()
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()
    except Error as e:
        print("Atualização não realizada: {}".format(e))
