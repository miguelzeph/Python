
from visual import *

ball = sphere()

ball1= sphere(pos =(0,5,1))


while True:
	rate(20)
	
	if scene.mouse.clicked:
		
		ball1.visible=False