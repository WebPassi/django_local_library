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
from zufall import *
import os
import random

def loeseGlg(term1,term2):
    glg=Eq(term1,term2)
    lsg=solve(glg,x)
    return lsg


def berechneNullstelle(funktion):
    return funktion.nullstelle()


def erstelleLG(form,zahlenbereich,ug,og):
    if zahlenbereich=="Z":
        if form=="einfach":
            f1=LinFunc(zufallZ0(ug,og),0)
            f2=LinFunc(0,zufallZ(ug,og))
            glg=Equation(f1.expr,f2.expr)
            return glg.zeigeGlg()
        elif form=="rechts0":
            f1=LinFunc(zufallZ0(ug,og),zufallZ0(ug,og))
            f2=LinFunc(0,0)
            glg=Equation(f1.expr,f2.expr)
            return glg.zeigeGlg()
        elif form=="rechtsZahl":
            f1=LinFunc(zufallZ0(ug,og),zufallZ0(ug,og))
            f2=LinFunc(0,zufallZ0(ug,og))
            glg=Equation(f1.expr,f2.expr)
            return glg.zeigeGlg()
        elif form=="linksundrechts": 
            f1=LinFunc(zufallZ0(ug,og),zufallZ0(ug,og))
            f2=LinFunc(zufallZ0(ug,og),zufallZ0(ug,og))
            glg=Equation(f1.expr,f2.expr)
            return glg.zeigeGlg()



def erstelleLG_latex(form,zahlenbereich,ug,og,anzahl=1,spalten=1):
    if anzahl==1:
        latexstr=math(latex(erstelleLG(form,zahlenbereich,ug,og)))
        aufg=makeExercise(latexstr)
        return aufg
    else:
        straufg=list(range(anzahl))
        for index in range(anzahl):
            straufg[index]=math(latex(erstelleLG(form,zahlenbereich,ug,og)))
        multi=multicol(straufg,spalten)
        aufg=makeExercise(multi)
        return aufg

def aufgWertetabelleGraph(funktion):
    aufg="Erstelle f\\\"ur die Funktion " + funktion.anzeigen() + " eine Wertetabelle und zeichne den dazugeh\\\"origen Graphen im Bereich von $x=-3$ bis $x=3$ in ein Koordinatensystem."
    return aufg


def aufgParabeleigenschaften(funktionsliste):
    aufg="Gib f\\\"ur die folgenden Parabeln den Scheitelpunkt, die Symmetrieachse, sowie die Nullstellen an. \n"
    graph=zeichneGraph(funktionsliste)
    return aufg+graph









