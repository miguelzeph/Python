# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


arquivo=open('./dados.txt','r')
ler=arquivo.readlines()
arquivo.close()


x=[]
#x1=np.arange(0,len(ler)+1)
#print x1
#print len(ler)
#print len(x)
#y=np.sin(x)
y=x #somente assim pra não dar erro, não entendi por que dava erro com sin
for i in range(0,len(ler)):
	
	x.append(float(ler[i][3:9]))
	
	
plt.plot(x,y,'r--')



plt.show()