from __future__ import division
from visual import *
from string import find

print """
Bruce Sherwood Fall 2000
Model the propagation of sound through a metal.
Linear chain of (N+2) atoms, first and last atoms fixed in position.
Atoms connected by interatomic "springs" (16 N/m for Al, 5 N/m for Pb).

Four parts of program to model propagation of sound through a metal:
(1) Click an atom to displace it, then click repeatedly to see motion.
(2) Same as (1), but also shows graph of displacements.
(3) Click an atom to displace it, click anywhere when pulse reaches right end.
(4) Same as (3), but lead atoms (Pb) instead of aluminum (Al).
Move to next part or back by clicking an atom at the end of the chain.
Atoms at the end of the chain are fixed in position.
"""

sw = scene.width = 800.
sh = scene.height = 600.
scene.x = scene.y = 0
scene.userzoom = scene.userspin = 0
scene.background = color.white
scene.foreground = color.black
gray = (0.5,0.5,0.5)

def cleaneformat(string): # convert 2.5E-006 to 2.5E-6; 2.5E+006 to 2.5E6
    index = find(string, 'E')
    if index == -1: return string # not E format
    index = index+1
    if string[index] == '-':
        index = index+1
    elif string[index] == '+':
        string = string[:index]+string[index+1:]
    while string[index] == '0':
        string = string[:index]+string[index+1:]
    return string

def makeinvisible(axis, disp, atoms, ticks, labels):
    axis.visible = 0
    disp.visible = 0
    for atom in atoms:
        atom.visible = 0
    for tick in ticks:
        tick.visible = 0
    for lab in labels:
        lab.visible = 0
        
def propagate(N, metal, showcurve=1, atomcolor=color.blue):
    d = properties[metal]['d'] # inter-nuclear distance
    m = properties[metal]['m'] # mass of one atome
    ks = properties[metal]['ks'] # effective stiffness of interatomic "spring" force
    dxinitial = 0.3*d # initial displacement of touched atom
    sy = ((N+2)*d)*(sh/sw) # height of display in world coordinates
    yoffset = d+(sy-d)/2. # location of curve centerline
    axis = curve(pos=[(0,yoffset,-d/10.),
                ((N+1)*d,yoffset,-d/10.)], color=gray, visible=showcurve)
    scale = 2.*((sy-d)/2.)/dxinitial # scale up graph of displacements
    if N <= 10:
        scale = scale/2.

    disp = curve(color=color.blue, visible=showcurve)
    for nn in range(N+2):
        disp.append(pos=(nn*d,yoffset,0))
    atoms = []
    ticks = []
    for nn in range(N+2): # movable masses from 1 to N; end atoms fixed
        atoms.append(sphere(pos=(nn*d,0.5*d,0), radius=0.5*d, color=atomcolor))
        atoms[nn].p = vector(0,0,0)
        if N <= 10:
            if not (nn == 0 or nn == (N+1)):
                ticks.append(curve(pos=[(nn*d,1.1*d,0),(nn*d,1.5*d,0)], color=gray))
    atoms[0].color = gray
    atoms[N+1].color = gray
    
    labels = [None,None,None,None]
    labels[0] = label(pos=atoms[0].pos+vector(0,d/2.,0), text='Back',
                      yoffset=10, linecolor=gray, opacity=0)
    labels[1] = label(pos=atoms[N+1].pos+vector(0,d/2.,0), text='Next',
                      yoffset=10, linecolor=gray, opacity=0)
    s = '%d %s atoms, ' % (N, metal) + cleaneformat('%1.1E m' % ((N+1)*d))
    labels[2] = label(pos=((N+1)*d/2.,d/2.,0), yoffset=10, height=20,
                      text= s, visible=0, box=0, line=0, opacity=0)
    labels[3] = label(pos=(0.8*N*d,d/2.,0),text='t = 0',
                      yoffset=10, height=20, visible=0, box=0, line=0, opacity=0)
    
    if N > 10:
        labels[2].visible = 1
        labels[3].visible = 1
    if showcurve:
        scene.center = ((N+1)*d/2.,sy/2.,0)
    else:
        scene.center = ((N+1)*d/2.,0,0)
    while 1:
        scene.mouse.getclick() # watch for clicking an atom to displace it
        if scene.mouse.pick in atoms:
            ith = atoms.index(scene.mouse.pick)
            if ith == 0 or ith == N+1: # clicked an end atom
                makeinvisible(axis, disp, atoms, ticks, labels)
                if ith == 0: return 'Back'
                else: return 'Next'
            atoms[ith].x = ith*d+dxinitial
            disp.y[ith] = yoffset+scale*dxinitial
            break
    t = 0.

    while 1: # main loop; for N <= 10 click to advance, else free run
        if N <= 10 or scene.mouse.clicked:
            scene.mouse.getclick()
            if scene.mouse.pick in atoms:
                ith = atoms.index(scene.mouse.pick)
                if ith == 0 or ith == N+1:
                    makeinvisible(axis, disp, atoms, ticks, labels)
                    if ith == 0: return 'Back'
                    else: return 'Next'
            if N > 10.: break
        rate(100)

