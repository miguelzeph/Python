from visual import *

scene.background =  (1,1,1)

#cargas positivas
part1=sphere(pos=(2,-2,0),color=(1,0,0))
part2=sphere(pos=(2,2,0),color=(1,0,0))
part3=sphere(pos=(-2,2,0),color=(1,0,0))
part4=sphere(pos=(-2,-2,0),color=(1,0,0))

#s=(+1,+1,+1,+1)

q1=1e-1
part1.radius=(q1**2)**(1.0/2.0) # (q1**2)(1.0/2.0) somente para deixar positivo = raiz(a**2) = modulo
q2=1e-1
part2.radius=(q2**2)**(1.0/2.0)
q3=1e-1
part3.radius=(q3**2)**(1.0/2.0)
q4=1e-1
part4.radius=(q4**2)**(1.0/2.0)



#carga de prova
part5=sphere(pos=(0,0,0),color=(0,0,1))

q5=1e-1
part5.radius=(q5**2)**(1.0/2.0)


#vetor
v1=arrow(pos=part5.pos,axis=(0,0,0),color=(0,1,0))
v2=arrow(pos=part5.pos,axis=(0,0,0),color=(0,1,0))
v3=arrow(pos=part5.pos,axis=(0,0,0),color=(0,1,0))
v4=arrow(pos=part5.pos,axis=(0,0,0),color=(0,1,0))





k=1
t=0
dt=0.01

curva=curve(color=part5.color)

verdade = True

while verdade:
	
	rate(50)
	
	t=t+dt
	
	r15=part1.pos-part5.pos
	r25=part2.pos-part5.pos
	r35=part3.pos-part5.pos
	r45=part4.pos-part5.pos
	
	
	F15 = ((k*q1*q5)/mag(r15)**2)*norm(r15)
	F25 = ((k*q2*q5)/mag(r25)**2)*norm(r25)
	F35 = ((k*q3*q5)/mag(r35)**2)*norm(r35)
	F45 = ((k*q4*q5)/mag(r45)**2)*norm(r45)
	
	
	
	part5.pos= part5.pos - (F15*t) - (F25*t) - (F35*t) - (F45*t)
	
	curva.append(part5.pos)
	
	v1.pos=part5.pos
	v2.pos=part5.pos
	v3.pos=part5.pos
	v4.pos=part5.pos
	
	
	v1.axis=-F15*2e2
	v2.axis=-F25*2e2
	v3.axis=-F35*2e2
	v4.axis=-F45*2e2
	
	#se for maior que um raio de 2.5 ...
	if mag(part5.pos) >= 2.5:
		verdade = False
		print "Fim"