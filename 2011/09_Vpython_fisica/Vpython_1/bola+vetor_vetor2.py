#from visual import *
import visual as vs

mig=vs.sphere(pos=(-5,-5,-5),radius=2,color=vs.color.cyan)
gui=vs.sphere(pos=(5,5,5),radius=2,color=vs.color.cyan)
pri=vs.sphere(pos=(10,10,0),radius=2,color=vs.color.cyan)

vector1=vs.arrow(pos=mig.pos,axis=gui.pos-mig.pos,color=vs.color.red)
vector2=vs.arrow(pos=gui.pos,axis=pri.pos-gui.pos,color=vs.color.red)
vector3=vs.arrow(pos=pri.pos,axis=mig.pos-pri.pos,color=vs.color.red)


