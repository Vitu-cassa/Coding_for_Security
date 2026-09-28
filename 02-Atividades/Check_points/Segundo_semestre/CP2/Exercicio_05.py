from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import time

app = Flask(__name__)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 5 — O ORDER BY que o %s não protege (Aulas 3, 6, 7 e 8/A05):
        Crie GET /api/eventos?ordenar_por=&ordem=&tamanho= sobre o MySQL.
        Descubra na prática que placeholder não parametriza nome de coluna e
        defenda com whitelist.
'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ✅ Defesa: mapa fechado de valores permitidos (Whitelist)
# Atuando como sentinela para os parâmetros recebidos via requisição HTTP
COLUNAS = {"data": "criado_em", "sev": "severidade", "ip": "ip_origem"}
ORDEM   = {"asc": "ASC", "desc": "DESC"}
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def _validar_parametros(ordenar_por, ordem, tamanho):
    '''
    Isola a validação lógica e a regra de negócio da rota HTTP.
    Retorna uma tupla (parametros_seguros, mensagem_de_erro).
    '''
    try:
        tamanho_int = int(tamanho)
        
        # Defesa do teto do servidor para prevenir DoS (condicional em linha)
        tamanho_int = (100 if tamanho_int > 100 else tamanho_int)
        
        if ordenar_por not in COLUNAS:
            return None, "campo de ordenação inválido"
        
        if ordem not in ORDEM:
            return None, "ordem inválida"
            
        parametros_seguros = {
            "coluna": COLUNAS[ordenar_por],
            "ordem": ORDEM[ordem],
            "tamanho": tamanho_int
        }
        return parametros_seguros, None
        
    except ValueError:
        return None, "tamanho deve ser inteiro"
    except Exception as e:
        return None, "Erro inesperado na validação: {}".format(e)


def _executar_query(parametros):
    '''
    Isola a comunicação direta com o banco de dados.
    Recebe apenas parâmetros que já passaram pela Whitelist.
    '''
    try:
        conexao = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="senha", # Ajustar para a senha do seu laboratório
            database="seguranca"
        )
        cursor = conexao.cursor(dictionary=True)

        coluna = parametros["coluna"]
        ordem = parametros["ordem"]
        tamanho = parametros["tamanho"]

        # A Hibridização: .format() injeta os identificadores seguros da whitelist.
        # O %s cuida exclusivamente do dado numérico (LIMIT), parametrizando a consulta.
        query = "SELECT * FROM eventos ORDER BY {} {} LIMIT %s".format(coluna, ordem)
        
        cursor.execute(query, (tamanho,))
        resultados = cursor.fetchall()
        
        return resultados, None

    except Error as e:
        return None, "Erro no banco de dados: {}".format(e)
    except Exception as e:
        return None, "Falha interna de execução: {}".format(e)
        
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()


@app.route('/api/eventos', methods=['GET'])
def _listar_eventos():
    # Captura os parâmetros e aplica lower() para bater com a Whitelist
    ordenar_por = request.args.get('ordenar_por', 'data').lower()
    ordem = request.args.get('ordem', 'desc').lower()
    tamanho = request.args.get('tamanho', '10')

    # Passo 1: Validação e Limpeza
    parametros_seguros, erro_validacao = _validar_parametros(ordenar_por, ordem, tamanho)
    
    if erro_validacao:
        return jsonify({"erro": erro_validacao}), 400

    # Passo 2: Execução
    eventos, erro_banco = _executar_query(parametros_seguros)
    
    if erro_banco:
        return jsonify({"erro_interno": erro_banco}), 500

    # Passo 3: Saída de Sucesso
    return jsonify(eventos), 200


if __name__ == '__main__':
    print("Iniciando procedimentos de segurança da API...")
    time.sleep(2)
    print("Carregando Whitelist de Defesa (Colunas e Ordem)...")
    time.sleep(2)
    print("Guarita pronta e operando na porta 5000!")
    
    try:
        app.run(port=5000, debug=True)
    except Exception as e:
        print("Falha severa ao iniciar o servidor: {}".format(e))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
RESPOSTA TEÓRICA (Entregável do Exercício):
Por que `LIMIT %s` funciona, mas `ORDER BY %s` não?

1. LIMIT %s funciona porque a cláusula espera um DADO numérico. O motor do MySQL 
   aceita o placeholder, valida o tipo e o processa com segurança.
2. ORDER BY %s falha porque, para evitar injeção, o motor escapa a variável com aspas 
   (ex: ORDER BY 'ip_origem'). O nome da coluna se transforma em uma string literal,
   destruindo a ordenação da tabela.
3. Conclusão da Arquitetura: Placeholders são blindagens para DADOS (valores de campos). 
   Identificadores estruturais (nomes de tabelas ou colunas) não podem ser parametrizados. 
   Quando o usuário precisa escolher a coluna, a única defesa possível é a Whitelist.
'''