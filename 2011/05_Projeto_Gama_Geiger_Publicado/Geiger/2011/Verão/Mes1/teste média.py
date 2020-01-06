# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import os



y=[3,10,3,2,0.5,7,4]

x=np.arange(0,len(y))

print sum(y)
print len(y)
print (sum(y)/len(y))



media=[(sum(y)/len(y))]*(len(y))
media=str(media[0])
media=media[0][0:1]
print (float(media))
media=[float(media)]*(len(y))
plt.plot(x,media)

plt.show()
