from visual import *

mola = helix(pos= (0,0,0),axis=(0,1,0), radius=0.2,coils=10,thickness=0.05,color=color.red)

x = 2
dx = 0.03

y= 0
dy = 0.001


while True:
	rate (100)
	
	
	y = y + dy 
	
	x = x+dx
	
	if (y >= +0.5 or y <= -0.5):
		dt = -dy
	
	if (x >= 5 or x <= 1):
		dx = -dx
		
	mola.axis = (x,y,0)
	
	
	