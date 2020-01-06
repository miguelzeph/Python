from __future__ import division
from visual import *

trail = curve(color=(1,1,1),radius=0.5)
ball = sphere(radius=0.25)

t=0
dt=0.01
while 2>1:
	rate(50)
	
	t = t+dt
	
	ball.pos=(t,t,0)
	
	trail.append(pos=ball.pos, retain=10) # last 50 points

