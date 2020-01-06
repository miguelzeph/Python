# -*- coding: utf-8 -*-

import os, sys

sys.path.insert(0, "%s/libs" %(os.getcwd()))

from libs.mylib import *

#import mylib.fatorial ..... as ....
#from mylib import fatorial .... 

n=int(raw_input("Informe o numero: "))

f=fatorial(n)

if f != None:
	print "O fatorial de %d é %d." %(n, fatorial(n))
else:
	print "Não existe fatorial de %d" %(n)

print "O quadrado de %d é %d." %(n, quadrado(n))
