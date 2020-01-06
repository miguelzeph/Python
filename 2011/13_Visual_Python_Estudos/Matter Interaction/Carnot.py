from visual import *
from visual.graph import *
from random import random

# A visualization of the Carnot cycle
# Bruce Sherwood, December 2001

# A rough approximation is made that the connecting rod exerts a force
# on the flywheel whose magnitude is the force of the gas on the piston.
# This assumes that the piston has negligible mass compared to the flywheel
# and it ignores geometrical issues associated with the rod being at an angle.

# Intermolecular collisions are ignored in this visualization.
# The molecular speeds are continually adjusted to match the macroscopic temperature.
# With a small number of molecules a full simulation would run erratically.

print """
Click to expose the inside of the Carnot engine.
Then click once for each expansion and compression in the first cycle.
  The visualization pauses to permit discussion.
  Note the PV diagram for the cycle.
After the first cycle the engine runs continuously, with the speed
  continually increasing.
The program stops when the angular step size becomes so large that
  the numerical integration becomes inaccurate.
"""

def showT():
    temp = T
    if T > TH: # small adjustments to eliminate e.g. '401 K' from displaying
        temp = TH
    elif T < TL:
        temp = TL
    thermometer.axis.y = temp*Tscale
    Tlabel.text = str(int(round(temp)))+' K'
    
def showomega():
    omegalabel.text = str(round(10.*L.z/Iwheel)/10.)+' rad/s'

maxcount = 10000  # if > 0, pause every maxcount time steps (50 is a good value)
# if maxcount very large, pause at end of each phase (isothermal or adiabatic)

winh=800
winw=800

scene = display(title="Carnot Cycle", width=winw, height=winh, x=0, y=0)
scene.range = 3
TH = 400.0
TL = 335.0
T = TH

thick = 0.1
wide = 1.
deep = wide
high = 2.
Lreservoir = 2.*deep
offsetReservoir = 1.4*Lreservoir
Tscale = (0.7*high)/T
gamma = 1.4 # monatomic gas
Rwheel = 0.8*wide
Iwheel = 10.
Rpin = 0.8*Rwheel
theta = -0.9*pi/2.
L = vector(0.,0.,0.)
dt = 0.01

cylcolor = (0.788,0.788,0.788)
pistoncolor = (1.000,0.704,0.000)
cyl = frame()
bottom = box(frame=cyl, pos=(0,-thick/2.,0),
             size=(wide,thick,deep), color=cylcolor)
left = box(frame=cyl, pos=(-wide/2.-thick/2.,high/2.,-thick/2.),
           size=(thick,high+2.*thick,deep+thick), color=cylcolor)
right = box(frame=cyl, pos=(wide/2.+thick/2.,high/2.,-thick/2.),
           size=(thick,high+2.*thick,deep+thick), color=cylcolor)
back = box(frame=cyl, pos=(0,high/2.,-deep/2.-thick/2.),
           size=(wide,high+2.*thick,thick), color=cylcolor)
front = box(frame=cyl, pos=(0,high/2.,deep/2.+thick/2.),
            size=(wide+2.*thick,high+2.*thick,thick), color=cylcolor)
lifter = frame(frame=cyl, pos=(0,0.2*high+thick/2.,0))
wheel = cylinder(frame=cyl, pos=(0,2.*high,-2.*thick), axis=(0,0,thick),
                 radius=Rwheel, color=cylcolor)
axle = cylinder(frame=cyl, pos=wheel.pos-vector(0,0,2.*thick), axis=(0,0,3.5*thick),
                radius=thick/2., color=color.red)
pin = cylinder(frame=cyl, pos=wheel.pos+Rpin*vector(cos(theta),sin(theta),0),
               axis=(0,0,3.*thick), radius=thick/2., color=color.red)
stripes = frame(pos=wheel.pos)
stripe1 = curve(frame=stripes, pos=[(-Rwheel,0,1.05*thick), (Rwheel,0,1.05*thick)], color=color.blue)
stripe2 = curve(frame=stripes, pos=[(0,-Rwheel,1.05*thick), (0,Rwheel,1.05*thick)], color=color.blue)
stripes.rotate(angle=theta, axis=(0,0,1))
piston = box(frame=lifter, pos=(0,0,0),
             size=(wide,thick,deep), color=pistoncolor)
