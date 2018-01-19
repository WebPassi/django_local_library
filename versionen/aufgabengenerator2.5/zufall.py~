#! /usr/bin/env python

#! /usr/bin/env python

## Author: Pasquale Franz
## Date: 26.01.2015

######
## Generate a table in latex-format with given values

import os
import random


from sympy.abc import *
from sympy import *
from elements import *
from functions import *

def zufallN(n):
    return random.randint(1,n)

def zufallZ(a,b):
    return random.randint(a,b)

### No 0, take instead 1
def zufallZ0(a,b):
    zahl=random.randint(a,b)
    if zahl == 0:
        zahl=1
    return zahl

def zufallQ(a,b):
    z=zufallZ(a,b)
    n=zufallZ0(a,b)
    return Rational(z,n)

def zufallQ0(a,b):
    z=zufallZ0(a,b)
    n=zufallZ0(a,b)
    return Rational(z,n)
    










