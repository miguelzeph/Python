############################################################
#                                                          # 
# Esse programa descreve o movimento de um pendulo simples #
#                                                          #
############################################################

from visual import *
from math import *

scene.range = (10,10,10)
scene.center = (0,-4,0)
scene.width = 400
scene.height = 700

massa= sphere (pos = (0,0,0), radius = 0.5, color=color.red)
base = box (pos = (0,-10,-2), size = (7,0.5,7))
haste = box (pos = (0,-4,-2), size = (0.6,12,0.6))
pitoco = cylinder (pos = (0,0,-2), radius=0.2, axis = (0,0,2), color = color.yellow)
fio = curve (pos = [(0,0,0),(massa.pos)])

l = 6
pi = 3.1415
teta0 = 30
teta = (180-teta0)*pi/180
dt = 0.01
g = -10
t = 0
omega = 0

while (1==1):
    rate (250)
    omega += -g*sin (teta)*dt/l
    teta += omega*dt
    massa.pos=(l*sin(teta), l*cos(teta), 0)
    fio.pos = [(0,0,0),(massa.pos)]