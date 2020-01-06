#from visual import *
import visual as vs

mig=vs.sphere(pos=(-10,-25,0),radius=2,color=vs.color.cyan)
gui=vs.sphere(pos=(5,0,0),radius=2,color=vs.color.cyan)

vector=vs.arrow(pos=mig.pos,axis=gui.pos-mig.pos,color=vs.color.red)


