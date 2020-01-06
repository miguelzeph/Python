#from visual import *
import visual as vs

mig=vs.sphere(pos=vs.vector(-5,0,0),radius=0.5,color=vs.color.cyan)
gui=vs.sphere(pos=vs.vector(-5,10,0),radius=0.5,color=vs.color.cyan)

arrow=vs.arrow(pos=mig.pos,axis=gui.pos-mig.pos,color=vs.color.red)

r=vs.vector(-5,10,0)
#dcas , faca um print em :
print r.x#retorna valor de x
print r.y
print r.z

b=0

while r.x < 10:
	vs.sphere(pos=r,radius=b,color=vs.color.cyan)
	r.x=r.x+1
	b=b+0.1#fazer bola crescer...