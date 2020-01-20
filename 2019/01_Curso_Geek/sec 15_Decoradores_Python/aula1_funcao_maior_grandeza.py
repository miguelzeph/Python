"""
Função de Maior Grandeza -> Higher Order Functions - HOF

O que isso significa?
- Quando uma linguagem de programação suporta
o conceito HOF, indica que podemos ter
funções que retornam outras funções,
como argumentos para outras funções, e até mesmo
criar variáveis do tipo de funções nos nossos
proramas.


"""



"""
#Exemplos - Definindo as Funções

def somar(a,b):

    return a+b

def diminuir(a,b):

    return a-b

def multiplicar(a,b):

    return a*b

def dividir(a,b):

    return a/b

def calcular(num1,num2,funcao):
    
    #estamos usando HOF aqui...
    return funcao(num1,num2)

# Testando as Funções

print(calcular(4,3,somar))
print(calcular(4,3,diminuir))
print(calcular(4,3,multiplicar))
print(calcular(4,3,dividir))
"""


#Nested Functions - Funções Aninhadas

#podemos ter funções dentro de funçoes

#Exemplo

from random import choice

def cumprimento(pessoa):

    def humor():
        return choice(["Triste","Feliz","Normal"])

    return humor() +' '+ pessoa

print(cumprimento("Angelina"))


# Retornando Funções de Outras Funções

def faz_me_rir():

    def rir():
        return "hahaha"
    return rir #Terei que usar o "()" para chamá-la


#Testando

rindo = faz_me_rir()

print(rindo()) # chamei aqui o "()"
