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

def _calculador_media(lista: list):
    '''
    Funcao recebe lista de nomes e notas e retorna a media das notas
    da sala.
    '''
    media = 0
    contador_notas = 0
    somatoria = 0
    for aluno,nota in lista:
        somatoria += nota
        contador_notas += 1
    
    media = somatoria/contador_notas
    return media

def _verificador_notas(media: float, lista: list):
    '''
    Função recebe a media e a lista de nome e notas e verifica os alunos com
    nota acima da media
    '''

    for aluno, nota in lista:
        if nota > media:
            print(f"- {aluno}: {nota}")

def _relatorio_notas(alunos_notas: list):

    '''
    Recebe as informações de notas de alunos e forata um relatorio.
    '''

    melhor_aluno, maior_nota = _maior_nota(alunos_notas)
    pior_aluno, pior_nota = _menor_nota(alunos_notas)
    media = _calculador_media(alunos_notas)

    print("\n=== Relatório de Notas ===")
    print(f"Maior nota: {melhor_aluno} - {maior_nota:.1f}")
    print(f"Menor nota: {pior_aluno} - {pior_nota:.1f}")
    print(f"Média da turma: {media:.1f}")
    
    print("\nAlunos acima da media:")
    _verificador_notas(media, alunos_notas)

def main():
    contador = 1
    autoteste = []

    _apresentacao()
    print("Autoteste:")
    autoteste = [
    ("Carlos", 8.5),
    ("Ana", 9.2),
    ("Bruno", 6.0),
    ("Diana", 7.8),
    ("Eduardo", 4.5),
    ]
    _relatorio_notas(autoteste)

    print("\nDigite o nome e nota dos alunos para um teste manual:")

    alunos_notas = []

    while contador <= 5:

        alunos_notas.append(_cadastrador_de_notas(contador))
        contador += 1
    _relatorio_notas(alunos_notas)

    _fim_script()

main()
