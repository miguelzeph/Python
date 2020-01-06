from __future__ import division
from visual import *
from visual.graph import *


scene.x=500
scene.y=190

scene.width=500#largura
scene.height=500#altura

#scene.autoscale=0
#scene.range=(100,1000,1000)
#scene.center=(50,60,0)

# principal ------------------------------------------
def main():
	#Grafico-------------------
	graph1 = gdisplay(x=0, y=0, width=800,height=800, 
			  title='Aceleracao do Satelite e Variacao do Raio', xtitle='t(s)', ytitle='a(m/s^2) e Raio resultante(m)10^6', 
			  xmax=6e6, xmin=0, ymax=5500, ymin=0, 
			  foreground=color.white, background=color.black)
			  
	funcao1 = gcurve(color=color.blue)		  
	funcao2 = gcurve(color=color.red)
	#--------------------------

	
	massOfEarth = 5.98e24   # kg
	massOfSatellite = 7.36e22    # kg
	radiusOfEarth = 6.38e6  # m
	radiusOfSatellite = 1.74e6   # m
	distanceEarthToSatellite = 3.84e8  # m - the moon

	dt = 100
	totalseconds = 0 

	G = 6.67e-11

	#earth = sphere(pos=(0,0,0),radius=radiusOfEarth,material=materials.earth)
	earth = sphere(pos=(0,0,0),radius=radiusOfEarth,color=(0,0,1))
	earth.mass = massOfEarth

	satellite = sphere(pos=(0,distanceEarthToSatellite,0),radius=radiusOfSatellite,color=color.white)
	satellite.mass = massOfSatellite

	trajetoria=curve(color=(1,0,0))


	speedOfSatellite = int(raw_input("Velocidade Inicial "))

	satellite.velocity = speedOfSatellite * vector(1,0,0)
	finished = False 
	while not finished:
		
		
		totalseconds += dt
		rate(100000)
		
		
		
		#pitagoras... acha o modulo do vetor
		distEarthToSatellite = mag(earth.pos - satellite.pos)
		
		#direcao do vetor normal , ou seja base canonica....modulo dele e 1... n=v/|v|
		ForceGravityOnTheSatelliteDir = norm(earth.pos - satellite.pos)    
		
		#modulo da forca entre as duas massas
		ForceGravityOnTheSatelliteMag = G * (earth.mass * satellite.mass) / distEarthToSatellite**2

		#vetor direcaoda forca
		ForceGravityOnTheSatellite = ForceGravityOnTheSatelliteMag * ForceGravityOnTheSatelliteDir

		satellite.acceleration = ForceGravityOnTheSatellite / satellite.mass
		satellite.velocity += satellite.acceleration*dt
		satellite.pos += satellite.velocity * dt + .5 * satellite.acceleration * dt**2
		trajetoria.append(pos=satellite.pos)
		
		
		funcao1.plot(pos=(totalseconds/1,abs(satellite.velocity)/1))
		funcao2.plot(pos=(totalseconds/1,distEarthToSatellite/1e6))
		
		if distEarthToSatellite <= radiusOfEarth:
			
			print "QUEDA DO SATELITE !!!!" 
			
			finished = True
			
#------------------------------------


main()