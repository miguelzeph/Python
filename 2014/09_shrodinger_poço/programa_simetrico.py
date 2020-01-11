from __future__ import division
import matplotlib.pyplot as plt
import numpy as np

V1=1 # altura da barreira
V2=2
V3=3
V4=4
V5=5
a=1 #poco
m = 1#9e-31 #massa e
h = 1#6e-34 #constante planck

E = np.arange(0,50,0.01) #Energia
k = np.sqrt(2*m*E)/h


ka =k*a

y1 = np.tan(ka)

y2 = -1.0/np.tan(ka)

y3 = np.sqrt(V1/E-1)
y4 = np.sqrt(V2/E-1)
y5 = np.sqrt(V3/E-1)
y6 = np.sqrt(V4/E-1)
y7 = np.sqrt(V5/E-1)

plt.plot(ka,y1,'b.',ka,y2,'r.',E,y3,E,y4,E,y5,E,y6,E,y7)
plt.xlim(0,5)
plt.ylim(0,5)

plt.show()
