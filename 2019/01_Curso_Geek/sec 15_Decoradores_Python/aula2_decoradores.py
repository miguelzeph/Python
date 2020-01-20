"""
Decoradores (Decorators)

O que são decorators?

- Decorators são funções;
- Decoratos envolvem outras funções e
aprimoram seu comportamento.
- Decorators também são HOF
- Utilizam @ (Syntact Sugar)... RECOMENDADO





#Decorators como função - Não recomendado

def seja_educado(funcao):
    def sendo():
        print('foi um prazer')
        funcao()
        print('tenha um ótimo dia')

    return sendo

def saudacao():
    print("seja Bem vindo(a) à casa")

#Testando 1

saudacao() #sem decorar

teste = seja_educado(saudacao) #Decorando.

teste() # testando, decorando

#veja, ela foi aprimorada...




#Testando 2

def raiva():
    print('Eu te odeio')

raiva_educada = seja_educado(raiva)

raiva_educada()

"""



# Decorators - Forma Recomendada....

def seja_educado_mesmo(funcao):

    def sendo_mesmo():

        print('foi um prazer conhecer vc')

        funcao()

        print('tenha um excelente dia')

    return sendo_mesmo

@seja_educado_mesmo #Não preciso criar variavel (DECORADOR)
def apresentando():
    print('Meu nome é Pedro')

#testando

apresentando()



# Ele jogou o "apresentando()" dentro do "seja_educado_mesmo"...

seja_educado_mesmo(apresentando()) # Dá no mesmo...


#Testando novamente

@seja_educado_mesmo
def dormir(): #Não pode ter argumentos quando usar decorators...

    print(f"dormir às 10:00")

dormir() #Sem parâmetros dentro do "Domir()"



# OBS: Não confundir DECORATOR com DECORATOR FUNCTION...

#Exemplo

def decorator_function(funcao): # ISSO é um DECORATOR FUNCTION

    return funcao

@decorator_function # ISSO é um DECORATOR
def faz_algo():
    print("\nFaz algo porra kkkkk")

faz_algo()