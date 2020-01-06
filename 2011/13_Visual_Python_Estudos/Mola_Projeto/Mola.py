
from visual import *



mola = helix(pos= (0,0,0),axis=(0,1,0), radius=0.2,coils=10,thickness=0.05,color=color.red)
bola = sphere(pos=mola.axis,radius = 0.4)
parede = box(pos=(0,0,0),size=(0.3,2,1))

x = 2
dx = 0.03



while (1==1):
	rate (250)
	
	x = x+dx
	
	if (x >= 5 or x <= 1):
		dx = -dx
		
	mola.axis = x
	bola.pos = mola.axis