"""
Polimorfismo = Poli (Muitos)+ Morfos (Formas)


"""

class Animal(object):

    def __init__(self, nome,):
        self.__nome = nome

    #ISSO É UM MÉTODO ABSTRATO!!!
    def falar(self):
        raise NotImplementedError("A classe Filha precisa ser implementada")

    def comer(self):
        print(f'{self.__nome} está comendo...')

class Cachorro(Animal):

    def __init__(self,nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala wau wau')

class Gato(Animal):

    def __init__(self,nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala algo')

#Testando

felix = Gato('Felix')
felix.comer()
felix.falar()



pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()



mikey = Rato('Mikey')
mikey.comer()
mikey.falar()