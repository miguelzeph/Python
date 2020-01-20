from personagem import *




class Homem(Personagem):

    def __init__(self, nome):

        # Personagem.__init__(self, nome, "Masculino", 100, 25, 30)
        super().__init__(nome, "Masculino", 100, 40, 25, 0.5, 1)




class Mulher(Personagem):

    def __init__(self, nome):

        super().__init__(nome, "Feminino", 100, 30, 10, 6.0, 3)




#h = Homem('Miguel')
#m = Mulher('Priscila')

#print(h.nome+': '+str(h.vida))
#print(m.nome+': '+str(m.vida))

#h.soco(m)
#m.soco(h)

#print(h.nome+': '+str(h.vida))
#print(m.nome+': '+str(m.vida))



"""
while (h.vida > 0 and m.vida > 0):
    h.soco(m)
    m.morte()

    if m.vida <= 0:
        break

    m.soco(h)
    h.morte()

    if h.vida <= 0:
        break

    print('\n')
    sleep(1)

"""
"""

while (h.vida > 0 and m.vida > 0):


    h.atacar(h,m)

    if m.vida <= 0:
        break

    m.atacar(m,h)

    if h.vida <= 0:
        break


    print('\n')
    sleep(2)

"""




