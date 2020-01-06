#from visual import *
import visual as vs

vs.scene.range = (20,10,10)

vector1=vs.arrow(pos=(0,0,0),axis=(0,10,0),color=vs.color.red)
vector2=vs.arrow(pos=(0,0,0),axis=(0,-10,0),color=vs.color.red)
vector3=vs.arrow(pos=(0,0,0),axis=(10,0,0),color=vs.color.red)
vector4=vs.arrow(pos=(0,0,0),axis=(-10,0,0),color=vs.color.red)