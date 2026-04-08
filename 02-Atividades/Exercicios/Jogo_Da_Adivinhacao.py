# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Jogo de Adivinhação
    Crie um jogo onde o computador sorteia um número entre 1 e 50 e o jogador tenta adivinhar.
    A cada tentativa, o programa diz se o palpite é "muito alto" ou "muito baixo". 
    O jogador tem no máximo 7 tentativas. Exiba quantas tentativas foram usadas ao acertar,
    e ao errar mostre qual era o número. Trate entradas inválidas (letras, negativos)
    sem gastar tentativa. 
    Use import random e random.randint(1, 50).

    import random

    # Exemplo de partida (número sorteado: 32):
    # === Jogo de Adivinhação ===
    # Tentei um número entre 1 e 50. Adivinhe!
    # Você tem 7 tentativas.
    #
    # Tentativa 1/7: 25
    # Muito baixo! ↑
    #
    # Tentativa 2/7: 40
    # Muito alto! ↓
    #
    # Tentativa 3/7: abc
    # Entrada inválida! Digite um número. (não conta como tentativa)
    #
    # Tentativa 3/7: 32
    # Parabéns! Acertou em 3 tentativas!

    # Se esgotar as tentativas:
    # Suas tentativas acabaram! O número era 32.
'''
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def apresentacao():
    print()
    print("+---------------------+")
    print("| Jogo da adivinhação | ")
    print("+---------------------+")
    print()

    print("Você tem 7 tentativas para acertar o numero que o computador escolheu!")
    print()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def fim_script():
    print()
    print("//////////////////////")
    print("/    Fim do script.  /")
    print("//////////////////////")
    print()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def numero_misterioso():

    print("O computador esta selecionando um numero.")

    for i in range(1,4):
        print(".")
        time.sleep(1)
    
    numero_misterioso = random.randint(1,50)

    return (numero_misterioso)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def comparador(numero_sorteado: int, numero_jogador: int):

    errou = False
    numero_jogador = int(numero_jogador)
    numero_sorteado = int(numero_sorteado)
    
    if numero_jogador > numero_sorteado:
        print('O numero é menor!')
        resultado = "errou"
    
    elif numero_jogador < numero_sorteado:
        print('O número é maior!')
        resultado = "errou"
    
    else:
        resultado = "acertou"
    
    return resultado
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def contador_de_vidas(vidas_jogador: int, resultado: str, tentativas: int):

    vidas_jogador = int(vidas_jogador)
    
    if resultado == "errou":
        vidas_jogador -= 1
        tentativas += 1
    
    return vidas_jogador, tentativas
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def fim_de_jogo(resultado: str, vidas: int, tentativas: int):
    
    if resultado == "acertou":
        print(f"\nParabéns! conseguiu em {tentativas} tentativas")
    else:
        print(f"\nSuas vidas chegaram à {vidas}.")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def main():

    apresentacao()

    VIDAS = 7
    NUMERO_SORTEADO = numero_misterioso()
    RESULTADO = None
    TENTATIVAS = 0

    while VIDAS > 0:
        print()

        if RESULTADO == "acertou":
            break
        
        else:
            print(f"Tentativa {VIDAS}/7:")
            numero_jogador = input("Seu palpite: ")
            print()
        
        if numero_jogador.isnumeric():
            
            RESULTADO = comparador(NUMERO_SORTEADO,  numero_jogador)
            VIDAS, TENTATIVAS = contador_de_vidas(VIDAS, RESULTADO, TENTATIVAS)

        else:
            print("Valor invalido!")
        
    fim_de_jogo(RESULTADO, VIDAS, TENTATIVAS)

    fim_script()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import random
import time

main()
