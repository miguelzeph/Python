# -*- coding: cp1252 -*-
from math import *
from visual.graph import *

scene.range = (30,30,30)
scene.center = (0,0,0)
scene.background = (0,0,0)
scene.width = 700
scene.height = 700

x = 0
y = 0
z = 0
t = 0


bola = sphere(pos=(x,y,z), radius=0.1, color=color.green)
meio2 = box(pos=(-1.5, 0, 0), size=(3,22,0), color=color.white)
meio3 = box(pos=(1.5, 0, 0), size=(3,22,0), color=color.blue)


N1 = 1 
N2 = 2 

angulo = 45
dt = 0.01

trilha = curve(color=bola.color)

teta1 = angulo*((math.pi)/180)
teta2 = math.asin(N1*math.sin(teta1)/N2)

bola.pos = (-30*math.cos(teta1), -30*math.sin(teta1), z)

while 1:
  rate(700)
  if bola.pos.x < 0:
    bola.pos = (bola.pos.x + dt*math.cos(teta1),
                 bola.pos.y + dt*math.sin(teta1), z) 
  else:
    bola.pos = (bola.pos.x + dt*math.cos(teta2),
                 bola.pos.y + dt*math.sin(teta2), z)

  trilha.append(pos=bola.pos)