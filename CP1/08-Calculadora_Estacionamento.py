# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 8:
        Calculadora de Estacionamento: Crie um programa para calcular o valor do estacionamento. 
        A tarifa funciona assim: primeira hora custa R$ 10.00, 
        horas adicionais custam R$ 5.00 cada (não tem meia hora — qualquer fração conta como hora cheia), 
        entre 22h e 6h cobra adicional noturno de 50% sobre o total, e 
        carros com placa terminando em número par ganham 10% de desconto às segundas-feiras. 
        O programa deve pedir: hora de entrada, hora de saída (formato 24h, apenas horas inteiras), 
        último número da placa e dia da semana. Exiba o detalhamento completo

        # Teste com estes cenários:
        testes = [
            {"entrada": 14, "saida": 16, "placa_final": 3, "dia": "quarta"},
            # 2 horas: R$10 + R$5 = R$15.00

            {"entrada": 9,  "saida": 9,  "placa_final": 7, "dia": "sexta"},
            # Menos de 1 hora: R$10.00 (mínimo)

            {"entrada": 23, "saida": 2,  "placa_final": 5, "dia": "sabado"},
            # 3 horas noturnas: (R$10 + R$5 + R$5) * 1.50 = R$30.00

            {"entrada": 8,  "saida": 12, "placa_final": 4, "dia": "segunda"},
            # 4 horas: R$10 + R$5 + R$5 + R$5 = R$25.00, desconto 10% = R$22.50

            {"entrada": 20, "saida": 3,  "placa_final": 2, "dia": "segunda"},
            # 7 horas, noturno + desconto segunda placa par
        ]

        # Saída esperada (cenário 3):
        # === Estacionamento ===
        # Entrada: 23h | Saída: 02h
        # Permanência: 3 horas
        # Tarifa base:     R$ 20.00
        # Adicional noturno (50%): R$ 10.00
        # Total:           R$ 30.00
