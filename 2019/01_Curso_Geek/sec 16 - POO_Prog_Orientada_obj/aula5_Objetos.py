"""
OBJETOS - São instâncias da Classe


"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):

        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:

     contador = 4999

     def __init__(self, limite, saldo):

         self.__numero = ContaCorrente.contador +1
         self.__limite = limite
         self.__saldo = saldo
         ContaCorrente.contador = self.__numero

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):

        self.__nome = nome
        self.__sobrenome = sobrenome.title()
        self.__email = email
        self.__senha = senha

    def nome_completo(self):
        return f'{self.__nome.title()} {self.__sobrenome.title()}'


# Vamos criar um Objeto = Instância

lamp1 = Lampada('branca',110,60) #isso é um OBJETO da classe lampada

cc1 = ContaCorrente(5000,20000) #isso é um OBJETO da classe contacorrente

user1 = Usuario('miguel','amaral','miguel@.com','1234') #isso é um OBJETO da classe usuario

print(user1.nome_completo())
