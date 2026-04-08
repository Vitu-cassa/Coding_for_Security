def definidor_de_idade(idade: int):
    idade = int(idade)

    if idade < 0:
        return "Idade invalida!"

    elif idade <= 11:
        return "criança"
    elif idade <=17:
        return "Adolescente"
    elif idade <= 17:
        return "Adulto"
    else:
        return "idoso"


print(definidor_de_idade(5))

print("********************************")

print(definidor_de_idade(15))

print("********************************")

print(definidor_de_idade(25))

print("********************************")

print(definidor_de_idade(70))

print("********************************")

print(definidor_de_idade(-3))

print("********************************")

print(definidor_de_idade(150))

print("********************************")