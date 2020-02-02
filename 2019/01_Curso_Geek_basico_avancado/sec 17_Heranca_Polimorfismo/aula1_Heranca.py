"""
Herança = Aproveitar código

#Exemplo:

Cliente:
    -nome
    -sobrenome
    -cpf
    -renda

Funcionario
    -nome
    -sobrenome
    -cpf
    -matricula

"""
"""

class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):

        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

#Testando

cliente1 = Cliente('Miguel','Amaral','xxx',1500)
funcionario1 = Funcionario('Miguel','Amaral','xxx',123)

print(cliente1.__dict__)
print(funcionario1.__dict__)

# Percebeu que temos vários parâmetros iguais????

# Estamos disperdiçando código...



"""

# Vamos deixar mais bonito o código..

# Quando uma classe herda de outra classe, a Classe herdada (PESSOA) é conhecida como:
    #-Super Classe
    #-Classe Mae
    #-Classe Pai
    #-Classe Base
    #-Classe Genérica... entre outras

# Quando uma classe herda de outra classe, a classe que Herda (exe: Cliente e Funcionário) é chamada de:
    #-Sub Classe
    #-Classe Filha
    #-Classe Específica

class Pessoa: #Genérico

    def __init__(self, nome, sobrenome, cpf): #Esses atributos são em comuns com as Classes abaixo

        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

class Cliente(Pessoa): #Herdando de Pessoa
    """Cliente pessoa Herdou todos os ATRIBUTOS e MÉTODOS de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):

        #Duas FORMAS de usar os Atributos da Classe Pessoa:------------------------

        #Forma 1 --- Super(RECOMENDADO)
        super().__init__(nome, sobrenome, cpf) # Vamos Herdar os Atributos

        #Forma 2 --- Chamando ela, NÃO ESQUEÇA DO SELFFFFFFF DAI (NÃO RECOMENDADO)
        #Pessoa.__init__(self, nome, sobrenome, cpf)

        #--------------------------------------------------------------------------


        self.__renda = renda

class Funcionario(Pessoa):
    """Funcionario pessoa Herdou todos os ATRIBUTOS e MÉTODOS de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula): #Herdando de Pessoa

        # Duas FORMAS de usar os Atributos da Classe Pessoa:------------------------

        # Forma 1 --- Super(RECOMENDADO)
        super().__init__(nome, sobrenome, cpf)  # Vamos Herdar os Atributos

        # Forma 2 --- Chamando ela, NÃO ESQUEÇA DO SELFFFFFFF DAI (NÃO RECOMENDADO)
        #Pessoa.__init__(self, nome, sobrenome, cpf)

        # --------------------------------------------------------------------------

        self.__matricula = matricula

        #REESCREVENDO UM MÉTODO!!! VEJA QUE O PYCHARM COLOCA UMA BOLINHA AZUL NO CANTO ESQUERDO...
        #Quando você faz isso, vai valer o método da Classe que você está, não da classe herdada!!!!
        #Exemplo:

    def nome_completo(self):
        return f"Funcionário: {self.__matricula}, Nome: {self._Pessoa__nome}"


cliente1 = Cliente('Miguel','Amaral','xxx',1500)
funcionario1 = Funcionario('Miguel','Amaral','xxx',123)

print(cliente1.__dict__)
print(funcionario1.__dict__)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
