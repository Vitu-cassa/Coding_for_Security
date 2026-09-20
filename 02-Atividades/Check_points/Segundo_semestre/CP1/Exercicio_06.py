# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''Exercício 6 — Índice e desempenho:
        Crie uma coleção com 1000 eventos gerados em laço, crie um índice no
        campo ip e demonstre uma consulta por IP. Explique em 2 linhas
        (comentário no código) por que o índice importa quando a coleção cresce.

        # Dica: gere eventos com um for e insert_many; use create_index("ip").
        # Consulte um IP específico e conte quantos eventos retornaram.

        # Saída esperada (exemplo):
        # 1000 eventos inseridos.
        # Índice criado em 'ip'.
        # Eventos do IP 185.220.101.1: 250
        # Comentário: sem índice a busca seria O(n) (varre tudo); com índice ~O(log n).
'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++