# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 1 — Contador de Vogais e Consoantes:
        Crie um programa que peça uma frase ao usuário e use um laço for para 
        percorrer cada caractere, contando quantas vogais e quantas consoantes 
        existem. Ignore números, espaços e caracteres especiais. 
        Exiba o total de cada um ao final.
        
        # Teste com estas frases:
        testes = [
            "Python para Seguranca",
            "Hello World 123!",
            "aeiou",
            "",
        ]

        # Saída esperada (frase 1):
        # Frase: "Python para Seguranca"
        # Vogais: 7
        # Consoantes: 11
'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def _apresentacao():
    print()
    print("+---------------------+")
    print("| Contador de Letras  | ")
    print("+---------------------+")
    print()

def _fim_script():
    print()
    print("//////////////////////")
    print("/     Fim script     /")
    print("//////////////////////")
    print()

def _separador_letras(frase: str):
    
    letras = []
    
    for letra in frase:
        if letra.isalpha():
            letra
            letras.append(letra)
        else:
            pass
    return letras

def _removedor_especial(letras):
    
    sem_especiais = []

    for letra in letras:
        if letra.isascii():
            sem_especiais.append(letra)
        else:
            pass
    return sem_especiais

def _separador_vogais_consoante(letras):
    
    vogais = ("a", "e", "i", "o", "u")
    contador_vogal = []
    contador_consoante = []

    for letra in letras:
        if letra in vogais:
            contador_vogal.append(letra)
        else:
            contador_consoante.append(letra)
    return contador_vogal, contador_consoante

def _autoteste(contador: int):
    
    contador = int(contador)

    if contador == 1:
        frase = "Python para Seguranca"
    elif contador == 2:
        frase = "Hello World 123!"
    elif contador == 3:
        frase = "aeiou"
    elif contador == 4:
        frase = ""
    return frase        

def _formatador_saida(frase: str, vogais, consoantes):
    print(f"Frase: {frase}")
    print(f"Vogais: {len(vogais)}")
    print(f"Consoantes: {len(consoantes)}")
    print()

def main():
    
    contador = 1
    frase = None

    _apresentacao()
    
    while contador <=4:
        frase = _autoteste(contador)
        letras = _separador_letras(frase)
        letras = _removedor_especial(letras)

        vogais, consoantes = _separador_vogais_consoante(letras)
        
        _formatador_saida(frase, vogais, consoantes)

        contador += 1
    
    print("--------------------------------")
    print("Teste Manual")
    print("Digite uma frase para um teste manual: ")
    frase = input("")

    print()

    letras = _separador_letras(frase)
    letras = _removedor_especial(letras)

    vogais, consoantes = _separador_vogais_consoante(letras)
    
    _formatador_saida(frase, vogais, consoantes)

    
    _fim_script()
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

main()
