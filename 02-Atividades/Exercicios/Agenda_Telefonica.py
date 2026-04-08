# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Agenda Telefônica:
        Crie uma agenda usando dicionário com menu para: adicionar, buscar, remover, listar e atualizar contatos.
        Trate casos de contato inexistente e duplicado. 
        Use estes dados iniciais para testar:
        agenda = {
            "Ana Silva": "(11) 98765-4321",
            "Bruno Costa": "(11) 91234-5678",
            "Carlos Souza": "(21) 99876-5432",
            "Diana Lima": "(31) 97654-3210"
        }
'''
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def _apresentacao():
    print()
    print("+---------------------+")
    print("| Agenda Telefonica   | ")
    print("+---------------------+")
    print()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def _fim_script():
    print()
    print("//////////////////////")
    print("/   Fechando Agenda  /")
    print("//////////////////////")
    print()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def _cabecalho():
    print()
    print("===== Agenda Telefonica =====")
    print()
    print("1 - Cadastrar")
    print("2 - Pesquisar")
    print("3 - Excluir")
    print("4 - Listar")
    print("5 - Atualizar")
    print("6 - Sair")
    print()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def _adicionar_contato():
            nome = input("Nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            AGENDA[nome] = telefone
            print()
            print("Contato Adicionado!")
            _buscar_contato(nome)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def _buscar_contato(nome: str):
            
            if nome in AGENDA:
                print(f"Contato: {nome} - {AGENDA[nome]}")
            else:
                print("Contato não encontrado!")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def _remover_contato(nome: str):
        if nome in AGENDA:
            del AGENDA[nome]
            print("Contato excluido!")
        else:
            print("Contato não encontrado!")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def _listar_contatos():
        print()
        print("Contatos na agenda:")
        for nome, telefone in AGENDA.items():
            print(f"{nome} - {telefone}.")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def _atualizar_contatos(nome: str):
      
        if nome in AGENDA:
            telefone = input("Digite o novo numero: ")
            AGENDA[nome] = telefone
            print("Contato atualizado!")
            _buscar_contato(nome)
        else:
            print("Contato não encontrado!")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        
def main():
    _apresentacao()

    while True:
        
        _cabecalho()
        opcao = input("Digite a opção desejada: ")
        print("---------------------------------------------")
        
        if opcao == "1":
            _adicionar_contato()
        
        elif opcao == "2":
            nome = input("Digite o nome do contato: ")
            _buscar_contato(nome)

        elif opcao == "3":
                nome = input("Digite o nome do contato para excluir: ")
                _remover_contato(nome)

        elif opcao == "4":
            _listar_contatos()

        elif opcao == "5":
            nome = input("Digite o nome do contato para ser atualizado: ")
            _atualizar_contatos(nome)

        elif opcao == "6":
             _fim_script()
             break 
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

AGENDA = {
    "Ana Silva": "(11) 98765-4321",
    "Bruno Costa": "(11) 91234-5678",
    "Carlos Souza": "(21) 99876-5432",
    "Diana Lima": "(31) 97654-3210"
}

main()
