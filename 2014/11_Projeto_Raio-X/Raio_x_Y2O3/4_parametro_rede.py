from __future__ import division


d = [3.24e-10,2.30e-10,2.18e-10,2.05e-10,1.62e-10,1.36e-10,1.48e-10,1.36e-10,1.34e-10]
hkl= [(3,1,0),(4,2,0),(3,3,2),(5,0,0),(6,2,0),(7,2,2),(4,4,4),(7,2,2),(7,3,0)]
a=[]

for i in range(0,len(d)):
	a.append(d[i]*((hkl[i][0]**2 + hkl[i][1]**2 + hkl[i][2]*2)**(1.0/2.0)))




arq = open('4_parametro_rede.txt','w')
arq.write("%s\n"%("a"))
for i in range(0,len(d)):

	escrever = "%.2e\n"%(a[i])
	arq.write(escrever)
escrever = "\n\n\n%.2e\n"%((sum(a)/(len(a))))
arq.write(escrever)
arq.close()








	

	



	



