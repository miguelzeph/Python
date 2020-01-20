"""
Ambas Trabalham bem juntas (Dir e Help)

dir() -> você coloca algo dentro da função, ela retorna para você quais funções podem
ser utilizadas naquela "coisa" que você inseriu

help() -> ela te explica alguma função/classe etc ... para sair digite q

DICA: Use o Console para testar

"""

print(dir()) # Mostra somente o que está na Raiz do Python

import random

print(dir()) # Agora o programa RANDOM entrou


print(dir(random)) #Vai mostrar todas funções do Random

#Estou com dúvida do que posso fazer com uma variável,

x = 'é uma string'

print(dir(x)) #Vai te mostrar tudo que é função que você pode aplicar na STRING

y = 10

print(dir(y)) #Vai te mostrar tudo que você pode fazer com um INTEIRO ..

#Exemplo de enumeração:

for nomes in dir(random):

    print(nomes)


# Exemplos com o Help..... APERTE Q PARA SAIR

help(print) # Te explica a função print

help(random)

help(random.random) #Dentro do MÓDULO random, existe uma FUNÇÃO também chamada de random

help(random.randint)

#vou fazer minha função e aplicar o Help

def miguel(a,b):

    """Essa função miguel é foda...
    é possível calcula tudo com ela!!!
    a = número
    b = número
    Função retorna a+b""" #DOCSTRING = comentários que sai no help
    return a+b

help(miguel)



# Importância de se ler as funções

# Por exemplo, o print() possui parâmetros opcionais, mas que podem te ajudar... veja


for i in range(0,6):

    num = random.randint(0,10)


    #print(num) # end = vazio, ele dá um \n por padrão (pula linha)
    print(num, end = ', ') #Veja que legal <--------------------------------



print('\n')

#Joguinho da Mega Sena

vetor = []
for i in range(0, 6):
    num = random.randint(1, 61)

    while num in vetor: #Enquanto tiver número repetido, continue sorteando um valor até n repetir

        num = random.randint(1,61)

    vetor.append(num)

    # print(num) # end = vazio, ele dá um \n por padrão (pula linha)
    print(num, end=', ')