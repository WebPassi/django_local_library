#! /usr/bin/env python

#! /usr/bin/env python

## Author: Pasquale Franz
## Date: 26.01.2015

######
## Generate a table in latex-format with given values

import os
#from mpmath import *
from sympy import *
from sympy.abc import *
#from sympy.mpmath import *
import mpmath

### Strings in expressions umwandeln

from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application


from fractions import Fraction
from decimal import Decimal


from elements import *
from functions import *
from zufall import *

### lsg: c=CAS, a=all (mit Rechenweg), s=short, p=pure (nur der Zahlenwert) 


transformations = (standard_transformations + (implicit_multiplication_application,))




##### Output:array mit [aufgabe,loesung,komplett] 
##### Input:
### term : regular term expression as string
def aufg_term_fix(term):
    term=str(term)
    ausdruck_latex=my_latex(term)

    ausdruck=parse_expr(term,transformations=transformations)
    

    loesung=ausdruck.expand()

    loesung_latex=latex(loesung)
 
    komplett = ausdruck_latex + " = " + loesung_latex 

    return [math(ausdruck_latex + "="),math(loesung_latex),math(komplett)]


##### Output:array mit [aufgabe,loesung,komplett] 
##### Input:
### variable : Variablennamen als LISTE
### art : ganz(ganze Zahlen)
### runden : Nachkommastellen bei Dezimalzahlen
### intervall : Zahlenbereich des Zufallsgenerators
### laenge :Anzahl der Auftreten der Variablen
def aufg_terme_addieren(variablen=['x'],art="ganz",runden=2,intervall=[2,7],laenge=2,aufgabentext="Fasse so weit wie möglich zusammen.",anzahl=1,spalten=1):
    
    aufgaben=[]
    aufgaben_lsg=[]
    aufgaben_lsg_skizze=[]
    for anz in list(range(anzahl)):
        ### zufaellige Werte vor den Variablen schreiben und Ausdruck generieren
        ausdruck=""
        for i in list(range(laenge)):
            var=random.choice(variablen)
        
            ### Zahlenbereiche
            if art == "ganz":
                par=random.randint(intervall[0],intervall[1])

            elif art == "dezimal":
                par=round(random.uniform(intervall[0],intervall[1]),runden)
            
            ### Negatives Vorzeichen: Klammer setzen
            if par < 0:
                ausdruck += "(" + str(par) + var + ")"
            else:
                ausdruck += str(par) + var

            if i < laenge-1:
                op=random.choice(['+','-'])
                ausdruck += op


        loesung=parse_expr(ausdruck,transformations=transformations)

        loesung_latex=latex(loesung)

        komplett = ausdruck + " = " + loesung_latex 


        aufgaben.append(math(ausdruck) + "=")
        aufgaben_lsg.append(math(loesung_latex))
        aufgaben_lsg_skizze.append(math(komplett))

    return [makeExercise(multicol(aufgaben,spalten),aufgabentext=aufgabentext),makeExercise(multicol(aufgaben_lsg,spalten),aufgabentext=aufgabentext),makeExercise(multicol(aufgaben_lsg_skizze,spalten),aufgabentext=aufgabentext)]



