from visual import *




#velocidade de giro dos protons/neutrons
velocidade_ang=0.00
ang=0.01

#Posic de giro desordenado
a=0
da = 0.01
b=5
db = 0.001
c=0
dc = 0.3

#tamanho do nucleo
nucleo=2
nc=0.025

#variacao da opacidade
opaco=0.1
op=0.05


quadro = frame(pos=(0, 0, 0))

#proton
local_light(pos=(0,0,0),color=(1,1,1))

#p1 = sphere(frame=quadro,pos=(0.5,0.3,0), radius=0.8 , color = color.red,material = materials.emissive)
p1 = sphere(frame=quadro,pos=(0.5,0.3,0), radius=0.8 , color = color.red)
#p2 = sphere(frame=quadro,pos=(-0.5,-0.30,0), radius=0.8 , color = color.red,material = materials.emissive)
p2 = sphere(frame=quadro,pos=(-0.5,-0.30,0), radius=0.8 , color = color.red)
#nucleo

#n1 = sphere(pos=(0,0,0), radius = nucleo , color = color.white , opacity=opaco,material = materials.emissive)
n1 = sphere(pos=(0,0,0), radius = nucleo , color = color.white , opacity=opaco)
#neutron
neu1 = sphere(frame=quadro,pos=(0.30,-0.5,0), radius=0.8 , color = (0.1,0.1,0.1))
neu2 = sphere(frame=quadro,pos=(-0.30,0.5,0), radius=0.8 , color = (0.1,0.1,0.1))
#campo
#c1 = sphere(pos=(0,0,0), radius = 5 , color = color.blue , opacity=0.2 )
#eletron
#e1 = sphere(pos=(0,0,0), radius=0.4, color = color.blue,opacity = 0.5,material = materials.emissive)
#e2 = sphere(pos=(0,0,0), radius=0.4, color = color.blue,opacity = 0.5,material = materials.emissive)
e1 = sphere(pos=(0,0,0), radius=0.4, color = color.blue,opacity = 0.5)
e2 = sphere(pos=(0,0,0), radius=0.4, color = color.blue,opacity = 0.5)
#trajetoria
curva1= curve(color =(1,1,1))#RGB
curva2= curve(color =(1,1,1))
#vetor sentido de rotac
v1=arrow(pos=(0,0,0),axis=(1,0,0),color=(1,0,0))
v2=arrow(pos=(0,0,0),axis=(1,0,0),color=(1,0,0))
#vetor campo magnetico
b1=arrow(pos=(0,0,0),axis=(0,1,0),color=(0,1,0))
b2=arrow(pos=(0,0,0),axis=(0,-1,0),color=(0,1,0))


#Dependencia... perceba que x e z serao um circulo e y sera a oscilacao (amplitude)
raio=12

t=0
dt=0.1

p=0
dp=0.6
#dp=0.3 Orbita defasada em 180

while True:
	
	rate(20)
	
	p = p+dp
	t = t+dt
    
	
	x=sin(t)*raio
	z=cos(t)*raio
	y=sin(p)
	
	d=pi
	
	X=sin(t+d)*raio
	Z=cos(t+d)*raio
	
	
	e1.pos=(x,y,z)
	e2.pos=(X,y,Z)
	v1.pos=e1.pos
	v1.rotate(axis=(0, 1, 0), angle=30)
	v2.pos=e2.pos
	v2.rotate(axis=(0, 1, 0), angle=-30)
	b1.pos=e1.pos
	b2.pos=e2.pos
	
	
	a = a + da
	b = b + db
	c = c + dc
	
	if abs(a) > 5.0:
		da = -da
	if abs(b) > 10.0:
		db = -db
	
	if abs(c) > 15.0:
		dc = -dc
	
	
	
	nucleo += nc
	
	if nucleo > 2.0:
		nc = -nc
	if  nucleo < 1.6:
		nc = -nc
	
	n1.radius = nucleo
	
	
	
	opaco = opaco + op
	
	if abs(opaco) > 0.45:
		op = -op
	elif abs(opaco) < 0.15:
		op = -op
	
	n1.opacity=opaco
	
	
	
	
	velocidade_ang += ang
	#print velocidade_ang
	if abs(velocidade_ang) > 1.0:
		ang = -ang
	
	quadro.rotate(axis=(a,b,c), angle=velocidade_ang)
	
	#p1.rotate(pos=(1, 1, 1), angle=50)
	#v2.rotate(pos=(2,0,0),axis=(0, 10, 0), angle=50)
	#neu1.rotate(pos=(1, 1, 1), angle=50)
	#neu2.rotate(axis=(0, 1, 0), angle=0.7)
	#n1.rotate(pos=(0, 0, 1), angle=25)
	
	
	curva1.append(pos=e1.pos)
	curva2.append(pos=e2.pos)