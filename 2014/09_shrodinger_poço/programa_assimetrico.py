from __future__ import division
import matplotlib.pyplot as plt
import numpy as np

V0=1 # altura da barreira 
V1=1

a=1 #poco
m = 1#9e-31 #massa e
h = 1#6e-34 #constante planck

E = np.arange(0,50,np.pi/100) #Energia
k = np.sqrt(2*m*E)/h

ka =k*a

alfa = np.sqrt(2*m*(V1-E))/h


y1 = ((k/alfa)*np.sin(ka)-np.cos(ka))/(np.sin(ka)+(k/alfa)*np.cos(ka))
#y1 = ((k/alfa)-(1/np.tan(ka)))/(1+(k/alfa)*(1/np.tan(ka)))
#y1 = -(-(k/alfa)*np.sin(ka)+np.cos(ka))/(np.sin(ka)+(k/alfa)*np.cos(ka))
y2 = np.sqrt(V0/E-1)




plt.plot(ka,y2,'b.',E,y2)


plt.xlim(0,5)
plt.ylim(0,5)

plt.show()
