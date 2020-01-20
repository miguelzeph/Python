"""
MRO - METHOD Resolution Order

"""

# O nosso Bug do PINGUIM...

# Lembra que não conseguiamos escolher qual Método ele ia executar?
# ... O método Cumprimentar? lembra que ele escolhia o que estava em primeiro na herança da classe?
#Então... esse é o objetivo da nossa aula


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar'

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra'

class Pinguim(Terrestre, Aquatico): # A ORDEM FAZ DIFERENÇA QUANDO OS MÉTODOS SE SUBSCREVEM!!!

    def __init__(self, nome):
        super().__init__(nome)

    #GAMBIARRA PARA USAR O CUMPRIMENTAR DE ANIMAL
    #--------------------------------------------
    def cumprimentar(self):
        return Animal.cumprimentar(self)

# Testando

tux = Pinguim('Tux')

# Com a Gambiarra ele executa o do Animal
print(tux.cumprimentar())


#Olha que interessante, ele mostra a ordem
#help(Pinguim)