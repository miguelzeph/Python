from __future__ import division
from visual import *

scene.background =  (1,1,1)
scene.range = 3

#cargas positivas
part1=sphere(pos=(-2,0,0),color=(1,0,0),radius=0.25)



curva1=curve(color=part1.color,radius=0.1)

t=0
o = 0

verdade = True

pos=(0,0,0)

while verdade:
	
	rate(50)
	
	dt=0.2
	do=0.1
	
	t=t+dt
	
	X=sin(t)
	Y=cos(t)
	
	pos = vector(X,Y,0) 
	
	o=o+do
	
	x=sin(o)+pos.x
	z=cos(o)
	y= pos.y
	
	part1.pos = (x,y,z)
	
	
	curva1.append(part1.pos)
	
	
	
	