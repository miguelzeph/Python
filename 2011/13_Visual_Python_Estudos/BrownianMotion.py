#=======================================================
# Simple demo to illustrate the motion of a Big brownian
# particle in a swarm of small particles in 2D motion.
# The spheres collide elastically with themselves and
# with the walls of the box. The masses of the spheres
# are proportional to their radius**3 (as in 3D).
#
# Clicking the left mouse button toggles the display of the
# orbit of the Big brownian sphere. Numerical arrays are
# used to improve the efficiency of the program.
#
# This version uses a multisegmented orbit to improve the
# display of the curve in VPython > 2.4. For proper display
# it needs a modern graphics cards (it may not work well
# with ancient display cards).
# 
#
# ** To exit the program press ESC **
#
# by E. Velasco. September 2009 version
#=======================================================
from visual import *
from random import *

FullScreen = True

if FullScreen: # Get the size of the window
    import Tkinter as Tk
    WinRoot = Tk.Tk()
    screen_w,screen_h = WinRoot.maxsize()
    WinRoot.destroy()
else:
    screen_w = 800
    screen_h = 574   # Almost 600 but not quite (to allow for window frame)

# Constants and time step
Nsp = 71                # Number of small spheres
Rb = screen_w/32.0      # Radius of the big sphere
Rs = Rb*0.43            # Radius of small spheres
Ms=(Rs/Rb)**3           # Mass of the small spheres (Mbig=1)

ShowOrbit = 0           # 0 = Do not show the big sphere trajectory
LBox=(screen_w/2,screen_h/2) # Size of the box = 2LBox[0].2LBox[1]

Dt = 0.020              # Time step
PSteps = 10             # Plot orbit every PSteps
Nt = 1                  # Number of steps counter

Lb0 = LBox[0]-Rb
Lb1 = LBox[1]-Rb
Ls0 = LBox[0]-Rs
Ls1 = LBox[1]-Rs

# Color definitions
CSpheres  = (0,0.5,0.9)      # Color of small spheres
CBigSphere  =  (0.9,0.2,0.1) # Color of big sphere
COrbit = color.yellow        # Color of orbit

# Properties of the display window 
window = display(title="Brownian Motion", width=800, height=600)
if FullScreen:
    window.fullscreen = 1      # Change to 0 to get a floating window
    window.cursor.visible = 0  # 0=Hide the mouse, 1=show
else:
    window.fullscreen = 0      # Change to 0 to get a floating window
    window.cursor.visible = 1  # 0=Hide the mouse, 1=show
window.range = LBox[0]     # = (LBox[0],LBox[0],LBox[0])
window.userspin = 0        # No rotation with mouse
window.userzoom = 0        # No zoom with mouse
window.forward = (0,0,1)       
window.lights = [] #[vector(0,0,-1)]
window.ambient = 1 #0
try:
    window.material=None
except:
    pass


class SegmentedCurve(object):

    def __init__(self, color=color.white, radius=0):
        self.color = color
        self.radius = radius   
        self.orbit = [curve(pos=[], color=self.color, radius=self.radius)]
        
    def append(self, vector):
        if len(self.orbit[-1].pos)>=1000: # Hardwired in VPython
            pt = self.orbit[-1].pos[-1]   # Last point of last segment
            self.orbit.append(curve(pos=[pt],color=self.color, radius=self.radius))
        self.orbit[-1].append(pos=vector)
    
    def clear(self):
        for n in xrange(len(self.orbit)-1,0,-1):
            self.orbit[n].pos=[]
            self.orbit[n].visible = False
            del self.orbit[n]
        self.orbit[0].pos=[]

seed()      # Randomize the random number generator

# Create the arrays with the initial positions of the spheres.
# Start with the big sphere at the center, then put the small
# spheres at random selected from a grid of possible positions.
ListPos=[(0,0)]

PossiblePos=[(x,y) for x in arange(-LBox[0]+2*Rs,LBox[0]-2*Rs,2.2*Rs)
             for y in arange(-LBox[1]+2*Rs,LBox[1]-2*Rs,2.2*Rs)
             if x*x+y*y > Rb+Rs]
             
if Nsp > len(PossiblePos)+1: Nsp = len(PossiblePos)+1

for s in xrange(Nsp-1):
    n = randint(0,len(PossiblePos)-1)
    ListPos.append(PossiblePos[n])
    del PossiblePos[n] 
del PossiblePos
             
Pos = array(ListPos)
del ListPos

# Create the confining box
#curve( pos=[(-LBox[0],LBox[1],0),(LBox[0],LBox[1],0),
#            (LBox[0],-LBox[1],0),(-LBox[0],-LBox[1],0),(-LBox[0],LBox[1],0)],
#       color=color.orange, radius=Rs*0.15 )

# Create an array with all the radius and a list with all the masses
Radius = concatenate( (array([Rb]),array([Rs]*(Nsp-1))) )
Mass=[1.0]+[Ms]*(Nsp-1)

# Create the initial array of velocities at random with big sphere at rest
ListVel=[(0.,0.)]
for s in xrange(1,Nsp):
    ListVel.append( (Rb*uniform(-1,1),Rb*uniform(-1,1)) )
