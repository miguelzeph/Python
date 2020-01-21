import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
img =mpimg.imread('./stinkbug.png') 
LUZ=img[:,:,0]
imgplot =plt.imshow(LUZ)
imgplot.set_cmap("spectral")
plt.colorbar()
plt.show()