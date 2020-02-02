# Exercicio 25

def S(*args):

    calculo = []

    for x in args:

        conta = (x** 2 + 1) / (x + 3)

        calculo.append(conta)


    return sum(calculo)


var = range(0,10)

print(S(*var))

#Exercício 26

def positivo(n):

    x = range(1,n+1)

    calculo = 0

    for i in range(0,len(x)):
        calculo = calculo + x[i]

    return calculo

print(positivo(10))

#ou poderia ter feito

calc = 0

vetor = range(0,10+1)

for x in vetor:

    calc = calc + x

print(calc)




#Exercício 27

def sinx(i=0,f=1,*args):


    for x in args:

        calculo = []

        for n in range(i,f):

            conta = ((-1)**n*(x*3.14)**(2*n+1))/(2*n+1)

            calculo.append(conta)



        print(f" para n = {i} até {f} e x = {x}, a conta deu = {sum(calculo)}")

vetor = range(0,5+1)

sinx(0,1,*vetor)
