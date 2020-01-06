from visual import *

quadro = frame(pos=(0, 0, 0))

box(frame=quadro,pos=(0,1,0),material=materials.wood)
sphere(pos=(0,0,0),radius=0.5)




while True:
 
	quadro.rotate(axis=(0, 1, 0), angle=0.1)
	rate(10)