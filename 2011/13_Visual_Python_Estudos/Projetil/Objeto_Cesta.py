# -*- coding: cp1252 -*-
from visual import *
from math import *


scene.range = (20,20,20)
scene.center = (40,30,60)
scene.width = 650
scene.height =450
scene.title = 'LANCAMENTO OBLIQUO'

#Material
bola = sphere (pos = (0,0,0), radius =1, color=(0,0,1))
trajetoria = curve(color=bola.color)
chao = box (pos = (40,-1,0), size = (80,0.5,10),color = (1,1,0.8),material=materials.rough)
teto = box (pos = (40,41,0), size = (80,0.5,10),color = (1,1,0.8),material=materials.rough)
anel = ring(pos=(75,20,0), axis=(0,1,0), radius=5, thickness=0.5, color = color.red)
parede = box (pos=(80,20,0), size=(0.5,42,10),material=materials.bricks)
parede2 = box (pos=(-1,20,0), size=(0.5,42,10),material=materials.bricks)

#Dados
y0 = float (input ('ALTURA DE LANCAMENTO: '))
print ''
v0 = float (input ('VELOCIDADE INICIAL: '))
print ''
teta0 =float (input ('ANGULO INICIAL: '))
print ''
pi = 3.141528
teta = teta0*pi/180
g = -9.8
vx = v0*cos(teta)
vy = v0*sin(teta)
dt = 0.01
t = 0
x = 0
y = 0
e = 0.4

v_y=vy-9.8*t
v_x=vx

vector1=arrow(pos=bola.pos,axis=vector(0,v_y/2,0),color=color.red)
vector2=arrow(pos=bola.pos,axis=vector(v_x/5,0,0),color=color.red)


Verdade = True
#while (bola.pos != anel.pos):
while Verdade:
	
	rate (150)
	
	if (bola.pos.x > 80 or bola.pos.x < 0):
		vx=-vx
		#vx=-vx*e
	if (bola.pos.y < 0 or bola.pos.y > 40):
		vy=-vy
		#vy=-vy*e
		
    
	vy += g*dt   
	y += vy*dt
	x += vx*dt
	bola.pos.x = x
	bola.pos.y = y + y0
	
	trajetoria.append(pos=bola.pos)
	
	
	#Vetor------
	v_y=vy-9.8*t
	v_x=vx
	
	vector1.pos=bola.pos
	vector1.axis.y=v_y/2
	vector2.pos=bola.pos
	vector2.axis.x=v_x/5
	#-----
	
	if (bola.pos.y <20 and bola.pos.y > 19):
		if (bola.pos.x <80 and bola.pos.x > 70):
			#raw_input('PARABENS !!! VOCE CONHSEGUIU')
			print 'PARABENS !!!! VOCE CONSEGUIU'
			
			Verdade = False
			c=0
			while True:
				rate(5)
				anel.color=(1,0,0)
				rate(5)
				anel.color=(0,0.5,1)  
			
	
			