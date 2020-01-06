# -*- coding: utf-8 -*-

from __future__ import division
import os, sys

sys.path.insert(0, "%s/Formulas_Nelson" %(os.getcwd()))

from Formulas_Nelson.Formulas import *

a = [2,2,2,2,2]
b = [1,2,2,7,2]
c = [6,1,2,2,2]
v = 3


print media(a)
print desvio(a,media(a))
print X(a,b,c)
print Xred(X(a,b,c),v)