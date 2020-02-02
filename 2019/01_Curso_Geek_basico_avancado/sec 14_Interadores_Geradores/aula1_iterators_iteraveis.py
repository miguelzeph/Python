"""

OBJETIVO DA AULA -> ITERATOR X ITERABLE

Iterator: (RESUMO... quando você consegue usar a funcao "next()"...)
- Objeto que pode ser iterado
- Objeto que retoma um dado

Iterable: (usar ufncao "iter()")
-Objeto que retoma um iterado


"""

nome = "Miguel"
numero = [1,2,3,4]


#criar iterable
it1 = iter(nome)
it2 = iter(numero)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
#print(next(it1)) #Vai dar Erro, não tem próximo...

print(next(it2))
print(next(it2))
print(next(it2))

# Equivalente ao meu..
for num in numero: #por baixo dos panos, ele faz o iter() e aplica o next
    print(num)
#Cada looping, ele usa o next...