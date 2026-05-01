# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 5 — Contador de Palavras com Dicionário:
        Crie um programa que receba um texto do
        usuário e conte quantas vezes cada palavra aparece, armazenando em um
        dicionário (palavra como chave, contagem como valor).
        Converta tudo para minúsculo antes de contar. Ao final, exiba as palavras
        ordenadas pela frequência (da mais frequente para a menos frequente) e
        destaque a palavra mais usada

        # Texto para teste:
        texto = "o gato viu o rato e o rato viu o gato e o gato correu"

        # Saída esperada:
        # === Contagem de Palavras ===
        # "o"      → 6 vezes
        # "gato"   → 3 vezes
        # "rato"   → 2 vezes
        # "viu"    → 2 vezes
        # "e"      → 2 vezes
        # "correu" → 1 vez
        #
        # Palavra mais frequente: "o" (6 vezes)
        # Total de palavras únicas: 6
'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from collections import Counter

def _apresentacao():
    print()
    print("+----------------------+")
    print("| Contador de Palavras |")
    print("+----------------------+")
    print()

def _fim_script():
    print()
    print("//////////////////////")
    print("/     Fim script     /")
    print("//////////////////////")
    print()

def _contador_palavras(texto: str):
    '''
    Função recebe uma frase e ordena e define as frequencias que as palavras
    aparecem.
    '''

    palavras = texto.split()
    frequencia = Counter(palavras)
    ordenado = dict(frequencia.most_common())

    print("\n=== Contagem de Palavras ===")
    for palavras in ordenado:
        print(f"'{palavras}' --> {ordenado[palavras]} vezes")


    mais_frequente = next(iter(ordenado))
    print(f"\nPalavras unicas: {len(ordenado)}")
    print(f"Palavra mais frenquente: {mais_frequente} ({ordenado[mais_frequente]} vezes)")

    return dict(ordenado), dict(frequencia)

def main():

    _apresentacao()

    print("Autoteste")

    TEXTO = "o gato viu o rato e o rato viu o gato e o gato correu"
    print(TEXTO)
    texto_minusculo = TEXTO.lower()
    _contador_palavras(texto_minusculo)
    print("\nDigite um texto para um teste manual:")

    texto = input("")
    texto_minusculo = texto.lower()
    _contador_palavras(texto_minusculo)

    _fim_script()

main()
