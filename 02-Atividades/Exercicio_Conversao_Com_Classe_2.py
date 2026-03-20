class Exercicio():

    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.n1 = 0
        self.n2 = 0
        self.peso = 0
        self.altura = 0

    def ImprimeInformacoes(self):
        print(f"Olá {self.nome}! Você tem {self.idade} e mora em {self.cidade}.")
        print(f"Para o exercicio da calculadora você indicou os numeros {self.n1} e {self.n2}:")
        self.Calculadora()
       # print(f"Você indicou que pesa {self.peso} e tem {self.altura}.")

    def Numeros(self, n1, n2):
        self.n1 = int(n1)
        self.n2 = int(n2)
    
    def Calculadora(self):
        soma = self.n1 + self.n2
        subtracao = self.n1 - self.n2
        multiplicacao = self.n1 * self.n2
        divisao = self.n1 / self.n2

        print(f"Soma = {soma}")
        print(f"Subtracao = {subtracao}")
        print(f"Multiplicação = {multiplicacao}")
        print(f"Divisão = {divisao}")


    def PesoAltura(self, peso, altura):
        self.peso = float(peso)
        self.altura = float(altura)



    def PulaLinha():
        print()
        print("++++++++++++++++++++++++++++++++")
        print()


    
usuario1 = Exercicio(
    nome = input("nome: "),
    idade = input("idade: "),
    cidade = input("Cidade: ")
)
print(vars(usuario1))

Exercicio.PulaLinha()

usuario1.Numeros(
    n1 = input("Indique um numero: "),
    n2 = input("Indique outro numero: ")
)
print(vars(usuario1))

Exercicio.PulaLinha()

usuario1.PesoAltura(
    peso = input("Indique seu peso: "),
    altura = input("Sua altura: ")
)
print(vars(usuario1))

Exercicio.PulaLinha()

usuario1.ImprimeInformacoes()