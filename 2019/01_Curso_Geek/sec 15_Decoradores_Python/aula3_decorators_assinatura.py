"""
Decorators com diferentes assinaturas

"""

def gritar(funcao):

    def aumentar(nome):

        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):

    return f"Olá, eu sou o(a) {nome}"

@gritar
def ordenar(principal, acompanhamento):

    return f"Olá, eu gostaria de {principal}, com {acompanhamento}"

#Testando

print(saudacao('Miguel'))


#Dá erro, pois estamos enviando 2 parâmetros
# e o gritar espera apenas 1...
#print(ordenar("picanha","batata"))




# Para resolver, utilizamos o Decorator Pattern

#Refatorando com Decorator Pattern

def gritarrr(funcao):

    def aumentar(*args, **kargs): #Mudamos aqui..
        return funcao(*args, **kargs).upper()
    return aumentar



@gritarrr
def saudacaooo(nome):

    return f"Olá, eu sou o(a) {nome}"

@gritarrr
def ordenarrr(principal, acompanhamento):

    return f"Olá, eu gostaria de {principal}, com {acompanhamento}"

print(saudacaooo("miguel"))
print(ordenarrr("carne",'arroz'))

print('\n\n')

def verifica_primeiro_argumento(valor):

    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f"valor incorreto, primeiro valor precisa ser {valor}"
            return funcao(*args,**kwargs)
        return outra
    return interna

@verifica_primeiro_argumento('pizza') #primeir arg tem que ser pizza
def comida_favorita(*args):
    print(args)
@verifica_primeiro_argumento(10) #primeiro arg tem que ser 10
def soma_dez(num1,num2):
    return num1 + num2

#Testando

print(soma_dez(10,12)) #22
print(soma_dez(1,21)) #tem q ser maior que 10 o primeiro parâmetro

print(comida_favorita('pizza','churrasco'))
print(comida_favorita('churrasco','pizza')) #precisa ser "pizza primeiro parâmetro
