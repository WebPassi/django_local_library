#! /usr/bin/env python

#! /usr/bin/env python

## Author: Pasquale Franz
## Date: 26.01.2015

######
## Generate a table in latex-format with given values

import os
from sympy import *
from sympy.abc import *

from elements import *
from functions import *
from zufall import *

### Aus einer Funktionsgleichung Wertetabelle und Graph zeichnen
def aufgWertetabelleGraph(funktion,lsg="n"):
    aufg="Erstelle f\\\"ur die Funktion " + funktion.anzeigen() + " eine Wertetabelle und zeichne den dazugeh\\\"origen Graphen im Bereich von $x=-3$ bis $x=3$ in ein Koordinatensystem. \\\\ \n"
    
    if lsg=="n":
        return aufg
    elif lsg=="a":
        lsg1=erstelleWertetabelle(funktion)
        lsg2=zeichneGraph(funktion)
        return aufg + lsg1 + lsg2



def aufgParabeleigenschaften(funktionsliste,lsg="n"):
    aufg="Gib f\\\"ur die folgenden Parabeln den Scheitelpunkt, die Symmetrieachse, sowie die Nullstellen an. \n"
    graph=zeichneGraph(funktionsliste,"allinone","y",0.7)

    if lsg=="n":
        tabelle=cross_table(["Scheitelpunkt","Symmetrieachse","Nullstellen"],erstelleNamensliste(funktionsliste),1.5)
        aufgabe=aufg+teileBlatt(graph,tabelle,0.35,0.65)
        return aufgabe    
    elif lsg=="a":
        z=list(range(len(funktionsliste)+1))
        z[0]=["","Scheitelpunkt","Symmetrieachse","Nullstellen"]
        for i,funktion in enumerate(funktionsliste):
            z[i+1]=[math(latex(funktion.name)),funktion.sp(),funktion.symachse(),zeigeErgebnisQuad(funktion.nullstelle())]
        tabelle=table(z,1.3)
        lsg=teileBlatt(graph,tabelle,0.35,0.65)
        return aufg + lsg 

def aufgParabeleigenschaftenAllgemein(funktionsliste,lsg="n"):
    aufg="Gib f\\\"ur die folgenden Parabeln Scheitelpunkt, Symmetrieachse, Nullstellen und \\\"Offnung an. Gib weiter an, ob die Parabeln durch Streckung oder Stauchung aus der Normalparabel entstehen. \n"
    graph=zeichneGraph(funktionsliste,"allinone","y",0.5)

    if lsg=="n":
        tabelle=cross_table(["Scheitelpunkt","Symmetrieachse","Nullstellen","\\\"Offnung","Form"],erstelleNamensliste(funktionsliste),1.3)
        aufgabe=aufg+teileBlatt(graph,tabelle,0.25,0.75)
        return aufgabe    
    elif lsg=="a":
        z=list(range(len(funktionsliste)+1))
        z[0]=["","Scheitelpunkt","Symmetrieachse","Nullstellen","\\\"Offnung","Form"]
        for i,funktion in enumerate(funktionsliste):
            z[i+1]=[math(latex(funktion.name)),funktion.sp(),funktion.symachse(),zeigeErgebnisQuad(funktion.nullstelle()),funktion.oeffnung(),funktion.form()]
        tabelle=table(z,1.3)
        lsg=teileBlatt(graph,tabelle,0.25,0.75)
        return aufg + lsg 


def aufgFunktionaufstellen(funktionsliste,lsg="n"): 
    aufg="Stelle f\\\"ur die Graphen aus Aufgabe 2 die zugeh\\\"origen Funktionsgleichungen auf. \n"
    if lsg=="n":
        return aufg
    elif lsg=="a":
        funktionen=[]
        for funktion in funktionsliste:
            funktionen.append(funktion.anzeigen())
        lsg=multicol(funktionen,3)
        return aufg+lsg



