from visual import *
#proton
p1 = sphere(pos=(0,0,0), radius=0.6 , color = color.red)
#nucleo
n1 = sphere(pos=(0,0,0), radius = 1 , color = color.white , opacity=0.3 )
#eletron
e1 = sphere(pos=(0,0,0), radius=0.3, color = color.blue,opacity = 0.5)
#campo
#c1 = sphere(pos=(0,0,0), radius = 7 , color = color.blue , opacity=0.2 )

#trajetoria
curva1= curve(color =(1,1,1))#RGB

#Dependencia... perceba que x e z serao um circulo e y sera a oscilacao (amplitude)
raio=7

t=0
dt=0.1

p=0
dp=0.4

while True:
	
	rate(20)
	
	p = p+dp
	t = t+dt
    
	x=sin(t)*raio
	z=cos(t)*raio
	y=sin(p)
    
	e1.pos=(x,y,z)

	curva1.append(pos=e1.pos)