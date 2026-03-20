"""
1. Peça nome, idade e cidade e exiba mensagem formatada.
2. Calculadora simples.
3. Calcule o IMC.
"""

print()
print("1. Pede nome, idade e cidade e imprime-os no terminal")
print()

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
cidade = input("Digite sua cidade: ")

print("Olá {}, você tem {}, e mora em {}".format(nome, idade, cidade))

print("+++++++++++++++++++++++++++++++++++")
print()

print("2. Calculadora simples. Soma, subtrai, multiplica e divide 2 numeros inteiros solicitados")
print()

n1 = input("Digite o primeiro numero: ")
n2 = input("Diite o segundo numero: ")

n1 = int(n1)
n2 = int(n2)

soma = (n1 + n2)
sub = (n1 - n2)
prod = (n1 * n2)
quo = (n1 / n2)

print(f"Soma = {soma}")
print(f"Subtração = {sub}")
print(f"Multiplicação = {prod}")
print(f"Divisão = {quo}")

print()
print("+++++++++++++++++++++++++++++++++++")
print()

print("3. Calcule o IMC.")
print()

print(f"{nome}, indique seu peso e altura:")
peso = input("Peso:" )
altura = input("Altura: ")

peso = float(peso)
altura = float(altura)

imc = peso/(altura ** 2)

print(f"{nome}, seu IMC é de {imc}!")
