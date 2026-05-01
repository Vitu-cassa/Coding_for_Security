# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 7 — Calculadora Segura com Exceções:
        Crie uma calculadora que opere em loop (while True) pedindo dois
        números e uma operação (+, -, *, /).
        O programa deve tratar com try/except: entrada não numérica (ValueError),
        divisão por zero (ZeroDivisionError) e operação inválida.
        Use else para exibir o resultado quando não houver erro e finally para
        exibir "Operação processada."
        sempre. O usuário pode digitar "sair" para encerrar.

    # Sequência de teste:
        # Número 1: abc     → "Erro: Digite apenas números!"
        # Número 1: 10
        # Número 2: 0
        # Operação: /       → "Erro: Divisão por zero!"
        # Número 1: 10
        # Número 2: 3
        # Operação: /       → "Resultado: 3.33"
        # Número 1: 5
        # Número 2: 3
        # Operação: %       → "Erro: Operação '%' não suportada. Use +, -, * ou /"
        # Número 1: sair    → "Encerrando calculadora."

        # Cada interação deve exibir ao final:
        # "Operação processada." (via finally)
'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def _apresentacao():
    print()
    print("+---------------------+")
    print("|  Calculadora Segura |")
    print("+---------------------+")
    print()

def _fim_script():
    print()
    print("//////////////////////")
    print("/     Fim script     /")
    print("//////////////////////")
    print()

def _Solicitador_numeros():
    '''
    Função verifica se a entrada digitada é um numero, e retorna verdadeiro
    caso sim.
    '''

    n = ""
    operando = True

    while operando:
        try:
            n = input("Digite o numero: ")
            if n.lower() == "sair":
                operando = False
                parar = True
            else:
                n = float(n)
                parar = False
                operando = False
        except ValueError:
            print("Erro: Digite apenas números!")

    return n, parar

def _menu():
    print()
    print("===== Escolha uma das operações =====")
    print()
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

def _somar(n1, n2):
    '''
    Recebe os dois numeros digitado imprime a soma entre eles.
    '''
    try:
        soma = (n1 + n2) 
        print("\n{:.2f}".format(soma))
    except:
        print("\nErro inesperado!")

def _subtrair(n1, n2):
    '''
    Recebe os dois numeros digitado imprime a subtração entre eles.
    '''
    try:
        sub = (n1 - n2) 
        print("\n{:.2f}".format(sub))
    except:
        print("\nErro inesperado!")

def _multiplicar(n1, n2):
    '''
    Recebe os dois numeros digitado imprime o produto entre eles.
    '''
    try:
        produto = (n1 * n2) 
        print("\n{:.2f}".format(produto))
    except:
        print("\nErro inesperado!")

def _dividir(n1, n2):
    '''
    Recebe os dois numeros digitado imprime o quociente entre eles.
    '''
    try:
        produto = (n1 / n2) 
        print("\n{:.2f}".format(produto))
    except ZeroDivisionError:
        print("\nErro: Divisão por Zero!")
    except:
        print("\nErro inesperado!")

def main():

    _apresentacao()
    continuar = True
    interromper = False

    while True:

        if interromper: break
        
        print("indique o primeiro numero:")
        numero_1, interromper = _Solicitador_numeros()
        if interromper: break

        print("indique o Segundo numero:")
        numero_2, interromper = _Solicitador_numeros()
        if interromper: break

        try:
            while continuar:

                    _menu()
                    opcao = input("\nDigite a opção desejada: ")
                    try:
                        if opcao == "1":
                            _somar(numero_1, numero_2)
                            continuar = False
                        elif opcao == "2":
                            _subtrair(numero_1, numero_2)
                            continuar = False
                        elif opcao == "3":
                            _multiplicar(numero_1, numero_2)
                            continuar = False
                        elif opcao == "4":
                            _dividir(numero_1, numero_2)
                            continuar = False
                        elif opcao == "5":
                            print("Encerrando calculadora.")
                            continuar = False
                        elif any(opcao):
                            print("Operação {} não suportada!".format(opcao))
                    except ValueError:
                        print("Digite um valor valido.")
        finally:
            print("\nOperação processada.")
            interromper = True


    _fim_script()

main()
