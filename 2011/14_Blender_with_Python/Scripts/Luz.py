import Blender
import math
import time

# Pega a cena atual
cena = Blender.Scene.GetCurrent()

#objetos da cena

obj=Blender.Object.Get()

lamp=obj[2]

# Altera a intensidade da luz
lamp.data.energy = 500
# Muda o tipo para "Sun"
lamp.data.type = 1
# Aumenta o número de samples
lamp.data.raySamplesX = 16
lamp.data.raySamplesY = 16
# E a cor
lamp.data.col = 0.0, 0.0, 0.8
# Cria outra fonte de luz
lamp1 = Blender.Lamp.New('Lamp')
lamp1.energy = 0.5
lamp1.col = .9, 1., 1.
_lamp1 = Blender.Object.New('Lamp')
# Muda o lugar da fonte (default = 0.0, 0.0, 0.0)
_lamp1.setLocation(6., -6., 6.)
# "Prende" a fonte de luz na cena
_lamp1.link(lamp1)
cena.objects.link(_lamp1)


