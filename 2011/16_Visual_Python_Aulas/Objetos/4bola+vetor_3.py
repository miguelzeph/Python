#from visual import *
import visual as vs

a=vs.sphere(pos=(-5,0,0),radius=2,color=vs.color.cyan)
b=vs.sphere(pos=(5,0,0),radius=2,color=vs.color.cyan)

vector=vs.arrow(pos=a.pos,axis=b.pos,color=vs.color.red)
vector1=vs.arrow(pos=b.pos,axis=a.pos,color=vs.color.red)
vector2=vs.arrow(pos=b.pos,axis=a.pos*(-1),color=vs.color.white)
vector3=vs.arrow(pos=a.pos,axis=b.pos*(-1),color=vs.color.white)
