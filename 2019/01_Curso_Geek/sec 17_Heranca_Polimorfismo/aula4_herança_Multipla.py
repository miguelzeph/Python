"""
Herança Múltipla

Como fazer?
- Por multiderivação Direta
- Por multiderivação Indireta

"""

# Multiderivação DIRETA

class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class Multiderivada(Base1, Base2, Base3):
    pass

#-----------------------------------

# Multiderivação INDIRETA

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class Multiderivada(Base3):
    pass

#---------------------------------


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
    # Ordem de Herança (a> b > c> ...)

    def __init__(self, nome):
        super().__init__(nome)

    # ele NADA

    # ele Anda

    # Quando cumprimentar, ele vai chamar o da PRIMEIRa herança na função
    #, ou seja, da classe dos TERRESTRES



tux = Pinguim('Tux')

print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar()) #Terrestre...


# Objeto é Instância de ...

print(f" Tux é instância de Pinguim?{isinstance(tux,Pinguim)}")
print(f" Tux é instância de Aquático?{isinstance(tux,Aquatico)}")
print(f" Tux é instância de Terrestre?{isinstance(tux,Terrestre)}")

#OBS: veja que sempre uma classe é instância de OBJECT...
print(f" Tux é instância de object?{isinstance(tux,object)}")

#class Pessoa(object): = class Pessoa: #É A MESMA COISA!!! (POR DE BAIXO DOS PANOS)
