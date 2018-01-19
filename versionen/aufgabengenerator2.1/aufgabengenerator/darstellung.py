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
import re

def zerlegung(expr):
    sum=expr.split(r"[+,-]")
    return sum
    

def bruch(expr):
    summanden=re.split(r"[+-]",expr)
    myexpr=expr
    xterm=range(len(summanden))
    zfaktor=range(len(summanden))
    nfaktor=range(len(summanden))
    newsummand=range(len(summanden))
    oldsummand=range(len(summanden))
    for index,summand in enumerate(summanden):
        oldsummand[index]=summand
        summand=re.sub(r'{x',r'{1 x',summand)
        try:
            z=re.search(r"\\frac{[^}]*}",summand)
            n=re.search(r"}{.*",summand)
            try:
                xterm[index]="x" + re.split(r' x', str(z.group(0)))[1]
            except:
                xterm[index]=""
            xterm[index]=re.sub(r'x}',r'x',xterm[index])
            zfaktor[index]=re.split(r'[{ }]', str(z.group(0)))[1]
            nfaktor[index]=re.split(r'[{}]', str(n.group(0)))[2]
            newsummand[index]="\\frac{" + latex(zfaktor[index]) + "}{" + latex(nfaktor[index]) + "}" + latex(xterm[index])
        except:
            newsummand[index]=summand
        oldexpr=oldsummand[index]
        oldexpr=re.sub(r'\\',r'\\\\',oldexpr)
        oldexpr=re.sub(r'\^',r'\\^',oldexpr)
        oldexpr=re.sub(r'\{',r'\\{',oldexpr)
        oldexpr=re.sub(r'\}',r'\\}',oldexpr)
        newexpr=newsummand[index]
        newexpr=re.sub(r'\\',r'\\\\',newexpr)
        myexpr=re.sub(oldexpr,newexpr,myexpr)
    return myexpr


def no0(zahl):
    if zahl == 0:
        return ""
    else:
        return latex(zahl)

def no1(zahl):
    if zahl == 1:
        return ""
    elif zahl == -1:
        return "-"
    else:
        return latex(zahl)


def zeigeFunktion(funktion):
    #dars=funktion.name + "(" + funktion.variable + ")=" + funktion.normalform()
    dars=latex(separate(funktion.expr))
    return dars













