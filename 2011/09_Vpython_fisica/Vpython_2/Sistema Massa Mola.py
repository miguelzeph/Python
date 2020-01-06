#from visual import *
import visual as vs

#objetos
floor=vs.box(lenght=5,width=1,height=0.1,color=vs.color.green)
wall=vs.box(pos=vs.vector(-floor.height/2,0.5+floor.height/2,0),lenght=0.1,width=1,height=0.1,color=vs.color.green)
spring =vs.helix