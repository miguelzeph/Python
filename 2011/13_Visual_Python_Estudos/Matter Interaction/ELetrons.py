from __future__ import division
from visual import *
# Bruce Sherwood, NCSU, February 2007
print """
Drag the electron sea left or right with the mouse.
"""
scene.background = color.white
scene.foreground = color.black
scene.width = 900
scene.height = 250
hw = 4
hh = 1
scene.range = 5
d = hw/20
bar = d/2

def plus(x,y):
    box(pos=(x,y,0), size=(bar/4,bar,0), color=color.red)
    box(pos=(x,y,0), size=(bar,bar/4,0), color=color.red)

def minus(x,y, f):
    box(frame=f, pos=(x-bar/4,y+bar/2,0), size=(bar,bar/4,0), color=color.blue)

block = curve(pos=[(-hw,-hh,0),(-hw,hh,0),(hw,hh,0),(hw,-hh,0),(-hw,-hh,0)],
              color=color.black)
for x in arange(-hw+d/2,hw,d):
    for y in arange(-hh+d/2,hh,d):
        plus(x,y)

mobile = frame(pos=(0,0,0))
for x in arange(-hw+d/2,hw,d):
    for y in arange(-hh+d/2,hh,d):
        minus(x,y,mobile)

start = None
while 1:
    rate(100)
    if start:
        mobile.pos.x = scene.mouse.pos.x-start
    if scene.mouse.events:
        m = scene.mouse.getevent()
        if m.drag:
            start = m.pos.x-mobile.pos.x
        elif m.drop:
            start = None
