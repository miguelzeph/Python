

#Exemplo

dic = {"a":1,"b":2,"c":3,"d":4}

dic_dobro = {chave:valor**2 for chave,valor in dic.items()}

print(dic_dobro)

# Exemplo

number = [1,2,3,4,33,45,67,100]

dic_new = {num: ("par" if num % 2 == 0 else "impar") for num in number}

print(dic_new)

# Mesmo exemplo sem comprehension dict

d = {}

for n in number:

    if (n % 2) == 0:
        d[n] = "par"
    else:
        d[n] = "impar"

print(d)

