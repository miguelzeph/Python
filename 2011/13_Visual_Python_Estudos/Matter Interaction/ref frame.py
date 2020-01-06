from __future__ import division
from visual import *
scene.background = color.white
scene.x = scene.y = 0
scene.width = 1000
scene.range = 15

## Ruth Chabay 2007
## in rest frame only right ball moves

print '''
Set REST_FRAME = True for rest frame (only right ball moves)
Set REST_FRAME = False for moving frame (moves with CM)
red dot indicates CM
'''

REST_FRAME = True       ##True or False
if REST_FRAME is True:
    scene.title = "Rest Frame"
else:
    scene.title = "Moving Frame"
    
#cm frame
b1=sphere(pos=(-3,0,0), radius=0.5, color=color.magenta)
b2=sphere(pos=(-1,0,0), radius=0.5, color=color.blue)
cms = sphere(pos=(-2,0,0), radius=0.1, color=color.red)
dt = 0.01
b2.v = vector(2,0,0)
b1.v = vector(0,0,0)
vcm = (b1.v + b2.v)/2
cms.v = vcm

if REST_FRAME is False:
    b2.v = b2.v-vcm
    b1.v = b1.v-vcm
    cms.v = vector(0,0,0)

b2o=vector(b2.radius,0,0)
v2a=arrow(pos=b2.pos+b2o, axis=b2.v, color=color.green, shaftwidth=0.2,
          fixedwidth=1, visible=0)
v1a=arrow(pos=b1.pos-b2o, axis=b1.v, color=color.green, shaftwidth=0.2,
          fixedwidth=1, visible=0)
cma=arrow(pos=cms.pos, axis=b2.v/2, color=color.green, shaftwidth=0.2,
          fixedwidth=1, visible=0)

while 1:
    b1.pos = vector(-3,0,0)
    b2.pos = vector(-1,0,0)
    cms.pos = vector(-2,0,0)
    v2a.pos = b2.pos+b2o
    v1a.pos = b2.pos+b2o
    scene.mouse.getclick()
    v2a.visible = 1
    v1a.visible = 1

    while b2.x < scene.range.x:
        rate(100)
        b2.pos = b2.pos + b2.v*dt
        b1.pos = b1.pos + b1.v*dt
        v2a.pos = b2.pos+b2o
        v1a.pos = b1.pos-b2o
        cms.pos = cms.pos + cms.v*dt
        cma.pos = cms.pos

    v2a.visible=0
    v1a.visible=0
    scene.mouse.getclick()
    