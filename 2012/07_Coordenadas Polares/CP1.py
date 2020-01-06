
from pylab import *
r = arange(0, 10, 0.01)
o = cos(r)
polar(o, r, color='r', lw=2)
title('Grafico em Coordenadas Polares')
show()