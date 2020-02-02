"""
len - retorna tamanho
abs - abusoluto... módulo
sum - somatório
round -
"""

# Len

x = [1,2,3,4,5,6,7]

print(len(x))

# OBS: Funções Dunder no Python - tudo que tem 2 underlines em volta da função (DE BAIXO DOS PANOS)

print(x.__len__()) # o Python faz isso por DEBAIXO DOS PANOS

# Abs - somente ára números

y = -10

print(abs(y))

# Sum

z = {1,2,3,4,5,6,7,7,7,7,7} # set não repete

print(sum(z))

print(sum(z,5)) # o Valor Default = 0, mas pode adicionar, ex: 5... exemplo: quando você sempre adiciona o freete na venda


# Round - arredondamento ->  round(numero,casa de precisão)

print(round(10.4983)) #default  = 0 para cada de precisão

print(round(10.4983,1))

print(round(10.4983,2))

print(round(10.4983,3))

print(round(10.4983865,4))
