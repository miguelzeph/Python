import Blender
import math

esfera=Blender.Object.Get("Sphere.001")

m1=250000
m2=1000
G=6.67e-11

vox=0.09
voy=0.005

for t in range(1000):

	x=esfera.LocX
	
	y=esfera.LocY
	
	r= math.hypot(x,y)
	
	a= G*m1*m2/r**2
	
	ax=-a*x/r
	ay=-a*y/r
	
	vx=vox+ax
	vy=voy+ay
	
	xf=x+vx
	yf=y+vy
	
	esfera.LocX=xf
	esfera.LocY=yf
	
	vox=vx
	voy=vy
	
	Blender.Redraw()
	