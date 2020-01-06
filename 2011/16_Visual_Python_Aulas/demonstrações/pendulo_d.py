from visual import *
from math import *
#Camera----------------
scene.range = (10,10,10)
scene.center = (0,-4,0)
scene.width = 400
scene.height = 700
#---------------------

massa1= sphere (pos = (0,0,0), radius = 0.5, color=color.red)
massa2= sphere (pos = (0,0,0), radius = 0.5, color=color.red)
base = box (pos = (0,-10,-2), size = (7,0.5,7))
haste = box (pos = (0,-4,-2), size = (0.6,12,0.6))
pitoco = cylinder (pos = (0,0,-2), radius=0.2, axis = (0,0,2), color = color.yellow)
fio1 = curve (pos = [(0,0,0),(massa1.pos)], color=color.magenta)
fio2 = curve (pos = [(massa1.pos),(massa2.pos)], color=color.magenta)


teta01 = 30.
teta02 = 0.
l = 3.5
pi = 3.1415
teta1 = (180-teta01)*pi/180
teta2 = (180-teta02)*pi/180
dt = 0.01
g = -10.
t = 0.
omega1 = 0.
omega2 = 0.
alfa1 = 0.
alfa2 = 0.


a = cos (teta1 - teta2)
b = sin (teta1 - teta2)

while (1==1):
    rate (250)
    alfa1 = (g/l*(sin(teta2)*a-2*sin(teta1))-omega1**2*b*a-omega2**2*b)/(2-a**2)
    alfa2 = omega1**2*b-g/l*sin(teta2) - alfa1*a
    omega1 += alfa1*dt
    omega2 += alfa2*dt
    teta1 += omega1*dt
    teta2 += omega2*dt
    massa1.pos=(l*sin(teta1), l*cos(teta1), 0)
    massa2.pos=(l*sin(teta1) + l*sin(teta2), l*cos(teta1) + l*cos(teta2), 0)
    fio1.pos = [(0,0,0),(massa1.pos)]
    fio2.pos = [(massa1.pos),(massa2.pos)]
	