pivot = cylinder(frame=lifter, pos=piston.pos+vector(0,thick/2.,-thick/2.),
                 axis=(0,0,thick), radius=thick/2., color=pistoncolor)
rod = cylinder(frame=lifter, pos=(pivot.x,pivot.y,0),
               axis=cyl.pos+pin.pos-(lifter.pos+pivot.pos)-vector(0,0,pin.z),
               radius=thick/5., color=pistoncolor)
Lrod = mag(rod.axis)              
thermometer = cylinder(frame=cyl, pos=(bottom.x+wide/2.+thick/2.,bottom.y+thick,deep/2.),
                       radius=thick/5.,
                       axis=(0,T*Tscale,0), color=color.red)
sphere(frame=cyl, pos=thermometer.pos, radius=thick/2., color=thermometer.color)
Tlabel = label(frame=cyl, pos=(bottom.x+wide/2.+thick/2.+thick,bottom.y+high/2.,deep/2.),
               xoffset=10, line=0, box=0, text=str(int(round(T)))+' K')
omegalabel = label(frame=cyl, pos=wheel.pos+vector(Rwheel,0,0),
                xoffset=10, line=0, box=0, text='0 rad/s')
                   
scene.autoscale = 0
scene.center = (0,0.8*high,0)
THreservoir = frame(pos=bottom.pos+vector(0,-Lreservoir/2.-thick/2.,0))
box(frame=THreservoir, pos=(0,0,0),size=(Lreservoir,Lreservoir,Lreservoir), color=color.red)
label(frame=THreservoir, pos=(0,0.4*Lreservoir,Lreservoir/2.), text=str(int(round(TH)))+' K',
      line=0, box=0)
TLreservoir = frame(pos=THreservoir.pos+vector(offsetReservoir,0,0))
box(frame=TLreservoir, pos=(0,0,0),size=(Lreservoir,Lreservoir,Lreservoir), color=color.blue)
label(frame=TLreservoir, pos=(0,0.4*Lreservoir,Lreservoir/2.), text=str(int(round(TL)))+' K',
      line=0, box=0)

gdisplay(title='PV', xtitle='V', ytitle='P', xmax=2.0, ymax=75,
         x=winw, y=0, width=400, height=winh)
PV = gcurve(color=color.cyan)

P = Pinitial = 66. # from old Ppiston+Nweights*Pweight = 12+3*18
T = Tinitial = TH
showT()

Natoms = 50  # change this to have more or fewer atoms
Matom = 4E-3/6E23 # helium mass
Ratom = 0.03 # wildly exaggerated size of helium atom
k = 1.4E-23 # Boltzmann constant
Atoms = []
colors = [color.red, color.green, color.blue,
          color.yellow, color.cyan, color.magenta]
poslist = []
plist = []
mlist = []
rlist = []
offset = 1.1*Ratom

pavg = sqrt(2.*Matom*1.5*k*TH)*(5E-5/dt) # average kinetic energy p**2/(2mass) = (3/2)kT

for i in range(Natoms):
    Lmin = -wide/2.+offset
    Lmax = wide/2.-offset
    x = Lmin+(Lmax-Lmin)*random()
    Lmin = bottom.y+thick/2.+offset
    Lmax = lifter.y+piston.y-thick/2.-offset
    y = Lmin+(Lmax-Lmin)*random()
    Lmin = -deep/2.+offset
    Lmax = deep/2.-offset
    z = Lmin+(Lmax-Lmin)*random()
    Atoms = Atoms+[sphere(pos=(x,y,z), radius=Ratom, color=colors[i % 6])]
    angle = pi*random()
    phi = 2*pi*random()
    px = pavg*sin(angle)*cos(phi)
    py = pavg*sin(angle)*sin(phi)
    pz = pavg*cos(angle)
    poslist.append((x,y,z))
    plist.append((px,py,pz))
    mlist.append(Matom)
    rlist.append(Ratom)

pos = array(poslist)
p = array(plist)
m = array(mlist)
m.shape = (Natoms,1) # Numeric Python: (1 by Natoms) vs. (Natoms by 1)
radius = array(rlist)
pos = pos+(p/m)*(dt/2.) # initial half-step
corner1 = array((-wide/2.+offset,bottom.y+thick/2.+offset,-deep/2.+offset))
corner2 = array((wide/2.-offset,lifter.y+piston.y-thick/2.-offset,deep/2.-offset))
picked = None

