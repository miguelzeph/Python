"""
docstrings serve para quando vc faz uma função, dai quando utilizar o comendo help(funcao) ... aparecerá
o que você colocou entre as 3 aspas duplas.

"""
def diz_oi():
    """Uma função que diz 'oi'""" #isso é uma docstring... quando você der help(diz_oi) vai aparecer isso
    return "oi"

help(diz_oi) #coloque sem os parentes da função... se não ela retorna o "oi".


from docstring_meu import doc # Se colocar * no lugar de doc = importa tudo
# #Só criei docstring_meu.py para poder importar

print(doc())

