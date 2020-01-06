#from visual import *
import visual as vs

vs.scene.range = (15,2,2)

r=vs.vector(0,0,0)


bola=vs.sphere(pos=r,radius=1,color=vs.color.blue)
vetor=vs.arrow(pos=r,axis=(2,0,0),color=vs.color.red)
parede_A=vs.box(pos=(-11,0,0),size=(0.5,5,5))
parede_B=vs.box(pos=(11,0,0),size=(0.5,5,5))

dt=0.1



while True:
	
	vs.rate(50)
	
	#abs = modulo
	if abs(r.x) >=10:#fr.x = somente eixo x...escolhi 2 pois e metade de 4...
		dt = -dt
		vetor.axis=-vetor.axis
	r.x=r.x+dt	
	vetor.pos=r
	bola.pos=r