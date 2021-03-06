#! /usr/bin/env python

## Author: Pasquale Franz
## Date: 26.01.2015

######
## Generate a table in latex-format with given values

from sympy.abc import *
from sympy import *
from elements import *
from functions import *
import os
import random

strFileName="sheet"
strFileTex=strFileName + ".tex"
strFilePdf=strFileName + ".pdf"
datei=open(strFileName + ".tex",'w')


#func=range(2)
#for i in func:
#    func[i]=LinFunc(1,2)
#s=func[0].anzeigen() + func[0].wertetabelle(range(-3,4))
#aufg=func[0].anzeigen()

func=LinFunc(3,-1)

name=func.anzeigen()
#wertetab=func.wertetabelle([-2,-1,0,1,2])
wertetab=func.wertetabelle()
graph=func.graph_zeichnen()

aufg=makeExercise(name+wertetab+graph)
sheet=makeSheet(aufg)

datei.write(sheet)

datei.close()
os.system('pdflatex ' + strFileTex)
os.system('evince ' + strFilePdf + '&')





