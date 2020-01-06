from visual import *

scene.autoscale=0

#scene.center=(0,0,0)
scene.range=(50,20,40)

scene.width = 800
scene.height =800


#Estrela---------------------------------------------------------------------------------------------------
def posic_estrela():
	
	R=25
	
	x=random.uniform(-100,100)*R
	y=random.uniform(-100,100)*R
	z=random.uniform(-100,100)*R
	
	loc = (x,y,z)
	return loc
	
def radius_estrela():
	
	t=random.uniform(1,4)
	
	return t
	
	

n = 100
for i in range (0,n):
	
	strela = sphere(pos = posic_estrela(),radius = radius_estrela() ,color=(1,1,1),material = materials.emissive)
#-----------------------------------------------------------------------------------------------------------------




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