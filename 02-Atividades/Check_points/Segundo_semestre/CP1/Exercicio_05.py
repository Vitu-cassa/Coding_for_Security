# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 5 — Transação com rollback:
        Simule uma transferência entre duas "contas" no MySQL (debita de uma,
        credita em outra). Se a segunda operação falhar (ex: conta inexistente),
        faça rollback e prove que o saldo da primeira conta não mudou.

        # Tabela: contas(id, titular, saldo)
        contas = [(1, "Alice", 1000), (2, "Bob", 500)]

        # Cenário de teste:
        # Transferir 200 de Alice para Bob      -> commit, saldos: Alice=800, Bob=700
        # Transferir 100 de Alice para conta 99 -> rollback, saldos INALTERADOS: Alice=800

        # Saída esperada:
        # Transferência 1 OK. Alice=800, Bob=700
        # Transferência 2 FALHOU (conta destino inexistente). Rollback. Alice=800
'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++