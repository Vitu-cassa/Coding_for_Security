# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 6: 
        Verificador de Ano Bissexto e Dia da Semana: Crie um programa que peça uma data (dia, mês e ano, separados) 
        e verifique: se o ano é bissexto (divisível por 4, exceto os divisíveis por 100, exceto os divisíveis por 400), 
        se o mês é válido (1-12), se o dia é válido para aquele mês (considere meses com 28/29, 30 ou 31 dias), 
        e exiba a data formatada. Se qualquer valor for inválido, exiba o motivo.

        # Dias por mês:
        # 31 dias: janeiro(1), março(3), maio(5), julho(7), agosto(8), outubro(10), dezembro(12)
        # 30 dias: abril(4), junho(6), setembro(9), novembro(11)
        # 28/29 dias: fevereiro(2) — 29 se bissexto, 28 se não

        # Teste com estas datas:
        testes = [
            (29, 2, 2024),   # Válida — 2024 é bissexto
            (29, 2, 2023),   # Inválida — 2023 não é bissexto
            (31, 4, 2025),   # Inválida — abril tem 30 dias
            (15, 8, 2025),   # Válida — 15/08/2025
            (29, 2, 2000),   # Válida — 2000 é bissexto (divisível por 400)
            (29, 2, 1900),   # Inválida — 1900 NÃO é bissexto (divisível por 100)
            (5, 13, 2025),   # Inválida — mês 13 não existe
            (0, 6, 2025),    # Inválida — dia 0 não existe
        ]

        # Saída esperada:
        # Data: 29/02/2024
        # Ano bissexto: Sim
        # Data válida!
        #
        # Data: 29/02/2023
        # Ano bissexto: Não
        # Data inválida: fevereiro de 2023 tem apenas 28 dias
'''
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def apresentacao():
    print()
    print("+--------------------------------+")
    print("|  Verificador de Ano Bissexto e | ")
    print("|        Dia da Semana           |")
    print("+--------------------------------+")
    print()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def fim_script():
    print()
    print("//////////////////////")
    print("/    Fim do script.  /")
    print("//////////////////////")
    print()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def verificador_bissexto(ano: int):

    # Casting
    ano = int(ano)

    bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    
    if bissexto:
       # print("Sim")
        return "Sim"
    else:
       # print("Não")
        return "Não"
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def identificador_mes(mes: int, dia: int, bissexto: bool):
    
    # Casting
    mes = int(mes)
    dia = int(dia)
   
    # Dias por mês:
        # 31 dias: janeiro(1), março(3), maio(5), julho(7), agosto(8), outubro(10), dezembro(12)
        # 30 dias: abril(4), junho(6), setembro(9), novembro(11)
        # 28/29 dias: fevereiro(2) — 29 se bissexto, 28 se não

    if mes == 1:
        return "Janeiro"
    
    elif mes == 2:
        return "fevereiro"  
    
    elif mes == 3:
        return "Março"
    
    elif mes == 4:
        return "Abril"
    
    elif mes == 5:
        return "Maio"
    
    elif mes == 6:
        return "junho"
    
    elif  mes == 7:
        return "julho"
    
    elif mes == 8:
        return "agosto"
    
    elif mes == 9:
        return "setembro"
    
    elif mes == 10:
        return "outubro"
    
    elif mes == 11:
        return "novembro"
    
    elif mes == 12:
        return "dezembro"
    
    else:
        return f"{mes}"
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def validador_data(dia: int, mes: int,  ano: int, bissexto):
    
    data_valida = False
    
    # Casting
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)

    
    dia_valido = (0 < dia <= 31)
    mes_valido = (0 < mes <= 12)
    ano_valido = (ano > 0)
   
    if (mes == 2 and dia > 29 and bissexto == "Sim"):
        data_valida = False
        return data_valida
    
    elif (mes == 2 and dia > 28 and bissexto == "Não"):
        data_valida = False
        return data_valida

    elif dia >= 31 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        data_valida = False
        return data_valida        
  
    elif dia_valido and mes_valido and ano_valido:
        data_valida = True
        return data_valida
    
    else:
        pass
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def erro_data_invalida(data_valida, mes: int, dia: int, bissexto):
    # casting
    mes = int(mes)
    dia = int(dia)

    if data_valida == False:
        print("data_valilda ->", data_valida)
    
    if (mes == 2 and dia > 28) or (mes == 2 and dia > 29 and bissexto == "Sim"):
        print("Fevereiro tem apenas 28 ou 29 dias (Se bissexto)!")
    elif  (mes > 12) or (mes <= 0):
        print(f"mês {mes} não existe!") 
    elif (dia >= 31) and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        print(f"{NOME_MES} tem apenas 30 dias!")
    
    elif (dia > 31):
        print(f"Não existe dia {dia}!")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Main()

cont = 1

apresentacao()

print("Teste Automatico:")

# Teste automatico
while cont < 8:

    if cont == 1:
        DIA = 29
        MES = 2
        ANO = 2024        

    elif cont == 2:
        DIA = 29
        MES = 2
        ANO = 2023
    
    elif cont == 3:
        DIA = 31
        MES = 4
        ANO = 2025
   
    elif cont == 4:
        DIA = 15
        MES = 8
        ANO = 2025

    elif cont == 5:
        DIA = 29
        MES = 2
        ANO = 2000

    elif cont == 6:
        DIA = 29
        MES = 2
        ANO = 1900

    elif cont == 7:
        DIA = 5
        MES = 13
        ANO = 2025

    elif cont == 8:
        DIA = 0
        MES = 6
        ANO = 2025
   
    BISSEXTO = verificador_bissexto(ANO)
    NOME_MES = identificador_mes(MES, DIA, BISSEXTO)
    DATA_VALIDA = validador_data(DIA, MES, ANO, BISSEXTO)
    
    print("*************************")
    print("Data: {}/{}/{}".format(DIA, NOME_MES, ANO))
    print("Ano bissexto:", verificador_bissexto(ANO))

    if DATA_VALIDA:
        print("Data Válida!")
    else:
        print("Data invalida")
        erro_data_invalida(DATA_VALIDA, MES, DIA, BISSEXTO)
    

    cont += 1
print("*************************")

# Teste manual
print()
print("Insira os dados para um teste manual:")
print()

print("Indique a data para verificação (dd/mm/aaaa): ")
DIA = int(input("Dia: "))
MES = int(input("Mês: "))
ANO = int(input("Ano: "))

print()
BISSEXTO = verificador_bissexto(ANO)
NOME_MES = identificador_mes(MES, DIA, BISSEXTO)
DATA_VALIDA = validador_data(DIA, MES, ANO, BISSEXTO)
    
print()
print("Data: {}/{}/{}".format(DIA, NOME_MES, ANO))
print("Ano bissexto:", verificador_bissexto(ANO))

if DATA_VALIDA:
    print("Data Válida!")
else:
    print("Data invalida")
    erro_data_invalida(DATA_VALIDA, MES, DIA, BISSEXTO)

fim_script()
