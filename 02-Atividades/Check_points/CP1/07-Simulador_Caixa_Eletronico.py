# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 7:

        Simulador de Caixa Eletrônico: Crie um programa que simule um caixa eletrônico. 
        O usuário digita um valor de saque (inteiro, múltiplo de 10) e o programa calcula 
        a menor quantidade de cédulas necessárias. 
        Cédulas disponíveis: R$ 200, R$ 100, R$ 50, R$ 20 e R$ 10. 
        Valide se o valor é positivo, inteiro e múltiplo de 10. Exiba cada cédula usada e a quantidade.

        # Teste com estes valores:
        testes = [
            380,    # 1x R$200, 1x R$100, 1x R$50, 1x R$20, 1x R$10
            1250,   # 6x R$200, 0x R$100, 1x R$50, 0x R$20, 0x R$10
            70,     # 0x R$200, 0x R$100, 1x R$50, 1x R$20, 0x R$10
            15,     # Inválido — não é múltiplo de 10
            -100,   # Inválido — valor negativo
            0,      # Inválido — valor zero
        ]

        # Saída esperada (saque R$ 380):
        # === Saque: R$ 380 ===
        # R$ 200: 1 cédula(s)
        # R$ 100: 1 cédula(s)
        # R$ 50:  1 cédula(s)
        # R$ 20:  1 cédula(s)
        # R$ 10:  1 cédula(s)
        # Total de cédulas: 5
'''
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def apresentacao():
    print()
    print("+--------------------------------+")
    print("|  Simulador Caixa Eletrônico    | ")
    print("+--------------------------------+")
    print()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def fim_script():
    print()
    print("//////////////////////")
    print("/    Fim do script.  /")
    print("//////////////////////")
    print()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def conferidor_de_valor(valor: int):

    # Casting
    valor = int(valor)

    valor_valido = (valor % 10 == 0 and valor > 0) 

    return valor_valido
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def calculador_cedulas(valor: int):

    # Casting
    cedulas_10 = 0
    cedulas_20 = 0
    cedulas_50 = 0
    cedulas_100 = 0
    cedulas_200 = 0
    
    valor = int(valor)

    while valor > 0:
        if valor >= 200:
            valor = valor - 200
            cedulas_200 += 1
        
        elif valor >= 100:
            valor = valor - 100
            cedulas_100 += 1
        
        elif valor >= 50:
            valor = valor - 50
            cedulas_50 += 1
        
        elif valor >= 20:
            valor = valor - 20
            cedulas_20 += 1
        
        elif valor >= 10:
            valor = valor - 10
            cedulas_10 += 1
    
    total_cedulas = (cedulas_10 + cedulas_20 + cedulas_50 + cedulas_100 + cedulas_200)
    
    print("R$ 200:", cedulas_200, "cedula(s)")
    print("R$ 100:", cedulas_100, "cedula(s)")
    print("R$  50:", cedulas_50, "cedula(s)")
    print("R$  20:", cedulas_20, "cedula(s)")
    print("R$  10:", cedulas_10, "cedula(s)")
    print("------------------------------")
    print("Total cedulas: ", total_cedulas)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def erros_valor(valor_valido: bool, valor: int):

    # casting
    valor = int(valor)
    valor_valido = bool(valor_valido)

    if valor_valido:
        pass
    else:
        if (valor < 0):
            print("Inválido - Valor apresentado é negativo!")
        elif (valor % 10 != 0):
            print(f"Inválido - R$ {valor} não é múltiplo de 10.")
        elif valor == 0:
            print("Inválido - Valor Zero.")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

cont = 1

# Main ()

apresentacao()

# Teste Automatico
print("Teste Automatico")
print("*************************")
while cont <= 6:
    if cont == 1:
        VALOR = 380
        VALOR_VALIDO = conferidor_de_valor(VALOR)

    elif cont == 2:
        VALOR = 1250
        VALOR_VALIDO = conferidor_de_valor(VALOR)       

    elif cont == 3:
        VALOR = 70
        VALOR_VALIDO = conferidor_de_valor(VALOR)

    elif cont == 4:
        VALOR = 15
        VALOR_VALIDO = conferidor_de_valor(VALOR)

    elif cont == 5:
        VALOR = -100
        VALOR_VALIDO = conferidor_de_valor(VALOR)

    elif cont == 6:
        VALOR = 0
        VALOR_VALIDO = conferidor_de_valor(VALOR)

    if VALOR_VALIDO:
        print()
        print(f"==== Saque: R$ {VALOR} ====")
        calculador_cedulas(VALOR)
    else:
        print()
        erros_valor(VALOR_VALIDO, VALOR)
        print()
    
    cont += 1
print("*************************")

# Teste manual
print()
print("Insira os dados para um teste manual:")
VALOR = int(input("Valor (R$): "))
VALOR_VALIDO = conferidor_de_valor(VALOR)

if VALOR_VALIDO:
    print()
    print(f"==== Saque: R$ {VALOR} ====")
    calculador_cedulas(VALOR)
else:
    print()
    erros_valor(VALOR_VALIDO, VALOR)
    print()
    
fim_script()
