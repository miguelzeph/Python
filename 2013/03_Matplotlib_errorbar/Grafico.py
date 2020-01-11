import matplotlib.pyplot as plt

#Centro

gama = [6.7,6.58,6.8,6.98]
gamaerro = [4.44,4.63,5,4.13]


wo = [520.35,520.4,520,519.3]
woerro = [1.19501046,1.29400541,1.025304833,1.308147545]

t = [10,15,20,30]

ax1 = plt.subplot(111)

plt.errorbar(t, gama,yerr= gamaerro,fmt='bo',label='gama')
plt.ylim(0,10)
plt.ylabel('Gama')
plt.xlabel('tempo')
plt.grid(True)
plt.legend(['gama'],2)
ax2 = plt.twinx()

plt.errorbar(t, wo,yerr= woerro,fmt='ro')
plt.ylim(510,530)
plt.ylabel('wo')
plt.legend(['wo'],1)


plt.xlim(5,35)
plt.show()