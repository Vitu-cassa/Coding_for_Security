# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercicio 1:
        Verificador de Idade: Crie um programa que peça a idade do usuário e exiba se ele é criança (0-11), adolescente (12-17), adulto (18-59) ou idoso (60+). 
        Se a idade for negativa ou maior que 120, exiba "Idade inválida".



        Teste com estas idades:
        idades = [5, 15, 25, 70, -3, 150]

        # Saída esperada:
        # Idade 5   → Criança
        # Idade 15  → Adolescente
        # Idade 25  → Adulto
        # Idade 70  → Idoso
        # Idade -3  → Idade inválida
        # Idade 150 → Idade inválida

        # BONUS: considere os meses e se o mes for < 0 ou > que 12 devolva o erro "Mes Invalido"
        Teste com os meses:
        meses[0, 2, 5, 6, 11, 13]    

        # Saída esperada:
        # Idade 5   → Mês Inválido
        # Idade 15  → Adolescente
        # Idade 25  → Adulto
        # Idade 70  → Idoso
        # Idade -3  → Idade inválida
        # Idade 150 → Mês Inválido
'''
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def definidor_de_idade(idade_em_anos: int, idade_em_meses: int = 0):
    
    idade_em_anos = int(idade_em_anos)
    idade_em_meses = int(idade_em_meses)

    if idade_em_meses <= 0 or idade_em_meses > 12:
        return "\nMês invalido"
    
    else:
        if idade_em_anos < 0 or idade_em_anos > 120:
            return "\n{} anos e {} meses -> Idade inválida".format(idade_em_anos, idade_em_meses)
        elif idade_em_anos <= 11:
            return f"\n{idade_em_anos} anos e {idade_em_meses} meses -> Criança"
        elif idade_em_anos <= 17:
            return "\n{} anos e {} meses -> Adolescente".format(idade_em_anos, idade_em_meses)
        elif idade_em_anos <= 59:
            return "\n{} anos e {} meses -> Adulto".format(idade_em_anos, idade_em_meses)
        else:
            return "\n{} anos e {} meses -> Idoso".format(idade_em_anos, idade_em_meses)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def apresentacao():
    print()
    print("+-------------------------+")
    print("|    Definidor de Idade   |")
    print("+-------------------------+")
    print()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def fim_script():
    print()
    print("//////////////////////")
    print("/    Fim do script.  /")
    print("//////////////////////")
    print()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    

# Main()

apresentacao()

# Testes automatizados

print("Teste das idades (automatico):")
print("********************************")
print(definidor_de_idade(5, 10))

print("********************************")
print(definidor_de_idade(15, 10))

print("********************************")
print(definidor_de_idade(25, 3))

print("********************************")
print(definidor_de_idade(70, 4))

print("********************************")
print(definidor_de_idade(-3, 5))

print("********************************")
print(definidor_de_idade(150, 1))

print("********************************")

print("\n++++++++++++++++++++++++++++++++++++++++++++++++++")
print()

print("Teste meses (Automatizado):")
print("********************************")
print(definidor_de_idade(5, 0))

print("********************************")
print(definidor_de_idade(15, 2))

print("********************************")
print(definidor_de_idade(25, 5))

print("********************************")
print(definidor_de_idade(70, 6))

print("********************************")
print(definidor_de_idade(-3, 11))

print("********************************")
print(definidor_de_idade(150, 13))

print("********************************")
print("\n++++++++++++++++++++++++++++++++++++++++++++++++++")
print()

# Teste manual
print("Indique uma idade e meses para um teste manual:")
idade = input("idade: ")
mes = input("meses: ")

print(definidor_de_idade(idade, mes))

fim_script()
