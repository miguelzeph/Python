"""
List - Comprehension = Criarmos uma nova lista com dados processados de outra
"""

#Exemplo 1
x =[1,2,3,4,5,6]

#isso é list comprehension
y = [novo *10 for novo in x]

print(y)

#Exemplo 2

z = [new /10 for new in y]

print(z)

# ---------------List comprehension x Loop-----------------------

# Loop

v = [1,2,3,4,5]

v2 = []

for num in v:

    dobrar = num*2

    v2.append(dobrar)

print(v2)

# List Comprehension

v3 = [a*2 for a in v]
print(v3)


# Exemplo 3

nome = "miguel"

v4 = [x for x in nome]

print(v4)

#Exemplo 4 - aumentar as letras iniciais

nomes = ["miguel","ana","priscila","cintia"]

for i in range(0,len(nomes)):

    nomes[i] = nomes[i].title()

v5 = [x for x in nomes]

print(v5)

#Exemplo 5 -

#bool() = diz se é verdadeiro ou falso

h = [0,1,2,3,"",[],(),{},True, False] #Vazios e 0 = False

v6 = [bool(valor) for valor in h]

print(v6)
