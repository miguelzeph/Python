"""
Escrevendo um iterador customizado
"""

#Vamos fazer nosso próprio "range()"...

#vamos ter que entrar em Orientação a OBJETO

#OBS: FUNÇÕES DENTRO DE CLASSES, SÃO CHAMADOS DE
#MÉTODOSSSSSSS (para saber apenas)


class Contador:

    #isso é um METODO, e não FUNCAO, pois está dentro de uma CLASSE
    def __init__(self,menor,maior):
        self.menor = menor
        self.maior = maior

    #Transforma a Classe em Iterator (Por baixo dos panos)
    def __iter__(self):
        return self

    #Aplicando o Next (por baixo dos panos)
    def __next__(self):

        if self.menor < self.maior:

            numero = self.menor
            self.menor = self.menor+1

            return numero
        raise StopIteration("Paramos aqui antes do erro :D")


con = Contador(1,5)

print(con.menor)
print(con.maior)

it = iter(con)

"""
print(next(it))
print(next(it))
print(next(it))
print(next(it))
#print(next(it)) #Deu o Erro, passamos da lista
"""




for numero in Contador(0,10): #Fizemos a função RANGE
    print(numero)