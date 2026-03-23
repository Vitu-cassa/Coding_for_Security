# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 10 (Desafio): 
        Calculadora de Imposto de Renda 2025:
        Crie um programa completo que calcule o Imposto de Renda mensal de um funcionário. 
        O programa deve pedir: salário bruto mensal, número de dependentes, se paga pensão alimentícia (e qual valor) 
        e se tem 65 anos ou mais. 
        O cálculo segue estas etapas nesta ordem:

        Etapa 1 — Base de cálculo: Comece com o salário bruto. Desconte INSS usando a tabela progressiva (calcule faixa por faixa, não aplique a alíquota sobre o total). 
        Depois desconte R$ 189.59 por dependente e o valor da pensão alimentícia (se houver). 
        Se o funcionário tem 65+ anos, desconte mais R$ 1.903.98 de isenção extra. O resultado é a base de cálculo do IR.

        Etapa 2 — INSS progressivo:
            # Tabela INSS 2025 (calcule faixa por faixa):
            # Até R$ 1.518.00         → 7.5%
            # De R$ 1.518.01 a R$ 2.793.88  → 9%
            # De R$ 2.793.89 a R$ 4.190.83  → 12%
            # De R$ 4.190.84 a R$ 8.157.41  → 14%
            # Acima de R$ 8.157.41   → teto (não desconta mais)

            # Exemplo para salário R$ 5.000.00:
            # Faixa 1: 1.518.00 * 7.5% = 113.85
            # Faixa 2: (2.793.88 - 1.518.00) * 9% = 114.83
            # Faixa 3: (4.190.83 - 2.793.88) * 12% = 167.63
            # Faixa 4: (5.000.00 - 4.190.83) * 14% = 113.28
            # Total INSS: R$ 509.59

        Etapa 3 — IR progressivo (sobre a base de cálculo):
            # Tabela IR 2025 (também progressiva, faixa por faixa):
            # Até R$ 2.259.20         → isento
            # De R$ 2.259.21 a R$ 2.826.65  → 7.5%
            # De R$ 2.826.66 a R$ 3.751.05  → 15%
            # De R$ 3.751.06 a R$ 4.664.68  → 22.5%
            # Acima de R$ 4.664.68   → 27.5%

        # Teste com estes cenários:
        testes = [
            {"salario": 2000.00, "dependentes": 0, "pensao": 0, "idoso": False},
            # INSS: R$ 157.17 | Base: R$ 1.842.83 | IR: isento

            {"salario": 5000.00, "dependentes": 2, "pensao": 0, "idoso": False},
            # INSS: R$ 509.59 | Dedução dep: R$ 379.18 | Base: R$ 4.111.23 | IR: R$ 263.02

            {"salario": 8000.00, "dependentes": 1, "pensao": 500, "idoso": False},
            # INSS: R$ 872.77 | Dedução dep: R$ 189.59 | Pensão: R$ 500 | Base: R$ 6.437.64

            {"salario": 3500.00, "dependentes": 0, "pensao": 0, "idoso": True},
            # INSS: R$ 401.36 | Isenção idoso: R$ 1.903.98 | Base: R$ 1.194.66 | IR: isento
        ]

        # Saída esperada (cenário 2):
        # ====================================
        # CONTRACHEQUE — Cálculo de IR Mensal
        # ====================================
        # Salário bruto:       R$ 5.000,00
        #
        # (-) INSS:            R$ 509,59
        #     Faixa 7.5%:      R$ 113,85
        #     Faixa 9%:        R$ 114,83
        #     Faixa 12%:       R$ 167,63
        #     Faixa 14%:       R$ 113,28
        #
        # (-) Dependentes (2): R$ 379,18
        # (-) Pensão:          R$ 0,00
        # (-) Isenção 65+:     R$ 0,00
        #
        # Base de cálculo IR:  R$ 4.111,23
        #
        # (-) IR:              R$ 263,02
        #     Faixa isenta:    R$ 0,00
        #     Faixa 7.5%:      R$ 42,56
        #     Faixa 15%:       R$ 138,66
        #     Faixa 22.5%:     R$ 81,04
        #     Faixa 27.5%:     R$ 0,00
        #
        # ====================================
        # Salário líquido:     R$ 4.227,39
        # ====================================
