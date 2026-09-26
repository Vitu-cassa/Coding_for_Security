
perfis = {
    "credenciais_do_SOC":      {"schema_fixo":True,  "precisa_acid":True,  "escala_horizontal":False, "tolera_atraso_de_consistencia":False, "dado_sensivel":True},
    "telemetria_de_sensores":  {"schema_fixo":False, "precisa_acid":False, "escala_horizontal":True,  "tolera_atraso_de_consistencia":True,  "dado_sensivel":False},
    "trilha_de_auditoria":     {"schema_fixo":False, "precisa_acid":False, "escala_horizontal":True,  "tolera_atraso_de_consistencia":False, "dado_sensivel":True},
    "carrinho_de_licencas":    {"schema_fixo":True,  "precisa_acid":True,  "escala_horizontal":False, "tolera_atraso_de_consistencia":False, "dado_sensivel":False},
    "cache_de_sessoes":        {"schema_fixo":True,  "precisa_acid":False, "escala_horizontal":True,  "tolera_atraso_de_consistencia":True,  "dado_sensivel":True},
    }

perfil_teste = {
    "Testes_de_Funcionalidade": {"schema_fixo":True,  "precisa_acid":True,  "escala_horizontal":True, "tolera_atraso_de_consistencia":True, "dado_sensivel":True}
                }
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 1 — Assistente de decisão de armazenamento (Aulas 1 e 8):
        Escreva recomendar(perfil) que recebe o perfil de um conjunto de dados
        e devolve uma recomendação fundamentada: qual banco usar, qual lado do
        CAP priorizar e qual risco OWASP a escolha errada cria. Nada de if solto
        no meio do código — a função precisa explicar a decisão.

        # Entrada: dict com as chaves
        #   schema_fixo (bool), precisa_acid (bool), escala_horizontal (bool),
        #   tolera_atraso_de_consistencia (bool), dado_sensivel (bool)
        #
        # Saída: dict {"banco": "MySQL"|"MongoDB", "cap": "CP"|"AP",
        #              "justificativa": str, "risco_owasp": str}

        perfis = {
        "credenciais_do_SOC":      {"schema_fixo":True,  "precisa_acid":True,  "escala_horizontal":False, "tolera_atraso_de_consistencia":False, "dado_sensivel":True},
        "telemetria_de_sensores":  {"schema_fixo":False, "precisa_acid":False, "escala_horizontal":True,  "tolera_atraso_de_consistencia":True,  "dado_sensivel":False},
        "trilha_de_auditoria":     {"schema_fixo":False, "precisa_acid":False, "escala_horizontal":True,  "tolera_atraso_de_consistencia":False, "dado_sensivel":True},
        "carrinho_de_licencas":    {"schema_fixo":True,  "precisa_acid":True,  "escala_horizontal":False, "tolera_atraso_de_consistencia":False, "dado_sensivel":False},
        "cache_de_sessoes":        {"schema_fixo":True,  "precisa_acid":False, "escala_horizontal":True,  "tolera_atraso_de_consistencia":True,  "dado_sensivel":True},
        }

        # Saída esperada (formato; as justificativas são suas):
        # credenciais_do_SOC     -> MySQL   | CP | "autenticar errado é pior que ficar fora do ar" | A07
        # telemetria_de_sensores -> MongoDB | AP | "perder 1s de log < parar de aceitar log"       | A09
        # trilha_de_auditoria    -> MongoDB | CP | "auditoria divergente não vale como prova"      | A08
        # ...
'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def _recomendar(perfis):
    for nome, itens in perfis.items():
        perfil = nome
        parametros = itens

        avaliacao = _avaliador(parametros)
        
        _formatador(perfil, avaliacao)

def _avaliador(parametros):
    try:
        avaliacao = {"sql": None,
                     "cap": None,
                     "owasp": None,
                     "justificativa": None}

        schema = parametros["schema_fixo"]
        acid = parametros["precisa_acid"]
        escala = parametros["escala_horizontal"]
        atraso_consistencia = parametros["tolera_atraso_de_consistencia"]
        dado_sensivel = parametros["dado_sensivel"]

        # Decide o banco
        if acid or (dado_sensivel and schema and atraso_consistencia):
            avaliacao["sql"] = True
        else:
            avaliacao["sql"] = False

        # Avalia o CAP
        if acid and schema and dado_sensivel:
            avaliacao["cap"] = "CP"

        elif escala and atraso_consistencia:
            avaliacao["cap"] = "AP"

        else:
            avaliacao["cap"] = "Verificar parametros."

        elif 
        return avaliacao
    
    except Exception as e:
        print("Erro nos dados: {}".format(e))

def _formatador(perfil, avaliacao):
    sql = avaliacao["sql"]

    if sql:
        banco = "MySQL"
    elif not sql:
        banco = "MongDb"
    else:
        banco = "Pesquisar banco e adicionar aos dados"
    print("{} -> {}".format(perfil, banco))

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Area dev

try:
    _recomendar(perfis)
except Exception as e:
    print("Erro na avaliação: {}".format(e))