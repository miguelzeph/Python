#=====================================================
# This program simulates a classical Tonk's gas,
# a gas of hard spheres of equal mass in a cubical box.
# The spheres collide elastically with themselves and
# with the walls of the box. Clicking the left mouse
# toggles a marker color in one of the spheres, to allow
# following that sphere with ease.
# This program uses numerical arrays to increase the
# spped of the computations.
#
# ** Right and mid click the mouse to rotate and zoom **
# ** Left click to toggle a marker in one sphere **
# ** To exit the program press ESC **
#
# by E. Velasco. September 2009 version
#=====================================================
from visual import *
from random import *
seed()      # Randomize the random number generator

# Constants and initial conditions
Nsp=55          # Number of spheres
R = 0.09        # Radiuss of spheres (box size = 2)

Dt = 0.005      # Time step

# Color definitions
CSpheres  = (0,0.6,1)     # Color of all spheres
CMarker   = color.yellow  # Color of marker for sphere0
CBox      = color.red     # Color of box
ShowMarker = 0            # Do not show the marker color

# Properties of the display window 
window = display(title="Tonk's gas", width=800, height=600)
window.fullscreen = 1      # Change to 0 to get a floating window
window.range = (2.9,2.9,2.9)
window.forward = (-0.7,1,-0.5)  
window.up = (0,0,1)        # psoitive z axis vertically up!    
window.lights = [vector(0,0,0.5)]
window.ambient=0.6
window.select()
try:
    window.material=None
except:
    pass

# Create the confining box
def side(P1,P2):
    V1 = vector(P1)
    V2 = vector(P2)
    return cylinder(pos=V1, axis=V2-V1, radius=0.012, color=CBox)

side((-1,-1,-1),(1,-1,-1))
side((1,-1,-1),(1,1,-1))
side((1,1,-1),(-1,1,-1))
side((-1,1,-1),(-1,-1,-1))

side((-1,-1,1),(1,-1,1))
side((1,-1,1),(1,1,1))
side((1,1,1),(-1,1,1))
side((-1,1,1),(-1,-1,1))

side((-1,-1,-1),(-1,-1,1))
side((1,-1,-1),(1,-1,1))
side((1,1,-1),(1,1,1))
side((-1,1,-1),(-1,1,1))

# An alternative way of doing it, although it looks better with cylinders.
##curve( pos=[(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,-1),
##            (-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1),(-1,-1,1),
##            (1,-1,1),(1,-1,-1),(1,1,-1),(1,1,1),(-1,1,1),(-1,1,-1)],
##       color=CBox, radius=0.012 )

# Create the initial position and radius of the spheres
InitPos=[]

x = -1+2*R
y = -1+2*R
z = -1+2*R
for s  in range(Nsp):
    InitPos.append(vector(x,y,z))
    x = x+3*R
    if x >= 1-2*R:
        x = -1+2*R
        y = y+3*R
    if y >= 1-2*R:
        y = -1+2*R
        z = z+3*R
    if z >= 1-2*R:
        if s != Nsp-1:
           Nsp = s+1
           print "Could not create all the spheres. Gas is too dense."
           if Nsp == 1: print "Instead, creating only one sphere."
           else: print "Instead, creating only",Nsp,"spheres."
           break
Pos = array(InitPos)
Radius = array([R]*Nsp)

# Create the initial velocities at random
InitVel=[]
for s in range(Nsp):
    vx = uniform(-1,1)
    vy = uniform(-1,1)
    vz = uniform(-1,1)
    InitVel.append(vector(vx,vy,vz))
Vel = array(InitVel)
 
# Create the spheres
Spheres = []
for s in range(Nsp):
    Spheres.append(sphere(pos=Pos[s], radius=R, color=CSpheres))

# Some auxiliary stuff
Id  =  identity(Nsp)
try:     # Old numeric (Old VPython)
    Dij =  (Radius+Radius[:,NewAxis])**2 # Matrix Dij=(Ri+Rj)**2
except:  # numpy (New VPython)
    Dij =  (Radius+Radius[:,None])**2 # Matrix Dij=(Ri+Rj)**2
    

# The main loop
while True :
    rate(250)     # Slow down the loop

    # Update all positions
    Pos = Pos + Vel*Dt

    # Check to see if the spheres are touching the walls
    for s in range(Nsp):
        for n in range(3):
            if Pos[s,n] <= -1+R:
                Pos[s,n] = -1+R
                Vel[s,n] = -Vel[s,n]
            if Pos[s,n] >= 1-R:
                Pos[s,n] = 1-R
                Vel[s,n] = -Vel[s,n]

    # Get the list the colliding spheres i,j encoded as i*Nsp+j
    try:     # Old numeric (Old VPython)
        Rij = Pos - Pos[:,NewAxis]
        Mag2ij = add.reduce(Rij*Rij,-1) # sphere-to-sphere distances**2
        colliding = less_equal(Mag2ij,Dij)-Id  
        hitlist =sort(nonzero(colliding.flat)).tolist()
    except:  # numpy (New VPython)
        Rij = Pos - Pos[:,newaxis]
        Mag2ij = add.reduce(Rij*Rij,-1) # sphere-to-sphere distances**2
        colliding = less_equal(Mag2ij,Dij)-Id  
        hitlist =sort(nonzero(colliding.flat)[0]).tolist()
    
    # Take care of the colliding spheres
    for ij in hitlist:
        s1,s2 = divmod(ij,Nsp)    # decode the colliding spheres pair (s1,s2) 
        hitlist.remove(s2*Nsp+s1) # remove symmetric (s2,s1) pair
        R12 = Pos[s2]-Pos[s1]
        d12 = mag(R12)-2*R
        tau = norm(R12)
        DR = d12/2*tau
        Pos[s1] += DR
        Pos[s2] -= DR
        DV = dot(Vel[s2]-Vel[s1],tau)*tau
        Vel[s1] +=  DV
        Vel[s2] -=  DV
        
    # Toggle color of Sphere 0 to a marker color
    if window.mouse.clicked:
        window.mouse.getclick()   # Empty the mouse queue
        ShowMarker = 1-ShowMarker # Toggle ShowMarker
        if ShowMarker == 1: Spheres[0].color = CMarker
        else :              Spheres[0].color = CSpheres
                      
    # Update the location of the spheres
    for s in range(Nsp):
        Spheres[s].pos = Pos[s]
