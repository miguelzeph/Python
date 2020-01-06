# -*- coding: utf-8 -*-
from __future__ import division
from math import *

import numpy as np
import matplotlib.pyplot as plt

A = [16217,5616,2293,1029,551,371]

t = [0,1,2,3,4,5]
t1 = np.arange(0,5,0.1)

des = []

A1 = []
A11 = []


A2 = []
A22 = []


for i in t:
	A1.append(15042*exp(-0.884*i))
	A2.append(14304*exp(-1.185*i) + 1914*exp(-0.348*i))
for i in t1:
	A11.append(15042*exp(-0.884*i))
	A22.append(14304*exp(-1.185*i) + 1914*exp(-0.348*i))
	
	
plt.plot(t,A,'go')
plt.plot(t,A1,'b.',t1,A11,'b--')
plt.plot(t,A2,'r.',t1,A22,'r--')

plt.show()


		

	







