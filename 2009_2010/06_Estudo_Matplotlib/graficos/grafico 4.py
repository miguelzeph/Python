import matplotlib.pyplot as plt
import numpy as np

t=np.arange(-5.0,5.0,0.2)
plt.plot(t,t**3,'r-',t,t**2,'bs',t,t*10,'g')
plt.show()
