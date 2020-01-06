from visual import *




scene.background = (1,1,1)

V = arange(-5, 10, 5)
K=15.

q = sphere(pos=(0,0,0), color=color.red, radius=0.4, charge=1.0)

curv = curve(color=(1,0,0))

quadro = frame(pos=q.pos)


for x in V:
    for y in V:
        for z in V:
           
            a=arrow(frame = quadro,pos=(x,y,z), axis=(0, 0.1, 0), color=(1.0, .5, 0),shaftwidth= 0.5)
            r = a.pos-q.pos
            if mag(r) == 0:
                a.axis=vector(0,0,0)
            else:
                E = K*q.charge*r/(mag(r)**3)
                a.axis=E

				
t = 0
dt = 0.1
while True:
	
	rate(20)
	
	quadro.pos = q.pos
	
	quadro.rotate(axis = (1,0,0), angle= 0.1)
	
	t = t + dt
	
	x = 3*sin(t)
	y = 3*cos(t)
	z = t
	
	q.pos = (x,y,z)
	
	curv.append(pos=q.pos)
	
	#quadro.rotate(axis = (1,0,0), angle= 0.1)
	