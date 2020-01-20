"""
Teste de Memória com Generators

"""

"""  -----------COM LISTAS demora uns 5min------------------
#Sequencia de Fibonacci - POR LISTAS
def fib_lista(max):

    nums = [] #LISTAS
    a,b = 0,1

    while len(nums) < max:
        nums.append(b)
        a,b = b,a+b
    return nums

#testando fibonacci

for n in fib_lista(100000): #449MB de Memoria, por LISTA (DEMORA uns 5min)
    print(n)
"""


# VAMOS FAZER COM GERADORES AGORA....


def fib_gen(max):
    a, b, contador = 0, 1, 0

    while contador < max:
        a, b = b, a+b

        yield a

        contador = contador+1 #Faz o Papel do Vetor Len(contador) para finalizar WHILE

# Testando com Geradores

for n in fib_gen(100000): #UTILIZA APENAS 2,6MB!!!!!!!!!!!!!!!!!! outro utilizava quase 500MB!!!!
    print(n)


# OBSERVAÇÃO, A MEMORIA UTILIZADA VARIA, MAS O TEMPO DE PROCESSAMENTO NÃO... NÃO PENSE QUE É PORQUE USA
# POUCA MEMORIA, QUE SERÁ MAIS RÁPIDO...


