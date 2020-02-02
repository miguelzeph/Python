"""
Nesta Aula o Professor ensinou sobre string
"""

nome = "miguel angelo do amaral junior"

print(nome.title())

print(nome[0:6])

print(nome[7::])


arquivo = "nome.txt"



#quero somente o nome sem a extensão

print(arquivo[0:len(arquivo)-4])#Slice the String


#quero somente a extensão

print(arquivo[len(arquivo)-4::])#Slice the String

#função Split

x = "Miguel Angelo"

y = x.split(" ")

print(y[0])

print(y[1])

# Função strip() = Remove os espaços... antes e/ou depois

#exemplo

nome = "    miguel Angelo do amaral      "

print(nome)
print(nome.strip())

