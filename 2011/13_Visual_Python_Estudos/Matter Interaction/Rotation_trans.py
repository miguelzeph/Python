from __future__ import division
from visual import *
## Ruth Chabay 2006-03-27  modified 2009-10-28
scene.background = color.white
scene.x=0
scene.width=1000
scene.range = 18
##print version
print '''
Helps visualize separation into v_CM and v_rel.
Click anywhere to start motion; click to pause, click to resume.
Change the variable CASE to change initial conditions.
Change visCM, visREL, visTOT flags to display v_cm or v_rel or v for a ball.
Change visTRAIL to display a trail for each ball.
Cyan arrow: v_cm; green arrows: v_rel;
Magenta and blue arrows: v of respective balls

CASE = 0: left ball fixed -- think about vcm & vrel
CASE = 1: v_CM=0, vibration, zero external force
CASE = 2: initially in motion, rotation + translation, zero external force
CASE = 3: initially in motion, rot + vib + trans, zero external force
CASE = 4: weaker spring, 0 initial stretch, const force on b2
CASE = 5: initially slightly stretched, at angle, const force
CASE = 6: vibration perp to translation; zero net force

CLEAN CASES ARE 2, 6 '''

CASE = 6     ## choose initial conditions (0-6); see descriptions below
visCM = 0       ## display arrows for vrel (1=True or 0=False)
visREL = 0      ## display cm and vcm (True or False)
visTOT = 0      ## instantaneous v of each ball
visTRAIL = 0    ## each ball leaves a trail
FARRVIS=0       ## force arrow visible

print 'CASE =', CASE

vscale=3*.5
fscale=5

w=1
L0=3.0*2
yo = vector(0,1.5*w/2,0)
b1=sphere(pos=(-14,0,0), radius=0.5, color=color.magenta, m=1)
b1.trail = curve(color=b1.color, visible = visTRAIL)
spring = helix(pos=b1.pos, axis=(L0,0,0), radius=0.25,
               coils=8, thickness=0.1, color=(0.7,0.5,0))
Lhat = norm(spring.axis)
b2=sphere(pos=spring.pos + vector(L0,0,0), radius=0.5,color=color.blue, m=1)
b2.trail = curve(color=b2.color, visible = visTRAIL)
cm = sphere(pos=(b1.pos+b2.pos)/2, radius=0.1, color=color.cyan, visible=visCM)
v1rel=arrow(pos=b1.pos, axis=(0,0,0), color=color.green,
            shaftwidth=0.2, fixedwidth=1, visible=visREL)
v2rel=arrow(pos=b2.pos, axis=(0,0,0), color=color.green,
            shaftwidth=0.2, fixedwidth=1, visible=visREL)
vcma = arrow(pos=cm.pos,axis=(0,0,0), color=color.cyan,
             shaftwidth=0.2, fixedwidth=1,visible=visCM)
v1tot=arrow(pos=b1.pos, axis=(0,0,0), color=b1.color,
            shaftwidth=0.2, fixedwidth=1, visible=visTOT)
v2tot=arrow(pos=b1.pos, axis=(0,0,0), color=b2.color,
            shaftwidth=0.2, fixedwidth=1, visible=visTOT)

if CASE is 6:   ## vibration perp to translation; zero net force
    L0 = 1*L0
    cmpos = b1.pos + 0.5*spring.axis
    b2.pos = cmpos + vector(0,L0/2,0)
    b1.pos = cmpos + vector(0,-L0/2,0)
    spring.pos = b1.pos
    spring.axis = (0,L0,0)
    spring.coils = 16
    pcm = vector(2,0,0)
    b2.p = pcm + vector(0,4,0)
    b1.p = pcm + vector(0,-4,0)
    Fext = vector(0,0,0)
    ks = 10
    vscale = vscale*1
if CASE is 5:               ## I can't remember why this peculiar case is included :)
    vscale=vscale*2
    b1.pos = b1.pos+yo      ## initially slightly stretched, at angle, const force
    b2.pos = b2.pos-yo
    spring.pos = b1.pos
    spring.axis = b2.pos-b1.pos
    b1.p = vector(0,0,0)
    b2.p = vector(0,0,0)
    Fext = vector(.5,0,0)
    ks=20
if CASE is 4:               ## weaker spring, 0 initial stretch, const force on b2
    vscale = vscale*2
    b1.p = vector(0,0,0)
    b2.p = vector(0,0,0)
    Fext = vector(.5,0,0)
    ks = 0.1
elif CASE is 3:             ## initially in motion, rot + vib + trans, zero external force
    b1.p = vector(4,-.5,0)
    b2.p = vector(-2,.5,0)
    Fext = vector(0,0,0)
    ks = 20
elif CASE is 2:             ## initially in motion, rotation + translation, zero external force
##    b1.p = vector(2,-.5,0)
##    b2.p = vector(2, .5, 0)
    b1.p = vector(2,-2,0)
    b2.p = vector(2, 2, 0)
    Fext = vector(0,0,0)
    ks = 20
elif CASE is 1:             ## v_CM=0, vibration, zero external force
    b1.p = vector(2,0,0)
    b2.p = vector(-2,0,0)
    Fext = vector(0,0,0)
    ks = 20
elif CASE is 0:             ## left ball fixed -- think about vcm & vrel
    b1.p = vector(0,0,0)    ## clicker Q 1&2
    b2.p = vector(0,0,0)
    Fext = vector(2,0,0)
    ks = 0.1    
dt = 0.0005
t = 0
scene.autoscale = 0
scene.mouse.getclick()
while 1:
    rate(1000)
    if scene.mouse.clicked:         ## pause if mouseclick; wait for another
        scene.mouse.getclick()
        scene.mouse.getclick()
    Lhat = norm(b2.pos-b1.pos)
    s = (mag(b2.pos - b1.pos))-L0
    Fspring = -ks*s*Lhat            ## force on ball 2 (blue) by spring
    b2.p= b2.p + (Fext+Fspring)*dt
    if CASE is 0:
        F1 = Fspring                 ## anchor left ball
        if b2.x > scene.range.x*1.1:  ## stop if offscreen
            break
    else:
        F1 = vector(0,0,0)              ## no external force on ball 1 (magenta)
    b1.p = b1.p +(F1- Fspring)*dt
    dr2 = (b2.p/b2.m)*dt
    b2.pos = b2.pos + dr2
    b2.trail.append(pos=b2.pos)
    dr1 =(b1.p/b1.m)*dt
    b1.pos = b1.pos + dr1
    b1.trail.append(pos=b1.pos)
    spring.pos = b1.pos
    spring.axis = b2.pos - b1.pos
    cm.pos=(b1.pos+b2.pos)/2
    vcm = (b1.p+b2.p)/(b1.m+b2.m)
    v1rel.axis=((b1.p/b1.m)-vcm)*vscale
    v1rel.pos=b1.pos
    v2rel.axis= ((b2.p/b2.m)-vcm)*vscale
    v2rel.pos=b2.pos
    v2tot.pos = b2.pos
    v2tot.axis = (b2.p/b2.m)*vscale
    v1tot.pos = b1.pos
    v1tot.axis = (b1.p/b1.m)*vscale
    vcma.pos=cm.pos
    vcma.axis=vcm*vscale
