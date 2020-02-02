"""2-) Teste se o ano é bissexto"""

ano = int(input("Digite o ano: "))

if ano%4 == 0:
    print("É ano bissexto, tem 366 dias")
else:
    print("Não é ano bissexto, tem 365 dias")