yinitial = lifter.y # begin isothermal expansion at TH (phase 0)
phase = 1
plot = 1
plotcolor = color.red
count = maxcount

scene.mouse.getclick()
front.visible = 0
scene.mouse.getclick()

while 1:
    rate(500)
    torque = cross(pin.pos-wheel.pos,P*norm(rod.axis)) # approximate force
    L += torque*dt
    dtheta = (L.z/Iwheel)*dt
    if dtheta > 0.045:
        break
    theta += dtheta
    stripes.rotate(angle=dtheta, axis=(0,0,1))
    pin.pos = (wheel.x+Rpin*cos(theta),wheel.y+Rpin*sin(theta),pin.z)
    oldy = (cyl.y+wheel.y)-(lifter.y+rod.y)
    newy = -Rpin*sin(theta)+sqrt(Lrod**2-(Rpin*cos(theta))**2)
    deltay = oldy-newy
    oldliftery = lifter.y
    lifter.y += deltay
    rod.axis = (cyl.pos+pin.pos)-(lifter.pos+rod.pos)-vector(0,0,pin.z)
    if phase == 1 or phase == 3: # isothermal
        P = P*oldliftery/lifter.y
    else: # adiabatic
        P = P*(oldliftery/lifter.y)**gamma
    T = Tinitial*(P*lifter.y)/(Pinitial*yinitial)
    showT()
    showomega()
    if plot:
        PV.plot(pos=(lifter.y,P), color=plotcolor)
    if phase == 1: # isothermal expansion
        if lifter.y >= 1.1:
            phase = 2
            plotcolor = color.yellow
            if maxcount > 0 and count != 0:
                scene.mouse.getclick()
            THreservoir.x -= offsetReservoir
            if maxcount > 0 and count != 0:
                count = maxcount
                scene.mouse.getclick()
    elif phase == 2: # adiabatic expansion
        if pin.x < 0 and T >= TL:
            phase = 3
            plotcolor = color.cyan
            if maxcount > 0 and count != 0:
                scene.mouse.getclick()
            TLreservoir.x -= offsetReservoir
            if maxcount > 0 and count != 0:
                count = maxcount
                scene.mouse.getclick()
    elif phase == 3: # isothermal compression
        if lifter.y <= 0.7:
            phase = 4
            plotcolor = color.yellow
            if maxcount > 0 and count != 0:
                scene.mouse.getclick()
            TLreservoir.x += offsetReservoir
            if maxcount > 0 and count != 0:
                count = maxcount
                scene.mouse.getclick()
    else:           # adiabatic compression
        if T >= TH:
            phase = 1
            plotcolor = color.red
            plot = 0
            if maxcount > 0 and count != 0:
                scene.mouse.getclick()
            THreservoir.x += offsetReservoir
            if maxcount > 0 and count != 0:
                count = maxcount
                scene.mouse.getclick()
                maxcount = 0
    count -= 1
    if count == 0:
        count = maxcount
        scene.mouse.getclick()

    # Update all positions of gas molecules
    pos = pos+(p/m)*dt

    # Bounce off walls
    outside = less_equal(pos,corner1) # walls closest to origin
    p1 = p*outside
    p = p-p1+abs(p1) # force p component inward
    corner2 = array((wide/2.-offset,lifter.y+piston.y-thick/2.-offset,deep/2.-offset))
    outside = greater_equal(pos,corner2) # walls farther from origin
    p1 = p*outside
    p = p-p1-abs(p1) # force p component inward
    dp = 2.*Matom*deltay/dt
    hit = greater(pos+(p/m)*dt,array((wide,lifter.y+piston.y-thick/2.-offset,deep)))
    p1 = p*hit
    p = p-p1-abs(p1)+dp*hit
    if deltay < 0: # piston headed down, move molecules down if above piston
        pos = pos-pos*hit+(lifter.y+piston.y-thick/2.-offset)*hit

    # Make sure the current average energy is consistent with the current temperature
    pavgnow = sum(mag(p))/Natoms
    p = p*sqrt(T/Tinitial)*(pavg/pavgnow)
             
    # Update positions of display objects
    for i in range(Natoms):
        Atoms[i].pos = pos[i]
        