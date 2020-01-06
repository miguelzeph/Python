from visual import *
#=============================================================
# This program visualizes the orbit of a particle of mass m in
# an atractive central force field = -alpha/r. The initial conditions
# are given by r=r0, r_dot=0 (i.e r0 is a turning point in r) and
# phi=0 phi_dot=k/r0*sqrt(alpha/m). The dimensionless parameter k
# adjusts the value of the angular momentum (k=1 corresponds to a
# circular orbit). We now rescale variables to a new r =r/r0 (so the
# starting point is now r=1) and rescale the time to a new time
# t=t*r0*sqrt(m/alpha), so phi_dot = k.
#
# The equations of motion in these new variables are:
# 
#  r_dot_dot = -1/r+k^2/r^3  and phi_dot = k/r^2
#
# with initial conditions: r=1, r_dot=0, phi_dot=0.  
# The program uses a very rudimentary midpoint solver for the
# equations of motion, but good enough for this demo.
# Change the value of k to get different orbits (k=1-> circle).
#
# ** To clear the orbit left-click the mouse **
# ** Right and mid click the mouse to rotate and zoom **
# ** To exit the program press ESC **
#
# by E. Velasco. October 2004
#=============================================================

# Constants and initial data
k = 0.475  # 1.0 for circular orbit
r = 1.0
r_dot = 0.0
phi = 0


# Time variable and increments
t=0
dt = 0.0075     #Full time step
dt2 = dt/2.0            

# Color definitions
Cobject  = color.yellow
Corbit = color.cyan
CL = color.red
CSun = color.green

# First define the properties of the display window 
window = display(title="1/r atractive force", width=800, height=600)
window.fullscreen = 1          # Change to 0 to get a floating window
window.range = (2,2,2)
#window.forward = (0,3,-1)
#window.up = (0,0,1)            # psoitive z axis vertically up!
window.lights = [vector(0,0,0.5)]
window.ambient=0.6
window.select()
try:
    window.material=None
except:
    pass

# Draw horizontal plane z=0 
span = 1.2
plane = curve( pos=[(-span,-span),(-span,span),(span,span),
              (span,-span),(-span,-span)], color=CL)

### Create the Angular Momentum (L) vector (along z axis)
### *** There are problems in some computers rendering arrows ***
#arrow(pos=(0,0,0), axis=(0,0,0.7), shaftwidth=0.03, color=CL )
sphere(pos=(0,0,0), radius=0.05, color=CSun)

# The object and its orbit
Object = sphere(pos=(1,0,0), radius=0.03, color=Cobject)
Object.orbit = curve(color=Corbit, radius=0)
Object.orbit.append(pos=Object.pos)

# The main loop

while 1:
  rate(100)
  
  # mid point variables
  r_mid = r+ r_dot*dt2
  r_dot_mid = r_dot+(-1/r+k**2/r**3)*dt2
  
  # full step varibles
  r = r + r_dot_mid*dt
  r_dot = r_dot+(-1/r_mid+k**2/r_mid**3)*dt
  phi = phi + (k/r_mid**2)*dt 
  
  # Update position of object
  Object.pos = vector(r*cos(phi), r*sin(phi), 0)
  Object.orbit.append(pos=Object.pos)

  # Clear the orbit on mouse click
  if window.mouse.clicked: 
      Object.orbit.pos=[Object.pos]
      window.mouse.getclick()  # Empty the mouse queue


