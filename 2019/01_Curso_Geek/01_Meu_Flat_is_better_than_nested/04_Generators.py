"""
Anteriormente vimos como a diferença de List compreension e Generators,
mas o que é um GENERATOR?

Bascimente, quando criamos um Generator, podemos aplicar funções que evitam
a utilização de FOR e CONDIÇÕES, exemplo:

- map() -> (EQUIVALE A UM COMPREENSION LIST COM FOR) serve para aplicarmos uma
função a cada elemento de uma lista, retornando uma nova lista contendo os
elementos resultantes da aplicaçãoda função

- filter() - (EQUIVALE A UM COMPREENSION LIST COM IF)  Faz uma filtragem...

- lambda() - (EQUIVALE A UMA FUNÇÃO SEM NOME, ELA DURA SOMENTE NA EXECUÇÃO)

- reduce() - **NÃO ACHEI ÚTIL!!!** é uma espécie de somatório...
"""
import math
list1 = [1, 4, 9, 100]

#-----Map(função, lista)------
raiz = map(math.sqrt, list1)
print(raiz)  # Não vai printar a lista, e sim o OBJETO... você precisa transformar:
#exemplo: dict(raiz) ... tuple(raiz) ... list(raiz)
list_raiz = list(raiz)
print(list_raiz)

# ou podemos simplicar tudo (MODO CORRETO)

raiz = list(map(math.sqrt, list1))
print(raiz)
#---------- SEM O MAP(), COMO FARIAMOS?----------

#Aplicariamos List Compreension "[]"
raiz = [math.sqrt(element) for element in list1]
print(raiz)


#--------Filter(function,list)----------
#vou criar uma função com condição
def nossa_condicao(x):
    return x>5
filtrar = filter(nossa_condicao,list1)
print(list(filtrar))

# ou podemos fazer por List Comprehension "[]" (NÃO PRECISAMOS FAZER FUNÇÃO)
filtrar = [element for element in list1 if element > 5]
print(filtrar)

# -------- Lambda()---------------------
"""
No exemplo da função filter(), tivemos que definir uma nova função 
(chamada "nossa_condicao") para usar somente dentro da função filter(),
sendo chamada uma vez para cada elemento. Ao invés de definir uma nova
função dessa forma, poderíamos definir uma função válida somente enquanto 
durar a execução do filter. Não é necessário nem dar um nome a tal função,
sendo portanto chamada de função anônima ou função lambda. Considere o exemplo
abaixo:"""

filtrar = filter(lambda x: x>5, list1)
print(list(filtrar))


# Podemos fazer por list comprehension
filtrar =[lambda element: element >5 for element in list1]  # Não deu certo kkk
print(filtrar)