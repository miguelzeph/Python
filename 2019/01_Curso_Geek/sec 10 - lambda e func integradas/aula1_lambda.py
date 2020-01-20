"""
Lambda = Funções sem nome
"""

# função em python

def teste(x):

    print(x*2)

teste(2)

# Lambda

calc = lambda x: x*2

print(calc(2))

#exemplo com varios parametros

func = lambda x,y,z,w: x*2-y*z+w

print(func(1,2,3,10))

# Exemplo  com lambda

nome_completo = lambda nome, sobrenome: nome.title()+" "+sobrenome.title()

print(nome_completo("miguel","amaral"))

#Exemplo melhorado

nome_compl = lambda nome, sobrenome: nome.strip().title()+" "+ sobrenome.strip().title()

print(nome_compl("   MIGUEl   ", "    amaral"))

#-----------------------------------logica importante--------------------------------------------------
# Vamos agora utilizar a expressão lambda onde realmente ela é útil...

# para isso vamos aplicar em uma função integrada (sort()) que já conhecemos

pessoas = ["Miguel Amaral", "Ana Aguiar", "Priscila Lobo", "Cintia Machado", "Astrogilda Derrico"]

pessoas.sort() # sort() = coloca na ordem através da PRIMEIRA LETRA
#OBS: ela não retorna... ela muda a variável "pessoas", por isso temos que printar pessoa e não printar pessoas.sort()

print(pessoas)

# Vamos agora ordenar pelo sobrenome... fazer uma função que faça ele pegar as palavras do sobrenome

pessoas.sort(key= lambda sobrenome: sobrenome.split(" ")[-1]) #[-1] pega o último termo do vetor

print(pessoas)
#------------------------------------------------------------------------------------------------------

# Criando função com lambda

def y(a,b,c):

    return lambda x: a*x**2 + b*x + c

resultado = y(1,1,1)(0)

print(resultado)