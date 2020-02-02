"""
o *args = ele monta uma lista com a quantidade de parâmetro q vc coloca

OBS: Poderíamos chamar de qualquer variável, só não pode esquecer
do * antes dela
exemplo:

*xxs
*tempo
*espace
*b
...


"""

#Entendendo o problema

def calc(a, b):
    return a+b

#ok
print(calc(10,10))

#bug 1 - item a menos
#print(calc(10))

#resolvendo o bug1 - basta eu já colocar algun valor
def calc1(a=1,b=2):
    return a+b
print(calc1(1)) #ele já entende que b = 2


#bug 2 - item a mais
#print(calc(10,10,10))

#resolvendo o bug 2 - basta eu adicionar mais parâmetros
def calc2(a,b,c):
    return a+b+c
#... espera... quer dizer que sempre que eu quiser
#adicionar mais valores eu preciso criar outros
#parâmetros???? então não estou resolvendo o problema

#-----------para isso serve *args-------------

#Exemplo:

def teste(*args):

    print(args)

teste()
teste(1)
teste(1,2)
teste(1,2,3)
teste(1,2,3,4)


#Exemplo:

def soma(*args):

    total = 0


    for numero in args:

        total = total + numero

    print(total)

soma()
soma(1)
soma(1,2)
soma(1,2,3)
soma(1,2,3,4)
soma(1.5,3.5,4.5)

#Exemplo - igual, mas menor

def soma1(*args):

    print(sum(args))

soma1()
soma1(1)
soma1(1,2)
soma1(1,2,3)
soma1(1,2,3,4)
soma1(1.5,3.5,4.5)

# Exemplo - arg

def senha(*args):

    if "Miguel" in args and "Amaral" in args:
        print(f"Bem vindo {args[0]} {args[1]}")
    else:
        print("Quem é você?")

senha()
senha("Miguel")
senha("Amaral")
senha("Miguel","Amaral")
senha("Miguel","Amaral","Junior",1000.23,"blablabla")


# DESEMPACOTAMENTO + *Args

#Problema

def lista_convidados(*args):

    for nome in args:
        print(nome)

lista = ["miguel","priscila","guilherme","mateus","ana","pai"] #poderia ser: lista[], tupla () ou sets {}

lista_convidados(lista) #Ele imprime uma vez apenas a lista inteira... o que quero é que ele imprima
#cada nome de uma vez...

#----------------------------Resolvendo com o *-----------------------------

def lista_convidados1(*args):

    for nome in args:
        print(nome)

lista_convidados1(*lista) #Esse asterisco (*) irá descompactar a lista nos argumentos!!!!

# Mais um exemplo

#Vamos aproveitar a função que criamos, soma1()

valores = [1,2,3,4,5]

#soma1(valores) #Erro ... Ele faz soma1([1,2,3,4,5],)... vai dar bug mesmo na função, tem que descompactar
soma1(*valores) #Ok com os ****


# Exemplo

def divide(*x):

    for div in x:

        print(f"10 dividido por {div} = {10/div}")


numeros = range(1,10)


divide(10)
divide(*numeros)

