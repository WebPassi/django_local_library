#! /usr/bin/env python

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



func=range(2)
#for i in func:
#    func[i]=LinFunc(1,2)
#s=func[0].anzeigen() + func[0].wertetabelle(range(-3,4))
#aufg=func[0].anzeigen()
func[0]=Function(x**3)
func[1]=Function(x**7-2*x**3)

integAufg=multicol([func[0].integral(1,3),func[1].integral(-2,2)],2)

#func=Function(x**3)

#name=func.anzeigen()
#integ=func.integral(2,5)
#wertetab=func.wertetabelle([-2,-1,0,1,2])
#wertetab=func.wertetabelle()
#graph=func.graph_zeichnen()

aufg=makeExercise(integAufg)
sheet=makeSheet(aufg)

datei.write(sheet)

datei.close()
os.system('pdflatex ' + strFileTex)
os.system('evince ' + strFilePdf + '&')