'''
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def apresentacao():
    print()
    print("+--------------------------------------+")
    print("| Calculadora de Imposto de Renda 2025 | ")
    print("+--------------------------------------+")
    print()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def fim_script():
    print()
    print("//////////////////////")
    print("/    Fim do script.  /")
    print("//////////////////////")
    print()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def faixa_INSS(salario_bruto: float):

    # Casting
    salario_bruto = float(salario_bruto)

    if salario_bruto <= 1518:
        faixa = 1
    elif 1518.01 <= salario_bruto <= 2793.88:
        faixa = 2
    elif 2793.89 <= salario_bruto <= 4190.83:
        faixa = 3
    else:
        faixa = 4
    
    return faixa
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def valor_INSS(faixa: int, salario_bruto: float):

    # Casting
    faixa = int(faixa)
    salario_bruto = int(salario_bruto)

    if faixa == 1:
        desconto_inss = (salario_bruto - 1518.00) * 0.075
    
    elif faixa == 2:
        desconto_inss = ((salario_bruto - 1518.00) * 0.09) + 113.85

    elif faixa == 3:
        desconto_inss = ((salario_bruto - 2793.88)* 0.12) + 228.68
    
    else:
        desconto_inss = ((salario_bruto - 4190.83) * 0.14) + 396.31

    return desconto_inss
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def valor_dependete(salario_bruto: float, dependente: int, pensao: float):

    # Casting
    salario_bruto = float(salario_bruto)
    dependente = int(dependente)
    pensao = float(pensao)

    isencao_dependente = pensao + (dependente * 189.59)

    return isencao_dependente
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def valor_idoso(idoso: bool):

    # Casting
    idoso = bool(idoso)

    if idoso:
        isencao_idoso = 1903.98
    else:
        isencao_idoso = 0
    
    return isencao_idoso
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def verificador_de_velhos(resposta: str):

    # Casting
    resposta = str(resposta.lower())

    if resposta == "s":
        idoso = True
    else:
        idoso = False
    
    return idoso
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def somador_descontos(desconto_inss: float):
    # casting
    desconto_inss = float(desconto_inss)

    total_descontos = desconto_inss
    
    return total_descontos
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def somador_isencao(isencao_dependente: float, isencao_idoso: float):
    isencao_dependente = float(isencao_dependente)
    isencao_idoso = float(isencao_idoso)

    total_isencao = isencao_idoso + isencao_dependente

    return total_isencao
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def base_calculo(salario_bruto: float, total_descontos: float, total_isencao: float):

    # casting
    salario_bruto = float(salario_bruto)
    total_descontos = float(total_descontos)
    total_isencao = float(total_isencao)
    
    valor_base = salario_bruto - total_descontos - total_isencao

    return valor_base
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def faixa_IR(valor_base: float):

    # casting
    valor_base = float(valor_base)

    if valor_base <= 2259.20:
        faixa_ir = 1
    
    elif 2259.21 <= valor_base <= 2826.65:
        faixa_ir = 2
    
    elif 2826.66 <= valor_base <= 3751.05:
        faixa_ir = 3
    
    elif 3751.06 <= valor_base <= 4664.68:
        faixa_ir = 4
    
    else:
        faixa_ir = 5
    
    return faixa_ir
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def valor_IR(faixa_ir: int, valor_base: float):

    # Casting
    faixa_ir = int(faixa_ir)
    valor_base = float(valor_base)

    if faixa_ir == 1:
        imposto_renda = 0
    
    elif faixa_ir == 2:
        imposto_renda = (valor_base - 2259.2) * 0.075

    elif faixa_ir == 3:
        imposto_renda = ((valor_base - 2829.65) * 0.15) + 42.56

    elif faixa_ir == 4:
        imposto_renda = ((valor_base - 3751.06) * 0.225) + 138.66 + 42.56
    
    elif faixa_ir == 5:
        imposto_renda = ((valor_base - 4664.68) * 0.275) + 138.66 + 42.56 + 205.56

    return imposto_renda
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def salario_liquido(valor_bruto: float, imposto_renda: float, total_descontos: float):

    # Casting
    valor_bruto = float(valor_bruto)
    imposto_renda = float(imposto_renda)
    total_descontos = float(total_descontos)
    # total_isencao = float(total_isencao)
    salario_liquido = valor_bruto - ((total_descontos + imposto_renda))

    return salario_liquido
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def contracheque():
    print()
    print("====================================")
    print("CONTRACHEQUE — Cálculo de IR Mensal")
    print("====================================")
    print(f"Salário bruto: R$ {SALARIO_BRUTO:.2f}")
    print()
    print(f"(-) INSS: R$ {DESCONTO_INSS:.2f}")
    print(f"(-) Dependentes ({DEPENDENTES}): R$ {ISENCAO_DEPENDENTE:.2f}")
    print(f"(-) Pensão: R$ {PENSAO:.2f}")
    print(f"(-) Isenção 65+: R$ {ISENCAO_IDOSO:.2f}")
    print()
    print(f"Base de cálculo IR: R$ {VALOR_BASE:.2f}")
    print()
    print(f"(-) IR: R$ {IMPOSTO_RENDA:.2f}")
    print()
    print("====================================")
    print(f"Salário líquido: R$ {SALARIO_LIQUIDO:.2f}")
    print("====================================")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Main()

cont = 1

apresentacao()
# Teste automatico
print("Auto-Teste")
print("********************")
while cont <= 4:
    if cont == 1: 
        SALARIO_BRUTO = 2000
        DEPENDENTES = 0
        PENSAO = 0
        IDOSO = "n"

        IDOSO = verificador_de_velhos(IDOSO)

        FAIXA = faixa_INSS(SALARIO_BRUTO)

        ISENCAO_DEPENDENTE = valor_dependete(SALARIO_BRUTO, DEPENDENTES, PENSAO)

        DESCONTO_INSS = valor_INSS(FAIXA, SALARIO_BRUTO)

        ISENCAO_IDOSO = valor_idoso(IDOSO)

        TOTAL_ISENCAO = somador_isencao(ISENCAO_DEPENDENTE, ISENCAO_IDOSO)
        TOTAL_DESCONTOS = somador_descontos(DESCONTO_INSS)

        VALOR_BASE = base_calculo(SALARIO_BRUTO, TOTAL_DESCONTOS, TOTAL_ISENCAO)

        FAIXA_IR = faixa_IR(VALOR_BASE)

        IMPOSTO_RENDA = valor_IR(FAIXA_IR, VALOR_BASE)

        SALARIO_LIQUIDO = salario_liquido(SALARIO_BRUTO, IMPOSTO_RENDA, TOTAL_DESCONTOS)
    
    elif cont == 2:
        SALARIO_BRUTO = 5000
        DEPENDENTES = 2
        PENSAO = 0
        IDOSO = "n"

        IDOSO = verificador_de_velhos(IDOSO)

        FAIXA = faixa_INSS(SALARIO_BRUTO)

        ISENCAO_DEPENDENTE = valor_dependete(SALARIO_BRUTO, DEPENDENTES, PENSAO)

        DESCONTO_INSS = valor_INSS(FAIXA, SALARIO_BRUTO)

        ISENCAO_IDOSO = valor_idoso(IDOSO)

        TOTAL_ISENCAO = somador_isencao(ISENCAO_DEPENDENTE, ISENCAO_IDOSO)
        TOTAL_DESCONTOS = somador_descontos(DESCONTO_INSS)

        VALOR_BASE = base_calculo(SALARIO_BRUTO, TOTAL_DESCONTOS, TOTAL_ISENCAO)

        FAIXA_IR = faixa_IR(VALOR_BASE)

        IMPOSTO_RENDA = valor_IR(FAIXA_IR, VALOR_BASE)

        SALARIO_LIQUIDO = salario_liquido(SALARIO_BRUTO, IMPOSTO_RENDA, TOTAL_DESCONTOS)

    elif cont == 3:
        SALARIO_BRUTO = 8000
        DEPENDENTES = 1
        PENSAO = 500
        IDOSO = "n"

        IDOSO = verificador_de_velhos(IDOSO)

        FAIXA = faixa_INSS(SALARIO_BRUTO)

        ISENCAO_DEPENDENTE = valor_dependete(SALARIO_BRUTO, DEPENDENTES, PENSAO)

        DESCONTO_INSS = valor_INSS(FAIXA, SALARIO_BRUTO)

        ISENCAO_IDOSO = valor_idoso(IDOSO)

        TOTAL_ISENCAO = somador_isencao(ISENCAO_DEPENDENTE, ISENCAO_IDOSO)
        TOTAL_DESCONTOS = somador_descontos(DESCONTO_INSS)

        VALOR_BASE = base_calculo(SALARIO_BRUTO, TOTAL_DESCONTOS, TOTAL_ISENCAO)

        FAIXA_IR = faixa_IR(VALOR_BASE)

        IMPOSTO_RENDA = valor_IR(FAIXA_IR, VALOR_BASE)

        SALARIO_LIQUIDO = salario_liquido(SALARIO_BRUTO, IMPOSTO_RENDA, TOTAL_DESCONTOS) 
    
    elif cont == 4:
        SALARIO_BRUTO = 3500
        DEPENDENTES = 0
        PENSAO = 0
        IDOSO = "S"

        IDOSO = verificador_de_velhos(IDOSO)

        FAIXA = faixa_INSS(SALARIO_BRUTO)

        ISENCAO_DEPENDENTE = valor_dependete(SALARIO_BRUTO, DEPENDENTES, PENSAO)

        DESCONTO_INSS = valor_INSS(FAIXA, SALARIO_BRUTO)

        ISENCAO_IDOSO = valor_idoso(IDOSO)

        TOTAL_ISENCAO = somador_isencao(ISENCAO_DEPENDENTE, ISENCAO_IDOSO)
        TOTAL_DESCONTOS = somador_descontos(DESCONTO_INSS)

        VALOR_BASE = base_calculo(SALARIO_BRUTO, TOTAL_DESCONTOS, TOTAL_ISENCAO)

        FAIXA_IR = faixa_IR(VALOR_BASE)

        IMPOSTO_RENDA = valor_IR(FAIXA_IR, VALOR_BASE)

        SALARIO_LIQUIDO = salario_liquido(SALARIO_BRUTO, IMPOSTO_RENDA, TOTAL_DESCONTOS)
    
    contracheque()
    cont += 1
print("********************")

# Teste Manual
print("Insira os valores para um teste manual:")

SALARIO_BRUTO = float(input("Bruto (R$): "))
DEPENDENTES = int(input("Dependentes: "))
PENSAO = float(input("Pensao (R$): "))
print("Mais de 65 anos?")
IDOSO = input("[s]im / [n]ão - ")

IDOSO = verificador_de_velhos(IDOSO)

FAIXA = faixa_INSS(SALARIO_BRUTO)

ISENCAO_DEPENDENTE = valor_dependete(SALARIO_BRUTO, DEPENDENTES, PENSAO)

DESCONTO_INSS = valor_INSS(FAIXA, SALARIO_BRUTO)

ISENCAO_IDOSO = valor_idoso(IDOSO)

TOTAL_ISENCAO = somador_isencao(ISENCAO_DEPENDENTE, ISENCAO_IDOSO)
TOTAL_DESCONTOS = somador_descontos(DESCONTO_INSS)

VALOR_BASE = base_calculo(SALARIO_BRUTO, TOTAL_DESCONTOS, TOTAL_ISENCAO)

FAIXA_IR = faixa_IR(VALOR_BASE)

IMPOSTO_RENDA = valor_IR(FAIXA_IR, VALOR_BASE)

SALARIO_LIQUIDO = salario_liquido(SALARIO_BRUTO, IMPOSTO_RENDA, TOTAL_DESCONTOS)

contracheque()

fim_script()
