from visual import *

quadro = frame(pos=(0, 0, 0))

vetor=arrow(frame=quadro,pos=(0,0,0),axis=(0,1,0),color=color.blue,material=materials.wood)

bola=sphere(frame=quadro,pos=(0,0,0),radius=0.5,color=color.red,material=materials.wood)






while True:
 
	quadro.rotate(axis=(0, 1, 0), angle=0.1)
	
	rate(100)