from __future__ import division
from visual import *
scene.background = color.white
scene.width = scene.height = 700
R=4e11
s1 = sphere(pos=(0,R,0), radius=1e10, color=color.magenta)
s2 = sphere(pos=(0,-R,0), radius=1e10, color=color.blue)
s3 = sphere(pos=(2*R,0,0), radius=1e10, color=color.green)
s1.m = 5e30
s2.m = 5e30
s3.m = 5e30*1e-1
G = 6.7e-11
v = sqrt(G*s1.m/(4*R))
s1.p = s1.m*vector(0,0,-v)
s2.p = s2.m*vector(0,0,v)
s3.p = vector(0,0,0)
t1=curve(color=s1.color)
t2=curve(color=s2.color)
t3=curve(color=s3.color)
dt = 60*1000
t = 0
while 1:
    rate(200)
    r21 = s2.pos - s1.pos
    F21 = -norm(r21)*G*s1.m*s2.m/mag(r21)**2
    r32 = s3.pos - s2.pos
    F32 = -norm(r32)*G*s3.m*s2.m/mag(r32)**2
    r31= s3.pos - s1.pos
    F31 = -norm(r31)*G*s3.m*s1.m/mag(r31)**2
    s3.p = s3.p + (F32+F31)*dt
    s2.p = s2.p + (F21-F32)*dt
    s1.p = s1.p + (-F21-F31)*dt
    s1.pos = s1.pos + (s1.p/s1.m)*dt
    s2.pos = s2.pos + (s2.p/s2.m)*dt
    s3.pos = s3.pos + (s3.p/s3.m)*dt
    t1.append(pos=s1.pos)
    t2.append(pos=s2.pos)
    t3.append(pos=s3.pos)
    t = t+dt