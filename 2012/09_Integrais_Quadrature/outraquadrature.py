from scipy import integrate
import numpy as np
def myfunc(y,x,z):
	return np.log(np.exp(y**2)*y-x+z)/np.sin(y**2)
 
# These are the arguments that will be passed as a and b to myfunc()
args = (0,0)
 
# Integrate myfunc() from 0.5 to 1.5
results = integrate.quadrature(myfunc, 0, 1, args)
print 'Integral = ', results[0], ' with error = ', results[1]