from visual import *
scene2 = display(title='ATOMO',x=0, y=0, width=600, height=500,center=(5,0,0), background=(0,0,0))
scene2.lights = [vector(6,0,2)]
#protons
n1 = sphere(pos=(0,-1,0), radius=1, color = (0.2,0.2,0.2))
n2= sphere(pos=(0,1,0), radius=1, color = (0.2,0.2,0.2))
p1 = sphere(pos=(-1,0,0), radius=1, color = color.red)
p2 = sphere(pos=(1,0,0), radius=1, color = color.red)
#eletrons
e1 = sphere(pos=(0,0,0), radius=0.5, color = color.blue)
e2 = sphere(pos=(0,0,0), radius=0.5, color = color.blue)

#lomas=label(text="www.lomasdeterciopelo.co.cr", pos=(0,-19,0))
t=0
dt=0.1
raio=10
curva1= curve(color =(1,1,1))#RGB
curva2= curve(color =(1,1,1))

while True:
	rate(20)
	t=t+dt
	
	x=sin(t)*raio
	y=cos(t)*raio
	z=cos(t)*raio
	
	
	e1.pos=(x,y,z)
	
	X=cos(t+0.5)*raio
	Y=cos(t+0.5)*raio
	Z=sin(t+0.5)*raio
	
	e2.pos=(X,Y,Z)
	
	curva1.append(pos=e1.pos)
	curva2.append(pos=e2.pos)