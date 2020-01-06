from visual import *
from math import *

scene.range = (16,12,12)
scene.center = (0,0,0)
scene.width = 800
scene.height = 300

bloco1 = box (pos=(-5,0,0), size=(2,2,2),color=color.green)
bloco2 = box (pos=(0,0,0), size=(2,2,2),color=color.green)
bloco3 = box (pos=(5,0,0), size=(2,2,2),color=color.green)
chao = box (pos = (0,-1.25,0), size =(25,0.5,7))
parede1 = box(pos = (-12,1,0), size = (0.5,4,7))
parede2 = box(pos = (12,1,0), size = (0.5,4,7))
mola1 = helix(pos=(-12,0,0),axis=7, radius=0.5,coils=8,thickness=0.1,color=color.red)
mola2 = helix(pos=bloco1.pos,axis=7, radius=0.5,coils=8,thickness=0.1,color=color.red)
mola3 = helix(pos=bloco2.pos,axis=7, radius=0.5,coils=8,thickness=0.1,color=color.red)
mola4 = helix(pos=bloco3.pos,axis=7, radius=0.5,coils=8,thickness=0.1,color=color.red)

x1 = 1.
x2 = 2.
x3 = -1.
x4 = 0.
k = 1.
m = 5.
dt = 0.1
v1 = 0.
v2 = 0.
v3 =0.

while (1==1):
    rate (100)
    a1 = k/m*(x2 - 2*x1)
    a2 = k/m*(x3 - 2*x2 + x1)
    a3 = k/m*(x4 - 2*x3 + x2)
    v1 += a1*dt
    x1 += v1*dt
    v2 += a2*dt
    x2 += v2*dt
    v3 += a3*dt
    x3 += v3*dt
    bloco1.pos.x = x1-5
    bloco2.pos.x = x2
    bloco3.pos.x = x3+5
    mola2.pos = bloco1.pos
    mola3.pos = bloco2.pos
    mola4.pos = bloco3.pos
    mola1.axis = bloco1.pos.x-parede1.pos.x
    mola2.axis = bloco2.pos.x-bloco1.pos.x
    mola3.axis = bloco3.pos.x-bloco2.pos.x
    mola4.axis = parede2.pos.x-bloco3.pos.x