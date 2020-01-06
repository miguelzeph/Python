from __future__ import division
from visual import *

print """
Bruce Sherwood Fall 2000
Revised Spring 2005 to display against a moving background.
Illustrates the momentum principle (Newton's 2nd law).
Drag a red force vector.
Object moves under the influence of this single force,
and bounces off the walls.
The dark blue arrow represents momentum.
"""

h = w = 500
scene.width = w
scene.height = h
scene.x = scene.y = 0
scene.background = color.white
wide = 1.
scene.fov = 0.001
scene.range = wide
scene.userzoom = 0
scene.userspin = 0
ball = sphere(pos=(0,0,0), radius=wide/20, color=(0,0.7,0))
ball.mass = 200.
ball.p = vector()
mpos = vector(0,0,0)
grid = frame()
trail = curve(frame=grid, color=ball.color)
gridd = 0.5*wide
gridr = 2*wide+gridd
gridcolor = (0.7,0.7,0.7)
for x in arange(-gridr,gridr+gridd/2,gridd):
    curve(frame=grid, pos=[(x,-gridr,0),(x,gridr,-0.1)], color=gridcolor)
for y in arange(-gridr,gridr+gridd/2,gridd):
    curve(frame=grid, pos=[(-gridr,y,0),(gridr,y,-0.1)], color=gridcolor)
dt = 0.02
Foffset = vector(0,0,-ball.radius)
Fvec = arrow(pos=ball.pos+Foffset, axis=(0,0,0), shaftwidth=wide/30., color=color.red)
pvec = arrow(pos=ball.pos, axis=(0,0,0), shaftwidth=wide/30., color=(.22,.33,.64))
Fmouse = 1. # F mouse scale factor
Fview = 1. # F view scale factor
pview = 0.025 # p view scale factor

drag = 0
F = vector(0,0,0)
count = 0
while 1:
    rate(200)
    if scene.mouse.events: # check for mouse events
        m = scene.mouse.getevent() # get the mouse info
        if m.drag == 'left' or m.press == 'left':
            drag = 1
        elif m.drop == 'left':
            drag = 0
    if drag:
        F = Fmouse*(scene.mouse.pos-scene.center)
    Fvec.axis = Fview*F
    ball.p = ball.p + F*dt
    ball.pos = ball.pos + (ball.p/ball.mass)*dt
    scene.center = ball.pos # follow the ball, keeping it in the center
    trail.append(pos=ball.pos)
    if abs(ball.pos.x) >= gridr:
        ball.p.x = -ball.p.x
    if abs(ball.pos.y) >= gridr:
        ball.p.y = -ball.p.y
    Fvec.pos = ball.pos
    Fvec.axis = Fview*F
    pvec.pos = ball.pos
    pvec.axis = pview*ball.p