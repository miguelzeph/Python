#from visual import *
import visual as vs

mig=vs.sphere(pos=(-5,0,0),radius=2,color=vs.color.cyan)
gui=vs.sphere(pos=(5,0,0),radius=2,color=vs.color.cyan)

vector=vs.arrow(pos=mig.pos,axis=gui.pos,color=vs.color.red)
vector1=vs.arrow(pos=gui.pos,axis=mig.pos,color=vs.color.red)

#fazer vetor mig ir para gui e gui ir para mig