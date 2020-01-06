#from visual import *
import visual as vs

vs.scene.range = (10,2,2)

r=vs.vector(0,0,0)

bola=vs.sphere(pos=r,radius=0.5,color=vs.color.blue)
vetor=vs.arrow(pos=r,axis=(1,0,0),color=vs.color.red)

dt=0.1

#Enquanto for verdade,realize a tarefa.
while r.x < 10:
	#velocidade dos quadros
	vs.rate(30)
	#Somente o valor de x do vetor r ira variar...
	r.x=r.x+dt	
	#Posic da bola/vetor sera variada somente em x
	bola.pos=r
	vetor.pos=r