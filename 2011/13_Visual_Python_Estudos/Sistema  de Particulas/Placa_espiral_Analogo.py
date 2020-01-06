from visual import *

scene.background =  (1,1,1)


def placa(n):
	
	k=[]
	for i in range(0,n):
		
		particula=sphere(pos=(i,0,0),radius = 0.5,color=(1,0,0))
		
		k.append(particula)
	return k
		

k = placa(10)		
	
p = sphere(pos=(-10,-10,0),radius = 0.5,color=(0,0,1))
#eletron
q=-1
#proton (cargas da placa)
Q=1
vel = vector(-0.1,0,0)

curva = curve(color=p.color)

v = arrow(pos=p.pos , axis = vel,color=(0,0,0))

while True:
	#rate(10)
	
	
	
	r = []
	for particula in k:
		
		r12=particula.pos-p.pos
		
		r.append(r12)
	
	F=[]
	for raio in r:
	
		f = (q*Q/mag(raio)**2)*norm(raio)
		
		F.append(f)
	
	
	for velocidade in range(0,len(F)):
		vel = vel + F[velocidade]
		p.pos = p.pos - vel
		curva.append(p.pos)
		
		v.pos = p.pos
		v.axis =-vel*1e1
		
		
	