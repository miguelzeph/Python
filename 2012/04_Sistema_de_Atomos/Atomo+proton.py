from __future__ import division
from visual import *

scene.background =  (1,1,1)
scene.range = 4

#cargas positivas
part1=sphere(pos=(-2,0,0),color=(1,0,0))
part2=sphere(pos=(2,0,0),color=(1,0,0))


q1=-1e-2
part1.radius=0.1 # (q1**2)(1.0/2.0) somente para deixar positivo = raiz(a**2) = modulo
q2=-1.e-2
part2.radius=0.1


#eletrons-------------
r = 2
pos5=part1.pos*r

part5=sphere(pos=pos5,color=(0,0,1))
part6=sphere(pos=-pos5,color=(0,0,1))



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

curva=curve(color=part5.color)
curva1=curve(color=part1.color)
curva2=curve(color=part2.color)
curva6=curve(color=part6.color)

verdade = True

while verdade:
	
	rate(1000)
	
	#-----------------
	t=t+dt
	
	o=o+do
	
	x=sin(o)+part1.x
	z=cos(o)+part1.z
	
	X=sin(o)+part1.x
	Y=cos(o)+part1.z
	
	part5.pos = vector(x,0,z)
	part6.pos = vector(X,Y,0)
	#-----------------
	
	
	
	t=t+dt
	
	#os eletrons nao sofreram essas forcas--------
	r12=part1.pos-part2.pos
	
	r15=part1.pos-part5.pos
	r25=part2.pos-part5.pos
	
	r16=part1.pos-part6.pos
	r26=part2.pos-part6.pos
	
	
	
	
	F15 = ((k*q1*q5)/mag(r15)**2)*norm(r15)
	F25 = ((k*q2*q5)/mag(r25)**2)*norm(r25)
	
	
	
	F16 = ((k*q1*q6)/mag(r16)**2)*norm(r16)
	F26 = ((k*q2*q6)/mag(r26)**2)*norm(r26)
	#repulsao dos protons
	F12 = ((k*q1*q2)/mag(r12)**2)*norm(r12)
	
	#-----------------------------------------------
	
	V = V - (+ (F15*t) + (F25*t))
	
	
	
	#part1.pos= part1.pos + (F15*t) + (F25*t)
	#part2.pos= part2.pos + (F25*t) + (F15*t)
	part1.pos= part1.pos + (F12*t) #---> tirando este ele fica fixo
	part2.pos= part2.pos + (F25*t) + (F26*t) - (F12*t) 
	
	curva.append(part5.pos)
	curva1.append(part1.pos)
	curva2.append(part2.pos)
	curva6.append(part6.pos)
	
	