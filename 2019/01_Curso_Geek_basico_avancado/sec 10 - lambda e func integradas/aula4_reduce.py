"""
Apartir das versões 3+ não é mais built-in.. ou seja temos que importá-la agora

reduce(funcão,dado)

-Como funciona a reduce()...
exemplo:
x = [a1,a2,a3...]

OBS: A FUNÇÃO TEM Q PEGAR 2 ELEMENTOS

1passo - pega a1 e a2 e aplica a função, guarda o resultado res = f(a1,a2)
2passo - pega res e a3 e aplica função... e assim por diante.

"""

# Programa que multiplica todos os elementos de uma lista (Fatorial!!!!)

#importar

from functools import reduce

dados = range(1,5+1)

#precisamos de uma função que receba 2 parâmetros...

func = lambda x,y: x*y

res = reduce(func,dados)

print(res)

# Exemplo - Fatorial -----

calc = 1

for x in dados:
    calc = calc * x
print(calc)

