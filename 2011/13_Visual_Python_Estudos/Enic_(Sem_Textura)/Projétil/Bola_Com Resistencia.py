# -*- coding: cp1252 -*-
from visual import *
from math import *
from visual.controls import *

scene.x=150
scene.y=150

scene.range = (20,20,20)
scene.center = (40,30,60)
scene.width = 650
scene.height =450
scene.title = 'LANCAMENTO OBLIQUO'


bola = sphere (pos = (0,0,0), radius =1, color=(0,0,1))
trajetoria = curve(color=bola.color)


#Dados
y0 = 0
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
e = 0.1
ve = 0

v_y=vy-9.8*t
v_x=vx

vector1=arrow(pos=bola.pos,axis=vector(0,v_y/2,0),color=color.red)
vector2=arrow(pos=bola.pos,axis=vector(v_x/5,0,0),color=color.red)


Verdade = True

while Verdade:
	
	rate (150)
	
	
	if bola.pos.y < 0:
		vy=-vy
		ve += e
		
		
    
	vy += g*dt - ve
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
	
	if bola.pos.y < -0.5 :
		Verdade = False
	#-----
	