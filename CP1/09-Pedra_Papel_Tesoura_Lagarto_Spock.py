# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 9:
Jogo de Pedra, Papel, Tesoura, Lagarto, Spock 
Crie o jogo expandido (da série The Big Bang Theory). O usuário escolhe por número (1-5) e o computador escolhe aleatoriamente.
As regras são: Tesoura corta Papel, Papel cobre Pedra, Pedra esmaga Lagarto, Lagarto envenena Spock, Spock derrete Tesoura, 
Tesoura decapita Lagarto, Lagarto come Papel, Papel refuta Spock, Spock vaporiza Pedra, Pedra quebra Tesoura. 
Exiba as escolhas, quem ganhou e o motivo (ex: "Spock vaporiza Pedra"). 
Use o módulo random para a escolha do computador — importe com import random e use random.randint(1, 5) para 
gerar um número aleatório entre 1 e 5.

import random

# Opções:
# 1 = Pedra
# 2 = Papel
# 3 = Tesoura
# 4 = Lagarto
# 5 = Spock

# Tabela de vitórias — quem a chave vence e com qual ação:
# Pedra    vence Tesoura ("quebra") e Lagarto ("esmaga")
# Papel    vence Pedra ("cobre") e Spock ("refuta")
# Tesoura  vence Papel ("corta") e Lagarto ("decapita")
# Lagarto  vence Papel ("come") e Spock ("envenena")
# Spock    vence Pedra ("vaporiza") e Tesoura ("derrete")

# Teste: Jogador escolhe 5 (Spock), computador escolhe 1 (Pedra)
# Saída:
# Você: Spock
# Computador: Pedra
# Spock vaporiza Pedra — Você venceu!

# Teste: Jogador escolhe 3 (Tesoura), computador escolhe 5 (Spock)
# Saída:
# Você: Tesoura
# Computador: Spock
# Spock derrete Tesoura — Computador venceu!

