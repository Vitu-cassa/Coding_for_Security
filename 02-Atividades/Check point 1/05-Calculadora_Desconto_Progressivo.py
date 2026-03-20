# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Exercício 5:
        Calculadora de Desconto Progressivo: Crie um programa para uma loja que aplica descontos baseados no valor da compra: até R$ 100 não tem desconto, 
        de R$ 100.01 a R$ 300 tem 10% de desconto, de R$ 300.01 a R$ 500 tem 15%, acima de R$ 500 tem 20%. Além disso, se o cliente for VIP (pergunte sim ou não), 
        ganha 5% extra em qualquer faixa. Exiba o valor original, o desconto aplicado, o desconto VIP (se houver) e o valor final.

        # Teste com estes valores:
        testes = [
            (80.00,  "nao"),  # Sem desconto, sem VIP
            (200.00, "nao"),  # 10% = R$ 20.00 → R$ 180.00
            (200.00, "sim"),  # 10% + 5% VIP = R$ 30.00 → R$ 170.00
            (450.00, "nao"),  # 15% = R$ 67.50 → R$ 382.50
            (1000.00, "sim"), # 20% + 5% VIP = R$ 250.00 → R$ 750.00
        ]

        # Saída esperada (compra R$ 200.00, VIP sim):
        # === Resumo da Compra ===
        # Valor original:  R$ 200.00
        # Desconto (10%):  R$ 20.00
        # Desconto VIP (5%): R$ 10.00
        # Valor final:     R$ 170.00
'''
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def apresentacao():
    print()
    print("+-------------------------+")
    print("|  Desconto Progressivo   |")
    print("+-------------------------+")
    print()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def fim_script():
    print()
    print("//////////////////////")
    print("/    Fim do script.  /")
    print("//////////////////////")
    print()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def descontos_compra(total: float):

    # Casting
    total = float(total)

    if (100.01 <= total <= 300.00):
        desconto_compra = 0.1
        return desconto_compra 
    
    elif (300.01 <= total <= 500.00):
        desconto_compra  = 0.15
        return desconto_compra
    
    elif (total > 500.00):
        desconto_compra  = 0.2
        return desconto_compra
    
    else:
        desconto_compra = 0
        return float(desconto_compra) 
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def cliente_VIP(resposta: str):

    sim = (resposta.capitalize() == "S")

    if sim:
        desconto_vip = 0.05
        return desconto_vip
    else:
        desconto_vip = 0.0
        return float(desconto_vip)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def desconto_total(desconto_vip: float, desconto_compra: float):

    total_desconto = desconto_compra + desconto_vip
    
    return float(total_desconto)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def valor_final(total:  float, total_desconto: float):
    
    # casting
    total = float(total)
    total_desconto = float(total_desconto)

    valor_final = total - (total * total_desconto)
    return float(valor_final)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def resumo_compra(total, desconto_compra, desconto_vip, valor_final):
    print("=== Resumo da Compra ===")
    print("Valor original:  R$ {}".format(total))
    print(f"Desconto ({desconto_compra * 100:.0f}%):  R$ {total * desconto_compra}")
    print("Desconto VIP ({:.0f}%): R$ {:.2f}".format((desconto_vip * 100), (total * desconto_vip)))
    print("-------------------------")
    print(f"Valor final:     R$ {valor_final:.2f}")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Main()

apresentacao()

cont = 1

# Teste automatico
while cont <= 5:
    if cont == 1:        
        total = 80
        resposta = "n"
        
        desconto_VIP = cliente_VIP(resposta)
        descontos_COMPRA = descontos_compra(total)
        desconto_TOTAL = desconto_total(desconto_VIP, descontos_COMPRA)
        valor_FINAL = valor_final(total, desconto_TOTAL)

    elif cont == 2:         
        total = 200
        resposta = "n"
        
        desconto_VIP = cliente_VIP(resposta)
        descontos_COMPRA = descontos_compra(total)
        desconto_TOTAL = desconto_total(desconto_VIP, descontos_COMPRA)
        valor_FINAL = valor_final(total, desconto_TOTAL)

    elif cont == 3:         
        total = 200
        resposta = "s"
        
        desconto_VIP = cliente_VIP(resposta)
        descontos_COMPRA = descontos_compra(total)
        desconto_TOTAL = desconto_total(desconto_VIP, descontos_COMPRA)
        valor_FINAL = valor_final(total, desconto_TOTAL)
    
    elif cont == 4:         
        total = 450
        resposta = "n"
        
        desconto_VIP = cliente_VIP(resposta)
        descontos_COMPRA = descontos_compra(total)
        desconto_TOTAL = desconto_total(desconto_VIP, descontos_COMPRA)
        valor_FINAL = valor_final(total, desconto_TOTAL)
    
    elif cont == 5:         
        total = 1000
        resposta = "s"
        
        desconto_VIP = cliente_VIP(resposta)
        descontos_COMPRA = descontos_compra(total)
        desconto_TOTAL = desconto_total(desconto_VIP, descontos_COMPRA)
        valor_FINAL = valor_final(total, desconto_TOTAL)

    resumo_compra(total, descontos_COMPRA, desconto_VIP, valor_FINAL)
    print()
    cont += 1

# Teste manual
print("Insira os dados para um teste manual:")
total = float(input("Valor total da compra: "))

print("Cliente é classificado como um dos planos VIP da loja?")
print("[S]im / [N]ão")
resposta = input("Digite a opção: ")

desconto_VIP = cliente_VIP(resposta)
descontos_COMPRA = descontos_compra(total)
desconto_TOTAL = desconto_total(desconto_VIP, descontos_COMPRA)
valor_FINAL = valor_final(total, desconto_TOTAL)

resumo_compra(total, descontos_COMPRA, desconto_VIP, valor_FINAL)

fim_script()
