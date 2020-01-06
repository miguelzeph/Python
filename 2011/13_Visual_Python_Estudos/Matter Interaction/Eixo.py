from __future__ import division
from visual import *
scene.background = color.white
scene.width = 800
scene.height = 800

def grid(max=10, rad=0.03):
    gray = (0.8,0.8,0.8)
    for x in range(-max,max+1,2):   ## parallel to z axis,  vary x
        cylinder(pos=(x,0,-max), axis=(0,0,2*max), radius=rad, color=gray, opacity=0.2)
    for z in range(-max,max+1,2):   ## parallel to x axis, vary z
        cylinder(pos=(-max,0,z), axis=(2*max,0,0), radius=rad, color=gray, opacity=0.2)
    for y in range(-max,max+1,2):   ## parallel to z axis, vary y
        cylinder(pos=(0,y,-max), axis=(0,0,2*max), radius=rad, color=gray, opacity=0.2)
    for z in range(-max,max+1,2):   ## parallel to y axis, vary z
        cylinder(pos=(0,-max,z), axis=(0,2*max,0), radius=rad, color=gray, opacity=0.2)

def axes(max=10, rad=0.1):
    xaxis=cylinder(color=(1,0,0), pos=(-max,0,0), axis=(2*max,0,0), radius=rad)
    xlbl=label(pos=(11,0,0), text="X", color=color.red, opacity=0, height=30)
    yaxis=cylinder(color=color.green, pos=(0,-max,0), axis=(0,2*max,0), radius=rad)
    ylbl=label(pos=(0,11,0), text="Y", color=color.green, opacity=0, height=30)
    zaxis=cylinder(color=color.blue, pos=(0,0,-max), axis=(0,0,2*max), radius=rad)
    xlbl=label(pos=(0,0,11), text="Z", color=color.blue, opacity=0, height=30)



grid()  ## if you don't want a grid, comment out this line
axes()

scene.mouse.getclick()   ## wait for mouse click

## change components of axis to change direction of arrow
r = arrow(pos=(0,0,0), axis = vector(8,9,5), color=color.magenta, shaftwidth=0.5)
