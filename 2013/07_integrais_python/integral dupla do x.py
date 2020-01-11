import scipy.integrate as si

func = lambda x,y: x
x1,x2 = 0,1
x3,x4 = lambda x: 0, lambda x: 1
I = si.dblquad(func,x1,x2,x3,x4)
print I
raw_input()

# tem q dar 0,25 ... veja q e ma integral simples.
