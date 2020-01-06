from __future__ import division
#import math
from math import *
import numpy as np

	
Q = np.arange(0,501)

#Valor inicial---
F1=[0.5]*500
#----------------

F2=[]

for i in range(1,len(F1)):
		
		
	F = (log(2))/(log(2*cosh(log(2)/F1[i]*(Q[i]-1)/(Q[i]+1))))
		
	a = "%1.3f"%(F)
		
	F2.append(a)

print"       F2        F1"
for i in range (0,len(F2)):
	
	print  "%3.0f"%(i),"__",F2[i],"___",F1[i]
	raw_input()
#------------func que readd---------------------
#F1=[]
#for i in range(0,len(F2)):
		
	#F1.append(F2[i])
#for i in range (0,len(F2)):
		
	#print  "%3.0f"%(i),"__",F2[i],"___",F1[i]
	#raw_input()
#-----------------------------------------------
	
