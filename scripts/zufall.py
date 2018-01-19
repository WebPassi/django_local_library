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
    
### Aus einer gegebenen Liste eine Zufallsliste erzeugen.
def zufallsliste(liste):
    zl=list(range(len(liste)))
    indexd=len(liste)-1
    indexu=0
    for i in zl:
        if indexd == 0:
            zl[indexu]=liste.pop(0)
        else:
            zz=random.randint(0,indexd)
            zl[indexu]=liste.pop(zz)
        indexu+=1
        indexd=indexd-1
    return zl

### Gibt eine Liste von Zufallszahlen mit vorgegebener Laenge und Zahlenbereich zurueck.
def listZufallszahlen(length,bereich="n"):
    zz=[]
    for i in range(length):
        if bereich=="n":
            zz.append(zufallN(500))
    return zz

def listZufallszahlenN(length,og):
    zz=[]
    for i in range(length):
        zz.append(zufallN(og))
    return zz

def listZufallszahlenZ(length,ug,og):
    zz=[]
    for i in range(length):
        zz.append(zufallZ0(ug,og))
    return zz

def listZufallseinheiten(length):
    einheiten=["g","mg","kg","t","m","mm","cm","dm","km"]
    ze=[]
    for i in range(length):
        ze.append("g")
    return ze
    








