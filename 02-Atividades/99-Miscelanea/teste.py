



# agrupa dados
# comportamentos 
# existe em memoria 


# camelCase
class ContaCorrente:

    # construtor
    def __init__(
            self, 
            nome_cliente: str, 
            cpf: int, 
            digito: int,
            numero: int = 0, 
            ):
        
        self.nome_cliente = nome_cliente
        self.cpf = cpf 
        self.numero = numero 
        self.digito = digito 
        self.saldo = 0
    
    def deposito(self, saldo_entrada):
        self.saldo += saldo_entrada
    
    def retirada(self, saldo_entrada):
        if self._validar_saldo(saldo_entrada):
            self.saldo -= saldo_entrada

    def _validar_saldo(self):
        if self.saldo < 0: 
            print( "saldo insuficient")
            return False
        
        return True 



    def imprimir_dados_do_cliente(self): 

        # print('nome: ' + str(self.nome_cliente) + ' cpf: ' + str(self.cpf) + ' - numero da conta: ' + str(self.numero) + '-' + str(self.digito) + ' saldo: ' + str(self.saldo))

        print(f'nome: {self.nome_cliente} - cpf: {self.cpf} - numero da conta: {self.numero}-{self.digito} saldo: {self.saldo}')


conta_1 = ContaCorrente(
    nome_cliente="Joao", 
    cpf=1234567890, 
    numero=12345, 
    digito=1
) # objeto 1 memoria 
print(type(conta_1))

# conta_1.deposito(10)
# conta_1.retirada(20)


conta_1.imprimir_dados_do_cliente()




conta_1 = ContaCorrente(
    "Joao", 
    1234567890, 
    12345, 
    1
) # objeto 1 memoria 

