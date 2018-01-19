#! /usr/bin/env python

## Author: Pasquale Franz
## Date: 26.01.2015

######
## Generate a table in latex-format with given values

from sympy.abc import *
from sympy import *
from skelet import Skelet
from elements import *
from functions import *
import os
import random

strFileName="sheet"
strFileTex=strFileName + ".tex"
strFilePdf=strFileName + ".pdf"
file=open(strFileName + ".tex",'w')

def zeichnen(function):
    function.graph_zeichnen()

def anz(function):
    function.anzeigen()

def tab(function):
    function.wertetabelle([-3,-2,-1,0,1,2,3])

#func=LinFunc(1,2)
e=Skelet()
multi=Multicol()
file.write(e.head())
#file.write(t.centered([1,2],[2,4]))
#file.write(func.wertetabelle([1,2]))
#file.write(func.graph_zeichnen())

func=range(2)
for i in func:
    func[i]=LinFunc(1,2)
s=func[0].anzeigen() + func[0].wertetabelle(range(-3,4))
#aufg=func[0].anzeigen()
gra=[s,s,s,s]
file.write(multi.col(gra,2))
file.write(e.end())
file.close()
os.system('pdflatex ' + strFileTex)
os.system('evince ' + strFilePdf + '&')