# Teste: Jogador escolhe 2 (Papel), computador escolhe 2 (Papel)
# Saída:
# Você: Papel
# Computador: Papel
# Empate!
'''
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def apresentacao():
    print()
    print("+-----------------------------------------------+")
    print("| Jogo de Pedra, Papel, Tesoura, Lagarto, Spock | ")
    print("+-----------------------------------------------+")
    print()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def fim_script():
    print()
    print("//////////////////////")
    print("/    Fim do script.  /")
    print("//////////////////////")
    print()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def menu_opcoes():
    print("Escolha entre 1 e 5 para jogar:")
    print("Opções:")
    print()
    print("1 = Pedra")
    print("2 = Papel")
    print("3 = Tesoura")
    print("4 = Lagarto")
    print("5 = Spock")
    print()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def escolha(escolha: int):

    # Casting
    escolha = int(escolha)

    if escolha == 1:
        define_escolha = "pedra"
        return define_escolha
    elif escolha == 2:
        define_escolha = "papel"
        return define_escolha
    elif escolha == 3:
        define_escolha = "tesoura"
        return define_escolha
    elif escolha == 4:
        define_escolha = "lagarto"
        return define_escolha
    elif escolha == 5:
        define_escolha = "spock"
        return define_escolha
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def vencedor(escolha_jogador: int, escolha_computador: int):

    # Casting
    escolha_computador = int(escolha_computador)
    escolha_jogador = int(escolha_jogador)

    if escolha_jogador == 1 and (escolha_computador == 3 or escolha_computador == 4):
        vencedor = "Jogador"
    elif escolha_jogador == 2 and (escolha_computador == 1 or escolha_computador == 5):
        vencedor = "Jogador"
    elif escolha_jogador == 3 and (escolha_computador == 2 or escolha_computador == 4):
        vencedor = "Jogador"
    elif escolha_jogador == 4 and (escolha_computador == 2 or escolha_computador == 5):
        vencedor = "Jogador"
    elif escolha_jogador == 5 and (escolha_computador == 1 or escolha_computador == 3):
        vencedor = "Jogador"
    else:
        vencedor = "Computador"
    
    return vencedor
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def condicao_vitoria(vencedor, perdedor):

    condicao_vitoria = None
# Tabela de vitórias — quem a chave vence e com qual ação:
# Pedra    vence Tesoura ("quebra") e Lagarto ("esmaga")
# Papel    vence Pedra ("cobre") e Spock ("refuta")
# Tesoura  vence Papel ("corta") e Lagarto ("decapita")
# Lagarto  vence Papel ("come") e Spock ("envenena")
# Spock    vence Pedra ("vaporiza") e Tesoura ("derrete")

    if vencedor == "pedra" and perdedor == "tesoura":
        condicao_vitoria = "quebra"
    
    elif vencedor == "pedra" and perdedor == "lagarto":
        condicao_vitoria = "esmaga"

    elif vencedor == "papel" and perdedor == "pedra":
        condicao_vitoria = "cobre"

    elif vencedor == "papel" and perdedor == "spock":
        condicao_vitoria = "refuta"

    elif vencedor == "tesoura" and perdedor == "papel":
        condicao_vitoria = "corta"

    elif vencedor == "tesoura" and perdedor == "lagarto":
        condicao_vitoria = "decapita"

    elif vencedor == "lagarto" and perdedor == "papel":
        condicao_vitoria = "come"

    elif vencedor == "lagarto" and perdedor == "spock":
        condicao_vitoria = "envenena"

    elif vencedor == "spock" and perdedor == "pedra":
        condicao_vitoria = "vaporiza"

    elif vencedor == "spock" and perdedor == "tesoura":
        condicao_vitoria = "derrete"

    return condicao_vitoria   
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def hora_do_duelo(vencedor, perdedor):

    print(f"Jogador: {JOGADOR}")
    print(f"Computador: {COMPUTADOR}")

    print(f"{vencedor} {CONDICAO_VENCEDOR} {perdedor} - {VENCEDOR} venceu!")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
# Main()

import random
cont = 1

apresentacao()

menu_opcoes()
# Teste Automatico
print("Auto-teste")
print("**********************")
while cont <= 3:
    print("+++++++++++++++++++")
    print()

    if cont == 1:
        ESCOLHA_JOGADOR = 5
        ESCOLHA_COMPUTADOR = 1

        JOGADOR = escolha(ESCOLHA_JOGADOR)
        COMPUTADOR = escolha(ESCOLHA_COMPUTADOR)
        VENCEDOR = vencedor(ESCOLHA_JOGADOR, ESCOLHA_COMPUTADOR)

        if ESCOLHA_JOGADOR == ESCOLHA_COMPUTADOR:
            print(f"Jogador: {JOGADOR}")
            print(f"Computador: {COMPUTADOR}")
            print("Empate!")
        else:
            if VENCEDOR == "Jogador":
                CONDICAO_VENCEDOR = condicao_vitoria(JOGADOR, COMPUTADOR)
                hora_do_duelo(JOGADOR, COMPUTADOR)
            else:
                CONDICAO_VENCEDOR = condicao_vitoria(COMPUTADOR, JOGADOR)
                hora_do_duelo(COMPUTADOR, JOGADOR)

    elif cont == 2:
        ESCOLHA_JOGADOR = 3
        ESCOLHA_COMPUTADOR = 5

        JOGADOR = escolha(ESCOLHA_JOGADOR)
        COMPUTADOR = escolha(ESCOLHA_COMPUTADOR)
        VENCEDOR = vencedor(ESCOLHA_JOGADOR, ESCOLHA_COMPUTADOR)

        if ESCOLHA_JOGADOR == ESCOLHA_COMPUTADOR:
            print(f"Jogador: {JOGADOR}")
            print(f"Computador: {COMPUTADOR}")
            print("Empate!")
        else:
            if VENCEDOR == "Jogador":
                CONDICAO_VENCEDOR = condicao_vitoria(JOGADOR, COMPUTADOR)
                hora_do_duelo(JOGADOR, COMPUTADOR)
            else:
                CONDICAO_VENCEDOR = condicao_vitoria(COMPUTADOR, JOGADOR)
                hora_do_duelo(COMPUTADOR, JOGADOR)

    elif cont == 3:
        ESCOLHA_JOGADOR = 2
        ESCOLHA_COMPUTADOR = 2

        JOGADOR = escolha(ESCOLHA_JOGADOR)
        COMPUTADOR = escolha(ESCOLHA_COMPUTADOR)
        VENCEDOR = vencedor(ESCOLHA_JOGADOR, ESCOLHA_COMPUTADOR)

        if ESCOLHA_JOGADOR == ESCOLHA_COMPUTADOR:
            print(f"Jogador: {JOGADOR}")
            print(f"Computador: {COMPUTADOR}")
            print("Empate!")
        else:
            if VENCEDOR == "Jogador":
                CONDICAO_VENCEDOR = condicao_vitoria(JOGADOR, COMPUTADOR)
                hora_do_duelo(JOGADOR, COMPUTADOR)
            else:
                CONDICAO_VENCEDOR = condicao_vitoria(COMPUTADOR, JOGADOR)
                hora_do_duelo(COMPUTADOR, JOGADOR)
    print()
    cont += 1
print("**********************")

# Teste manual
print("Arrisque uma partida contra o computador!")
print()

menu_opcoes()

ESCOLHA_JOGADOR = int(input("Escolha uma opção: "))
ESCOLHA_COMPUTADOR = random.randint(1, 5)
print()

JOGADOR = escolha(ESCOLHA_JOGADOR)
COMPUTADOR = escolha(ESCOLHA_COMPUTADOR)
VENCEDOR = vencedor(ESCOLHA_JOGADOR, ESCOLHA_COMPUTADOR)

if ESCOLHA_JOGADOR == ESCOLHA_COMPUTADOR:
    print(f"Jogador: {JOGADOR}")
    print(f"Computador: {COMPUTADOR}")
    print("Empate!")
elif ESCOLHA_JOGADOR > 5:
    print("Escolha uma opção valida!")

else:
    if VENCEDOR == "Jogador":
        CONDICAO_VENCEDOR = condicao_vitoria(JOGADOR, COMPUTADOR)
        hora_do_duelo(JOGADOR, COMPUTADOR)
    else:
        CONDICAO_VENCEDOR = condicao_vitoria(COMPUTADOR, JOGADOR)
        hora_do_duelo(COMPUTADOR, JOGADOR)

fim_script()
