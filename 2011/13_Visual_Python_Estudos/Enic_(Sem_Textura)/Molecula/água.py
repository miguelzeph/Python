from visual import *


scene2 = display(background=(1,1,1))

quadro = frame(pos=(0,0,0))


O = sphere(frame = quadro,pos=(0,0,0), radius = 0.8,color=(1,0,0))
h = sphere(frame = quadro,pos=(1.5,-2,0), radius = 0.4,color=(0,0,1))
h1 = sphere(frame = quadro,pos=(-1.5,-2,0), radius = 0.4,color=(0,0,1))


cilindro1=cylinder(frame = quadro,pos=(0,0,0), axis = h.pos,radius =0.1,opacity=0.5)
cilindro1=cylinder(frame = quadro,pos=(0,0,0), axis = h1.pos,radius =0.1,opacity=0.5)

while True : 
	rate(55)
	#quadro.rotate(axis = (0,1,0), angle= 0.05)
	quadro.rotate(axis = (1,0,0), angle= 0.03)
	quadro.rotate(axis = (0,0,1), angle= 0.05)