from visual import *

terra = sphere(radius = 10,material = materials.earth)
Lua = sphere(radius = 0.5,material = materials.rough)
trajetoria = curve(color=(1,1,1))

t=0
dt = 0.01
r=25
r1=15
while True:
	rate(50)
	
	t=t+dt
	
	x =sin(t)*r
	z = cos(t)*r1
	
	Lua.pos =(x,0,z)
	
	terra.rotate(axis=(0,1,0), angle=0.008)
	
	trajetoria.append(Lua.pos)