'''
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def apresentacao():
    print()
    print("+--------------------------------+")
    print("|  Calculadora de Estacionamento | ")
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
def calculador_tarifa(hora_entrada: int, hora_saida: int, noturno: bool, desconto: bool):

    # Casting
    tarifa = 0
    hora_entrada = int(hora_entrada)
    hora_saida = int(hora_saida)
    noturno = bool(noturno)

    tempo_permanencia = calculador_permanencia(hora_entrada, hora_saida)

    if tempo_permanencia <= 1:
        tarifa = 10
 
    elif tempo_permanencia > 1:
        tarifa = 10
        tempo_permanencia = tempo_permanencia - 1

        while tempo_permanencia > 0:
            tarifa = tarifa + 5
            tempo_permanencia -= 1
    
    if noturno:
        tarifa = tarifa + (tarifa * 0.5) 

    if desconto:
        tarifa = tarifa - (tarifa * 0.1)   
    
    return float(tarifa)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def verificador_noturno(hora_entrada: int, hora_saida: int):

    # casting

    hora_entrada = int(hora_entrada)
    hora_saida = int(hora_saida)
    
    if (hora_entrada >= 22 or hora_entrada <= 6) or (hora_saida >= 22 or hora_saida <= 6):
        noturno = True
        return noturno
    else:
        noturno = False
        return noturno
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def verificador_desconto(dia: str, final_placa):

    # Casting
    dia = str(dia.lower())
    final_placa = int(final_placa)

    if dia == "segunda" and final_placa % 2 == 0:
        desconto = True

    else:
        desconto = False
    
    return desconto
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def texto_saida(hora_entrada: int, hora_saida: int, tarifa: float, noturno: bool):

    # Casting
    tarifa = float(tarifa)
    hora_entrada = int(hora_entrada)
    hora_saida = int(hora_saida)
    tempo_permanencia = calculador_permanencia(hora_entrada, hora_saida)

    if hora_entrada > 24 or hora_saida > 24:
        print("Hora inválida!")
    else:
        print("=== Estacionamento ===")
        print(f"Entrada {hora_entrada}h | Saída: {hora_saida}h")
        print(f"Permenência: {tempo_permanencia}h")
        if noturno:
            print(f"Adicional Noturno: Sim")
        else:
            print(f"Adicional Noturno: Não")
        print("---------------------------------")
        print(f"Total: {tarifa:.2f}")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def calculador_permanencia(hora_entrada: int, hora_saida: int):

    # Casting
    hora_entrada = int(hora_entrada)
    hora_saida = int(hora_saida)

    if hora_entrada > hora_saida:
        tempo_permanencia = (hora_saida + 24) - hora_entrada
    else:
        tempo_permanencia = hora_saida - hora_entrada
    
    return tempo_permanencia
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

cont = 1

# Main()

apresentacao()

# Teste automatico:
print("Teste Automatico:")
print("**************************")
while cont <= 5:
    if cont == 1:
        HORA_ENTRADA = 14
        HORA_SAIDA = 16
        FINAL_PLACA = 3
        DIA = "quarta"

        NOTURNO  = verificador_noturno(HORA_ENTRADA, HORA_SAIDA)
        DESCONTO = verificador_desconto(DIA, FINAL_PLACA)
        TARIFA = calculador_tarifa(HORA_ENTRADA, HORA_SAIDA, NOTURNO, DESCONTO)
    
    elif cont == 2:
        HORA_ENTRADA = 9
        HORA_SAIDA = 9
        FINAL_PLACA = 7
        DIA = "sexta"

        NOTURNO  = verificador_noturno(HORA_ENTRADA, HORA_SAIDA)
        DESCONTO = verificador_desconto(DIA, FINAL_PLACA)
        TARIFA = calculador_tarifa(HORA_ENTRADA, HORA_SAIDA, NOTURNO, DESCONTO)        

    elif cont == 3:
        HORA_ENTRADA = 23
        HORA_SAIDA = 2
        FINAL_PLACA = 5
        DIA = "sabado"

        NOTURNO  = verificador_noturno(HORA_ENTRADA, HORA_SAIDA)
        DESCONTO = verificador_desconto(DIA, FINAL_PLACA)
        TARIFA = calculador_tarifa(HORA_ENTRADA, HORA_SAIDA, NOTURNO, DESCONTO) 

    elif cont == 4:
        HORA_ENTRADA = 8
        HORA_SAIDA = 12
        FINAL_PLACA = 4
        DIA = "Segunda"

        NOTURNO  = verificador_noturno(HORA_ENTRADA, HORA_SAIDA)
        DESCONTO = verificador_desconto(DIA, FINAL_PLACA)
        TARIFA = calculador_tarifa(HORA_ENTRADA, HORA_SAIDA, NOTURNO, DESCONTO) 

    elif cont == 5:
        HORA_ENTRADA = 20
        HORA_SAIDA = 3
        FINAL_PLACA = 2
        DIA = "Segunda"

        NOTURNO  = verificador_noturno(HORA_ENTRADA, HORA_SAIDA)
        DESCONTO = verificador_desconto(DIA, FINAL_PLACA)
        TARIFA = calculador_tarifa(HORA_ENTRADA, HORA_SAIDA, NOTURNO, DESCONTO) 

    print()
    texto_saida(HORA_ENTRADA, HORA_SAIDA, TARIFA, NOTURNO)
    cont += 1

# Teste manual
print()
print("Insira os dados para um teste manual:")
HORA_ENTRADA = int(input("Entrada (hh): "))
HORA_SAIDA = int(input("Saída (hh): "))
FINAL_PLACA = int(input("Final da placa: "))
DIA = input("Dia da semana: ")

NOTURNO  = verificador_noturno(HORA_ENTRADA, HORA_SAIDA)
DESCONTO = verificador_desconto(DIA, FINAL_PLACA)
TARIFA = calculador_tarifa(HORA_ENTRADA, HORA_SAIDA, NOTURNO, DESCONTO)

print()
texto_saida(HORA_ENTRADA, HORA_SAIDA, TARIFA, NOTURNO)

fim_script()
