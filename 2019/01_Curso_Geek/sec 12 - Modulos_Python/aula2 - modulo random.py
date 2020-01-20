
# Só quero importar a função RANDOM da biblioteca RANDOM...
import random

#Exemplo - funcao Random

x = random.random() # 0 - 1

print("%.2f"%(x)) # apenas duas casas depois da vírgula



#uniform(a,b)-> gera valores aleatorios entre um intervalo definido (números quebrados)

for i in range(0,10):

    print(random.uniform(3,7)) #não chega até 7

#randint(a,b) -> números aleatórios em um intervalo (números inteiros)

for i in range(0,10):

    print(random.randint(3,7)) #não chega até 7


#choice() -> escolhe um valor para você

jogar = ['pedra','papel', 'tesoura']


print(random.choice(jogar))

letras = 'Miguel Angelo do Amaral Junior'

print(random.choice(letras))

#shuffle() -> embaralha os dados


cartas = ["A",1,2,3,4,5,6,7,8,9,10,"Q","J","K"]

print(cartas)
random.shuffle(cartas)
print(cartas)

#Exemplo, distribuir cartas na mesa

for i in range(0,len(cartas)):

    random.shuffle(cartas)

    #Função pop
    #pop() = por padrão ele printa e remove o último elemento
    #pop(0) = printa e remove o primeiro elemento.. p(1) = segundo elemento... p(3) = ... etc

    print(cartas.pop())

print(cartas) #Vazio



