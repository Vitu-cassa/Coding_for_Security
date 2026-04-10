ATIVOS = [
            {"nome": "SRV-WEB01", "tipo": "servidor", "ip": "192.168.1.10",
            "so": "Ubuntu 22.04", "status": "ativo", "ultimo_acesso": "2025-02-20"},
            {"nome": "PC-RH03", "tipo": "estacao", "ip": "192.168.1.45",
            "so": "Windows 11", "status": "ativo", "ultimo_acesso": "2025-01-05"},
            {"nome": "SW-CORE01", "tipo": "switch", "ip": "192.168.1.1",
            "so": "Cisco IOS", "status": "inativo", "ultimo_acesso": "2024-11-15"},
            {"nome": "SRV-DB01", "tipo": "servidor", "ip": "192.168.1.20",
            "so": "Debian 12", "status": "ativo", "ultimo_acesso": "2025-02-19"},
        ]
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''Inventário de Ativos:
        Crie um sistema de inventário com lista de dicionários. Permita 
        cadastrar, listar com filtro (por tipo/status), buscar por IP e 
        gerar relatório de ativos inativos há mais de 30 dias. Salve em JSON. 
        Dados iniciais:


        ativos = [
            {"nome": "SRV-WEB01", "tipo": "servidor", "ip": "192.168.1.10",
            "so": "Ubuntu 22.04", "status": "ativo", "ultimo_acesso": "2025-02-20"},
            {"nome": "PC-RH03", "tipo": "estacao", "ip": "192.168.1.45",
            "so": "Windows 11", "status": "ativo", "ultimo_acesso": "2025-01-05"},
            {"nome": "SW-CORE01", "tipo": "switch", "ip": "192.168.1.1",
            "so": "Cisco IOS", "status": "inativo", "ultimo_acesso": "2024-11-15"},
            {"nome": "SRV-DB01", "tipo": "servidor", "ip": "192.168.1.20",
            "so": "Debian 12", "status": "ativo", "ultimo_acesso": "2025-02-19"},
        ]

'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def _apresentacao():
    print()
    print("+-------------------------+")
    print("| Inventário de Ativos    | ")
    print("+-------------------------+")
    print()
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def _fim_script():
    print()
    print("//////////////////////")
    print("/   Fim do Script    /")
    print("//////////////////////")
    print()
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def _inativos(ativos: list):
    inativos = []

    ultimos_dias = _extrator_dias(ativos)
    # print(ultimos_dias)    

    for nome in ativos:
        for i in ultimos_dias:
            if int(i) > 15:
                inativos.append(ativos)
    return inativos

def _extrator_dias(ativos):
    dia = [ativo["ultimo_acesso"][-2:] for ativo in ativos]

    # for i in dia:
    #     dia_extraido = int(i)
    #     print("tipo:", type(dia_extraido), "->", dia_extraido)
    return dia

def main():
    INATIVOS = _inativos(ATIVOS)
    
    for i in ATIVOS:
        print(i["nome"])

from datetime import date

main()
