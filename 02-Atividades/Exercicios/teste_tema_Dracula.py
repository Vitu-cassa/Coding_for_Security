# Mega-demo de teste do esquema de cores no Dracula
# Comentários verdes e itálicos

import math
import random

# Constantes globais
PI = 3.14159
MAX_ITERACOES = 10

# Classe com métodos e variáveis de instância
class Circulo:
    def __init__(self, raio):
        self.raio = raio
        self.area = 0
        self.perimetro = 0

    def calcula_area(self):
        self.area = PI * self.raio ** 2
        return self.area

    def calcula_perimetro(self):
        self.perimetro = 2 * PI * self.raio
        return self.perimetro

# Função com parâmetros e variáveis locais
def imprime_resultado(circulo):
    area = circulo.calcula_area()
    perimetro = circulo.calcula_perimetro()
    mensagem = f"Círculo: raio={circulo.raio}, área={area}, perímetro={perimetro}"
    print(mensagem)

# Listas, dicionários e loops
numeros = [1, 2, 3, 4, 5]
quadrados = {n: n**2 for n in numeros}
cubos = {n: n**3 for n in numeros}

for n in numeros:
    print(f"{n} ao quadrado é {quadrados[n]}, ao cubo é {cubos[n]}")

# Condicionais e operadores
x = 10
y = random.randint(1, 10)
if x > y:
    resultado = x - y
else:
    resultado = x + y

# Operadores diversos
soma = x + y
produto = x * y
divisao = x / y
resto = x % y
potencia = x ** y

# Criando objetos e chamando métodos
c1 = Circulo(7)
imprime_resultado(c1)

c2 = Circulo(5)
imprime_resultado(c2)

# Strings e formatação
nome = "Python"
mensagem_final = f"Olá {nome}, esta é uma demonstração completa do tema Dracula."
print(mensagem_final)

# Mais comentários finais
# Variáveis: x, y, soma, produto, divisao, resto, potencia, area, perimetro
# Estruturas: listas, dicionários, loops, condicionais
# Constantes: PI, MAX_ITERACOES
# Funções: calcula_area, calcula_perimetro, imprime_resultado, print
# Classes: Circulo