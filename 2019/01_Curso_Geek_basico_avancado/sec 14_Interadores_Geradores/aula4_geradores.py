"""

Geradores (generators)  são Iterator ...

Mas nem todo Iterador, é um Gerador

- Geradores podem ser criados por funções geradores
- funções geradores recebem a palavra "yield"
- Generatores podem ser criados com Expressões geradoras

--------------------------------------------------------------------------------------
/ Function                                /Generator Function
--------------------------------------------------------------------------------------
/ utilizam "return"                       / utilizam "yield"
/ retorna uma vez                         / podem utilizar yield multiplas vezes
/ retorna sempre um valor (vazio = None   / retorna um generator



"""

#Exemplo de Gerator Function

def conta_ate(valor_maximo):
    contador = 1

    while contador <= valor_maximo:
        yield contador #Ele espera o NEXT... se usar Return vai falhar...
        contador = contador +1

# Generator Function não é um generator,
#ela gera um generator...

gen = conta_ate(5)

print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))

for num in gen:

    print(num)#Ele começa a partir do 4!!!!! Pois já chamamos
    #ele lá em cima...

lista = list(gen) #Ficou  vaziou, pois já chamamos todos...
print(lista)

