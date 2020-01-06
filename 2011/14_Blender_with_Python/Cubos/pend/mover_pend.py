import Blender
import math
import time

nome=["Cube"]

#Variavei minha ...
obj=Blender.Object.Get(nome[0])

dtx=0.2
dty=0.2
x=0
y=0

l=8

while True:
	
	time.sleep(0.1)
	
	y=y+dty
	x=x+dtx		
	
	obj.LocX = math.cos(x)*l
	obj.LocY = math.sin(y)*l
	
	
	
	Blender.Redraw()
	
		