# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 4 — Análise de Notas com Tuplas:
        Crie um programa que receba as notas de 5 alunos (nome e nota) e
        armazene cada par como uma tupla dentro de uma lista.
        Depois, usando laços, calcule e exiba:
        a maior nota e o nome do aluno, a menor nota e o nome do aluno,
        a média da turma, e quais alunos estão acima da média.
        Use for para percorrer a lista.
        
        # Dados para teste (podem ser digitados ou hardcoded):
            alunos = [
                ("Carlos", 8.5),
                ("Ana", 9.2),
                ("Bruno", 6.0),
                ("Diana", 7.8),
                ("Eduardo", 4.5),
            ]

            # Saída esperada:
            # === Relatório de Notas ===
            # Maior nota: Ana - 9.2
            # Menor nota: Eduardo - 4.5
            # Média da turma: 7.2
            #
            # Alunos acima da média:
            # - Carlos: 8.5
            # - Ana: 9.2
            # - Diana: 7.8
'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def _apresentacao():
    print()
    print("+---------------------+")
    print("|  Analise de Notas   | ")
    print("+---------------------+")
    print()

def _fim_script():
    print()
    print("//////////////////////")
    print("/     Fim script     /")
    print("//////////////////////")
    print()

def _cadastrador_de_notas(num_aluno: int):
    '''
    Função recebe as notas dos alunos e seus nomes e os
    armazena em uma lista, retornando-a.
    '''

    novo_aluno = input(f"Aluno(a) {num_aluno}: ")
    nota_aluno = float(input(f"Nota do(a) {novo_aluno}: "))

    return novo_aluno, nota_aluno

def _maior_nota(lista_notas: list):

    '''
    Função recebe a lista de nomes e notas do aluos e verifica
    qual aluno teve a maior nota.
    '''

    maior_nota = 0
    melhor_aluno = None
    for aluno, nota in lista_notas:
        if nota > maior_nota:
            maior_nota = nota
            melhor_aluno = aluno
    return melhor_aluno, maior_nota

def _menor_nota(lista_notas: list):
    '''
    Função recebe a lista de nomes e notas e verifica qual aluno
    obteve e menor nota.
    '''
    menor_nota = 10
    pior_aluno = None

    for aluno, nota in lista_notas:
        if nota < menor_nota:
            menor_nota = nota
            pior_aluno = aluno

    return pior_aluno, menor_nota

def main():
    contador = 1
    alunos_notas = []

    _apresentacao()
    print("Digite o nome e nota dos alunos:")

    # while contador <= 5:

    #     alunos_notas.append(_cadastrador_de_notas(contador))
    #     contador += 1
    alunos_notas = [
    ("Carlos", 8.5),
    ("Ana", 9.2),
    ("Bruno", 6.0),
    ("Diana", 7.8),
    ("Eduardo", 4.5),
]
    melhor_aluno, melhor_nota = _maior_nota(alunos_notas)
    print(melhor_aluno, melhor_nota)
    pior_aluno, menor_nota = _menor_nota(alunos_notas)
    print(pior_aluno, menor_nota)

    _fim_script()

main()
