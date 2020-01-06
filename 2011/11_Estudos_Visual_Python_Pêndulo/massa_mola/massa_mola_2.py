from visual import *
from math import *
from visual.graph import * 

scene.range = (12,12,12)
scene.center = (0,0,0)
scene.width = 800
scene.height = 300

bloco= box (pos=(0,0,0), size=(2,2,2),color=color.green)
chao = box (pos = (0,-1.25,0), size =(15,0.5,7))
parede1 = box(pos = (-7,1,0), size = (0.5,4,7))
mola1 = helix(pos=(-7,0,0),axis=(7,0,0), radius=0.5,coils=6,thickness=0.1,color=color.red)
parede2 = box(pos = (7,1,0), size = (0.5,4,7))
mola2 = helix(pos=bloco.pos,axis=(7,0,0), radius=0.5,coils=6,thickness=0.1,color=color.red)

x = 1.
k = 10.
m = 1.
dt = 0.01
t = 0
v = 0.
caixa1 = label(pos=(0,2,0), text='x = %1.1f' % x)

while (1==1):
    rate (100)
    if scene.mouse.clicked:
        break
    v += dt*(-2*k/m*bloco.pos.x)
    x += v*dt
    mola1.axis = bloco.pos-parede1.pos + (0,1,0) 
    bloco.pos.x = x
    mola2.pos = bloco.pos
    mola2.axis = parede2.pos-bloco.pos - (0,1,0)
    t = t + dt
    caixa1.text='x = %1.2f' % x