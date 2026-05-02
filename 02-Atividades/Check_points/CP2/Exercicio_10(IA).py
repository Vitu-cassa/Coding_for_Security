import random
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''Exercício 10 (Desafio) — Sistema Completo de Gerenciamento de Senhas:
        Crie um programa que combine todos os conceitos das aulas 6-8 em um
        sistema de gerenciamento de senhas. O programa deve usar um while True
        com menu: [1] Cadastrar senha (serviço + senha), [2] Listar serviços,
        [3] Buscar senha por serviço, [4] Gerar senha aleatória,
        [5] Avaliar força de todas as senhas, [6] Exportar relatório, [7] Sair.

        Requisitos:

        Armazene as senhas em um dicionário (serviço como chave, senha como valor)
        Não permita serviços duplicados (trate com exceção ou validação)
        Ao cadastrar, avalie a força da senha (fraca/média/forte) usando for para verificar critérios
        Gerar senha aleatória de tamanho N usando for + random.choice com letras, números e símbolos
        Avaliar força deve percorrer todas as senhas do dicionário com for e classificar cada uma
        Exportar relatório deve usar try/except para tratar erro de escrita em arquivo
        Trate todas as entradas inválidas com try/except

        import random

# Dados iniciais:
senhas = {
    "gmail": "MinhaS3nha!",
    "github": "Dev@2024Seguro",
    "banco_dados": "db123",
}

# Critérios de força:
# Fraca:  < 8 caracteres
# Média:  8+ chars com letras e números (sem especial)
# Forte:  8+ chars com maiúscula, minúscula, número e especial

# Caracteres para geração aleatória:
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"

# Sequência de teste:
# [1] Cadastrar: "linkedin" / "Minha@Senha1" → "Cadastrado! Força: Forte"
# [1] Cadastrar: "gmail" / "outra"           → "Erro: Serviço já cadastrado!"
# [4] Gerar: tamanho=16                      → exibe senha aleatória gerada
# [5] Avaliar todas:
#     gmail:      "MinhaS3nha!"     → Forte
#     github:     "Dev@2024Seguro"  → Forte
#     banco_dados: "db123"          → Fraca
#     linkedin:   "Minha@Senha1"    → Forte
# [6] Exportar → salva relatório em "senhas_relatorio.txt"
#     → "Relatório exportado com sucesso!"
#     (se der erro de escrita: "Erro ao exportar: [mensagem]")
# [7] Sair → "Encerrando..."
'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class ServicoDuplicado(Exception):
    pass

class ServicoNaoEncontrado(Exception):
    pass


def _apresentacao():
    print()
    print("+-------------------------------+")
    print("| Gerenciador de Senhas Seguro |")
    print("+-------------------------------+")
    print()


def _fim_script():
    print()
    print("//////////////////////")
    print("/     Fim script     /")
    print("//////////////////////")
    print()


def _menu():
    print("\n===== MENU =====")
    print("[1] Cadastrar senha")
    print("[2] Listar serviços")
    print("[3] Buscar senha")
    print("[4] Gerar senha aleatória")
    print("[5] Avaliar força das senhas")
    print("[6] Exportar relatório")
    print("[7] Sair\n")


def _verificador_servico(senhas, servico):
    if servico in senhas:
        raise ServicoDuplicado("Serviço já cadastrado!")


def _buscar_servico(senhas, servico):
    if servico not in senhas:
        raise ServicoNaoEncontrado("Serviço não encontrado!")
    return senhas[servico]


def _avaliador_forca(senha):
    tamanho = len(senha)

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False

    especiais = "!@#$%&*"

    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        elif caractere in especiais:
            tem_especial = True

    if tamanho < 8:
        return "Fraca"

    if tem_maiuscula and tem_minuscula and tem_numero and tem_especial:
        return "Forte"

    if tem_numero and (tem_maiuscula or tem_minuscula):
        return "Média"

    return "Fraca"


def _cadastrar_senha(senhas):
    try:
        servico = input("Serviço: ")
        _verificador_servico(senhas, servico)

        senha = input("Senha: ")
        forca = _avaliador_forca(senha)

        senhas[servico] = senha

        print(f"Cadastrado! Força: {forca}")

    except ServicoDuplicado as e:
        print(f"Erro: {e}")


def _listar_servicos(senhas):
    print("\nServiços cadastrados:")
    for servico in senhas:
        print(f"- {servico}")


def _buscar_senha(senhas):
    try:
        servico = input("Digite o serviço: ")
        senha = _buscar_servico(senhas, servico)
        print(f"Senha: {senha}")
    except ServicoNaoEncontrado as e:
        print(f"Erro: {e}")


def _gerador_senha():
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"

    try:
        tamanho = int(input("Tamanho da senha: "))
        senha = ""

        for _ in range(tamanho):
            senha += random.choice(caracteres)

        print(f"Senha gerada: {senha}")

    except ValueError:
        print("Erro: Digite um número válido!")


def _avaliar_todas(senhas):
    print("\n=== Avaliação de Senhas ===\n")
    for servico in senhas:
        senha = senhas[servico]
        forca = _avaliador_forca(senha)
        print(f"{servico}: \"{senha}\" → {forca}")


def _exportar_relatorio(senhas):
    try:
        with open("senhas_relatorio.txt", "w") as arquivo:
            arquivo.write("=== Relatório de Senhas ===\n\n")

            for servico in senhas:
                senha = senhas[servico]
                forca = _avaliador_forca(senha)
                arquivo.write(f"{servico}: {senha} → {forca}\n")

        print("Relatório exportado com sucesso!")

    except Exception as e:
        print(f"Erro ao exportar: {e}")


def main():

    senhas = {
        "gmail": "MinhaS3nha!",
        "github": "Dev@2024Seguro",
        "banco_dados": "db123",
    }

    _apresentacao()

    while True:
        _menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            _cadastrar_senha(senhas)

        elif opcao == "2":
            _listar_servicos(senhas)

        elif opcao == "3":
            _buscar_senha(senhas)

        elif opcao == "4":
            _gerador_senha()

        elif opcao == "5":
            _avaliar_todas(senhas)

        elif opcao == "6":
            _exportar_relatorio(senhas)

        elif opcao == "7":
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")

    _fim_script()


main()