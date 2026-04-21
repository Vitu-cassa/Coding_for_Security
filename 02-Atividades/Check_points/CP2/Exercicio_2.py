# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 2 — Validador de Senha com Regras:
        Crie um programa que peça uma senha ao usuário repetidamente
        (usando while) até que ela atenda TODOS os critérios: mínimo 8
        caracteres, pelo menos 1 letra maiúscula, pelo menos 1 letra minúscula,
        pelo menos 1 número e pelo menos 1 caractere especial (!@#$%&*).
        A cada tentativa inválida, informe quais critérios não foram atendidos.
        Use break para sair quando a senha for válida.

        # Teste com estas senhas:
        testes = [
            "abc",              # Fraca: faltam maiúscula, número, especial, 
                                         < 8 chars
            "abcdefgh",         # Faltam maiúscula, número, especial
            "Abcdefgh",         # Faltam número e especial
            "Abcdefg1",         # Falta especial
            "Cyber@2024",       # Válida!
        ]

        # Saída esperada (senha "Abcdefgh"):
        # Senha inválida! Problemas encontrados:
        # - Falta pelo menos 1 número
        # - Falta pelo menos 1 caractere especial (!@#$%&*)
        # Digite outra senha:
'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def _apresentacao():
    print()
    print("+---------------------+")
    print("| Validador de Senha  | ")
    print("+---------------------+")
    print()

def _fim_script():
    print()
    print("//////////////////////")
    print("/     Fim script     /")
    print("//////////////////////")
    print()

def _autoteste(contador: int):

    if contador == 1:
        senha = "abc"
    elif contador == 2:
        senha = "abcdefgh"
    elif contador == 3:
        senha = "Abcdefgh"
    elif contador == 4:
        senha = "Abcdefg1"
    elif contador == 5:
        senha = "Cyber@2024"
    elif contador == 6:
        senha = "SENHAMAIUSCULA"
    
    return senha

def _verificador_tamanho(senha: str):
    
    tamanho = None
    erro_tamanho = ""

    cont_carac = len(senha)

    if cont_carac >= 8:
        tamanho = True
    else:
        tamanho = False
        erro_tamanho = "Senha curta!"
    
    return tamanho, erro_tamanho

def _confirmador_senha_igual(senha: str, confirma_senha: str):

    igual = None
    erro_igual = ""

    if senha == confirma_senha:
        igual = True
    else:
        igual = False
        erro_igual = "As senhas digitadas são diferentes"
    
    return igual, erro_igual

def _verificador_maiuscula(senha):
    maiuscula = None
    erro_maiuscula = ""

    for letra in senha:
        if letra.isupper():
            maiuscula = True
            break
        else:
            maiuscula = False
            erro_maiuscula = "Não tem letra maiuscula"
    return maiuscula, erro_maiuscula

def _verificador_minuscula(senha):
    
    minuscula = None
    erro_minuscula = ""

    for letra in senha:
        if letra.islower():
            minuscula = True
            break
        else:
            minuscula = False
            erro_minuscula = "Não tem letra minuscula"
    return minuscula, erro_minuscula

def _verificador_numero(senha: str):

    numero = None
    erro_numero = ""

    for num in senha:
        if num.isnumeric():
            numero = True
            break
        else:
            numero = False
            erro_numero = "Senha não contem numero."
    
    return numero, erro_numero

def _verificador_especial(senha):
    especial = None
    erro_especial = ""

    for espec in senha:
        if espec.isalnum() == False:
            especial = True
            break
        else:
            especial = False
            erro_especial = "Senha não contem caracter especial."
    return especial, erro_especial

def _validor_senha(senha, confirma_senha):

    senha_valida = True
    igual, erro_igual = _confirmador_senha_igual(senha, confirma_senha)
    tamanho, erro_tamanho = _verificador_tamanho(senha)
    tem_maiuscula, erro_maiuscula = _verificador_maiuscula(senha)
    tem_minuscula, erro_minuscula = _verificador_minuscula(senha)
    tem_numero, erro_numero = _verificador_numero(senha)
    tem_especial, erro_especial = _verificador_especial(senha)

    print("senha ->", senha)

    if igual:
        pass
    else:
        print(erro_igual)
        senha_valida = False

    if tamanho:
        pass
    else:
        print(erro_tamanho)
        senha_valida = False
    
    if tem_maiuscula:
        pass
    else:
        print(erro_maiuscula)
        senha_valida = False
    
    if tem_minuscula:
        pass
    else:
        print(erro_minuscula)
        senha_valida = False

    if tem_numero:
        pass
    else:
        print(erro_numero)
        senha_valida = False
    
    if tem_especial:
        pass
    else:
        print(erro_especial)

    if senha_valida:
        print("Senha valida!")

    return senha_valida


    print("senha:", senha)
    print("tamanho ->", len(senha), "->", tamanho, )    
    print("tem_maiuscula ->", tem_maiuscula)
    print("tem_minuscula ->", tem_minuscula)
    print("tem_numero ->", tem_numero)
    print("tem_especial ->", tem_especial)

def main():

    contador = 1
    senha_valida = False

    _apresentacao()

    print("Autoteste")
    print()

    while contador <= 6:
        senha = _autoteste(contador)
        confirma_senha = senha

        _validor_senha(senha, confirma_senha)

        print('---------------------------------------')
        contador += 1

    print("Teste Manual")
    print()

    while senha_valida == False:
        senha = input("Cadastre sua senha: ")

        confirma_senha = input("Digite a senha novamente: ")
        print()
        senha_valida = _validor_senha(senha, confirma_senha)
        print('---------------------------------------')

    _fim_script()
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

main()
