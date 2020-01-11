from pylab import *

x,y = ogrid[-5:5:0.01,-5:5:0.01]

X = np.arange(-1.9, 1.9, 0.1)
Y = np.arange(-1.9, 1.9, 0.1)
X, Y = np.meshgrid(X, Y)

z = (1+4*np.cos(np.sqrt(3)*X*2.456/2.0)*np.cos(Y*2.456/2.0)+4*(np.cos(Y*2.456/2.0))**2)**(1.0/2.0)

ext = [-1,1,-1,1]

imshow(z,origin = 'lower')
contour(z, origin = 'lower')

xlabel('x')
ylabel('y')
title('TESTE')
#savefig('graf.png')
show()