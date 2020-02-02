"""
Python é uma linguagem de tipagem dinâmica = não precisa declarar o tipo da variável


Temos 2 tipos de scopo:

[1] Variável Global: São variáveis conhecidas, ou seja, seu scopo compreende todo o programa

[2] Variavel Local: São reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está
limitado no bloco que foi declarado

"""

#Exemplo - Fácil...

x = 10 #Variavel Global

if x == 10:

    y = 100 #Variável Local

    print(f"{x}, {str(y)}")

