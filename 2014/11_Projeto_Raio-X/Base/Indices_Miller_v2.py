from __future__ import division
import numpy as np
import xlwt

valores = [3,4,8,11,12]

def hkl(h,k,l):
			
	hkl= h**2+k**2+l**2
					
	if hkl == valores[i]:
		print "(%.0f,%.0f,%.0f)"%(h,k,l)
		
		
						


for i in range(0,len(valores)):
	for h in range(0,4):
		hkl= h**2
					
		if hkl == valores[i]:
			print "(%.0f,%.0f,%.0f)"%(h,0,0)
			break
		
		
		for k in range(0,4):
			hkl = h**2+k**2
			
			if hkl == valores[i]:
				print "(%.0f,%.0f,%.0f)"%(h,k,0)
				break
			
			for l in range(0,4):
			
				hkl= h**2+k**2+l**2
				
				if hkl == valores[i]:
					print "(%.0f,%.0f,%.0f)"%(h,k,l)
					break
				


	

	



	



