import Blender
import math
import time

# Pega a cena atual
cena = Blender.Scene.GetCurrent()

#objetos da cena

obj=Blender.Object.Get()

camera=obj[0]
cubo=obj[1]
lampada=obj[2]

#mover camera

camera.setLocation(8., -8., 4.)
camera.setEuler(math.radians(70), 0.,math.radians(45))

# Muda a lente
camera.data.lens = 30

	


