"""

Conjuntos - Teoria dos conjuntos da Matemática

No python, Conjuntos = Sets

- Conjuntos, não possuem valores DUPLICADOS
- Conjuntos, não possuem valores ORDENADOS
- Elementos não são acessados via indice, ou seja, não são indexados

Conjuntos Também é {}

---- Diferença de Mapas/dicionários x Conjuntos ----

- Mapas: Tem Chave/Valor
- Conjuntos: Tem Valor


"""

#Conjuntos

x = {6,7,9,9,1,2,2,2,2,2,3,4,5,5,5} #Iguinora os valores repetidos e
# coloca na ordem crescente...

print(type(x))
print(x)
#  Transformando Tuplas e Lista em Sets

y = (1,1,2,2,3,3,4,4)

y_s = set(y)

print(y_s)

z = [9,9,9,8,7,6,5,4,3]

z_s = set(z)

print(z_s)

# Verificar

if 3 in z:
    print("Tem o 3")
else:
    print("Não tem o 3")

# Todos

dados = [9,8,7,6,5,4,3,2,1,1,1,1,1]

tupla = tuple(dados)
print(tupla)

lista = list(dados)
print(lista)

dicionario = {}.fromkeys(dados,"teste") # Não Repete Chaves
print(dicionario)

conjunto = set(dados) # Não Repete Elementos e coloca ordem crescente
print(conjunto)

# Exemplo de utilidade - quando quero sumir com elementos repetidos
# Além disso ele coloca na ordem

visita = ("Taubaté","Taubaté", "Caçapava", "SP", "SP")

visita_set = set(visita)

print(visita_set)

# Adicionando valores no Set

visita_set.add("Brasil")

print(visita_set)

# Adicionando valores
visita_set.add("Bahia")
print(visita_set)

#Removendo Valores
visita_set.remove("SP") #Não retorna valor
print(visita_set)

#Copiando um Conjunto para outro (Deep x Shallow)


#Forma 1 - Deep Copy - (São independentes) Você cria outro conjunto (set)... você altera um e não mexe no outro

novo = visita_set.copy()

novo.add("Argentina")

print(novo)
print(visita_set) #Não alterou com a mudança em "novo"


# Forma 2 = Shallow Copy - ambos são modificados

novo = visita_set

novo.add("New York")

print(novo)
print(visita_set) #Alterou...

# Podemos remover todos os elementos de um set

novo.clear()

print(novo)


# Teoria dos Conjuntos - Matemática

#Exemplo: Estudantes de Python e Java

# fazem somente python: Priscila e Guilherme
# fazem somente Java:  Jorge e Daniel
# fazem ambos os cursos: Miguel e Ana

python = {"miguel","priscila","ana","guilherme"}
java = {"daniel", "jorge","ana","miguel"}

# União (A ou B)

#forma 1

uniao = python.union(java) # ou uniao = java.union(python)

print(uniao)

#forma 2 - utilizando o caractere "pipe" = |

uniao = python | java

print(uniao)

# intersecção (A e B)

#forma 1

interseccao = python.intersection(java)

print(interseccao)

#forma 2 - utilizando o "e comercial" = &

intersecao = python & java

print(intersecao)

# Somente me Python

A = python.difference(java)
print(A)

# Somente em java

B = java.difference(python)
print(B)




