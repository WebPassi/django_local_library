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
import random

def ab_terme():
    strFileName="terme"
    strFileTex=strFileName + ".tex"
    strFilePdf=strFileName + ".pdf"
    datei=open(strFileName + ".tex",'w')
    terme=list(range(3))
    terme[0]=3*x
    terme[1]=-5*x
    terme[2]=8*x
    term=Term(terme)
#    aufg=makeSheet(makeExercise(latex(term.test()[2])))
    aufg=makeSheet(makeExercise(term.zeigeAusdruck()))
    datei.write(aufg)
    datei.close()
    os.system('pdflatex ' + strFileTex)
    os.system('evince ' + strFilePdf + '&')    


def ab_linglg():
    strFileName="lineare_gleichungen"
    strFileTex=strFileName + ".tex"
    strFilePdf=strFileName + ".pdf"
    datei=open(strFileName + ".tex",'w')
    
    anzahl_aufgaben=6
    anzahl_menge=9
    glgsymp = [[0 for spalte in range(anzahl_menge)] for zeile in range(anzahl_aufgaben)]
    glg = [[0 for spalte in range(anzahl_menge)] for zeile in range(anzahl_aufgaben)]
    lsg = [[0 for spalte in range(anzahl_menge)] for zeile in range(anzahl_aufgaben)]
    aufg = range(anzahl_aufgaben)
    ### Einfache lineare Gleichungen
    for i in range(anzahl_menge):
        linterm1=LinTerm(zufallZ0(-10,10),0)
        linterm2=LinTerm(0,zufallZ0(-10,10))
        glgsymp[0][i]=Equation(linterm1,linterm2)
        glg[0][i]=Equation(linterm1,linterm2).zeigeGlg()
        lsg[0][i]=glgsymp[0][i].zeigeLsg()
    multi=multicol(glg[0],3)    
    aufg[0]=makeExercise(multi)

    ### Rechts 0
    for i in range(anzahl_menge):
        linterm1=LinTerm(zufallZ0(-10,10),zufallZ(-10,10))
        linterm2=LinTerm(0,0)
        glgsymp[1][i]=Equation(linterm1,linterm2)
        glg[1][i]=Equation(linterm1,linterm2).zeigeGlg()
        lsg[1][i]=glgsymp[1][i].zeigeLsg()
    multi=multicol(glg[1],3)    
    aufg[1]=makeExercise(multi)

    ### Rechts Zahl
    for i in range(anzahl_menge):
        linterm1=LinTerm(zufallZ0(-10,10),zufallZ(-10,10))
        linterm2=LinTerm(0,zufallZ(-10,10))
        glgsymp[2][i]=Equation(linterm1,linterm2)
        glg[2][i]=Equation(linterm1,linterm2).zeigeGlg()
        lsg[2][i]=glgsymp[2][i].zeigeLsg()
    multi=multicol(glg[2],3)    
    aufg[2]=makeExercise(multi)

    ### Links Rechts
    for i in range(anzahl_menge):
        linterm1=LinTerm(zufallZ0(-10,10),zufallZ(-10,10))
        linterm2=LinTerm(zufallZ0(-10,10),zufallZ(-10,10))
        glgsymp[3][i]=Equation(linterm1,linterm2)
        glg[3][i]=Equation(linterm1,linterm2).zeigeGlg()
        lsg[3][i]=glgsymp[3][i].zeigeLsg()
    multi=multicol(glg[3],3)    
    aufg[3]=makeExercise(multi)

    ### Klammern links, Zahl rechts
    for i in range(anzahl_menge):
        linterm1=LinTerm(zufallZ0(-10,10),zufallZ(-10,10),zufallZ0(-10,10))
        linterm2=LinTerm(0, zufallZ(-10,10))
        glgsymp[4][i]=Equation(linterm1,linterm2)
        glg[4][i]=Equation(linterm1,linterm2).zeigeGlg()
        lsg[4][i]=glgsymp[4][i].zeigeLsg()
    multi=multicol(glg[4],3)    
    aufg[4]=makeExercise(multi)

    ### Klammern links, Klammer rechts
    for i in range(anzahl_menge):
        linterm1=LinTerm(zufallZ0(-10,10),zufallZ(-10,10),zufallZ0(-10,10))
        linterm2=LinTerm(zufallZ0(-10,10),zufallZ(-10,10),zufallZ0(-10,10))
        glgsymp[5][i]=Equation(linterm1,linterm2)
        glg[5][i]=Equation(linterm1,linterm2).zeigeGlg()
        lsg[5][i]=glgsymp[5][i].zeigeLsg()
    multi=multicol(glg[5],2)    
    aufg[5]=makeExercise(multi)

    
    ### Aufgabe zusammenstellen
    aufgaben=""
    for a in aufg:
        aufgaben+=a

    ### Loesungen
    loes=range(54)
    strloes=""
    index=0
    for i in range(6):
        for j in lsg[i]:
            loes[index]=j
            strloes+=scriptstyle(latex(loes[index])) + " , "
            index+=1    
    ### Loesungen zufall
    zufloes=zufallsliste(loes)
    strzufloes=""
    for i in zufloes:
        strzufloes+=scriptstyle(latex(i)) + " , "
    ab=makeSheet(aufgaben + strzufloes + "\\\\[0.2em] \n" + strloes)
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







