"""
Modulo collection - counter (contador)

- é utiliado para contar qualquer interável (lista, tupla, set) ...
- ele retorna o resultado em forma de DICIONÁRIO

"""

from collections import Counter

#exemplo 1

x = [1,2,3,4,4,4,4,1,1,2,2,5,5,6,7,8,9,9]

y = Counter(x)

print(y)

#exemplo 2

z = ('miguel',"miguel","Miguel","Miguel","pri", "pri", "pri", "pri")

h = Counter(z)

print(h)

#exemplo 3

nome = "Miguel Angelo do Amaral Junior"

quantidade = Counter(nome)

print(quantidade)

#Exemplo 4 - palavras

texto = "Física é uma ciência natural que estuda as propriedades da matéria e da energia, " \
        "estabelecendo relações entre elas. Baseia-se em experimentações da vida que nasce na Física " \
        "e morre na Física"

palavra = texto.split(" ")

palavra_cont = Counter(palavra)

print(palavra_cont)

# Encontra as 4 palavras que mais se repetem!!!

print(palavra_cont.most_common(4))





