from __future__ import division
from visual import *


massOfEarth = 5.98e24   # kg
massOfSatellite = 7.36e22    # kg
radiusOfEarth = 6.38e6  # m
radiusOfSatellite = 1.74e6   # m
distanceEarthToSatellite = 3.84e8  # m - the moon

dt = 100
totalseconds = 0 

G = 6.67e-11

earth = sphere(pos=(0,0,0),radius=radiusOfEarth,color=color.blue)
earth.mass = massOfEarth

satellite = sphere(pos=(0,distanceEarthToSatellite,0),radius=radiusOfSatellite,color=color.white)
satellite.mass = massOfSatellite



speedOfSatellite = 800

satellite.velocity = speedOfSatellite * vector(1,0,0)

finished = False 
while not finished:
    totalseconds += dt
    rate(1000)
    
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




