from __future__ import division
import numpy as np


teta2 = [27.516,39.156,41.294,44.169,56.685,68.93,62.74,68.96,69.88]
teta = []

for i in range(0,len(teta2)):
	teta.append(((teta2[i]*np.pi/180.00)/2.0))


d = []


arq = open('2_distancia.txt','w')
arq.write("%s	%s	%s	%s\n"%("Pico","2Teta","Teta","d"))
for i in range(0,len(teta)):

	d.append(float(1.54056e-10/(2*np.sin(teta[i]))))
	escrever = "%s	%.2f	%.2f	%.2e\n"%(i+1,teta2[i],teta[i],d[i])
	arq.write(escrever)
arq.close()






	

	



	



