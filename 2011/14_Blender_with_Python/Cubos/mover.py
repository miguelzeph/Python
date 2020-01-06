import Blender

nome=["Cube"]

#Variavei minha ...
obj=Blender.Object.Get(nome[0])

dtx=0.2
dty=0.2
x=obj.LocX
y=obj.LocY
while True:
	if abs(x) >= 20:
		dtx=-dtx
	if abs(y) >= 10:
		dty=-dty
		
	y=y+dty
	x=x+dtx		
	
	obj.LocX = x
	obj.LocY = y
	Blender.Redraw()
	
		