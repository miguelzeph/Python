"""
Lista Comprehension -

Podemos adicionar valores Lógicos!

"""

#Exemplo

n = [1,2,3,4,5]

impar = [numero for numero in n if (numero % 2) != 0 ]
par = [numero for numero in n if (numero % 2) == 0]

print(impar)
print(par)