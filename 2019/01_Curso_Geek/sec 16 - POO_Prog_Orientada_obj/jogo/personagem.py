
from random import choice

from numpy import arange

from time import sleep



class Personagem:

    def __init__(self, nome, sexo, vida, ataque, defesa, critico, hp_rec):
        self.nome = nome
        self.sexo = sexo
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.critico = critico
        self.hp_rec = hp_rec


    def morte(self):

        if self.vida <= 0:
            return print(f'{self.nome} morreu...')

    def hp_recuperacao(self):

        if self.vida == 100:
            pass

        elif self.vida < 100:

            self.vida = self.vida + self.hp_rec

            if self.vida > 100:

                self.vida = 100




    def esquiva(self, esquivou ):

        return print(f'{esquivou.nome} esquivou do ataque!!!')




    def soco(self, sofreu):

        if sofreu.vida > 0:

            crit = arange(1,1+self.critico,0.25)
            hit = (self.ataque - sofreu.defesa)*round(choice(crit),0) #round(num,casadecimal)


            if hit <= 0:
                return print(f'{sofreu.nome} defendeu todo o ataque')

            else:

                sofreu.vida = sofreu.vida - hit

                return print(f'{self.nome} deu um hit de {hit} na {sofreu.nome}')




    def atacar(self, ativo, passivo):

        self.hp_recuperacao()

        print(f'--------Turno do(a) {ativo.nome}----------')
        sorteio = [1,4,5,6,7]

        escolher = choice(sorteio)



        if  (escolher >= 1 and escolher <=3):
                ativo.esquiva(passivo)

        if  (escolher >= 4 and escolher <=7):
                ativo.soco(passivo)

        if passivo.vida <= 0:
                passivo.morte()

        print(f'{ativo.nome}: {ativo.vida}')
        print(f'{passivo.nome}: {passivo.vida}')