def aufgGraph(funktionsliste,lsg="n"):
    aufg="Zeichne die Graphen der folgenden Funktionen in ein gemeinsames Koordinatensystem. Verwende dabei die Schablone. \n"
    funktionen=erstelleFunktionsliste(funktionsliste)
    if lsg=="n":
        return aufg+multicol(funktionen,3)
    elif lsg=="a":
        lsg=zeichneGraph(funktionsliste)
        return aufg+multicol(funktionen,3) + lsg   
        
def aufgAuswahl(funktionsliste, dars1, dars2, anz1=1, anz2=3, lsg="n", platz1=0.5, platz2=0.5):
    if lsg=="a":
        for i,f in enumerate(funktionsliste):
            if not i == 0:
                f.streichen=True
    fauswahl1=[]
    fauswahl2=[]
    for i in range(anz1):
        fauswahl1.append(funktionsliste[i])
    for i in range(anz2):
        fauswahl2.append(funktionsliste[i])
    fauswahl2=zufallsliste(fauswahl2)

    if dars1=="Funktionsgleichung":
        ls=zeigeFunktionsgleichung(fauswahl1,1) 
    elif dars1=="Graph":
        ls=zeichneGraph(fauswahl1,"normal","n",0.6)
    elif dars1=="Wertetabelle":
        ls="" 
    
    if dars2=="Funktionsgleichung":
        rs=zeigeFunktionsgleichung(nummeriereFunktionen(fauswahl2),1) 
    elif dars2=="Graph": 
        rs=zeichneGraph(fauswahl2,"normal","n",0.4) 
    elif dars2=="Wertetabelle":
        rs="" 
    return teileBlatt(ls,rs,platz1,platz2)
    
def aufgAuswahlGraph(funktionsliste,lsg="n"):
    aufg="Streiche die Graphen, die nicht zur Funktionsgleichung passen. \\\\ \n"
    if lsg=="n":
        aufg+=aufgAuswahl(funktionsliste,"Funktionsgleichung","Graph",1,len(funktionsliste),"n",0.35,0.65)
        return aufg
    elif lsg=="a":
        aufg+=aufgAuswahl(funktionsliste,"Funktionsgleichung","Graph",1,len(funktionsliste),"a",0.35,0.65)
        return aufg
        
def aufgAuswahlFunktion(funktionsliste,lsg="n"):
    aufg="Unterstreiche die Funktionsgleichung, die zum Graphen passt. \\\\ \n"
    if lsg=="n":
        aufg+=aufgAuswahl(funktionsliste,"Graph","Funktionsgleichung",1,len(funktionsliste),"n",0.3,0.7)
        return aufg
    elif lsg=="a":
        aufg+=aufgAuswahl(funktionsliste,"Graph","Funktionsgleichung",1,len(funktionsliste),"a",0.3,0.7)
        return aufg


def aufgNormalform(funktionsliste,lsg="n"):

    if lsg=="n":
        aufg+=aufgAuswahl(funktionsliste,"Graph","Funktionsgleichung",1,len(funktionsliste),"n",0.3,0.7)
        return aufg
    elif lsg=="a":
        aufg+=aufgAuswahl(funktionsliste,"Graph","Funktionsgleichung",1,len(funktionsliste),"a",0.3,0.7)
        return aufg

def aufgScheitelpunktform(funktionsliste,lsg="n"):
    aufg="Unterstreiche die Funktionsgleichung, die zum Graphen passt. \\\\ \n"
    if lsg=="n":
        aufg+=aufgAuswahl(funktionsliste,"Graph","Funktionsgleichung",1,len(funktionsliste),"n",0.3,0.7)
        return aufg
    elif lsg=="a":
        aufg+=aufgAuswahl(funktionsliste,"Graph","Funktionsgleichung",1,len(funktionsliste),"a",0.3,0.7)
        return aufg

