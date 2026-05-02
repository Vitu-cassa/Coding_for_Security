# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 9 — Analisador de Logs de Segurança:
        Crie um programa que analise uma lista de logs (strings),
        extraindo informações com manipulação de strings e armazenando em
        dicionários. Para cada log: extraia o nível (INFO/WARNING/ERROR),
        o IP de origem e a mensagem. Conte os eventos por nível,
        identifique o IP com mais erros e gere um relatório.
        Use for, dicionários e try/except para tratar logs malformados.

        logs = [
    "[2025-02-20 08:15:01] [INFO] Login ok - IP: 192.168.1.10",
    "[2025-02-20 08:15:03] [WARNING] Area restrita - IP: 10.0.0.5",
    "[2025-02-20 08:15:10] [ERROR] Falha auth - IP: 185.220.101.1",
    "[2025-02-20 08:15:15] [INFO] Arquivo acessado - IP: 192.168.1.10",
    "[2025-02-20 08:15:22] [ERROR] Conexao recusada - IP: 185.220.101.1",
    "[2025-02-20 08:15:30] [WARNING] Certificado SSL - IP: 172.16.0.3",
    "[2025-02-20 08:15:35] [ERROR] Falha auth - IP: 10.0.0.5",
    "log malformado sem formato correto",
    "[2025-02-20 08:15:45] [ERROR] Timeout - IP: 185.220.101.1",
    "[2025-02-20 08:15:50] [WARNING] CPU alta - IP: 192.168.1.20",
    "[2025-02-20 08:16:01] [ERROR] Falha auth - IP: 185.220.101.1",
    "[2025-02-20 08:16:05] [INFO] Firewall ok - IP: 192.168.1.10",
]

# Saída esperada:
# === Relatório de Logs ===
# INFO:    3 eventos
# WARNING: 3 eventos
# ERROR:   4 eventos
# Logs malformados: 1
#
# IP com mais erros: 185.220.101.1 (3 erros)
#
# Detalhamento de erros:
#   185.220.101.1 → 3 erros
#   10.0.0.5      → 1 erro
'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class LogMalformado(Exception):
    pass


def _apresentacao():
    print()
    print("+----------------------------+")
    print("| Analisador de Logs de Seg  |")
    print("+----------------------------+")
    print()

def _fim_script():
    print()
    print("//////////////////////")
    print("/     Fim script     /")
    print("//////////////////////")
    print()

def _extrator_log(log):
    '''
    Extrai nível, IP e mensagem de um log.
    '''
    try:
        partes = log.split("] ")

        nivel = partes[1].replace("[", "").replace("]", "")
        resto = partes[2]

        mensagem, ip_parte = resto.split(" - IP: ")
        ip = ip_parte.strip()

        return {
            "nivel": nivel,
            "ip": ip,
            "mensagem": mensagem
        }

    except Exception:
        raise LogMalformado("Log malformado!")


def _processador_logs(logs):
    '''
    Processa os logs e gera estatísticas.
    '''
    contagem_nivel = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    erros_por_ip = {}
    logs_malformados = 0

    for log in logs:
        try:
            dados = _extrator_log(log)

            nivel = dados["nivel"]
            ip = dados["ip"]

            contagem_nivel[nivel] += 1

            if nivel == "ERROR":
                if ip not in erros_por_ip:
                    erros_por_ip[ip] = 0
                erros_por_ip[ip] += 1

        except LogMalformado:
            logs_malformados += 1

    return contagem_nivel, erros_por_ip, logs_malformados


def _ip_com_mais_erros(erros_por_ip):
    '''
    Retorna o IP com maior número de erros.
    '''
    maior_ip = None
    maior_qtd = 0

    for ip in erros_por_ip:
        if erros_por_ip[ip] > maior_qtd:
            maior_ip = ip
            maior_qtd = erros_por_ip[ip]

    return maior_ip, maior_qtd


def _relatorio(contagem_nivel, erros_por_ip, logs_malformados):
    '''
    Exibe o relatório final.
    '''
    print("\n=== Relatório de Logs ===\n")

    print("INFO:   {} eventos".format(contagem_nivel["INFO"]))
    print("WARNING:{} eventos".format(contagem_nivel["WARNING"]))
    print("ERROR:  {} eventos".format(contagem_nivel["ERROR"]))
    print("Logs malformados: {}\n".format(logs_malformados))

    ip, qtd = _ip_com_mais_erros(erros_por_ip)

    print("IP com mais erros: {} ({} erros)\n".format(ip, qtd))

    print("Detalhamento de erros:")
    for ip in erros_por_ip:
        print("  {} → {} erros".format(ip, erros_por_ip[ip]))


def main():

    logs = [
        "[2025-02-20 08:15:01] [INFO] Login ok - IP: 192.168.1.10",
        "[2025-02-20 08:15:03] [WARNING] Area restrita - IP: 10.0.0.5",
        "[2025-02-20 08:15:10] [ERROR] Falha auth - IP: 185.220.101.1",
        "[2025-02-20 08:15:15] [INFO] Arquivo acessado - IP: 192.168.1.10",
        "[2025-02-20 08:15:22] [ERROR] Conexao recusada - IP: 185.220.101.1",
        "[2025-02-20 08:15:30] [WARNING] Certificado SSL - IP: 172.16.0.3",
        "[2025-02-20 08:15:35] [ERROR] Falha auth - IP: 10.0.0.5",
        "log malformado sem formato correto",
        "[2025-02-20 08:15:45] [ERROR] Timeout - IP: 185.220.101.1",
        "[2025-02-20 08:15:50] [WARNING] CPU alta - IP: 192.168.1.20",
        "[2025-02-20 08:16:01] [ERROR] Falha auth - IP: 185.220.101.1",
        "[2025-02-20 08:16:05] [INFO] Firewall ok - IP: 192.168.1.10",
    ]

    _apresentacao()

    contagem_nivel, erros_por_ip, logs_malformados = _processador_logs(logs)

    _relatorio(contagem_nivel, erros_por_ip, logs_malformados)

    _fim_script()

main()