##### Output:array mit [aufgabe,loesung,komplett] 
##### Input:
### eins, zwei, drei : [Symbolname,art,intervall]
### art : ganz(ganze Zahlen)
### intervall : Zahlenbereich des Zufallsgenerators
### position : Position der Klammer (vorne, hinten)
### runden : Nachkommastellen bei Dezimalzahlen
### ax(by+cz) oder (ax+by)*cz
def aufg_eine_klammer(eins,zwei,drei,position="hinten",runden="2"):

    try:
        ug=eins[2][0]
        og=eins[2][1]
    except:
        ug=2
        og=7

    try:
        if eins[1] == "ganz":
            a=random.randint(ug,og)
        elif eins[1] == "dezimal":
            a=round(random.uniform(ug,og,runden))
        else:
            a=random.randint(ug,og)
    except:
            a=random.randint(ug,og)

            
    try:
        ug=zwei[2][0]
        og=zwei[2][1]
    except:
        ug=2
        og=7


    try:
        if zwei[1] == "ganz":
            b=random.randint(ug,og)
        elif zwei[1] == "dezimal":
            b=round(random.uniform(ug,og,runden))
        else:
            b=random.randint(ug,og)
    except:
            b=random.randint(ug,og)


    try:
        ug=drei[2][0]
        og=drei[2][1]
    except:
        ug=2
        og=7

    try:
        if drei[1] == "ganz":
            c=random.randint(ug,og)
        elif drei[1] == "dezimal":
            c=round(random.uniform(ug,og,runden))
        else:
            c=random.randint(ug,og)
    except:
            c=random.randint(ug,og)



    x=eins[0]
    y=zwei[0]
    z=drei[0]

    op=random.choice(['+','-'])

    
    if position == "hinten":
        ausdruck=str(a) + x + "*" +  "(" + str(b) + y + op + str(c) + z + ")"
    elif position == "vorne":
        ausdruck="(" + str(a) + x + op + str(b) + y + ")" + "*" + str(c) + z


    loesung=parse_expr(ausdruck,transformations=transformations).expand()

    loesung_latex=latex(loesung)

    ausdruck=ausdruck.replace('*','\\cdot')

    komplett = ausdruck + " = " + loesung_latex 


    return [math(ausdruck) + "=",math(loesung_latex),math(komplett)]




##### Output:array mit [aufgabe,loesung,komplett] 
##### Input:
### eins, zwei, drei : [Symbolname,art,intervall]
### art : ganz(ganze Zahlen)
### intervall : Zahlenbereich des Zufallsgenerators
### position : Position der Klammer (vorne, hinten)
### runden : Nachkommastellen bei Dezimalzahlen
### (ax+by)(cz+dz1)
def aufg_zwei_klammern(eins,zwei,drei,vier,runden="2"):

    try:
        ug=eins[2][0]
        og=eins[2][1]
    except:
        ug=2
        og=7

    try:
        if eins[1] == "ganz":
            a=random.randint(ug,og)
        elif eins[1] == "dezimal":
            a=round(random.uniform(ug,og,runden))
        else:
            a=random.randint(ug,og)
    except:
            a=random.randint(ug,og)

            
    try:
        ug=zwei[2][0]
        og=zwei[2][1]
    except:
        ug=2
        og=7


    try:
        if zwei[1] == "ganz":
            b=random.randint(ug,og)
        elif zwei[1] == "dezimal":
            b=round(random.uniform(ug,og,runden))
        else:
            b=random.randint(ug,og)
    except:
            b=random.randint(ug,og)


    try:
        ug=drei[2][0]
        og=drei[2][1]
    except:
        ug=2
        og=7

    try:
        if drei[1] == "ganz":
            c=random.randint(ug,og)
        elif drei[1] == "dezimal":
            c=round(random.uniform(ug,og,runden))
        else:
            c=random.randint(ug,og)
    except:
            c=random.randint(ug,og)


    try:
        ug=vier[2][0]
        og=vier[2][1]
    except:
        ug=2
        og=7

    try:
        if vier[1] == "ganz":
            d=random.randint(ug,og)
        elif vier[1] == "dezimal":
            d=round(random.uniform(ug,og,runden))
        else:
            d=random.randint(ug,og)
    except:
            d=random.randint(ug,og)



    x=eins[0]
    y=zwei[0]
    z=drei[0]
    z1=vier[0]

    op1=random.choice(['+','-'])
    op2=random.choice(['+','-'])

    
    ausdruck="(" + str(a) + x + op1 + str(b) + y + ")(" + str(c) + z + op2 + str(d) + z1 + ")"

    ausdruck=my_latex(str(parse_expr(ausdruck,transformations=transformations)))


    loesung=parse_expr(ausdruck,transformations=transformations).expand()


    loesung_latex=latex(loesung)

    komplett = ausdruck + " = " + loesung_latex 

    return [math(ausdruck) + "=",math(loesung_latex),math(komplett)]










