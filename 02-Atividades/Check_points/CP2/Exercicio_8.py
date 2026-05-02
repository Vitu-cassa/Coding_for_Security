ativos = [
        {"nome": "SRV-WEB01", "tipo": "servidor", "ip": "192.168.1.10", "status": "ativo"},
        {"nome": "PC-RH03", "tipo": "estacao", "ip": "192.168.1.45", "status": "ativo"},
        {"nome": "SW-CORE01", "tipo": "switch", "ip": "192.168.1.1", "status": "inativo"},
    ]
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 8 — Inventário de Ativos com CRUD:
        Crie um programa que gerencie um inventário de ativos de rede usando
        uma lista de dicionários. Cada ativo tem:
        nome, tipo (servidor/estação/switch/roteador),
        IP e status (ativo/inativo).
        O programa deve ter menu com:
        [1] Cadastrar ativo, [2] Listar ativos, [3] Buscar por IP,
        [4] Alterar status, [5] Remover ativo, [6] Sair.
        Trate com exceções entradas inválidas
        (ex: IP duplicado, ativo não encontrado).
        Use for para buscas e listagens.

    # Dados iniciais:
        ativos = [
        {"nome": "SRV-WEB01", "tipo": "servidor", "ip": "192.168.1.10", "status": "ativo"},
        {"nome": "PC-RH03", "tipo": "estacao", "ip": "192.168.1.45", "status": "ativo"},
        {"nome": "SW-CORE01", "tipo": "switch", "ip": "192.168.1.1", "status": "inativo"},
    ]

    # Sequência de teste:
    # [1] Cadastrar: nome="SRV-DB01", tipo="servidor", ip="192.168.1.20" → "Cadastrado!"
    # [1] Cadastrar: ip="192.168.1.10" → "Erro: IP já cadastrado!"
    # [3] Buscar: ip="192.168.1.45"  → exibe dados do PC-RH03
    # [3] Buscar: ip="8.8.8.8"       → "Ativo não encontrado"
    # [4] Alterar: ip="192.168.1.1", novo status="ativo" → "Status atualizado!"
    # [5] Remover: ip="192.168.1.45" → "Ativo removido!"
    # [2] Listar → exibe todos os ativos formatados

'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from time import sleep

class IpDuplicado(Exception):
    pass

class IpNaoEncontrado(Exception):
    pass

class NomeNaoEncontrado(Exception):
    pass

def _apresentacao():
    print()
    print("+----------------------+")
    print("| Inventário de Ativos |")
    print("+----------------------+")
    print()

def _fim_script():
    print()
    print("//////////////////////")
    print("/     Fim script     /")
    print("//////////////////////")
    print()

def _menu():
    print()
    print("===== Gerenciador de Ativos =====")
    print()
    print("1 - Cadastrar ativo")
    print("2 - Listar ativos")
    print("3 - Buscar por IP")
    print("4 - Alterar Status")
    print("5 - Remover ativo")
    print("6 - Sair")
    print()

def _verificador_duplicado(lista,  novo_ip):
    '''
    Verifica a duplicidade de IPs nas listas de ativos.
    '''
    for ativo in lista:
        if novo_ip == ativo["ip"]:
            raise IpDuplicado("Ip Duplicado")

def _verificador_cadastro(ativos, ip_busca):
    '''
    Verifica se o ativo esta cadastrado, consultando pelo ip.
    '''
    for ativo in ativos:
            if ip_busca == ativo["ip"]:
                return
    raise IpNaoEncontrado("Ip Não Encontrado!")

def _verificador_nome(ativos, nome_modificar):
    '''
    Verifica se o ativo esta cadastrado, consultando pelo nome.
    '''
    for ativo in ativos:
        if nome_modificar == ativo["nome"]:
            return
    raise NomeNaoEncontrado("Ativo Não cadastrado.")

def _adicionador_de_ativo(ativos):
    '''
    Função recebe um dicionario de ativos, adiciona o ativo necessário,
    e retorna a lista atualizada.
    '''
    novo_ativo = {}
    invalido = True

    print("Digite as informações do novo ativo:")

    while invalido:
        try:
            novo_nome = input("Nome: ")
            novo_tipo = input("Tipo: ")
            novo_ip = input("IP: ")
            novo_status = input("Status: ")
            _verificador_duplicado(ativos, novo_ip)
            invalido = False
        except IpDuplicado as e:
            print("Erro {}".format(e))
            invalido = True

    novo_ativo["nome"] = novo_nome
    novo_ativo["tipo"] = novo_tipo
    novo_ativo["ip"] = novo_ip
    novo_ativo["status"] = novo_status

    return novo_ativo

def _listador_de_ativos():
    '''
    Lista todos os Ativos.
    '''
    print("\n======== Ativos cadastrados ========\n")
    for ativo in ativos:
        sleep(1)
        print("---------------------------------")
        for i in ativo:
            print("{}: {}".format(i, ativo[i]))
    print("---------------------------------")

def _buscador_ip():
    '''
    Verifica se existe um ativo consultando pelo IP.
    '''
    try:
        ip_busca = input("\nIndique o IP do ativo desejado: ")
        _verificador_cadastro(ativos, ip_busca)
        for ativo in ativos:
            if ip_busca == ativo["ip"]:
                for i in ativo:
                    print("{}: {}".format(i, ativo[i]))
    except IpNaoEncontrado as e:
        print("\nErro: {}".format(e))
        _listador_de_ativos()

def _modificador_status():
    '''
    Modifica o status atual de um ativo.
    '''
    nome_modificar = input("Indique o nome do ativo para modificar: ")
    status_modificar = input("Indique o novo status: ")
    _verificador_nome(ativos, nome_modificar)

    for ativo in ativos:
        if nome_modificar == ativo["nome"]:
            ativo["status"] = status_modificar

def _removedor_ativo():
    ativo_remover = input("Digite o nome do ativo: ")
    _verificador_nome(ativos, ativo_remover)

    for ativo in ativos:
        if ativo_remover == ativo["nome"]:
            ativos.remove(ativo)
            break

def main():

    opcao = ""

    _apresentacao()

    while True:
        _menu()

        opcao = input("Escolha uma das opções acima: ")

        if opcao == "1":
            ativos.append(_adicionador_de_ativo(ativos))
        elif opcao == "2":
            _listador_de_ativos()
        elif opcao == "3":
            _buscador_ip()
        elif opcao == "4":
            try:
                _modificador_status()
            except NomeNaoEncontrado as e:
                print("Erro: {}".format(e))
                _listador_de_ativos()
        elif opcao == "5":
            try:
                _removedor_ativo()
            except NomeNaoEncontrado as e:
                print("Erro: {}".format(e))
                _listador_de_ativos()
        elif opcao == "6":
            break
        else:
            print("\nEscolha uma opção válida!")
        
    _fim_script()

main()
