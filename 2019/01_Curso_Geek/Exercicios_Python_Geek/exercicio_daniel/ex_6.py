"""6-) Jogo da adivinhação"""
import random
adivinhar = random.randint(0,100)
cont = 1
win = False
while cont <= 10 or win == True:
    tentativa = int(input(f"Tente {cont}: "))
    if tentativa == adivinhar:
        print("PARABÉNS!!!!!!! VOCÊ ACERTOU")
        win = True
    else:
        print("Você Errou")
    cont +=1
if win == False:
    print(f"O número secreto era -> {adivinhar} <-")