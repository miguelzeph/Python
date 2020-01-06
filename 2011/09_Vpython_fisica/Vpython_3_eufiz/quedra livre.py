from visual import *

#scene.width=800#largura
#scene.height=600#altura

#scene.autoscale=0
#scene.range=(100,100,100)
#scene.center=(0,40,0)

ball=sphere(pos=(0,100,0),radius=2,color=color.red)
ground=box(pos=(0,-1,0),size=(10,2,10))

gravity=9.8 #m/s^2
seconds=0
dt= 0.01

finished= False

while not finished:
	rate(100)
	seconds=seconds+dt#ou podemos colcoar , seconds+=dt
	#seconds +=dt , ele add seconds + dt ...
	
	
	#position function:y(t)=y0+v0.t-0.5*g*t**2
	altura=100+0*seconds-0.5*9.8*(seconds)**2
	#fazer variar o vetor em y...
	ball.pos=(0,altura,0)
	
	if altura <=0:#quando altura for igual ou menor a zero
		finished=True#parar o loop
		print 'seconds to drop(tempo de queda):'+str(seconds)