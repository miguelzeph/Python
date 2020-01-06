from visual import *

#---------TELA-------------

scene.center = (0,0,0)
scene.width = 800
scene.height = 600
scene.range = (1.0e9,1.0e9,1.0e9)

#------------Terra
terra=sphere(pos=vector(0,0,0),radius=6.38e6)
massa_terra=5.98e24
#-------------Satelite
sat=sphere(pos=vector(0,3.84e8,0),radius=1.74e6)
massa_sat=7.36e22

rapidez_sat=500
velocidade_sat= rapidez_sat*vector(1,0,0)
#---------------dados
tempo=0
dt=100

#mylabel = label(pos=(0,3.84e8+ 100000000,0))

G = 6.67e-11

finished = False

while not finished:
	
	tempo=tempo+dt
	rate(10000)
	
	r=mag(terra.pos-sat.pos)
	
	vetor_gravitacional=norm(terra.pos-sat.pos)
	
	forc_gravitacional=G*(massa_sat*massa_terra)/r**2
	
	FORC=forc_gravitacional*vetor_gravitacional
	
	#F=m.a --> a=F/m 
	
	acel_sat=FORC/massa_sat
	
	velocidade_sat=velocidade_sat+acel_sat*dt
	sat.pos = sat.pos+velocidade_sat*dt+0.5*acel_sat*dt**2