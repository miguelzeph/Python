"""
Filter - filtrar dados de determinada coleção
"""

import statistics

#dados coletados

x = [1.5,0,2,3.7,7.8,10,2.4,-0.5]

media = statistics.mean(x)

print(media)

# a função Filter() recebe uma função e um interavel (igual a maps)

res = filter(lambda y: y > media, x)
print(type(res)) #tipo filter
guardar = list(res)
print(guardar)

print(list(res)) # Assim como a maps(), após utilizar ela zera a função
print(guardar) # por isso é bom guardar em uma variavel!!!

# Exemplo

paises = ["","argentina","brasil","","chile","",""]

func = filter(None,paises)
#func = filter(lambda x: len(x) > 0, paises) #também dá
#func = filter(lambda x: x != "", paises) #também dá

print(list(func))

# Map() x Filter()

#Map() = recebe função e interável => retorna valores
#Filter() = recebe função e interável => retorna o valor filtrado


# Exemplo mais Complexos

tweeter = [
    {"user": "Miguel", "tweets": ["Kkkkk essa foi boa", "que legal..", "ok.. entendi"]},
    {"user": "Priscila", "tweets": ["que legal..", "ok.. entendi"]},
    {"user": "Ana", "tweets": []},
    {"user": "Junior", "tweets": ["cade o paper?"]},
    {"user": "Cintia", "tweets": []}
]

#filtre os usuários inativos

inativos = filter(lambda escreveu: len(escreveu["tweets"]) == 0,tweeter)
print(list(inativos))

#outra forma
inativos = filter(lambda escreveu: not escreveu["tweets"],tweeter)
#pois lista vazia retorna False... com o not ele vira True
print(list(inativos))

# Combinar Map() e Filter()

pessoas = ["Ana", "Miguel", "Junior"]

#Colocou a função filter() dentro do interativo do map()
#map(func,interativo)... filer(func,interativo)... = map(func,filter(func,interativo))

lista = list(map(lambda nome: f"Sua instrutora é {nome}",filter(lambda nome: len(nome) < 5,pessoas)))


print(lista)