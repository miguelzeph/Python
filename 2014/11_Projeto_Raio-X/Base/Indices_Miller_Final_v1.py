from __future__ import division
import numpy as np
import xlwt

valores = [3,4,8,11,12]
						
planos = {}
for i in range(0,len(valores)):
	planos[i]=[]
	for l in range(0,4):
		
		for k in range(0,4):
			
			for h in range(0,4):
			#Mudei a ordem do loop h,k,l para deixar os valores hkl crescentes
			
				hkl= h**2+k**2+l**2
				
				if hkl == valores[i]:
					planos[i].extend(["(%.0f,%.0f,%.0f)"%(h,k,l)])
					
for i in range(0,len(valores)):
	print planos[i][0]
					
				



	

	



	



