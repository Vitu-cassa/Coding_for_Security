# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 4:
        Classificador de Triângulos: Crie um programa que peça 3 valores representando os lados de um triângulo. 
        Primeiro, verifique se os valores formam um triângulo válido 
        (a soma de dois lados deve ser maior que o terceiro — teste as 3 combinações). 
        Se for válido, classifique como equilátero (3 lados iguais), isósceles (2 lados iguais) ou escaleno (3 lados diferentes). 
        Se não for válido, exiba "Não forma triângulo".


        # Teste com estes valores:

        testes = [
            (5, 5, 5),    # Equilátero
            (5, 5, 3),    # Isósceles
            (3, 4, 5),    # Escaleno
            (1, 2, 10),   # Não forma triângulo (1 + 2 < 10)
            (0, 5, 5),    # Não forma triângulo (lado zero)
            (7, 7, 12),   # Isósceles
        ]


        # Saída esperada:
        # Lados: 3, 4, 5
        # Triângulo válido: Escaleno
        #
        # Lados: 1, 2, 10
        # Não forma triângulo
'''
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def definidor_de_triangulos(lado1: int, lado2: int, lado3: int):
    # Casting
    lado1 = int(lado1)
    lado2 = int(lado2)
    lado3 = int(lado3)

    # chave para verificar se forma triângulo

    forma = (lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado1 + lado2))

    if forma:
        if (lado1 == lado2 == lado3):
            return f"lados: {lado1}, {lado2}, {lado3} \nTriângulo válido: Equilatero."
        elif ((lado2 == lado1) or (lado2 == lado3) or (lado2 == lado3)):
            return f"lados: {lado1}, {lado2}, {lado3} \nTriângulo válido: Isósceles."
        else:
            return f"lados: {lado1}, {lado2}, {lado3} \nTriângulo válido: Escaleno."
    else:
        return "Os lados {}, {} e {} não formam um triângulo.".format(lado1, lado2, lado3)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def apresentacao():
    print()
    print("+-------------------------+")
    print("| Definidor de Triangulos |")
    print("+-------------------------+")
    print()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def fim_script():
    print()
    print("//////////////////////")
    print("/    Fim do script.  /")
    print("//////////////////////")
    print()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# main()
apresentacao()

print("Testes automatizados:")
print("***************************************")
print(definidor_de_triangulos(5,5,5))
print("***************************************")
print(definidor_de_triangulos(5,5,3))
print("***************************************")
print(definidor_de_triangulos(3,4,5))
print("***************************************")
print(definidor_de_triangulos(1,2,10))
print("***************************************")
print(definidor_de_triangulos(0,5,5))
print("***************************************")
print(definidor_de_triangulos(7,7,12))
print("***************************************")
print()

print("Insira os lados do triangulo para um teste manual:")
lado1 = input("Primeiro lado: ")
lado2 = input("Segundo lado: ")
lado3 = input("Terceiro lado: ")

print("\n" + definidor_de_triangulos(lado1, lado2, lado3))

fim_script()
