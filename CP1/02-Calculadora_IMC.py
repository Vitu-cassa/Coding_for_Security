# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 2:
        Calculadora de IMC: Crie um programa que peça peso (kg) e altura (m), calcule o IMC (peso / altura²) e exiba a 
        classificação: abaixo do peso (< 18.5), peso normal (18.5 - 24.9), sobrepeso (25.0 - 29.9), obesidade (≥ 30.0). Exiba o resultado com 1 casa decimal.



        # Teste com estes valores:
        testes = [
            (52.0, 1.75),   # IMC 17.0 → Abaixo do peso
            (70.0, 1.75),   # IMC 22.9 → Peso normal
            (85.0, 1.70),   # IMC 29.4 → Sobrepeso
            (110.0, 1.65),  # IMC 40.4 → Obesidade
        ]

        # Saída esperada:
        # Peso: 70.0 kg | Altura: 1.75 m
        # IMC: 22.9 - Peso normal
'''
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def calculadora_imc(peso: float, altura: float):
    
    # Casting
    peso = float(peso)
    altura = float(altura)

    # Verifica se altura é maior que zero
    
    if altura <= 0:
        return "Altura inválida"
    else:
        # calculo do IMC

        imc = peso / (altura * altura)

        # Define se a pessoa esta com sobrepeso ou não

        abaixo = (imc < 18.5)
        normal = (18.5 <= imc <= 24.9)
        sobrepeso = (25.0 <= imc <= 29.9)
        obesidade = imc >= 30

        # Retorna as mensagens
        if abaixo:
            return f"{imc:.1f} -> abaixo do peso."
        elif normal:
            return "{:.1f} -> Peso normal.".format(imc)
        elif sobrepeso:
            return "{:.1f} -> Sobrepeso".format(imc)
        elif obesidade:
            return "{:.1f} -> Obesidade".format(imc)
        else:
            return "Verifique se os dados foram digitados corretamente!"
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def apresentacao():
    print()
    print("+-------------------------+")
    print("|     Calculadora IMC     |")
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

print("Testes automatizados:")

print(calculadora_imc(52.0, 1.75))
print("******************************")

print(calculadora_imc(70.0, 1.75))
print("******************************")

print(calculadora_imc(85.0, 1.75))
print("******************************")

print(calculadora_imc(110.0, 1.75))
print("******************************")

print("\n+++++++++++++++++++++++++++++++++++++++++++++++++")
print("\nIndique um peso e altura para um teste manual:")

peso = input("Indique o peso (Kg): ")
altura = input("Indique altura (m): ")

print()
print(calculadora_imc(peso, altura))

fim_script()
