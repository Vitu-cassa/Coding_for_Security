ativos = [
        {"nome": "SRV-WEB01", "tipo": "servidor", "ip": "192.168.1.10", "status": "ativo"},
        {"nome": "PC-RH03", "tipo": "estacao", "ip": "192.168.1.45", "status": "ativo"},
        {"nome": "SW-CORE01", "tipo": "switch", "ip": "192.168.1.1", "status": "inativo"},
    ]

# novo_ip = "192.168.1.10"
# for i in ativos:

#     if novo_ip in i["ip"]:
#         print("IP duplicado")
#         print(i)
#         break

# class IpDuplicado(Exception):
#     def __init__(self, duplicado, message="IP duplicado!"):
#         self.message = message
#         self.duplicado = duplicado
#         super().__init__(self.message)

# def _verificador_duplicado(lista, novo_ip):
    
#     duplicado = False
    
#     for ativo in lista:

#         if novo_ip in ativo["ip"]:
#             duplicado = True
#             raise ValueError("IP duplicado!")

#     return duplicado
ip_busca = "192.168.1.10"

for ativo in ativos:
    if ip_busca not in ativo["ip"]:
        print("não é esse", ativo["nome"])
    else:
        print('É esse: ', ativo["nome"])