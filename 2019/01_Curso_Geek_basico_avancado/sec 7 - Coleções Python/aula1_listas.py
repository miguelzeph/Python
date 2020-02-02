"""
-Listas são Arrays. (C e Java eles chamam de Arrays)

-Em python você não define o tamanho, você cria a lista
e adiciona elementos. Diferente de outras linguagens.

-Nas listas, podemos colocar qualquer tipo de dados.

-As listas em python são representadas por colchetes []

-Podemos colocar tipos de elementos diferentes dentro de uma lista
exemplo: a = [1,2,'oi'] ... str com int

-Listas são Mutaveis

"""

a = []

print(type(a)) # class "list"

# -------Procurar elementos---------

v =[0,1,2,8,9,10]

if int(input("Digite um número: ")) in v:

    print("Esse número está neste vetor")

else:

    print("Esse número não está dentro deste vetor")

# --------outro exemplo------

a = 'miguel'

'm' in a # = True

# ------Ordenando Lista------

b = [10,1,0,2,5,4,9,7,8]

print(b)

b.sort() # Organizando crescente

print(b)

# -------Contagem de elementos -----

c = "Miguel Angelo do Amaral Junior"

print(c.count('i')) #quantos "i" tem no meu nome

#Adicionando elementos por append() -> somente 1 elemento por vez

b.append(100)

print(b)

#Adicionando elementos por extende() ... ele adiciona um conjunt de um em um

b1 = [2,2,2,2,2,5,5,5,5]

b.extend(b1) # Se eu usar o append(), ele iria add um vetor dentro de um vetor

print(b)

# Podemos substituir o extende por

b2 = b1 + b #mesma coisa que o extend()

print(b2)


#Contar os elementos len()

print(len(b))

# Removendo elementos de uma lista pop()

b.pop() # remove o último elemento
b.pop(0) # remove o primeiro elemento
b.pop(3) # remove o quarto elemento ...

print(b)

# fazendo uma lista virar uma string

nome = ["Miguel","Angelo","do","Amaral"]

print(" ".join(nome)) #Adiciona entre os nomes um ESPAÇO
print(",".join(nome)) #Adiciona entre os nomes uma VIRGULA
print("".join(nome)) #Tudo grudado

# Enumerate()

a = ['casa','apartamento','cozinha']

for x, y in enumerate(a): # x = numero do elemento... y = nome do elemento

    print(f"{x} {y}")

# Index() ... ele te fala qual o índice do elemento
#OBS: se não tiver o elemento, ele gera ValueError

v = [9,1,1,1,1,2,3,4,5,6,6,7]

print(v.index(9)) # qual a posição do 9 no vetor v?

print(v.index(1)) # qual a posição do 1 no vetor v? (Ele pega o primeiro)

print(v.index(1, 4)) # procura o 1 a partir do elemento 3 em diante.

print(v.index(1, 3, 6)) # procura o 1 entre os índices 4 r 6


#Operações Matemáticas

x = [1,2,3,5]

print(sum(x)) #Soma tudo
print(min(x)) #Valor Min
print(max(x)) #Valor Max
print(len(x)) #Tamanho da Lista

# Transformar Lista (Array) = [Colchetes] para Tupla = (Parentes)

t = tuple(x)

print(t)

# Deep Copy X Shallow copy

#forma 1 - Deep Copy = quando você copia uma lista para uma nova variável... ela não muda a anterior
x = [1,2,3]
y = x.copy() #Deep Copy...

y.append(4)

print("Deep Copy")
print(f"{x}\n{y}")

#forma 2 - Shallow Copy = agora uma é igual a outra... mexeu em uma, mexeu na outra

x = [1,2,3]
y = x #Shallow Copy...

y.append(4)
x.append(6)

print("Shallow Copy")
print(f"{x}\n{y}")