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
    # Cria tabela
    cursor = conexao.cursor()
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

    # Insere os ativos

#    cursor.execute(
#        "INSERT INTO ativos (nome, ip, tipo, criticidade, status) \
#        VALUES ('teste', '1.1.1.1', 'maquininha', 'baixa', 'ativo')")
#    conexao.commit()
    cursor.executemany(
       "INSERT INTO ativos (nome, ip, tipo, criticidade, status) \
        VALUES (%s, %s, %s, %s, %s)", ativos)
    conexao.commit()
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
