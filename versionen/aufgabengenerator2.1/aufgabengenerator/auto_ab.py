#! /usr/bin/env python

#! /usr/bin/env python

## Author: Pasquale Franz
## Date: 26.01.2015

######
## Generate a table in latex-format with given values
import os


from elements import *
from functions import *
from darstellung import *
from aufgaben import *
from zufall import *



def ab_linglg():
    strFileName="lineare_gleichungen"
    strFileTex=strFileName + ".tex"
    strFilePdf=strFileName + ".pdf"
    datei=open(strFileName + ".tex",'w')
    linglg=list(range(2))
    linglg[0]=erstelleLG_latex("einfach","Z",-10,10,6,3)
    linglg[1]=erstelleLG_latex("einfach","Z",-10,10,6,3)
    aufg=linglg[0]+linglg[1]
    ab=makeSheet(aufg)
    datei.write(ab)
    datei.close()
    os.system('pdflatex ' + strFileTex)
    os.system('evince ' + strFilePdf + '&')    

def ab_quadfunc():
    strFileName="sheet"
    strFileTex=strFileName + ".tex"
    strFilePdf=strFileName + ".pdf"
    datei=open(strFileName + ".tex",'w')
    f=QuadFunc(zufallQ(-5,5),zufallQ(-9,9),zufallZ(-9,9))
    func=math(zeigeFunktion(f))
    aufg=makeExercise(func)
    ab=makeSheet(aufg)
    g=QuadFunc(Rational(1,5),Rational(1,5),Rational(1,5))
    testexpr=latex(g.expr) 
    datei.write(testexpr + "\n")
    datei.write(bruch(testexpr))
    #datei.write(ab)
    datei.close()
    #os.system('pdflatex ' + strFileTex)
    #os.system('evince ' + strFilePdf + '&')    

    



def ab_integral():
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







