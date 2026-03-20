#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 3:
        Conversor de Moedas: Crie um programa que exiba um menu com 3 opções de 
        conversão: Real → Dólar, Real → Euro, Real → Libra. O usuário escolhe a opção, 
        digita o valor em reais e o programa exibe o valor convertido com 2 casas decimais. 
        Se o usuário escolher uma opção inválida, exiba "Opção inválida". Se digitar um valor negativo, exiba "Valor inválido".


        # Cotações fixas para o exercício:

        cotacoes = {
            "dolar": 5.15,
            "euro": 5.55,
            "libra": 6.45
        }


        # Menu:
        # [1] Real → Dólar
        # [2] Real → Euro
        # [3] Real → Libra

        # Teste: opção 1, valor R$ 100.00
        # Saída: R$ 100.00 = US$ 19.42

        # Teste: opção 2, valor R$ 250.00
        # Saída: R$ 250.00 = € 45.05

        # Teste: opção 5
        # Saída: Opção inválida
'''
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# menu para seleção de opção
def menu():
    print("\nEscolha uma das opções para conversão:")
    print("[1] Real → Dólar")
    print("[2] Real → Euro")
    print("[3] Real → Libra")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Converte em dolar
def real_dolar(real: float):
    real = float(real)

    # Converte para dolar
    dolar = real * 5.15
    return dolar
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Converte em euro
def real_euro(real: float):
    real = float(real)

    # Converte para euro
    euro = real * 5.55
    return euro
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Converte em libra
def real_libra(real: float):
    real = float(real)

    # Converte para libra
    libra = real * 6.45
    return libra
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def apresentacao():
    print()
    print("$$$$$$$$$$$$$$$$$$$$$$$")
    print("$ Conversor de moedas $")
    print("$$$$$$$$$$$$$$$$$$$$$$$")
    print()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def fim_script():
    print()
    print("//////////////////////")
    print("/    Fim do script.  /")
    print("//////////////////////")
    print()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Main()

apresentacao()

real = float(input("Digite a quantidade para conversão (R$): "))

menu()

escolha = input("\nDigite a opção: ")

if escolha == "1":
    dolar = real_dolar(real)
    print("\nR$ {:.2f} = US$ {:.2f}".format(real, dolar))

elif escolha == "2":
    euro = real_euro(real)
    print("\nR$ {:.2f} = € {:.2f}".format(real, euro))

elif escolha == "3":
    libra = real_libra(real)
    print("\nR$ {:.2f} = £ {:.2f}".format(real, libra))

else:
    print("\nOpção inválida!")

fim_script()
