"""
1. Peça nome, idade e cidade e exiba mensagem formatada.
2. Calculadora simples.
3. Calcule o IMC.
"""

class Exercicio:
    def __init__(self, nome: str, idade: int, cidade: str, n1: int, n2: int, peso: float, altura: float):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.n1 = n1
        self.n2 = n2
        self.peso = peso
        self.altura = altura

    def exercicio1 (self):
        print(f"Olá {self.nome}. Você tem {self.idade} anos e mora em {self.cidade}!")
    
    def exercicio2 (self):
        
        self.n1 = int(self.n1)
        self.n2 = int(self.n2)

        soma = self.n1 + self.n2
        sub = self.n1 - self.n2
        mult = self.n1 * self.n2
        div = self.n1 / self.n2

        print(f"As quatro operações basicas usando {self.n1} e {self.n2} são: ")
        print(f"Soma = {soma}")
        print(f"Subtração = {sub}")
        print(f"Multiplicação = {mult}")
        print(f"Divisão = {div}")

# Main

nome = input("Indique seu nome: ")
idade = input("Indique sua idade: ")
cidade = input("Indique sua cidade: ")

cadastro = Exercicio(
    nome = nome,
    idade = idade,
    cidade = cidade
)

cadastro.exercicio1()

cadastro = Exercicio(
    n1 = input("Indique um numero: "),
    n2 = input("Digite outro numero: ")
)


cadastro.exercicio2()

print(vars(cadastro))