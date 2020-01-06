import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img=mpimg.imread('./stinkbug.png')
imgplot = plt.imshow(img)



plt.plot([1,2,3,4],[1,4,9,16])
plt.axis([0,600,0,400])
plt.show()
