# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 6 — Blacklist de IPs com Sets:
        Crie um programa que compare dois sets:
        um com IPs que acessaram o servidor e outro com uma blacklist de
        IPs maliciosos. Usando operações de conjuntos, descubra e exiba:
        quais IPs maliciosos foram detectados (interseção),
        quais IPs são seguros (diferença), quais IPs da blacklist não apareceram
        (diferença inversa) e o total de IPs únicos
        considerando ambas as listas (união).
        Exiba os resultados formatados.

        acessos = {"192.168.1.10", "10.0.0.5", "185.220.101.1", "172.16.0.3",
                "192.168.1.20", "91.240.118.172", "10.0.0.12", "45.33.32.156"}

        blacklist = {"185.220.101.1", "45.33.32.156", "91.240.118.172",
                    "23.94.5.100", "104.244.72.115"}

        # Saída esperada:
        # === Relatório de Segurança ===
        # IPs maliciosos detectados (3):
        #   - 185.220.101.1
        #   - 45.33.32.156
        #   - 91.240.118.172
        #
        # IPs seguros (5):
        #   - 192.168.1.10
        #   - 10.0.0.5
        #   - 172.16.0.3
        #   - 192.168.1.20
        #   - 10.0.0.12
        #
        # IPs da blacklist não detectados (2):
        #   - 23.94.5.100
        #   - 104.244.72.115
        #
        # Total de IPs únicos: 10
'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def _apresentacao():
    print()
    print("+---------------------+")
    print("|  Blacklist de IPs   |")
    print("+---------------------+")
    print()

def _fim_script():
    print()
    print("//////////////////////")
    print("/     Fim script     /")
    print("//////////////////////")
    print()

def _detector_ips_maliciosos(set_acessos: set, set_blacklist: set):
    '''
    Função recebe as listas de IPS que efetuaram acessos e IPs na blacklist
    e os separa em grupos:
    maliciosos, não detectados e seguros.
    returna as listas para o programa principal.
    '''

    maliciosos = []
    seguros = []
    nao_cadastrado = []

    for ip in set_acessos:
        if ip in set_blacklist:
            maliciosos.append(ip)
        else:
            seguros.append(ip)
    
    for ip in set_blacklist:
        if ip in set_acessos:
            pass
        else:
            nao_cadastrado.append(ip)

    return maliciosos, seguros, nao_cadastrado

def _contador_ips_unicos(maliciosos: list, seguros: list, nao_cadastrados: list):
    '''
    conta e retorna quantos IPS unicos foram detectados.
    '''
    ips_unicos = len(maliciosos) + len(seguros) + len(nao_cadastrados)

def _mostrador_de_ip(lista: list):
    '''
    Realiza o print dos IPS na saida do relatorio.
    '''
    for ip in lista:
        print("   - {}".format(ip))
def _relatorio():
    '''
    Gera um relatorio dos IPS baseado nas listas analisadas.
    '''
    ips_maliciosos, ips_seguros, ips_naocadastrados = _detector_ips_maliciosos(ACESSOS, BLACKLIST)
    qntd_unicos = _contador_ips_unicos(ips_maliciosos, ips_seguros, ips_naocadastrados)
    print("=== Relatório de Segurança ===")
    print("\nIPs maliciosos detectados ({}):".format(len(ips_maliciosos)))
    _mostrador_de_ip(ips_maliciosos)

    print("\nIPs seguros ({}):".format(len(ips_seguros)))
    _mostrador_de_ip(ips_seguros)

    print("\nIPs da blacklist não detectados ({}):".format(len(ips_naocadastrados)))
    _mostrador_de_ip(ips_naocadastrados)

    print("\nTotal de IPs únicos: 10".format(qntd_unicos))
    


def main():

    _apresentacao()

    _relatorio()

    _fim_script()

ACESSOS = {"192.168.1.10", "10.0.0.5", "185.220.101.1", "172.16.0.3",
        "192.168.1.20", "91.240.118.172", "10.0.0.12", "45.33.32.156"}

BLACKLIST = {"185.220.101.1", "45.33.32.156", "91.240.118.172",
            "23.94.5.100", "104.244.72.115"}

main()

