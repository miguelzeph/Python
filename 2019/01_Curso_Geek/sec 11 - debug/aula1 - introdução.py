# Erros mais comuns... existem vários

#Exceptions = Error ... são sinônimos

# 1-) SyntaxError - você escreveu algo que o python não -------
# reconhece como linguagem

# exemplo
"""
def oi:
    print"oi"

"""
# certo


def oi():
    print('oi')
oi()

# Exemplo

# None = 1 #utilizar palavra reservada pelo python...
# ----------------------------------------------------------


# 2-) NameError - ocorre quando uma variável n foi definida

# Exemplo:

# printf('oi')

# print(x) # x não está definido


# 3-) TypeError

#Exemplo:

#len(10) #Len não tem para tipo INT... só SET, LIST, TUPLA


# 4-) IndexError - (índices) tentamos acessar uma lista, onde não exista o elemento

# Exemplo:

#y = [1,2,3]

#z = y[10] #só temos até 2...


# 5-) ValueError - quando uma função integrada (built-in) recebe um argumento
# com tipo correto, mas valor inapropriado

#z = int("sou uma string")
#z1 = int('10') #correto


# 6-) KeyError - temos acessar um elemento em um DICIONÁRIO, com uma CHAVE que não existe

#dic = {'oi':10}

#dic['tchau']


# AttributeError - ocorre quando uma variável não tem um atributo/função

#Exemplo

x = (11,2,3,6,4,3,2,1) #Imutável, logo não troca posição e nao aumenta

#x.append(10) #não pode... tem que ser []

#x.sort() # idem...



#IdentationError - quando não respeitamos o modo "cascada" do python

#for i in range(0,10):
#print(i)

#Correto
#for i in range(0,10):
#    print(i)
