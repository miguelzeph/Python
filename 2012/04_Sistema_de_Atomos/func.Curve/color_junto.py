from __future__ import division
from visual import *

c= curve( pos=[(-1,0,0)], color=color.blue,radius=1)
c.append( pos=(0,0,0) ) # add a blue point (optional)
c.append( pos=(0,0,0), color=color.orange) # same point
c.append( pos=(1,0,0) ) # add orange point