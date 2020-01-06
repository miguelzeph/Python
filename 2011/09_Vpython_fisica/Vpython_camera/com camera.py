from visual import *
#----------------------------
scene.center = (0,0,0)
#manipula o quadro....
scene.width = 1000
scene.height = 1000

scene.range = (100,10,10)
#--------------------------
parede=box(pos=(-1,0,0),size=(1,10,10))
parede1=box(pos=(20,0,0),size=(1,10,10))
ball=sphere(pos=vector(0,0,0),radius=1)
v0=10
segundos=0
dt=0.01

a=100
while a >0:
	rate(100)
	a=a-1
	segundos = segundos +dt
	alcance= 0+v0*segundos#mru
	ball.pos=vector(alcance,0,0)
	if a == 0:
		segundos=0
		
		while a < 100:
			
			rate(100)
			a=a+1
			segundos = segundos +dt
				
			alcance=ball.x-v0*segundos#mru
			ball.pos=vector(alcance,0,0)
			ball.color=color.green
	