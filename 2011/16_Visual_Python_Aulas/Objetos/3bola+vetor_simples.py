#from visual import *
import visual as vs

vs.scene.range = (10,10,10)


a=vs.sphere(pos=(0,0,0),radius=2,color=vs.color.cyan)
b=(5,0,0)

vector=vs.arrow(pos=a.pos,axis=b,color=vs.color.red)
