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
            glg=Eq(f1.expr,f2.expr)
            return glg
        elif form=="rechts0":
            f1=LinFunc(zufallZ0(ug,og),zufallZ0(ug,og))
            f2=LinFunc(0,0)
            glg=Eq(f1.expr,f2.expr)
            return glg
        elif form=="rechtsZahl":
            f1=LinFunc(zufallZ0(ug,og),zufallZ0(ug,og))
            f2=LinFunc(0,zufallZ0(ug,og))
            glg=Eq(f1.expr,f2.expr)
            return glg
        elif form=="linksundrechts": 
            f1=LinFunc(zufallZ0(ug,og),zufallZ0(ug,og))
            f2=LinFunc(zufallZ0(ug,og),zufallZ0(ug,og))
            glg=Eq(f1.expr,f2.expr)
            return glg



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










