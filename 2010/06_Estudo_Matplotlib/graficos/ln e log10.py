import matplotlib.pyplot as plt
import numpy as np
import math
#from math import log = importar somente log da biblioteca math
x=np.arange(0,100000,1)
y=np.log(x)
y1=np.log10(x)


plt.plot(x,y,'r--',x,y1,'b--')
plt.axis([-1000,10000,0,10])
plt.title('Graficos de Ln e Log')
plt.xlabel('valores x')
plt.ylabel('valores y')
plt.show()