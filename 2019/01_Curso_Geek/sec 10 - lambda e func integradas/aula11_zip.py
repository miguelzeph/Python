"""
Zip - cria um interável (zip object)
"""

lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]

zip1 = zip(lista1,lista2)

print(type(zip1))
print(zip1)
print(list(zip1))

zip2 = zip(lista1,lista2,"abcde")
print(tuple(zip2))

# ele mistura os elementos.

#obs: Tem um problema, se você passar os vetores com tamanhos diferentes, ele faz somente até o par de igualdade

#exemplo
n1 = [1,2,3,4,5,6,7,8,9,0,10,11] #lista
n2 = (1,2,3) #tupla
n3 = {3,2,4,5,6,7} # set

zip3 = zip(n1,n2,n3)
print(list(zip3)) # só fez os 3 primeiros...

zip4 = zip(n1, n2)

print(dict(zip4))

print(dict(zip4)) #usou uma vez, ele reseta....

# Misturando os tipos de vetores...

lista = [1,2,3,4,5,6]

tuplas = (1,2,3,8,7,6,7,8,98,7,6)

dicionario = {"carro":1, "moto":2, "barco": 0}

zip5 = list(zip(lista,tuplas,dicionario.values()))

zip6 = tuple(zip(lista,tuplas,dicionario.keys()))

zip7 = dict(zip(tuplas, dicionario.keys()))


print(zip5)
print(zip6)
print(zip7)

# Exemplo mais complexo

prova1 = [10,8,7]
prova2 = [2,4,5]
alunos = ["Ana","Gui","Pri"]

#pegar a maior nota
final = {dado[0]: max(dado[1],dado[2]) for dado in zip(alunos,prova1,prova2)} #fácil.. parece difícil

print(final)