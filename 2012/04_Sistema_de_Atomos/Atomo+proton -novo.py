from __future__ import division
from visual import *

scene.background =  (1,1,1)
scene.range = 4




quadro=frame(pos=(0,0,0))

#cargas positivas
part1=sphere(pos=(-2,0,0),color=(1,0,0))
part2=sphere(pos=(2,0,0),color=(0,0,1))



q1=-2.1e-2
part1.radius=0.1 # (q1**2)(1.0/2.0) somente para deixar positivo = raiz(a**2) = modulo
q2=1.e-2
part2.radius=0.1


#eletrons-------------
r = 1
r1=r
pos5=part1.pos*r
pos6=part1.pos*r1

part5=sphere(pos=pos5,color=(0,0,1))
part6=sphere(pos=-pos6,color=(0,0,1))



#----------------------------
V = 0*vector(0,1,0)

q5=1e-2
q6=q5
part5.radius=0.1
part6.radius=part5.radius


k=1
t=0
dt=1e-3
o = 0
do=6e-3

curva=curve(frame=quadro,color=part5.color)
curva6=curve(frame=quadro,color=part6.color)
for i in arange(0,2*pi,0.01):	
	
	o=i
	
	x=sin(o)*r
	z=cos(o)*r
	
	X=sin(o)*r1
	#Y=cos(o)*r1
	Z=cos(o)*r1
	
	
	
	curva.append((x,0,z))
	#curva6.append((X,Y,0))
	curva6.append((X,0,Z))
	





curva1=curve(color=part1.color)
curva2=curve(color=part2.color)


verdade = True

F15=vector(0,0,0)
F25=vector(0,0,0)
F16=vector(0,0,0)
F26=vector(0,0,0)
F12=vector(0,0,0)

while verdade:
	
	
	rate(10000000000)
	
	quadro.pos=part1.pos
	
	#-----------------
	t=t+dt
	
	o=o+do
	
	x=sin(o)*r+part1.x
	z=cos(o)*r+part1.z
	
	X=-sin(o)*r1+part1.x
	#Y=cos(o)*r1+part1.y
	Z=cos(o)*r1+part1.z
	
	part5.pos = vector(x,0,z)
	#part6.pos = vector(X,Y,0)
	part6.pos = vector(X,0,Z)
	#-----------------
	
	
	
	t=t+dt
	
	#os eletrons nao sofreram essas forcas--------
	r12=part1.pos-part2.pos
	
	r15=part1.pos-part5.pos
	r25=part2.pos-part5.pos
	
	r16=part1.pos-part6.pos
	r26=part2.pos-part6.pos
	
	
	n=1000
	
	F15 =+ ((k*q1*q5)/mag(r15)**2)*norm(r15) #+ F15/n
	F25 =+ ((k*q2*q5)/mag(r25)**2)*norm(r25) #+ F25/n
	
	
	
	F16 =+((k*q1*q6)/mag(r16)**2)*norm(r16) #+ F16/n
	F26 =+((k*q2*q6)/mag(r26)**2)*norm(r26) #+ F26/n
	#repulsao dos protons
	F12 =+ ((k*q1*q2)/mag(r12)**2)*norm(r12) #+ F12/n
	
	#-----------------------------------------------
	
	V = V - (+ (F15*t) + (F25*t))
	
	
	
	#part1.pos= part1.pos + (F15*t) + (F25*t)
	#part2.pos= part2.pos + (F25*t) + (F15*t)
	
	#tem que levar em consideracao as interacoes com os eletrons..
	part1.pos= part1.pos + (F12*t) - (F25*t) - (F26*t) #---> tirando este ele fica fixo
	
	part2.pos= part2.pos + (F25*t) + (F26*t) - (F12*t) 
	
	
	
	curva1.append(part1.pos)
	curva2.append(part2.pos)
	
	
	
	
	