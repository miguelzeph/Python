"""
Locals() e Globals()


Essa aula não está no curso, eu que fiz...

* Problema: eu queria criar objetos através de funções, sem precisar ficar declarando a variável de modo iterável...

->Exemplo jeito que eu não quero:

pessoa1 = Classe(....)
pessoa2 = Classe(....)
.
.
.
pessoan = Classe(....)

-> Exemplo que eu quero:

for i in range(0,10):

    pessoai = Classe(....)


-> SOLUÇÃO ENCONTRADA através da função LOCALS(), veja
"""

# Exemplo 1
locals()['x'] = "fui criado como x" # isso é equivalente a x=1

print(x)

# Exemplo 2 - com FOR
for i in range(0,10):
    locals()[f"pessoa{i}"] = i

print(pessoa1,pessoa2,pessoa3,pessoa4)

#Exemplo 3 - com Funções - TEMOS QUE USAR GLOBALS()
def cria(nome):

    x = globals() #não dá certo ocm locals()

    x[f'{nome}'] = nome

   # return x # Não precisei

cria('Miguel')
print(Miguel)

# Exemplo 4 - Classe e função

class Amostra:

    def __init__(self,nome,er,ei,ur,ui, d):

        self.nome = nome
        self.er = er
        self.ei = ei
        self.ur = ur
        self.ui = ui
        self.d = d #espessura

arquivos = ['amostra1','amostra2','amostra3']

for arquivo in arquivos:

    locals()[f'{arquivo}'] = Amostra(arquivo, [], [], [], [], 5)

print(amostra1.d)
print(amostra2.d)
print(amostra3.d)

# ESSE JEITO FICA RUIM NA HORA DE VOCÊ CHAMAR OS OBJETOS... POR ISSO EU FIZ UM MELHOR
# ESTÁ NA AULA 7
