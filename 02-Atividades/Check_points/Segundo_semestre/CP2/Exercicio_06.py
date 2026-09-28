from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import time

app = Flask(__name__)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 6 — Controle de acesso quebrado (Aulas 3, 6 e 8/A01):
        Uma API de incidentes em que cada analista só pode ver os seus incidentes, 
        e apenas nível >= 5 pode apagar qualquer um. 
        Autenticação por header X-API-Key validado no MySQL com query parametrizada.
'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Dados Iniciais para popular o laboratório
analistas  = [(1, "ana", "key-ana-001", 5), (2, "bruno", "key-bruno-002", 2)]
incidentes = [(1, 1, "Brute force SSH", "critica"), (2, 2, "Phishing no RH", "media")]
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def _conectar():
    ''' Retorna a conexão com o banco de dados. '''
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="sua_senha", # Ajustar para o seu laboratório
        database="seguranca"
    )

def _preparar_banco():
    '''
    Demole e recria as tabelas do laboratório a cada inicialização 
    para garantir um ambiente limpo para os testes de IDOR.
    '''
    try:
        conexao = _conectar()
        cursor = conexao.cursor()
        
        cursor.execute("DROP TABLE IF EXISTS incidentes")
        cursor.execute("DROP TABLE IF EXISTS analistas")
        
        cursor.execute("""
            CREATE TABLE analistas(
                id INT PRIMARY KEY,
                nome VARCHAR(20),
                api_key VARCHAR(50) UNIQUE,
                nivel INT
            )
        """)
        
        cursor.execute("""
            CREATE TABLE incidentes(
                id INT PRIMARY KEY,
                dono_id INT,
                titulo VARCHAR(50),
                severidade VARCHAR(20),
                FOREIGN KEY (dono_id) REFERENCES analistas(id)
            )
        """)
        
        cursor.executemany(
            "INSERT INTO analistas (id, nome, api_key, nivel) VALUES (%s, %s, %s, %s)", 
            analistas
        )
        cursor.executemany(
            "INSERT INTO incidentes (id, dono_id, titulo, severidade) VALUES (%s, %s, %s, %s)", 
            incidentes
        )
        
        conexao.commit()
        
    except Error as e:
        print("Falha na fundação do banco: {}".format(e))
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()


def _validar_acesso():
    '''
    Sentinela de Autenticação (A07)
    Lê o Header X-API-Key e parametriza a busca no banco para evitar SQLi.
    Retorna o dicionário do usuário ou None se falhar.
    '''
    api_key = request.headers.get('X-API-Key')
    
    if not api_key:
        return None
        
    try:
        conexao = _conectar()
        cursor = conexao.cursor(dictionary=True)
        
        # Query parametrizada: A chave API é tratada estritamente como DADO (%s)
        cursor.execute("SELECT * FROM analistas WHERE api_key = %s", (api_key,))
        usuario = cursor.fetchone()
        
        return usuario
        
    except Error as e:
        print("Erro de autenticação no BD: {}".format(e))
        return None
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()

# -----------------------------------------------------------------------------
# ROTAS DA API
# -----------------------------------------------------------------------------

@app.route('/api/incidentes', methods=['GET'])
def _listar_meus_incidentes():
    usuario = _validar_acesso()
    
    if not usuario:
        # 401 Unauthorized: "Não sei quem você é"
        return jsonify({"erro": "Autenticação obrigatória."}), 401
        
    try:
        conexao = _conectar()
        cursor = conexao.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM incidentes WHERE dono_id = %s", (usuario['id'],))
        meus_incidentes = cursor.fetchall()
        
        return jsonify(meus_incidentes), 200
        
    except Error as e:
        return jsonify({"erro_interno": str(e)}), 500
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()


@app.route('/api/incidentes/<int:id_incidente>', methods=['GET'])
def _buscar_incidente_especifico(id_incidente):
    usuario = _validar_acesso()
    
    if not usuario:
        return jsonify({"erro": "Autenticação obrigatória."}), 401
        
    try:
        conexao = _conectar()
        cursor = conexao.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM incidentes WHERE id = %s", (id_incidente,))
        incidente = cursor.fetchone()
        
        if not incidente:
            return jsonify({"erro": "Incidente não encontrado."}), 404
            
        # Defesa IDOR (A01): Verifica o dono. 
        # O retorno é 403 com mensagem genérica para não vazar a existência do ID para atacantes.
        if incidente['dono_id'] != usuario['id']:
            # 403 Forbidden: "Sei quem você é, e você não pode entrar aqui"
            return jsonify({"erro": "Acesso negado."}), 403
            
        return jsonify(incidente), 200
        
    except Error as e:
        return jsonify({"erro_interno": str(e)}), 500
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()


@app.route('/api/incidentes/<int:id_incidente>', methods=['DELETE'])
def _deletar_incidente(id_incidente):
    usuario = _validar_acesso()
    
    if not usuario:
        return jsonify({"erro": "Autenticação obrigatória."}), 401
        
    try:
        conexao = _conectar()
        cursor = conexao.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM incidentes WHERE id = %s", (id_incidente,))
        incidente = cursor.fetchone()
        
        if not incidente:
            return jsonify({"erro": "Incidente não encontrado."}), 404
            
        # Defesa de Autorização Vertical: Nível >= 5 ou dono do próprio incidente
        eh_dono = (incidente['dono_id'] == usuario['id'])
        eh_admin = (usuario['nivel'] >= 5)
        
        if not (eh_dono or eh_admin):
            return jsonify({"erro": "Acesso negado. Nível insuficiente."}), 403
            
        cursor.execute("DELETE FROM incidentes WHERE id = %s", (id_incidente,))
        conexao.commit()
        
        return jsonify({"msg": "Incidente {} removido com sucesso.".format(id_incidente)}), 200
        
    except Error as e:
        return jsonify({"erro_interno": str(e)}), 500
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()


if __name__ == '__main__':
    print("Forjando tabelas e populando laboratório...")
    _preparar_banco()
    time.sleep(2)
    print("Laboratório inicializado. Ana (Lvl 5) e Bruno (Lvl 2) na base.")
    time.sleep(1)
    print("Guarita IDOR operando na porta 5000!")
    
    try:
        app.run(port=5000, debug=True)
    except Exception as e:
        print("Falha severa ao iniciar o servidor: {}".format(e))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
RESPOSTA TEÓRICA (Entregável do Exercício):
Diferença entre 401 e 403, e a mitigação do IDOR:

1. O Erro 401 (Unauthorized) sinaliza falha de identidade. O servidor diz: "Não 
   reconheço seu X-API-Key". Ele bloqueia na guarita externa.
2. O Erro 403 (Forbidden) sinaliza falha de autorização. O servidor diz: "Sei que
   você é o Bruno (nível 2), mas você não tem crachá para este cofre".
3. A Defesa IDOR exige que o 403 seja cego. Se o erro revelasse "Incidente pertence
   à Ana", um atacante enumeraria todos os IDs válidos apenas observando a mudança 
   das mensagens de erro (Information Disclosure). O acesso deve ser negado sem 
   confirmar a existência do recurso.
'''