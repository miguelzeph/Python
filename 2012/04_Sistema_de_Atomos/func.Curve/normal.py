from __future__ import division
from visual import *



spiral = curve( color = color.cyan )
for t in arange(0, 2*pi, 0.1):
    spiral.append( pos=(t,sin(t),cos(t)) )