from flask import Flask, render_template_string, make_response
from pymongo import MongoClient
import time

app = Flask(__name__)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 7 — XSS onde ninguém procura: dentro do atributo (Aulas 6, 7 e 8/A05):
        Monte GET /dashboard que renderiza uma tabela de incidentes vindos do MongoDB, 
        incluindo o nome do ativo dentro de um atributo HTML (<img src="/icone.png" alt="...">). 
        Prove que sua defesa segura dois payloads diferentes.
'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Payloads Maliciosos para popular o laboratório (MongoDB)
p1 = "<script>alert('xss1 - injeção direta de tag')</script>"
p2 = 'x" onerror="alert(\'xss2 - quebra de atributo\')'

incidentes_iniciais = [
    {"_id": 1, "titulo": "Ataque Clássico", "ativo": p1},
    {"_id": 2, "titulo": "Ataque Furtivo (Atributo)", "ativo": p2}
]
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def _conectar_mongo():
    ''' Retorna a conexão com o MongoDB. '''
    client = MongoClient("mongodb://localhost:27017/")
    return client["seguranca"]

def _preparar_banco():
    '''
    Limpa a coleção antiga e insere os payloads maliciosos
    para garantir que os testes XSS aconteçam em ambiente controlado.
    '''
    try:
        db = _conectar_mongo()
        colecao = db["incidentes_xss"]
        
        colecao.drop()
        colecao.insert_many(incidentes_iniciais)
        
    except Exception as e:
        print("Erro na fundação do banco MongoDB: {}".format(e))

# -----------------------------------------------------------------------------
# DEFESA EM PROFUNDIDADE: O Escudo CSP
# -----------------------------------------------------------------------------
@app.after_request
def _aplicar_csp(resposta):
    '''
    Injeta o header Content-Security-Policy em TODAS as respostas da API.
    A regra "default-src 'self'" proíbe categoricamente a execução de 
    qualquer JavaScript inline (como os nossos alert() dos payloads).
    '''
    resposta.headers['Content-Security-Policy'] = "default-src 'self'"
    return resposta

# -----------------------------------------------------------------------------
# ROTAS E TEMPLATES (Jinja2)
# -----------------------------------------------------------------------------

# Template Seguro (O Jinja2 aplica Autoescape HTML nativamente)
TEMPLATE_SEGURO = """
<!DOCTYPE html>
<html>
<head><title>Dashboard Seguro</title></head>
<body>
    <h2>🛡️ Dashboard de Incidentes (SEGURO)</h2>
    <table border="1" cellpadding="5">
        <tr><th>ID</th><th>Título</th><th>Ativo (Imagem no atributo ALT)</th></tr>
        {% for inc in incidentes %}
        <tr>
            <td>{{ inc._id }}</td>
            <td>{{ inc.titulo }}</td>
            <td>
                <!-- O Jinja converte < e " para entidades HTML (&lt; e &quot;) -->
                <img src="/static/alerta.png" alt="{{ inc.ativo }}">
                Texto bruto renderizado: {{ inc.ativo }}
            </td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

# Template Inseguro (Uso intencional do filtro |safe para anular a defesa)
TEMPLATE_INSEGURO = """
<!DOCTYPE html>
<html>
<head><title>Dashboard INSEGURO</title></head>
<body>
    <h2>⚠️ Dashboard de Incidentes (INSEGURO)</h2>
    <table border="1" cellpadding="5">
        <tr><th>ID</th><th>Título</th><th>Ativo (Imagem no atributo ALT)</th></tr>
        {% for inc in incidentes %}
        <tr>
            <td>{{ inc._id }}</td>
            <td>{{ inc.titulo | safe }}</td>
            <td>
                <!-- O filtro |safe ordena que o motor confie cegamente no dado -->
                <img src="/static/alerta.png" alt="{{ inc.ativo | safe }}">
                Texto bruto renderizado: {{ inc.ativo | safe }}
            </td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route('/dashboard', methods=['GET'])
def _dashboard_seguro():
    try:
        db = _conectar_mongo()
        incidentes = list(db["incidentes_xss"].find())
        return render_template_string(TEMPLATE_SEGURO, incidentes=incidentes)
    except Exception as e:
        return "Erro interno: {}".format(e), 500


@app.route('/dashboard-inseguro', methods=['GET'])
def _dashboard_inseguro():
    try:
        db = _conectar_mongo()
        incidentes = list(db["incidentes_xss"].find())
        return render_template_string(TEMPLATE_INSEGURO, incidentes=incidentes)
    except Exception as e:
        return "Erro interno: {}".format(e), 500


if __name__ == '__main__':
    print("Forjando coleções no MongoDB...")
    _preparar_banco()
    time.sleep(2)
    print("Laboratório populado com payloads maliciosos.")
    time.sleep(1)
    print("Guarita Anti-XSS (CSP ativo) rodando na porta 5000!")
    
    try:
        app.run(port=5000, debug=True)
    except Exception as e:
        print("Falha severa ao iniciar o servidor: {}".format(e))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
RESPOSTAS TEÓRICAS (Entregável do Exercício):

1. Por que um `|safe` mal colocado reabriria o buraco?
R: O Jinja2 protege a aplicação convertendo caracteres de controle (<, >, ", ') em 
entidades HTML seguras (&lt;, &quot;). O `|safe` desliga essa conversão, dizendo ao motor 
para vomitar o texto cru no navegador, permitindo que a injeção quebre a sintaxe HTML e vire código executável.

2. A Mágica do CSP em Ação:
Mesmo acessando a rota `/dashboard-inseguro` — onde o HTML é quebrado intencionalmente —, 
os pop-ups de `alert()` não vão estourar na sua tela. Isso prova que o CSP 
(Content-Security-Policy) é a última e mais forte muralha (Defense in Depth). Se a 
higienização do código falhar e o atacante injetar o script, o CSP ordena que o 
navegador se recuse a executá-lo.
'''