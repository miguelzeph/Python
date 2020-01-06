from visual import *

ball=sphere(pos=vector(0,0,0),radius=1)
v0=10
segundos=0
dt=0.01

a=100
while a > 0:
	rate(100)
	a=a-1
	segundos = segundos +dt
	alcance= 0+10*segundos#mru
	ball.pos=vector(alcance,0,0)
while a<100:
	rate(100)
	a=a+1
	segundos = segundos +dt
	alcance= 0-10*segundos#mru
	ball.pos=vector(alcance,0,0)
	ball.color=color.green
	