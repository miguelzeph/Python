"""

"Seek" utilizado para mover o "Cursor"

Pois, quando você lê um doc, o cursor vai para o final, dai quando você lê ele novamente,
o arquivo está vazio, pois ele foi para o fim... entendeu? Faça teste... printe
2 x um open() com read()

"""


arquivo = open('teste.txt')

print(arquivo.read())

#cursor foi para o fim, se sentar printar de novo, não terá nada...

#voltar o cursor pro início

arquivo.seek(0)

#readline() - le uma linha.

arquivo = open('teste.txt')

print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())

#readlines() - cria um vetor com linha

arquivo = open('teste.txt')

ler = arquivo.readlines()

print(ler[0])
print(len(ler))

#close() -> Sempre feche o arquivo!!

arquivo.close()

#closed -> verifica se fechamos o arquivo

print(arquivo.closed) #True = fechado... #False = aberto




