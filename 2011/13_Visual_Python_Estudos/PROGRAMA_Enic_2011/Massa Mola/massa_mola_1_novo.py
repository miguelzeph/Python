# -*- coding: cp1252 -*-
from visual.graph import * 
from visual import *
from math import *

print '\n\
###############################################################\n\
#                                                             # \n\
# Esse programa descreve o movimento de um sistema massa-mola #\n\
#                                                             #\n\
###############################################################\n\
'
x = float (input ('Por favor, digite o deslocamento inicial do bloco: '))
k = float (input ('Por favor, digite a constante elástica da mola: '))
m = float (input ('Por favor, digite a massa do bloco: '))

scene.x=200
scene.y=200
#scene.center = (0,0,0)
#scene.width = 800
#scene.height = 300
bloco= box (pos=(0,0,0), size=(2,2,2),color=color.green)
chao = box (pos = (0,-1.25,0), size =(15,0.5,7))
parede1 = box(pos = (-7,1,0), size = (0.5,4,7))
mola = helix(pos=(-7,0,0), axis=(7,0,0), radius=0.5,coils=6,thickness=0.1,color=color.red)

graph1 = gdisplay(x=0, y=0, width=250, height=250, 
          title='E vs. t', xtitle='t(s)', ytitle='E(J)', 
          xmax=50., xmin=0., ymax=20, ymin=0, 
          foreground=color.white, background=(0,0,0))

funcao1 = gcurve(color=color.cyan)
funcao2 = gcurve(color=color.red)
funcao3 = gcurve(color=color.magenta)


dt = 0.01
v = 0
t = 0
caixa1 = label(pos=(0,2,0), text='x = %1.1f' % x)

while (1==1):
    rate (100)
    v += dt*(-k/m*bloco.pos.x)
    x += v*dt
    mola.axis = bloco.pos-parede1.pos + (0,1,0)
    bloco.pos.x = x
    t = t + dt
    caixa1.text='x = %1.2f' % x
    if t < 20:
        funcao1.plot(pos=(t,m*v**2/2))#Energia Cinetica
        funcao2.plot(pos=(t,k*x**2/2))#Energia Potencial Elastica
        funcao3.plot(pos=(t,m*v**2/2+k*x**2/2))#Energia Mecanica