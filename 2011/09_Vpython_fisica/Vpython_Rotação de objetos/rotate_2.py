from visual import *

quadro = frame(pos=(0, 0, 0))

box(frame=quadro,pos=(2,1,0),material=materials.wood)
caixa=sphere(pos=(0,0,0),radius=0.5,material=materials.wood)





while True:
 
	quadro.rotate(axis=(0, 1, 0), angle=0.1)
	caixa.rotate(axis=(1,0,0),angle=1)
	rate(10)