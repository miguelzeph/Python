from homem_mulher import *

h = Homem('Miguel')
m = Mulher('Priscila')

print('\n----------------------------------')
print('Começa o jogo...Miguel x Priscila')
print('----------------------------------\n')
sleep(2.0)

print('-------HP------------')
print(h.nome+': '+str(h.vida))
print(m.nome+': '+str(m.vida))
print('---------------------\n')
sleep(2.0)



while (h.vida > 0 and m.vida > 0):


    h.atacar(h,m)


    if m.vida <= 0:
        break

    sleep(5.0)

    print('\n')

    m.atacar(m,h)

    if h.vida <= 0:
        break


    print('\n')
    sleep(5.0)


