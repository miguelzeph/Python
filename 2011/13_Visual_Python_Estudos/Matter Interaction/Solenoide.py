from visual import *

print """
Bruce Sherwood Spring 2000, revised Dec. 2001
Drag or click to show the field interactively.
Uses Numeric for speed.
"""

scene.width = 800
scene.height = 700
scene.background = color.white
L = 1.0
R = 0.2
k = 1E-7 # mu-zero/4pi
I = 1.0
Ncoils = 10
Bscale = (L/2.)/(4*pi*1E-7*Ncoils*I/L)
dangle = pi/20
angle = arange(0,Ncoils*2*pi+dangle,dangle)
helix = curve(x=-L/2.+L*angle/(Ncoils*2*pi), y=R*cos(angle), z=R*sin(angle),
              color=(1,0.7,0.2), radius=0.005)

delta = helix.pos[1:] - helix.pos[:-1]
center = (helix.pos[:-1] + helix.pos[1:])/2.
scene.range = 0.7*L
vwidth = L/50.

def BField(obs):
    r = obs-center
    rmag = mag(r)
    rmag.shape = (-1,1)
    try:
        return (k*I*cross(delta, r)/rmag**3).sum(axis=0)
    except:
        return sum(k*I*cross(delta, r)/rmag**3)

Bvector = arrow(axis=(0,0,0), shaftwidth=vwidth, color=(0,1,1))
drag = 0
while 1:
    if drag:
        newobs = scene.mouse.pos
        if newobs != obs:
            obs = newobs
            Bvector.axis = Bscale*BField(obs)
            Bvector.pos = obs
    if scene.mouse.events:
        m = scene.mouse.getevent()
        if m.drag:
            drag = 1
            obs = None # force update of position
##            scene.cursor.visible = 0
        if m.drop:
            drag = 0
##            scene.cursor.visible = 1
            arrow(pos=obs, axis=Bscale*BField(obs), shaftwidth=vwidth, color=(0,1,1))
        elif m.click:
            arrow(pos=m.pos, axis=Bscale*BField(m.pos), shaftwidth=vwidth, color=(0,1,1))
