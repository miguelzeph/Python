import numpy as np
import matplotlib.pyplot as plt
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)
t1= np.arange(0.0,10.0,0.00001)
t2= np.arange(0.0,10.0,0.00002)
t3= np.arange(0.0,10.0,0.1)

plt.figure(1)
plt.subplot(211)
plt.plot(t1,f(t1),"bo",t2,f(t2),'k')

plt.subplot(212)
plt.plot(t2,np.cos(2*np.pi*t2),'r--')


plt.plot(t3,np.sin(np.pi*t3),'k')

plt.show()  
