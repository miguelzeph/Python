"""
Criando vários objetos em forma de Array...

é melhor que o outro jeito mostrado na aula6, pois agora fica fácil chamar!
"""


class Amostra(object):
    def __init__(self, nome, ur, ui):
        self.nome = nome
        self.ur = ur
        self.ui = ui

# Simulando meus arquivos.
TXT = ['niquel.txt', 'carbono.txt', 'teflon.txt']

# Lista de Objetos.
samples = []

# Criando os objetos dentro do For
for arquivo in TXT:
    samples.append(Amostra(arquivo[:-4], None, None))

# Dados...
ur = [1, 2, 3, 4]
ui = [1, 2, 3, 4]

# Introduzindo os dados dentro dos meus OBJETOS em Array
for sample in samples:
    sample.ur = ur
    sample.ui = ui

# Testando eles...
print(samples[0].__dict__)
print(samples[1].__dict__)

print(samples[0].ur)
print(samples[0].ur[0])
