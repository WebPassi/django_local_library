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

def meinTest():
    strFileName="sheet"
    strFileTex=strFileName + ".tex"
    strFilePdf=strFileName + ".pdf"
    datei=open(strFileName + ".tex",'w')
    func=range(2)
    func1=polynom(1)
    func2=polynom(2)
    multi=multicol([func1.randIntegral(),func2.randIntegral()],2)
    aufg=makeExercise(multi)
    sheet=makeSheet(aufg)
    datei.write(sheet)
    datei.close()
    os.system('pdflatex ' + strFileTex)
    os.system('evince ' + strFilePdf + '&')