Vel = array(ListVel)
del ListVel

# Create the spheres (really cylinders in 2D)
Spheres = [cylinder(pos=Pos[0], radius=Radius[0], axis=(0,0,Rs*0.2), 
                    color=CBigSphere)]

for s in xrange(1,Nsp):
    Spheres.append( cylinder(pos=Pos[s],axis=(0,0,Rs*0.2),
                             radius=Radius[s], color=CSpheres) )


# Create the segmented curve = orbit and put initial point with some z-value
orbit = SegmentedCurve(color=COrbit)
if ShowOrbit:
    orbit.append(vector(Pos[0])+vector(0,0,-0.1))

# Auxiliary variables
Id = identity(Nsp)
try:     # Old numeric (Old VPython, version <5)
    Dij =  (Radius+Radius[:,NewAxis])**2 # Matrix Dij=(Ri+Rj)**2
except:  # numpy (New VPython, version 5 and up)
    Dij =  (Radius+Radius[:,newaxis])**2 # Matrix Dij=(Ri+Rj)**2

# The main loop
while True :
    rate(600)   # Slow things down in fast computers        

    # Update all positions
    add(Pos,Vel*Dt,Pos)      # Fast version of Pos = Pos + Vel*Dt
    
    # Impose the bouncing at the walls
##    for s in xrange(Nsp):
##        for n in xrange(2):
##            if Pos[s,n] <= -LBox[n]+Radius[s]:
##                Pos[s,n] = -LBox[n]+Radius[s]
##                Vel[s,n] = -Vel[s,n]
##            if Pos[s,n] >= LBox[n]-Radius[s]:
##                Pos[s,n] = LBox[n]-Radius[s]
##                Vel[s,n] = -Vel[s,n]

    if Pos[0,0] <=  -Lb0:
        Pos[0,0] = -Lb0
        Vel[0,0] = -Vel[0,0]
    if Pos[0,0] >= Lb0:
        Pos[0,0] = Lb0
        Vel[0,0] = -Vel[0,0]
    if Pos[0,1] <=  -Lb1:
        Pos[0,1] = -Lb1
        Vel[0,1] = -Vel[0,1]
    if Pos[0,1] >= Lb1:
        Pos[0,1] = Lb1
        Vel[0,1] = -Vel[0,1]
    for s in xrange(1,Nsp):
        if Pos[s,0] <=  -Ls0:
            Pos[s,0] = -Ls0
            Vel[s,0] = -Vel[s,0]
        if Pos[s,0] >= Ls0:
            Pos[s,0] = Ls0
            Vel[s,0] = -Vel[s,0]
        if Pos[s,1] <=  -Ls1:
            Pos[s,1] = -Ls1
            Vel[s,1] = -Vel[s,1]
        if Pos[s,1] >= Ls1:
            Pos[s,1] = Ls1
            Vel[s,1] = -Vel[s,1]
        
    # Create the set of all pairs and the list the colliding spheres
    try:     # Old numeric (Old VPython, versions < 5)
        Rij = Pos - Pos[:,NewAxis]
        Mag2ij = add.reduce(Rij*Rij,-1) # sphere-to-sphere distances**2
        colliding = less_equal(Mag2ij,Dij)-Id  
        hitlist =sort(nonzero(colliding.flat)).tolist()
    except:  # numpy (New VPython, versions >= 5)
        Rij = Pos - Pos[:,newaxis]
        Mag2ij = add.reduce(Rij*Rij,-1) # sphere-to-sphere distances**2
        colliding = less_equal(Mag2ij,Dij)-Id  
        hitlist =sort(nonzero(colliding.flat)[0]).tolist()

    # Check to see if the spheres are colliding
    for ij in hitlist:
        s1,s2 = divmod(ij,Nsp)    # decode the spheres pair (s1,s2) colliding
        hitlist.remove(s2*Nsp+s1) # remove symmetric (s2,s1) pair from list
        R12 = Pos[s2]-Pos[s1]
        d12 = Radius[s1]+Radius[s2] - mag(R12)
        tau = norm(R12)
        DR0 = d12*tau
        x1 = Mass[s1]/(Mass[s1]+Mass[s2])
        x2 = 1-x1                 # x2 = Mass[s2]/(Mass[s1]+Mass[s2])
        DR = array(DR0)[:-1]      # 2D vector DR
        Pos[s1] -= x2*DR
        Pos[s2] += x1*DR
        DV0 = 2*dot(vector(Vel[s2]-Vel[s1]),tau)*tau
        DV =array(DV0)[:-1]       # 2D vector DV0
        Vel[s1] +=  x2*DV
        Vel[s2] -=  x1*DV

    # Toggle the orbit
    if window.mouse.clicked:
        window.mouse.getclick()   # Empty the mouse queue
        ShowOrbit = 1 - ShowOrbit
        Nt = 0
        if ShowOrbit == 0: orbit.clear()
         
    # Update the location of the spheres
    for s in xrange(Nsp):
        Spheres[s].pos = Pos[s]
    if ShowOrbit == 1:
        if Nt%PSteps == 0:
           orbit.append(vector(Pos[0])+vector(0,0,-0.1))
        Nt = Nt+1
