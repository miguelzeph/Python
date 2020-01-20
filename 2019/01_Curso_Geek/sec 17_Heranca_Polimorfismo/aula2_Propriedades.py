"""
POO - Properties
"""


"""
class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):

        self.__numero = Conta.contador +1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__numero

    def extrato(self):
        return f"Saldo de {self.__saldo} do cliente {self.__titular}"

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor


    '''
    Em java utiliza-se muito esse conceito de criar métodos para ver(get) e ajustar(set)
    os atributos PRIVADOS... o Python nos possibilita alterar sem precisar de métodos, massss
    nao é recomendado.
    '''

    def get_numero(self):
        return self.__numero
    def get_titular(self):
        return self.__titular
    def get_saldo(self):
        return self.__saldo
    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = self.__limite + limite

conta1 = Conta("Miguel", 3000, 5000)

conta2 = Conta("Priscila",2000, 4000)


print(conta1.extrato())
print(conta2.extrato())

#Quero somar o Saldo das duas Contas

#Método Errado de Acesso... (PRIVADOS)
soma = conta1._Conta__saldo+ conta2._Conta__saldo

print(soma)

#Maneira correta de Acessar (criando um método...)
soma = conta1.get_saldo() + conta2.get_saldo()

print(soma)
#--------------------------------------


conta1.set_limite(1000000)
print(conta1.get_limite())
"""

# ----------------------- Getters e Setters são muito legais no JAVA... mas em PYTHON não, temos as propriedades!!!!

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):

        self.__numero = Conta.contador +1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__numero

    def extrato(self):
        return f"Saldo de {self.__saldo} do cliente {self.__titular}"

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor


    @property #Não preciso usar parenteses dai...
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property #Visualizar (getter)
    def limite(self):
        return self.__limite

    @limite.setter #Alterar... (setter)
    def limite(self, novo_limite):
        self.__limite = novo_limite



conta1 = Conta("Miguel", 3000, 5000)

conta2 = Conta("Priscila",2000, 4000)


print(conta1.extrato())
print(conta2.extrato())

#Quero somar o Saldo das duas Contas

#POR CAUSA DO @PROPERTY, NÓS FAZEMOS ACESSOS SEM OS
#PARENTESES DE UM MÉTODO!!!
soma = conta1.saldo+ conta2.saldo


print(soma)

conta1.limite = 7653

print(conta1.limite)
