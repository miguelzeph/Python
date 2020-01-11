import scipy.integrate as si

func = lambda x,y: x*y
x1,x2 = 0,1
y1,y2 = lambda x: 0, lambda x: 1
I = si.dblquad(func,x1,x2,y1,y2)
print I
raw_input()

# tem q dar 0,25 ... veja q e ma integral simples.

# integral(0,1) x.dx vezes integral(0,1) y.dy ... resulta em 1/4