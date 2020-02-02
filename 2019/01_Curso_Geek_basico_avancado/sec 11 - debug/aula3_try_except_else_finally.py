#Exemplo
"""
# -------Forma 1 - mais utilizada
try:
    num = int(input("Informe um Número: "))
    print(f"você digitou um número inteiro: {num}")
except ValueError:
    print("Valor incorreto")

# ---------Forma 2 - Com ELSE (pouco utilizada)

#else é executado somente se não ocorrer o erro.
try:
    num = int(input("Informe um Número: "))

except ValueError:
    print("Valor incorreto")

else:
    print(f"você digitou um número inteiro: {num}")


# FINALLY -> SEMPRE SERÁ EXECUTADO, COM OU SEM ERRO.


try:
    num = int(input("Informe um Número: "))

except ValueError:
    print("Valor incorreto")

else:
    print(f"você digitou um número inteiro: {num}")

finally:
    print ("com ou sem erro, eu sempre sou executado hohoho")

"""

def dividir(a,b):

    try:
        print(a/b)
    except (TypeError,ValueError,ZeroDivisionError) as errinho:
        print(f"Ocorreu um problema... {errinho}")
dividir(10,'a')



# Eu gosto de usar assim

try:
    print(x)
except: #Sem nada, ele engloba tudo dai

    print("Deu Erro")


def oi():

    try:
        return x #n existe x, nao vai conseguir
    except:
        a = 'DEU ERRO'
        return a

print(oi())