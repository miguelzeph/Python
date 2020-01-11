from __future__ import division
import numpy as np


teta2 = [20.50,29.16,33.75,35.91,39.83,43.49,48.51,53.18,56.18,57.64,59.04,60.43]
teta = []
teta_angulo =[]

for i in range(0,len(teta2)):
	teta.append(((teta2[i]*np.pi/180.00)/2.0))
	teta_angulo.append(teta2[i]/2)


d = []


arq = open('2_distancia.txt','w')
arq.write("%s	%s	%s	%s\n"%("Pico","2Teta","Teta","d"))
for i in range(0,len(teta)):

	d.append(float(1.54056e-10/(2*np.sin(teta[i]))))
	escrever = "%s	%.2f	%.2f	%.2e\n"%(i+1,teta2[i],teta_angulo[i],d[i])
	arq.write(escrever)
arq.close()






	

	



	



