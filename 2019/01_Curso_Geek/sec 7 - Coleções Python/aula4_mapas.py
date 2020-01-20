"""

Mapas = Dicionários

"""

receita ={"jan":10,"fev":20,"marc":30}

#interar sobre dicionários

for i in receita:

    #print(i) #imprime as chaves

    #print(receita[i]) #imprime os valores

    print(f"Chave: {i}, Valor: {receita[i]}")

# Descobrindo as chaves

print(receita.keys())

# Descobrindo os valores

print(receita.values())

# Descobrindo chave e valor

print(receita.items()) #Retorna tuplas


#Interar no modo Pythonico

for i in receita.keys():

    print(f"Chave: {i}, Valor: {receita[i]}")