def aufgNormalform(funktionsliste,lsg="n"):
    aufgtext="Bringe die Funktionsgleichungen auf Normalform. \\\\ \n"
    fnf=[]
    fsp=[]
    for f in funktionsliste:
        fnf.append("$" + latex(f.name) + "(" + latex(f.variable) + ")=" + latex(f.scheitelpunktform()) + "$")
        fsp.append("$" + latex(f.name) + "(" + latex(f.variable) + ")=" + latex(f.scheitelpunktform()) + "$ \\\\ \n" + "$" + latex(f.name) + "(" + latex(f.variable) + ")=" + latex(f.normalform()) + "$ \\\\ \n")        
    aufg=multicol(fnf,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(fsp,3)
    aufg_lsg=aufgtext+aufg_lsg
    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg


def aufgScheitelpunktform(funktionsliste,lsg="n"):
    aufgtext="Bringe die Funktionsgleichungen auf Scheitelpunktform. \\\\ \n"
    fnf=[]
    fsp=[]
    for f in funktionsliste:
        fnf.append("$" + latex(f.name) + "(" + latex(f.variable) + ")=" + latex(f.normalform()) + "$")
        fsp.append("$" + latex(f.name) + "(" + latex(f.variable) + ")=" + latex(f.normalform()) + "$ \\\\ \n" + "$" + latex(f.name) + "(" + latex(f.variable) + ")=" + latex(f.scheitelpunktform()) + "$ \\\\ \n")        
    aufg=multicol(fnf,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(fsp,3)
    aufg_lsg=aufgtext+aufg_lsg
    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg

def quadErg(quadfunk):
    f=quadfunk
    s=[]
    test=r**2
    s.append("\\begin{align} \n")
    if quadfunk.a==1:
        s.append(latex(f.name) + "(" + latex(f.variable) + ")" + "&=" + latex(f.expr) + " \\\\ \n")
        s.append(latex(f.name) + "(" + latex(f.variable) + ")" + "&=" + latex(x**2) + vorzeichen(f.b) + latex(x) + "+ \\left(\\frac{" + latex(f.b) + "}{2}\\right)^2 - \\left( \\frac{" + latex(f.b) + "}{2}\\right) ^2 " + vorzeichensum(f.c) +  " \\\\ \n")
    s.append(latex(f.name) + "(" + latex(f.variable) + ")" + "&=(" + latex(x) + vorzeichensum(Rational(f.b,2)) + ")^2- \\left( \\frac{" + latex(f.b) + "}{2}\\right) ^2 " + vorzeichensum(f.c) +  " \\\\ \n")    
    s.append(latex(f.name) + "(" + latex(f.variable) + ")" + "&=(" + latex(x) + vorzeichensum(Rational(f.b,2)) + ")^2" + vorzeichensum((f.b/2.0)**2+f.c))
    s.append("\\end{align} \n")
    
    glgs=""
    for schritt in s:
        glgs+=schritt
        
    return glgs
        




##### Zufallskonstruktionen

### lineare Gleichungen
def erstelleLG_alt(form,zahlenbereich,ug,og):
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
### lineare Gleichungen
def erstelleLG(art,zahlenbereich,ug,og):
    if zahlenbereich=="Z":
        if art=="einfach":
            f1=LinFunc(zufallZ0(ug,og),0) 
            f2=LinFunc(0,zufallZ(ug,og))
            glg=Equation(f1.expr,f2.expr)
            return glg
        elif art=="rechts0":
            f1=LinFunc(zufallZ0(ug,og),zufallZ0(ug,og))
            f2=LinFunc(0,0)
            glg=Equation(f1.expr,f2.expr)
            return glg
        elif art=="rechtsZahl":
            f1=LinFunc(zufallZ0(ug,og),zufallZ0(ug,og))
            f2=LinFunc(0,zufallZ0(ug,og))
            glg=Equation(f1.expr,f2.expr)
            return glg
        elif art=="linksundrechts": 
            f1=LinFunc(zufallZ0(ug,og),zufallZ0(ug,og))
            f2=LinFunc(zufallZ0(ug,og),zufallZ0(ug,og))
            glg=Equation(f1.expr,f2.expr)
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

def prozentwert(gw,ps,ds="p"):
    if ds=="p":
        return Float(gw)*Float(ps)/100.0
    else:
        return Float(gw)*Float(ps)

def prozentsatz(gw,pw):
    return Float(pw)/Float(gw)
        

def grundwert(pw,ps,ds="p"):
    if ds=="p":
        return Float(pw)*100.0/Float(ps)
    else:
        return Float(pw)/Float(ps)

def aufgProzentwert(ps,ds,gw,eh):
    aufgtext="Bestimme den Prozentwert."
    straufg=list(range(len(gw)))
    for i,grundwert in enumerate(gw):
        if ds[i]=="p":
            straufg[i]="$" + latex(ps[i]) + "\\%$ von $" + latex(gw[i]) + "$ " + str(eh[i]) 
        else:
            straufg[i]="$" + latex(ps[i]) + "$ von $" + latex(gw[i]) + "$ " + str(eh[i]) 
    multi=multicol(straufg,3)
    return aufgtext + multi

def bspProzentwert(ps,ds,gw,eh):
    aufgtext="Wieviel sind "
    if ds=="p":
        straufg="$" + latex(ps) + "\\%$ von $" + latex(gw) + "$ " + str(eh) + "?" 
    else:
        straufg="$" + latex(ps) + "$ von $" + latex(gw) + "$ " + str(eh) 
    lsgweg="\\qquad {\\em L\\\"osung:} $\\frac{" + latex(ps) + "}{100}\\cdot " + latex(gw) + "$ " + str(eh) + " $ = " + latex(deutsch(runden(prozentwert(gw,ps),4))) + "$ " + str(eh)
    return aufgtext + straufg + lsgweg

def aufgProzentsatz(pw,gw,eh):
    aufgtext="Bestimme den Prozentsatz."
    straufg=list(range(len(gw)))
    for i,grundwert in enumerate(gw):
        straufg[i]="$" + latex(pw[i]) + "$ " + str(eh[i]) + " von $" + latex(gw[i]) + "$ " + str(eh[i]) 
    multi=multicol(straufg,3)
    return aufgtext + multi

def bspProzentsatz(pw,gw,eh):
    aufgtext="Wieviel Prozent sind "
    straufg="$" + latex(pw) + "$ " + str(eh) + "~von $" + latex(gw) + "$ " + str(eh) + "?" 
    lsgweg="\\qquad {\\em L\\\"osung:} $\\frac{" + latex(pw) + "}{" + latex(gw) + "}\\cdot " + "100\\%  = " + latex(deutsch(runden(prozentsatz(gw,pw)*100.0,4))) + "\\%$ "
    return aufgtext + straufg + lsgweg


def aufgGrundwert(pw,eh,ps,ds):
    aufgtext="Bestimme den Grundwert."
    straufg=list(range(len(pw)))
    for i,prozentwert in enumerate(pw):
        if ds[i]=="p":
            straufg[i]="$" + latex(pw[i]) + "$ " + str(eh[i]) + " sind $" + latex(ps[i]) + "\\%$."
        else:
            straufg[i]="$" + latex(pw[i]) + "$ " + str(eh[i]) + " sind $" + latex(ps[i]) + "$."
    multi=multicol(straufg,3)
    return aufgtext + multi

def bspGrundwert(pw,eh,ps,ds):
    aufgtext="$" + latex(pw) + "$ sind $" + latex(ps) + "\\%$. Wieviel sind 100\\%?"   
    lsgweg="\\qquad {\\em L\\\"osung:} $" + latex(pw) + "$ " + str(eh) + "$\\cdot \\frac{100}{" + latex(ps) + "}= " + latex(deutsch(runden(grundwert(pw,ps),4))) + "$ " + str(eh)
    return aufgtext + lsgweg

