from __future__ import division
#import math
from math import *
import numpy as np

V1=[0.5]*501
V2=[]

def tentativa(F1,F2):	
	Q = np.arange(1,502)

	#Valor inicial---
	
	#----------------

	F2=[]

	for i in range(0,len(F1)):
			
			
		F = (log(2))/(log(2*cosh(log(2)/F1[i]*(Q[i]-1)/(Q[i]+1))))
			
		a = "%1.4f"%(F)
			
		F2.append(float(a))
		
		#tive que colocar para ele add no vetor fora da func
		V2.append(float(a))

	#print"       F2        F1"
	#for i in range (0,len(F2)):
		
		#print  "%3.0f"%(i),"__",F2[i],"___",F1[i]
		#raw_input()
	return F2
		
tentativa(V1,V2)

k=1

while 1==1:
	
	#print"       F1        F2"
	
	#for i in range (0,len(V2)):
		
	#	print  "%3.0f"%(i),"__",V1[i],"___",V2[i]
		#raw_input()
		
	if V1==V2:
		print 'numero de tentativas =',k
		raw_input()
		
		for i in range(0,len(V2)):
			print  "%3.0f"%(i),"__","%3.4f"%(V1[i]),"___","%3.4f"%(V2[i])
			raw_input()
		
			
		
		break
		
	
	V1=V2
	V2=[]
	tentativa(V1,V2)
			
	#print 'tentativa',k
	
	k=k+1
	
	#raw_input()

	
