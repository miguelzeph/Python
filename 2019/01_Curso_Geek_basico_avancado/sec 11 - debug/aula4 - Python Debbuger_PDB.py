"""
Duas maneiras de ver os bugs...


1-) PDB - Python Debugger

ou

2-) pelo IDL... (nosso caso PyCharm)

OBS: NAO FIQUE DANDO PRINT PRA SABER ONDE ESTÁ O BUG... ESSA É A MANEIRA "FEIA"


"""

#Exemplo - Pelo PyCharm (GOSTEI DESSA)

#Clique ao lado do número de linha, para definir início e fim do que iremos analisar

def dividir(a,b):

    try:
        return int(a)/(b)

    except (ValueError, ZeroDivisionError) as E:
        return f"Ocorreu o problema: {E}"

print(dividir(10,1))

#Exemplo  PDB (importar)

import pdb # no python 3.7 não precisa mais importar, basta você usar a função

#breakpoint() ... já inicia o Debug

#Muita decoreba... mais fácil com o pycharm



