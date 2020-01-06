# -*- coding: utf-8 -*-
from __future__ import division
from math import *

import numpy as np
import matplotlib.pyplot as plt

A = [16217,5616,2293,1092,551,371]

t = [0,1,2,3,4,5]
#t = np.arange(0,5,0.1)

des = []

A1 = []


A2 = []


for i in t:
	A1.append(15042*exp(-0.884*i))
	A2.append(14304*exp(-1.185*i) + 1914*exp(-0.348*i))
	
	#print i,A1[i],A2[i],'\n'

#plt.plot(t,A1,'bo')
#plt.plot(t,A2,'ro')

#plt.show()


for i in t:
	
	des.append((A[i])**(1.0/2.0))
	
#print des,'\n'

# Qui-Quadrado

import os, sys

sys.path.insert(0, "%s/Formulas_Nelson" %(os.getcwd()))

from Formulas_Nelson.Formulas import *

X1 = []
X2 = []

X1.append(X(A,A1,des))
X2.append(X(A,A2,des))

print X1 , X2

v1 = 5
v2 = 4

print Xred(X1[0],v1) , Xred(X2[0],v2)

		

	