######################################  
        for nn in range(1, N+1):
            Fright = ks*(atoms[nn+1].x-atoms[nn].x-d) # force exerted by atom to right
            Fleft = -ks*(atoms[nn].x-atoms[nn-1].x-d) # force exerted by atom to left
            atoms[nn].p.x = atoms[nn].p.x+(Fright+Fleft)*dt # update momentum

        for nn in range(1, N+1): # after updating all momenta, update positions
            atoms[nn].x = atoms[nn].x+(atoms[nn].p.x/m)*dt
            disp.y[nn] = yoffset+scale*(atoms[nn].x-nn*d)

        t = t+dt
        s = cleaneformat('t = %1.2E s' % t)
        labels[3].text = s
######################################
        
    if N > 10:
        dist = (N-ith)*d
        s = '%s\nv = %0.0f m/s' % (cleaneformat('dist. = %1.2E m' % dist), dist/t) # speed of sound
        arr = arrow(pos=(atoms[ith].x,0.1*N*d,0),
                    axis=(atoms[N].x-atoms[ith].x,0,0),
                    shaftwidth=d, color=color.cyan)
        report = label(pos=arr.pos+0.5*arr.axis, height=20,
                       yoffset=15, text=s, box=0, line=0, opacity=0)
        print s
        scene.mouse.getclick()
        arr.visible = 0
        report.visible = 0
        if scene.mouse.pick in atoms:
            ith = atoms.index(scene.mouse.pick)
            if ith == 0 or ith == N+1:
                makeinvisible(axis, disp, atoms, ticks, labels)
                if ith == 0: return 'Back'
                else: return 'Next'
        
    makeinvisible(axis, disp, atoms, ticks, labels)
    return 'Next'

def setstate(ret, state, maxstate):
    if ret == 'Next': state = state+1
    else: state = state-1
    if state < 0: state = maxstate
    if state > maxstate: state = 0
    return state

properties = {'Al': {'m': 27e-3/6e23, 'ks': 16., 'd': (1./2.7e-3)**(1./3.)*0.01},
              'Pb': {'m': 207e-3/6e23, 'ks': 5., 'd': (1./11.6e-3)**(1./3.)*0.01} }
for metal in properties.keys():
    properties[metal]['d'] = properties[metal]['d']*properties[metal]['m']**(1./3.)
dt = 2.*pi*sqrt(properties['Al']['m']/properties['Al']['ks'])/30.
dAl = properties['Al']['d']
state = 0
maxstate = 3

while 1:
    if state == 0:
        length = 10.*dAl
        N = int(length/properties['Al']['d'])
        scene.range = (N+4)*dAl/2.
        ret = propagate(N, 'Al', showcurve=0)
        state = setstate(ret, state, maxstate) 
    elif state == 1:
        length = 10.*dAl
        N = int(length/properties['Al']['d'])
        scene.range = (N+4)*dAl/2.
        ret = propagate(N, 'Al', showcurve=1)
        state = setstate(ret, state, maxstate) 
    elif state == 2:
        length = 100.*dAl
        N = int(length/properties['Al']['d'])
        scene.range = 1.1*length/2.
        ret = propagate(N, 'Al', showcurve=1)
        state = setstate(ret, state, maxstate) 
    elif state == 3:
        length = 100.*dAl
        N = int(length/properties['Pb']['d'])
        scene.range = 1.1*length/2.
        ret = propagate(N, 'Pb', showcurve=1, atomcolor=color.green)
        state = setstate(ret, state, maxstate)