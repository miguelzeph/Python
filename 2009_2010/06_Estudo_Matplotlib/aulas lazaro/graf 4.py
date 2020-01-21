import numpy as np
import matplotlib.pyplot as plt

mu =100
sigma =15

x = mu + sigma*np.random.randn(1000)

#calcula o histograma dos dados

n,bins,patches = plt.hist(x,50,normed=1, facecolor='g', alpha=0.75)

plt.xlabel('frequencia')
plt.ylabel('probabilidades')
plt.title('histograma de IQ')

plt.text(60,0.025,r'$\mu=100,\\sigma=15$')
plt.axis([40,160,0,0.03])
plt.grid(True)

plt.show()
