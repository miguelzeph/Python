"""

Bloco With ...

"""

#forma 1: Você precisa fechar o arquivo com a função CLOSE()

arquivo = open('teste.txt')

print(arquivo.read())

arquivo.close()


#Forma 2 - Com o With, você não precisa fechar, ele mesmo faz

with open('teste.txt') as arquivo:
    print(arquivo.read())