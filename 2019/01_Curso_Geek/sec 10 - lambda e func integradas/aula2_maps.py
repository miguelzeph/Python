"""
MAPS - fazemos o mapeamento de valores de uma função
"""

def area(r):

    return 3.14*r**2

print(area(2))


#Forma 1

raios = [2,5,8,10]

areas = []

for raio in raios:

    calc = 3.14*raio**2
    areas.append(calc)

print(areas)

#forma 2 - Maps = maps recebe uma função e um interavel

mapas = map(area,raios)
print(type(mapas))
print(list(mapas))

#forma 3 - Mapas com lambda

mapas = map(lambda r: 3.14*r**2,raios)
print(list(mapas))
print(list(mapas))# depois de usar a func map(), ele zera

# Exemplos

#temperatura das cidades em graus celsius
cidades = [("taubaté",20), ("sjc",30), ("CPV", 40)]

#transformar para kelvin

#k = 273+c

c_para_k = lambda dado: (dado[0], 273+dado[1])

print(list(map(c_para_k,cidades))) #converteu de celsius para kelvin
