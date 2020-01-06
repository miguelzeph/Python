#from visual import *
import visual as vs

mig=vs.sphere(pos=vs.vector(-5,0,0),radius=0.5,color=vs.color.cyan)
gui=vs.sphere(pos=vs.vector(-5,10,0),radius=0.5,color=vs.color.cyan)

arrow=vs.arrow(pos=mig.pos,axis=gui.pos-mig.pos,color=vs.color.red)

r=vs.vector(-5,10,0)


b=0

while r.x < 100:
	vs.rate(10)
	
	gui.pos=r#ou seja, posic de gui sera variada somente em x, pois o r.x esta crescendo 1 em 1
	r.x=r.x+1
	r.y=r.y+1
	