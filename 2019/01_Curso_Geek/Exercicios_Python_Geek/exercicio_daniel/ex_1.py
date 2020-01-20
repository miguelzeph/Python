"""1-) Programa que receba um número e verifique
se ele está entre 0 e 10 e é par"""


num = int(input('Digite um número: '))

if num >= 0 and num <=10 and num%2 == 0:

    print("O número está entre 0 e 10 e é par")
else:
    print('Não deu...')