"""
Listas aninhadas (Nested Lists)

"""

#Exemplo matriz

x = [[1,2,3],[4,5,6],[7,8,9]]


print(f" {x[0]}\n {x[1]}\n {x[2]}")

# x[linha][coluna]
print(x[2][0])
print(x[0][1])

#Exemplo Loop - sem list comprehension

for linha in x:
    for num in linha:
        print(num)

#Exemplo Loop - com list comprehension

[print(valor) for linha in x for valor in linha]

# ou (outra lógica)

[[print(valor) for valor in linha] for linha in x]


#Gerando uma Matriz 3x3

matriz_3x3 = [[linha for linha in range(0,3)] for col in range(0,3)]

for linha in matriz_3x3:

    print(linha)

#Gerando 8x8

xadrez = [[ln  for ln in range(0,8)] for col in range(0,8)]

[print(l) for l in xadrez ]