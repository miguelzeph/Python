

class Personagem:

    def __init__(self, nome, hp, atak):

        self.nome = nome
        self.hp = hp
        self.atak = atak

    def soco(self, inimigo):

        inimigo.hp = inimigo.hp - self.atak

        escrever =  f'{self.nome} deu um dano de {self.atak} em {inimigo.nome}'

        return print(escrever)




class Homem(Personagem):

    def __init__(self,nome):
        super().__init__(nome,100,30)

class Mulher(Personagem):

    def __init__(self, nome):
        super().__init__(nome, 150,15)


personagem1 = Homem('Miguel')
personagem2 = Mulher('Priscila')

personagem1.soco(personagem2)
personagem2.soco(personagem1)