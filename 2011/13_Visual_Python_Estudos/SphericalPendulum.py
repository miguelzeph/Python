#=============================================================
# This program visualizes the orbit of a spherical pendulum.
# The program uses a very rudimentary midpoint solver for the
# equations of motion, but good enough for this demo.
# Change the initial conditions to get different orbits.
# To clear the orbit click the mouse.
# To exit the program press ESC
#
# by E. Velasco. September 2009
#=============================================================
from visual import *

# Constants and initial conditions
g = 9.805           # in m/s^2
L = 1.0             # in m

theta = 120.0*pi/180.0
phi = 0.0
thetaDot = 0.0
phiDot = 4.2 # sqrt(g/(L*cos(theta))) and thetaDot=0 for circular pendulum

# Time variable and increments
t=0
dt = 0.01*sqrt(L/g)     #Full time step
dt2 = dt/2.0
TimeRate = 0.6/dt 

# Color definitions
Cbob  = color.yellow
Corbit = color.cyan
Cplumb = color.red

# First define the properties of the display window 
window = display(title="Spherical Pendulum", width=800, height=600)
window.fullscreen = 1          # Change to 0 to get a floating window
window.center=(0,0,0.3)
window.range = (2.5*L,2.5*L,2.5*L)
window.forward = (0,-1,0.2)
window.up = (0,0,-1)           # psoitive z axis vertically down!
window.lights = [0.5*norm(vector(1,0,-1)),0.5*norm(vector(-1,0,-1))]
window.ambient=0.3
window.select()
try:
    window.material=None
except:
    pass

info = label(pos=(-1.5*L,0,-L))
info.text = "Click mouse to clear orbit.\nPress Esc to exit program."

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

# Draw horizontal plane z=0
span = 1.2*L
plane = curve( pos=[(-span,-span),(-span,span),(span,span),
              (span,-span),(-span,-span)], color=Cplumb)

# Create the plumbline pointing down
PlumbLine = cylinder(axis = (0,0,1.15*L), radius=0.01*L, color=Cplumb)
Plumb = cone(pos=(0,0,1.15*L), axis=(0,0,0.2*L), radius=0.03*L, color=Cplumb)

# define trigonometric variables to improve efficency
cos_t = cos(theta)
sin_t = sin(theta)
cos_p = cos(phi)
sin_p = sin(phi)

CQ = phiDot*sin_t*sin_t    # Ang mom_z Conserved quantity
E  = (phiDot*sin_t)**2 + thetaDot**2 -2*g/L*cos_t # Energy

if( abs(sin_t) < 1.0e-10 ): # modified sin(theta)
    sin_tmod = 1.0e-10
else:
    sin_tmod = sin_t

# The bob and string
bob = sphere(radius=0.075*L, color=Cbob)
bob.pos = vector(L*sin_t*cos_p, L*sin_t*sin_p, L*cos_t)
bob.orbit = SegmentedCurve(color=Corbit, radius=0)
bob.orbit.append(bob.pos)

string = cylinder(axis=bob.pos, radius=0.01*L)

# The main loop

while 1:
  rate(TimeRate)
  
  # mid point variables (we do not need phiM or phiDotM)
  thetaM = theta+thetaDot*dt2
  thetaDotM = thetaDot+(-g/L*sin_t+CQ**2*cos_t/sin_tmod**3)*dt2
  # full step varibles
  sin_tmod = sin(thetaM) 
  if( abs(sin_tmod) < 1.0e-10):
      sin_tmod = 1.0e-10
  theta = theta + thetaDotM*dt
  phi = phi + (CQ/sin_tmod**2)*dt
  thetaDot = thetaDot +(-g/L*sin(thetaM)+CQ**2*cos(thetaM)/sin_tmod**3)*dt

  cos_t = cos(theta)
  sin_t = sin(theta)
  cos_p = cos(phi)
  sin_p = sin(phi)

  if( abs(sin_t) < 1.0e-10 ):
      sin_tmod = 1.0e-10
  else:
      sin_tmod = sin_t

  # Get thetaDot from conservation of energy.
  # This step can be removed and the program will
  # also work fine. However, it may improve stability.
  radical = E + 2*g/L*cos_t - CQ**2/sin_tmod**2
  if( radical < 0 ):
     thetaDot = 0
  elif( thetaDot >= 0 ):
      thetaDot = sqrt( radical )
  else:
      thetaDot = -sqrt( radical ) 

  # Update position of pendulum 
  bob.pos = vector(L*sin_t*cos_p, L*sin_t*sin_p, L*cos_t)
  string.axis=bob.pos
  bob.orbit.append(bob.pos)

  # Clear the orbit on mouse click
  if window.mouse.clicked:
      window.mouse.getclick()  # Empty the mouse queue
      bob.orbit.clear()
      bob.orbit.append(bob.pos)
      


