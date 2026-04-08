# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Numeros Primos: 
    Números Primos: Crie um programa que encontre todos os números primos entre 1 e 100. Um número é primo quando é maior que 1 e 
    divisível apenas por 1 e por ele mesmo. Para verificar, teste se o número é divisível por algum valor de 2 até ele-1 — se nenhum dividir, 
    é primo. Exiba os primos formatados em linhas de 10 números e ao final mostre o total encontrado.
    
    # Dica de lógica:
        # Para cada número N de 2 a 100:
        #     eh_primo = True
        #     Para cada divisor D de 2 a N-1:
        #         Se N % D == 0:
        #             eh_primo = False
        #             break (não precisa testar mais)

    # Saída esperada:
        #   2   3   5   7  11  13  17  19  23  29
        #  31  37  41  43  47  53  59  61  67  71
        #  73  79  83  89  97
        # Total de primos: 25
'''
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def apresentacao():
    print()
    print("+----------------+")
    print("| Numeros Primos | ")
    print("+----------------+")
    print()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def fim_script():
    print()
    print("//////////////////////")
    print("/    Fim do script.  /")
    print("//////////////////////")
    print()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def entrada_numero ():
    
    print("Indique os números para ver quantos primos tem no intervalo entre eles: ")
    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite outro número: "))
    
    return numero1, numero2
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def ajustador_de_intervalo (numero1: int, numero2: int):

    if numero1 > numero2:
        numero_inicio = numero2
        numero_fim = numero1
    else:
        numero_inicio = numero1
        numero_fim = numero2

    return numero_inicio, numero_fim
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def definidor_de_primos(numero_inicio: int, numero_fim: int):
    
    numero_inicio = int(numero_inicio)
    numero_fim = int(numero_fim)

    numeros_primos = []
    
    for numero in range(numero_inicio, numero_fim):
        if numero > 1:
            primo = True

            for d in range (2, numero):
                if numero % d == 0:
                    primo = False
                    break
                
            if primo:
                numeros_primos.append(numero)
                    
    return numeros_primos
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def formatador (numeros_primos, intervalo_inicio: int, intervalo_fim: int):

    print("Os números primos encontrados foram:")

    for primo in numeros_primos:
        print(primo, end = " ")

    print(f"\nExistem {len(numeros_primos)} números primos entre {intervalo_inicio} e {intervalo_fim}!")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def main ():

    autoteste()
    print()

    print("Execução Manual:")
    print()
    
    NUMERO1, NUMERO2 = entrada_numero()

    NUMERO_INICIO, NUMERO_FIM = ajustador_de_intervalo(NUMERO1, NUMERO2)

    NUMEROS_PRIMOS = definidor_de_primos(NUMERO_INICIO, NUMERO_FIM)

    formatador(NUMEROS_PRIMOS, NUMERO_INICIO, NUMERO_FIM)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def autoteste():
    print("Auto-Teste:")
    
    numero1 = 1
    numero2 = 100
    
    numero_inicio, numero_fim = ajustador_de_intervalo(numero1, numero2)

    numeros_primos = definidor_de_primos(numero_inicio, numero_fim)

    formatador(numeros_primos, numero_inicio, numero_fim)

apresentacao()

main()

fim_script()
