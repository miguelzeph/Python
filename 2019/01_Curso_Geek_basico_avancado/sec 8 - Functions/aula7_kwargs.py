"""
**kwargs -> parecido com o *args... mas você usa com dicionários
"""

def teste(**kwargs):

    print(kwargs)

teste(a=1,b=2,c=3,d=4) #mota um dicionario

"""
Podemos ter nas funções (NESTA ORDEM):
1- Parâmetros Obrigatórios
2- *args
3- Parâmetros Não Obrigatórios
4- **kwargs
"""
#exemplo:

def funcao(nome, idade, *args, solteiro = True, **kwargs):
    print(f"{nome} tem {idade} anos") #Parâmetro Obrigatório
    print(args) # Args
    if solteiro: #Parâmetro Não Obrigatório
        print("Solteiro")
    else:
        print("Casado")
    print(kwargs) # Kwargs

funcao("Miguel", 28)
funcao("Miguel", 28,1,2,3,4,5,6)
funcao("Miguel", 28,1,1,1,1,1,1,solteiro = False)
funcao("Miguel", 28,1,1,1,1,1,1,solteiro = False, jogo = "Metal Gear", Linguagem = "Python", Materia = "Fisica")


# Outro exemplo da importância da ordem dos parâmetros

def mostra(a,b,*args,nome = "miguel",**kwargs):

    return a,b,args,nome,kwargs

print(mostra(1,2,"args","args","args", nome = "Amaral",c=10,d=20,e=30))

# ----------------Desempacotar com Kwargs !!!-------------

def mostra_nome(**kwargs):

    print(f"{kwargs['nome']} {kwargs['sobrenome']}")

mostra_nome(nome="Ana",sobrenome="Aguiar") #funciona fácil...

nome = {'nome': 'Miguel', 'sobrenome': 'Amaral'}

#mostra_nome(nome) # Error ... tem que desempacotar

#temos que desempacotar esse dicionário

mostra_nome(**nome)


