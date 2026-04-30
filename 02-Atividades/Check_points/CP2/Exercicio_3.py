# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 3 — Gerenciador de Lista de IPs: 
        Crie um programa com menu interativo (usando while True) que gerencie
        uma lista de endereços IP. O menu deve ter as opções:
        [1] Adicionar IP, [2] Remover IP, [3] Listar todos, [4] Buscar IP,
        [5] Sair.
        Não permita IPs duplicados na lista. Na busca, informe se o IP foi 
        encontrado e em qual posição. Use break para sair do loop quando o 
        usuário escolher a opção 5.

        # Lista inicial para teste:
            ips = ["192.168.1.1", "10.0.0.5", "172.16.0.3"]

            # Sequência de teste:
            # [1] Adicionar: "192.168.1.10" → "IP adicionado!"
            # [1] Adicionar: "10.0.0.5"    → "IP já existe na lista!"
            # [4] Buscar: "172.16.0.3"     → "IP encontrado na posição 3"
            # [4] Buscar: "8.8.8.8"        → "IP não encontrado"
            # [2] Remover: "10.0.0.5"      → "IP removido!"
            # [3] Listar                   → exibe todos os IPs numerados
            # [5] Sair                     → "Encerrando..."
'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from time import sleep

def _apresentacao():

    print("+---------------------+")
    print("| Gerenciador de IPs  | ")
    print("+---------------------+")
    print()

def _fim_script():
    print()
    print("//////////////////////")
    print("/     Fim script     /")
    print("//////////////////////")
    print()

def _autoteste():
    print()

def _verificador_duplicado(lista: list, novo_ip):
    
    duplicado = False
    
    if novo_ip in lista:
        duplicado = True
    return duplicado

def _menu():

    print("Escolha uma das opçoes abaixo:")
    print()
    print("[1] Adicionar IP")
    print("[2] Remover IP")
    print("[3] Listar todos")
    print("[4] Buscar IP")
    print("[5] Sair")

def _adicionador_IP(escolha: str, lista_atualizada: list):
    novo_ip = input("Digite o novo IP: ")

    duplicado = _verificador_duplicado(lista_atualizada, novo_ip)

    if duplicado:
        print("IP duplicado!")
    else:
        lista_atualizada.append(novo_ip)
        print("IP {} Adicionado com sucesso!".format(novo_ip))
    return lista_atualizada

def _listador_ips(lista):
    for ip in lista:
        print(ip)
        sleep(0.5)

def _removedor_ip(lista):
    remover_ip = input("Digite o IP pra remoção: ")

    try:
        lista.remove(remover_ip)
        print("{} Removido!".format(remover_ip))
    except ValueError:
        print("IP não cadastrado!")

    return lista

def _procurador_ip(lista):
    procurar_ip = input("Digite o IP para busca: ")

    try:
        posicao = (lista.index(procurar_ip) + 1)
        print("IP encontrado na posição {}.".format(posicao))
    except ValueError:
        print("IP não encontrado!")

def main():

    lista_ips = ["192.168.1.1", "10.0.0.5", "172.16.0.3"]

    while True:

        _apresentacao()

        _menu()

        escolha = input("Digite sua escoha: ")

        if escolha == "1":
            lista_ips = _adicionador_IP(escolha, lista_ips)
        
        elif escolha == "2":
            lista_ips = _removedor_ip(lista_ips)

        elif escolha == "3":
            _listador_ips(lista_ips)

        elif escolha == "4":
            _procurador_ip(lista_ips)

        elif escolha == "5":
            print("Obrigado por usar o Gerencidor!")
            break

        else:
            print("Digite uma das opções válidas!")

    _fim_script()
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

main()
