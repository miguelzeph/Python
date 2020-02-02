"""
vetor.sort() = organiza seu vetor pela ordem... (ele altera o vetor)

sorted(vetor) = '     '     '    '    '   '  ... (ele cria uma lista)


"""

#Exemplo

x = [9,6,3,5,8]

x.sort() #alterou

print(x)

y = [7,6,5,4,3]

y1 = sorted(y) #criou outra lista

print(y1)


# Exemplo

# o sorted() ele organiza pelo tamanho (padrão)... veja o exemplo abaixo

cadastro = [
    {"user": "Miguel", "idade": 28, "profissão": "programador", "faculdade": "Física"},
    {"user": "Priscila", "idade": 26},
    {"user": "Gui", "idade": 25, "profissão": "Médico"}
]

# Se eu aplicar o sorted() diretamente, ele vai organizar por quem tem mais elementos no dict

#print(sorted(cadastro)) #erro - #Quando tiver dicionarios, temos que chamar outro parâmetros, se não ele não entende
# parâmetro key..

print(sorted(cadastro, key = len)) # key = len -> faz pelo tamanho do dict o ordenamento (menor pro maior)

print(sorted(cadastro, key = lambda chave: chave["user"])) # Organiza pelos "user" (nome- ordem alfabética)

print(sorted(cadastro, key = lambda chave: chave["idade"])) # por idade...

# parâmetro REVERSE - inverto  ordem

print(sorted(cadastro, key = lambda chave: chave["idade"], reverse = True)) # idade maior para menor



