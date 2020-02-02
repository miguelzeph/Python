"""
Nós já definimos usamos funções...

Vamos aprender a defini-las


def nome_da_funcao(c/s paramentros):] #Pythonico = Sempre com lestras minusculas e separado por underline (snake case)
    ....
    ...
    ..
    .
    return


obs: Parâmetros = São variáveis introduzidas nas funções
    Argumentos = São dados passados durante a execução de uma função
"""

#Exemplo 1

def diz_oi():
    print('oi')

diz_oi()

#Exemplo 2

def calcule(a,b):
    calcule = a+b
    print(calcule)

calcule(10,10)

#y = 100 + calcule(10,10) # Vai dar TypeError, pois calcule(10,10) retorna "None"

#print(y)

#Exemplo 3 - vamos agora retornar valores

def calc(a,b,c):

    calcule = a+b+c

    return calcule

x = 100 + calc(10,10,10)

print(x)

# Exemplo 4 - Contador

def cont(a):

    print(a)

    #return a


for i in range(0,5):

    cont(i)
# ----------------função com RETURN-----------------
# Já dei alguns exemplos, tem funções que nos dão um RETORNO...

# Exemplo

x = [1,2,3,1000]

print(x.pop()) # aqui tem return... ele fala o número q ele removeu
print(x.remove(1)) # aqui não tem return
# Ou seja, Retorna Nome... dentro da função remove() não tem o comando "return"


# Exemplo

def quadrado(a):

    return a**2

quadrado(2) #Não printa...
print(quadrado(2)) # Aqui eu mantei printar o Return...

# Exemplo

def logica(a):

    if a > 0:
        return "é positivo"
    elif a < 0:
        return "é negativo"
    else:
        return "é zero"

print(logica(int(input("Digite um número: "))))

# Exemplo

from random import random


def moeda():

    moeda = random() #valor entre 0 e 1

    if moeda > 0.5:
        return "Cara"
    else: #esse else é desnecessário...
        return "Coroa"

print(moeda())
#----------------------------------------------------------------------------------
# Keys words Arguments = Se você usar os parâmetros nomeados, não interessa a ordem.

#exemplo sem Key words

def nome_completo(nome,sobrenome):
    print(f"{nome} {sobrenome}")

#ordem ok
nome_completo("Miguel","Amaral")

#ordem errada
nome_completo("Amaral","Miguel")

#----Com Keys Words Arguments----- (tanto faz a ordem

#ordem ok
nome_completo(nome= "Miguel", sobrenome= "Amaral")
nome_completo(sobrenome= "Amaral", nome = "Miguel") #tanto faz a ordem

#Viu a diferença????

#---------------------------------------------------------------------------------

#Exemplo mais complexo

def mostra(nome = "miguel", instrutor = False):
    if nome == "miguel" and instrutor:
        print("Bem vindo Miguel")
    elif nome == "miguel":
        print("Eu pensei que você era instrutor")
    else:
        print(f"Olá {nome}")

mostra()
mostra(instrutor = True)
mostra(True)
mostra("Ozzy")
mostra(nome = "Priscila")


# Variavel em forma de função----------

def test(nome,idade):
    print(f"{nome} tem {idade} anos")

variavel = test

#portanto...
variavel("Miguel",28)
#Pegou a Lógica????????
#---------------------------------------



#Agora vamos aplicar aqui, dentro das funções


def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

# Funcao dentro de outra! com a mesma jogada anterior
def mat(a, b, funcao=soma):  # Padrao ele usa a funcao soma()
    return funcao(a,b)

print(mat(10,10)) # Padrao vai usar func = Soma
print(mat(10,10,funcao= subtracao)) # func = subtracao


# Variável Global X Variável Local
#Em python a Local ganha da Global

#exemplo

variavel = 10 #Variável global

def numero():

    variavel = 100 #Variável Local

    return variavel

print(numero()) # Vai printar 100 e não 10

# Você não pode chamar uma variável local fora da função

#exemplo:

def a():
    t = "tempo" #Variável Local
    return t

"""print(t) # Vai dar Erro!!! ela é Local e não Global"""


# OBS: Sempre busque evitar usar variável GLOBAL


# Utilizando a Variável Global dentro da Função

tempo = 10 #h

def intervalo():

    global tempo #Agora ele entende a variável fora
    # da função!

    tempo_aula = tempo*5

    print(tempo_aula)

intervalo()


# Utilizando variável de função dentro de função
# Não é muito usual
def fora():
    cont = 0

    def dentro():

        nonlocal cont #não é global

        cont = cont + 1

        return cont

    return dentro()

print(fora())

from aula6_args import divide

divide(10)