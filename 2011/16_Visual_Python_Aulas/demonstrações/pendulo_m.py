from visual import *
from math import *

###############################################################
#                                                             #
# Esse programa descreve o movimento de um pendulo cujo ponto #
# de suspensao esta preso a uma mola de constante k.          #
#                                                             #
###############################################################

scene.range = (8,7,10)
scene.center = (3,-2,0)
scene.width = 800
scene.height = 500
scene.background = (0.5,0.5,0.5)

massa1= box (pos = (0,0,0), size=(1,1,1), color=(1,0.1,0.1))
massa2= sphere (pos = (0,0,0), radius = 0.5, color=(0.1,0.5,1))
parede = box(pos = (-3,0,0), size = (1,4,4))
barra = cylinder (pos = (-3,0,0), axis=(12,0,0), radius=0.1)
mola = helix(pos=(-3,0,0), axis=(7,0,0), radius=0.3,coils=8,thickness=0.07,color=color.red)
fio = curve (pos = [(massa1.pos),(massa2.pos)], color=(0,0,0), radius=0.03)

L0 = 3
L = 5.
teta0 = 10.
k = 100.
m1 = 1
m2 = .1
teta = (180-teta0)*pi/180
dt = 0.01
g = -10.
t = 0.
omega = 0.
v = 0.
a = 0.
alfa = 0.
x = 3.3

while (1==1):
    rate (100)
    a = (m2*L*sin(teta)*omega**2 - m2*g*L*sin(teta)*cos(teta) - k*(x-L0)) / (m1 + m2 + m2*L*(cos(teta))**2)
    alfa = -g*sin(teta) + a*cos(teta)
    v = v + a*dt
    x = x + v*dt
    omega = omega + alfa*dt
    teta = teta + omega*dt
    massa1.pos = (x,0,0)
    massa2.pos = (x+L*sin(teta), L*cos(teta),0)
    mola.axis = massa1.pos-parede.pos
    fio.pos = [(massa1.pos),(massa2.pos)]