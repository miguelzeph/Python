# Todos os dados vindo por INPUT = String

print('Qual seu nome?\n')

nome = input("Digite seu nome: \n")

idade = input("Digite sua idade: \n")

print(nome+' tem '+idade+' anos')




#-------Versão Python 2x---------

print("%s tem %s anos"%(nome,idade))

#-------Versão Python 3x---------

print("{0} tem {1} anos".format(nome,idade))

#-------Versão Python 3.7--------

print(f"{nome} tem {idade} anos")

print(f"{nome} nasceu em {2019 - int(idade)}\n")

# OBS: Cast = mudança no formato do dado... exemplo: Int para stirng...
