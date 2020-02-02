"""

open() -> função integrada do python

help(open) -> Leia a função

"""

arquivo = open('texto.txt')

#for nome in dir(arquivo): print(nome) #Veja as funções de open()


#OBS: a função open() trabalha com um lance chamado "CURSOR"... ou seja, se você manda ele
#ler algo, ele irá ler e parar no fim, se mandar ler novamente o mesmo arquivo, ele não
#irá ler, pois irá parar lá no fim...



#read - lê todo o conteudo do arquivo
ler = arquivo.read()
print(ler)



# Ler por linhas---------

#forma 1
ler_linhas_novo = ler.split('\n')
print(ler_linhas_novo)

#forma2
#readlines - é a função direta... (IGUAL AO ANTERIOR)
ler_linha = arquivo.readlines()
print(ler_linha)
#-------------------------


#Pŕoxima aula iremos aprender a trabalhar com o "CURSOR"...

