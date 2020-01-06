from __future__ import division
from visual import *

t = arange(0, 10, 0.1)
curve( x = sin(t), y = 1.0/(1+t),     z = t**0.5, red = cos(t), green = 0, blue = 0.5*(1-cos(t)) )