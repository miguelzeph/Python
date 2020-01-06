# -*- coding: cp1252 -*-

from visual import *

mola = helix(pos=(0,0,0), axis=(0,1,0), radius=0.5,coils=6,thickness=0.1,color=color.red)

k=0
dk=0.1
while True:

	k = k+dk
	rate (10)
	mola.axis =mola.axis + (0,k,0)
	
	if abs(k) >= 2:
		k=-1