"""
Prezervando Metadatas com Wraps

Metadatas -> são dados intrínsecos dos arquivos, exemplo: tamanho, data...

Wraps -> São FUNÇÕES que envolvem elementos com diversas finalidades

"""

#Problema

def ver_log(funcao):

    def logar(*args,**kwargs):

        """Funcao Logar"""
        print(f"Função: {funcao.__name__}") #Nome
        print(f"Documentação: {funcao.__doc__}") #Documentação da Função

        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a,b): #soma = nome da função...
    """soma dois numeros""" #isso é a documentação....
    return a+b

soma(1,1)
print('\n')
print(soma(1,1))


# Vamos ao problema... os metadados da função foram alterados... Entendeu???
print('\n')

print(soma.__name__) # Era para ser "soma".
print(soma.__doc__) # Era para ser "Soma dois Numeros"



print('\n')


#RESOLVENDO ISSO... tem que usar wraps

from functools import wraps #Preserva os metadatas das funções!



def ver_log(funcao):
    @wraps(funcao) #PRONTO, fizemos um decorator dentro dela, agora está correto.
    def logar(*args,**kwargs):

        """Funcao Logar"""
        print(f"Função: {funcao.__name__}") #Nome
        print(f"Documentação: {funcao.__doc__}") #Documentação da Função

        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a,b): #soma = nome da função...
    """soma dois numeros""" #isso é a documentação....
    return a+b

print(soma(10,10))

print('\n')

#Resolvemos o Problema!!!

print(soma.__name__) # Era para ser "soma".
print(soma.__doc__) # Era para ser "Soma dois Numeros"