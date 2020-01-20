"""
Teste de Velocidade com expressões geradoras

"""

"""

# Generator X Generator Expression

def nums():
    for num in range(1,10):
        yield num

ge1 = nums()

print(next(ge1)) #Generators
print(next(ge1))
print(next(ge1))


ge2 = (num for num in range(1,10))

print(next(ge2)) # Generation Expression
print(next(ge2))
print(next(ge2))

"""

#Realizando o Teste de Velocidade
import time


#Generator Expression

gen_inicio = time.time()

print(sum(num for num in range(1000000)))

gen_tempo = time.time() - gen_inicio

#List Comprehension

list_inicio = time.time()

print(sum([num for num in range(1000000)]))

list_tempo = time.time() - list_inicio

print(f"Generator Expression: {gen_tempo}") #Demora MENOS
print(f'List Comprehension levou {list_tempo}')



