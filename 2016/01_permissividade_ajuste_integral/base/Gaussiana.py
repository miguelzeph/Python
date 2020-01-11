import matplotlib.pyplot as plt
import numpy as np

dados = [2,2,4,5,5,5,5,5,5,7,8,9,9]

xm = np.mean(dados)
dp = np.std(dados)

x = np.arange(0,10,0.1)
y = 1/(dp*np.sqrt(2*np.pi))*np.exp((-1/2)*((x-xm)/dp)**2)

plt.plot(x,y)

plt.grid(True)
print dp
plt.show()
