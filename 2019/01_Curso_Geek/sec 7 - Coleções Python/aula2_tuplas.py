"""
Tuplas são quase iguais as Listas



1 - tuplas são representadas por parentes () ou sem nada
exemplo:
x = (1,2,3,4)  Tupla
x = 1,2,3,4  Tupla

PORTANTO... AS VIRGULAS SÃO QUE DEFINE SE É TUPLA OU Ñ

2 - tuplas são imutáveis, ou seja, ao se criar uma tuplas, ela não muda.
Você cria outra tuplas em vez disso... portanto, algumas funções que
são aceitas nas lista, como extend().. append() ..., não são aceitos nas
tuplas

3 - Basicamente são muito parecidas...

Por que utilizar Tuplas?

-> São mais rápidas
-> Elas deixam os seus códigos mais seguros (Imutabilidade)

Exemplo : mes = ("janeiro","fevereiro",...,"Dezembro")... Pra que usar lista neste caso????
"""

x = (1,2,3)  # Isso é uma Tupla
print(type(x))

y = 1,2,3  # Isso é uma Tupla - Importante é a Vírgula para criar tupla !
print(type(y))

z = (2)  # Isso é um INT
print(type(z))

k = 1, #Isso é uma Tupla

# Tuplas não tem Shallow Copy

v = (1,2,3,4)
f = v
