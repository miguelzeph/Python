import Blender
import math
import time

# Pega a cena atual
cena = Blender.Scene.GetCurrent()

#objetos da cena

obj=Blender.Object.Get()


cubo=obj[1]

cena.objects.unlink(cubo)
	


