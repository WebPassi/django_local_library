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
from sympy.mpmath import *

#import re



from elements import *
from functions import *
from zufall import *

### lsg: c=CAS, a=all (mit Rechenweg), s=short, p=pure (nur der Zahlenwert) 
def aufgNullstelle(func,lsg="c"):
### Nullstellen
    ft=[]
    dump = LinFunc(0,0)
    glg = Equation(func,dump)
    glgns = glg.equation
#    lsgns = makereal(solve(glgns,x,real=True))
    lsgns = solve(glgns,x,real=True)

    if lsg == "c":
        ft.append("{\\bf Nullstellen:} \n")
        ft.append("\\begin{align*} \n")
        ft.append("f(x)&=0 \\\\ \n")
        ft.append(latex(func.expr)  + "&=0 \\\\ \n")
        if len(lsgns) == 0:
            ft.append("\\end{align*} \n")
            ft.append("Keine L\\\"osung $\\Rightarrow$ Keine Nullstellen")
        elif len(lsgns) == 1:
            ft.append("\\text{Mit CAS:} \\\\ \n")
            ft.append("x&=" + latex(lsgns[0]))
            ft.append("\\end{align*} \n")
            ft.append("$\Rightarrow$ Nullstelle bei $N(" + latex(lsgns[0]) + "|" + latex(func.expr.subs(x,lsgns[0])) + ")$ \\\\ \n")
        else:
            for index in range(len(lsgns)):
                try:
                    ft.append("x_" + str(index+1) + "&=" + latex(lsgns[index].evalf(2)) + "\\\\ \n")
                except IndexError:
                    ft.append("\n")
                    ft.append("\\end{align*} \n")
        text=""
        for t in ft:
            text+=t
        return text

### lsg: c=CAS, a=all (mit Rechenweg), s=short, p=pure (nur der Zahlenwert) 
def aufgyStelle(f,xstelle,lsg="c"):
    text=""
    if lsg == "c":
        text="{\\bf Funktionswert:} \\\\ \n"
        text+="$" + latex(f.name) + "(" + latex(xstelle) + ")" + "=" + latex(f.ywert(xstelle)) + "$"
        text+="\\qquad (mit CAS)"
    return text

def aufgxStelle(f,ystelle,lsg="c"):
    text=""
    if lsg == "c":
        text+="{\\bf Funktionsstelle:} \n"
        text+="\\begin{align*} \n"
        text+=(latex(f.vonx) + "&=" + latex(ystelle)) + "\\\\ \n"
        text+=latex(f.expr)  + "&=0 \\\\ \n"
        text+="\\text{Mit CAS:} \\\\ \n"
        text+=latex(f.variable) + "&=" + latex(f.xwert(ystelle)[0]) + " \n"
        text+="\\end{align*} \n"
        return text
    
    
def aufgSteigungGerade(f,lsg="c"):
    alpha=degrees(atan(f.a)).evalf(2)
    text=""
    if lsg=="o":
        text+="$m=" + latex(f.a) + "=" + latex((f.a*(100.0)).evalf(4)) + "\\% \\qquad \\alpha=" + latex((alpha)) + "^{\\circ}$"
        return text
    elif lsg=="c":
        text+="{\\bf Steigung} (in Prozent):" + "\\quad $m=" + latex(f.a) + "=" + latex((f.a*(100.0)).evalf(4)) + "\\%$ \\\\ \n"   
        text+="{\\bf Steigungswinkel:} \\\\ \n" 
        text+="\\begin{align*} \n"
        text+="\\tan(\\alpha) &=" + latex(f.a) + "\\\\ \n"
        text+="\\text{mit CAS:} \\\\ \n"
        text+="\\alpha &=" + latex((alpha)) + "^{\\circ} \n"
        text+="\\end{align*} \n"
        return text

def aufgGeradeAufstellen(f,x1,x2,lsg="c"):
    y1=f.ywert(x1)
    y2=f.ywert(x2)
    text=""
    if lsg=="c":
        text+="{\\bf Geradengleichung aufstellen:} \\quad $y=mx+c$ (*) \\\\ \n"
        text+="{\\bf Steigung bestimmen:} \\\\ \n"
        text+="$m=\\frac{" + "(" + latex(y2) + ")" + "-" + "(" + latex(y1) + ")" + "}{" + "(" + latex(x2) + ")" + "-" + "(" + latex(x1) + ")" + "}=" + latex(f.a) + "$ \\\\ \n"
        text+="$y$-Wert, $x$-Wert und $m$ in (*) einsetzen: \n"
        text+="\\begin{align*} \n"
        text+=latex(y1) + "&=" + latex(f.a) + "\\cdot" + latex(x1) + "+ c \\\\ \n"
        text+=latex(f.b) + "&= c \n" 
        text+="\\end{align*} \\\\ \n"
        text+="{\\bf Funktionsgleichung:} \n"
        text+="\\[" + latex(f.gleichung) + "\\]"
        return text

def aufgSchnittpunktGeraden(f,g,lsg="c"):
    ft=[]
    glgns = Eq(f.expr,g.expr)
    lsgns = makereal(solve(glgns,x,real=True))
    text=""

    if lsg=="c":
        ft.append("{\\bf Schnittpunkt:} \n")
        ft.append("\\begin{align*} \n")
        ft.append(latex(f.vonx) + "&=" + latex(g.vonx) + " \\\\ \n")
        ft.append(latex(f.expr)  + "&=" + latex(g.expr) + " \\\\ \n")
        if len(lsgns) == 0:
            ft.append("\\end{align*} \n")
            ft.append("Keine L\\\"osung $\\Rightarrow$ Kein Schnittpunkt / Parallel")
        elif len(lsgns) == 1:
            ft.append("\\text{mit CAS:} \\\\ \n")
            ft.append("x&=" + latex(lsgns[0]))
            ft.append("\\end{align*} \n")
            ft.append("$\Rightarrow$ Schnittpunkt bei $N(" + latex(lsgns[0]) + "|" + latex(f.expr.subs(x,lsgns[0])) + ")$ \\\\ \n")
        else:
            for index in range(len(lsgns)):
                try:
                    ft.append("x_" + str(index+1) + "&=" + latex(lsgns[index].evalf(2)) + "\\\\ \n")
                except IndexError:
                    ft.append("\n")
                    ft.append("\\end{align*} \n")
        for t in ft:
            text+=t
        return text

def aufgSchnittwinkelGeraden(f,g,lsg="c"):
    alpha=degrees(atan(abs((f.a-g.a)/(1+f.a*g.a)))).evalf(2)
    text=""
    if lsg=="c":
        text+="{\\bf Schnittwinkel:} \\\\ \n" 
        text+="\\begin{align*} \n"
        text+="\\tan(\\alpha) &=" + "\\left|\\frac{m_1-m_2}{1+m_1\\cdot m_2}\\right| \\\\ \n"
        text+="\\tan(\\alpha) &=" + "\\left|\\frac{(" + latex(f.a) + ")-(" + latex(g.a) + ")}{1+(" + latex(f.a) + ")(" + latex(g.a) + ")}\\right| \\\\ \n"
        text+="\\text{mit CAS:} \\\\ \n"
        text+="\\alpha &=" + latex((alpha)) + "^{\\circ} \n"
        text+="\\end{align*} \n"
        return text


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

"""
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
"""


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


def aufgVektor_norm(vektor,lsg="p"):
    if type(vektor) is not list:
        vektor=[vektor]
    
    betrag=[]
    for v in vektor:
        betrag.append(latex(norm(v,2)))

    ende=makeSheet(makeExercise(multicol(betrag,3)))

        
    if lsg=="p":
        betrag=norm(vektor,2)
    return ende



### Potenzen

def aufgZehnerpotenzMultaufgabe(potenzliste,lsg="n"):
    aufgtext="Schreibe ohne Potenz als Multiplikationsaufgabe. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for p in potenzliste:
        aufgabe="$" + latex(p.basis) + "^{" + latex(p.exponent) + "}=$"
        potenz.append(aufgabe)
        loesung="$" + latex(p.basis)
        for l in range(p.exponent-1):
            loesung+="\\cdot" + latex(p.basis)
        loesung+="$"
            

        potenz_lsg.append(aufgabe + loesung)

    aufg=multicol(potenz,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,3)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg


def aufgZehnerpotenzPotenzaufgabe(potenzliste,lsg="n"):
    aufgtext="Schreibe als Potenz. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for p in potenzliste:
        aufgabe="$" + latex(p.basis)
        for l in range(p.exponent-1):
            aufgabe+="\\cdot" + latex(p.basis)
        aufgabe+="=$"
        potenz.append(aufgabe)
            
        loesung="$" + latex(p.basis) + "^{" + latex(p.exponent) + "}$"

        potenz_lsg.append(aufgabe + loesung)

    aufg=multicol(potenz,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,3)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg




def aufgZehnerpotenzBruch(potenzliste,lsg="n"):
    aufgtext="Schreibe als Bruch. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for p in potenzliste:
        aufgabe="$" + latex(p.basis) + "^{" + latex(p.exponent) + "}=$"
        potenz.append(aufgabe)

        loesung="$\\frac{1}{" + latex(p.basis) + "^{" + latex(-p.exponent) + "}}$" 

        potenz_lsg.append(aufgabe + loesung)

    aufg=multicol(potenz,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,3)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg




def aufgZehnerpotenzWurzel(potenzliste,lsg="n"):
    aufgtext="Schreibe als Wurzel. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for p in potenzliste:
        aufgabe="$" + latex(p.basis) + "^{" + latex(p.exponent) + "}=$"
        potenz.append(aufgabe)

        loesung="$\\sqrt[" + latex(p.exponent.q) + "]{" + latex(p.basis) + "}^{\\," + latex(p.exponent.p) + "}$" 

        potenz_lsg.append(aufgabe + loesung)

    aufg=multicol(potenz,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,3)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg

def aufgZehnerpotenzWurzelPotenz(potenzliste,lsg="n"):
    aufgtext="Schreibe als Potenz. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for p in potenzliste:
        aufgabe="$\\sqrt[" + latex(p.exponent.q) + "]{" + latex(p.basis) + "}^{\\," + latex(p.exponent.p) + "}=$" 
        potenz.append(aufgabe)

        loesung="$" + latex(p.basis) + "^{" + latex(p.exponent) + "}$"
        potenz_lsg.append(aufgabe + loesung)

    aufg=multicol(potenz,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,3)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg




def aufgZehnerpotenzOhne(potenzliste,lsg="n"):
    aufgtext="Berechne ohne Taschenrechner. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for p in potenzliste:
        potenz.append("$" + latex(p.basis) + "^{" + latex(p.exponent) + "}=$")
        potenz_lsg.append("$" + latex(p.basis) + "^{" + latex(p.exponent) + "}=" + latex(p.ergebnis) + "$")

    aufg=multicol(potenz,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,3)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg



def aufgZehnerpotenzWiss(faktorenliste,potenzliste,lsg="n"):
    aufgtext="Bringe die Zahlen in die Form $0,... \cdot 10^{?}$. (z.B. $23,46 = 0,2346 \cdot 10^2$) \\\\ \n"

    potenz=[]
    potenz_lsg=[]

    for i,p in enumerate(potenzliste):
        aufgabe=("$" + latex(faktorenliste[i] * p.ergebnis) + "=$").replace(".",",")
        potenz.append(aufgabe)

        loesung=("$" + latex(faktorenliste[i]) + "\\cdot" + latex(p.basis) + "^{" + latex(p.exponent) + "}$").replace(".",",")

        potenz_lsg.append(aufgabe + loesung)

    aufg=multicol(potenz,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,3)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg

def aufgZehnerpotenzFaktor(faktorliste,potenzliste,lsg="n"):
    aufgtext="Berechne ohne Taschenrechner. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for i,p in enumerate(potenzliste):
        potenz.append(("$" + latex(faktorliste[i]) + "\\cdot" + latex(p.basis) + "^{" + latex(p.exponent) + "}=$").replace(".",","))

        potenz_lsg.append(("$" + latex(faktorliste[i]) + "\\cdot" + latex(p.basis) + "^{" + latex(p.exponent) + "}=" + latex(faktorliste[i]*p.ergebnis) + "$").replace(".",","))

    aufg=multicol(potenz,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,3)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg



def aufgZehnerpotenzAdd(potenzliste1,potenzliste2,lsg="n"):
    aufgtext="Berechne ohne Taschenrechner. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for i,p in enumerate(potenzliste1):
        potenz.append("$" + latex(p.basis) + "^{" + latex(p.exponent) + "}" + "+" + latex(potenzliste2[i].basis) + "^{" + latex(potenzliste2[i].exponent) + "}=$")
        potenz_lsg.append("$" + latex(p.basis) + "^{" + latex(p.exponent) + "}" + "+" + latex(potenzliste2[i].basis) + "^{" + latex(potenzliste2[i].exponent) + "}=" + latex(p.ergebnis + potenzliste2[i].ergebnis) + "$")

    aufg=multicol(potenz,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,3)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg


def aufgZehnerpotenzFaktorAdd(faktorenliste1,potenzliste1,faktorenliste2,potenzliste2,lsg="n"):
    aufgtext="Berechne ohne Taschenrechner. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for i,p in enumerate(potenzliste1):
        aufgabe="$" + latex(faktorenliste1[i]) + "\\cdot" + latex(p.basis) + "^{" + latex(p.exponent) + "}" + "+" + latex(faktorenliste2[i]) + "\\cdot" + latex(potenzliste2[i].basis) + "^{" + latex(potenzliste2[i].exponent) + "}=$"
        potenz.append(aufgabe)

        loesung="$" + latex((faktorenliste1[i] * (p.ergebnis)) + (faktorenliste2[i] * (potenzliste2[i].ergebnis))) + "$"
        potenz_lsg.append(aufgabe + loesung)

    aufg=multicol(potenz,2)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,2)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg

def aufgZehnerpotenzMult(potenzliste1,potenzliste2,lsg="n"):
    aufgtext="Multipliziere ohne Taschenrechner. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for i,p in enumerate(potenzliste1):
        potenz.append("$" + latex(p.basis) + "^{" + latex(p.exponent) + "}" + "\\cdot" + latex(potenzliste2[i].basis) + "^{" + latex(potenzliste2[i].exponent) + "}=$")
        potenz_lsg.append("$" + latex(p.basis) + "^{" + latex(p.exponent) + "}" + "\\cdot" + latex(potenzliste2[i].basis) + "^{" + latex(potenzliste2[i].exponent) + "}=" + latex(p.ergebnis * potenzliste2[i].ergebnis) + "$")

    aufg=multicol(potenz,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,3)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg


def aufgZehnerpotenzMultGleicheBasis(potenzliste1,potenzliste2,lsg="n"):
    aufgtext="Schreibe als eine Potenz. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for i,p in enumerate(potenzliste1):
        aufgabe="$" + latex(p.basis) + "^{" + latex(p.exponent) + "}" + "\\cdot" + latex(potenzliste2[i].basis) + "^{" + latex(potenzliste2[i].exponent) + "}=$"
        potenz.append(aufgabe)

        loesung="$" + latex(p.basis) + "^{" + latex(p.exponent + potenzliste2[i].exponent) + "}$"

        potenz_lsg.append(aufgabe + loesung)

    aufg=multicol(potenz,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,3)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg


def aufgZehnerpotenzDivGleicheBasis(potenzliste1,potenzliste2,lsg="n"):
    aufgtext="Schreibe als eine Potenz. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for i,p in enumerate(potenzliste1):
        aufgabe="$\\frac{" + latex(p.basis) + "^{" + latex(p.exponent) + "}}" + "{" + latex(potenzliste2[i].basis) + "^{" + latex(potenzliste2[i].exponent) + "}}=$"
        potenz.append(aufgabe)

        loesung="$" + latex(p.basis) + "^{" + latex(p.exponent - potenzliste2[i].exponent) + "}$"

        potenz_lsg.append(aufgabe + loesung)

    aufg=multicol(potenz,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,3)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg



def aufgZehnerpotenzFaktorMult(faktorenliste1,potenzliste1,faktorenliste2,potenzliste2,lsg="n"):
    aufgtext="Multipliziere ohne Taschenrechner. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for i,p in enumerate(potenzliste1):
        aufgabe="$" + latex(faktorenliste1[i]) + "\\cdot" + latex(p.basis) + "^{" + latex(p.exponent) + "}" + "\\cdot" + latex(faktorenliste2[i]) + "\\cdot" + latex(potenzliste2[i].basis) + "^{" + latex(potenzliste2[i].exponent) + "}=$"
        potenz.append(aufgabe)

        
        loesung="$" + latex(faktorenliste1[i] * p.ergebnis * faktorenliste2[i] * potenzliste2[i].ergebnis) + "$"
        potenz_lsg.append(aufgabe + loesung)

    aufg=multicol(potenz,2)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,2)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg






def aufgZehnerpotenzEinheiten(zahlenliste, einheitenliste,lsg="n"):
    aufgtext="Bringe in die Grundeinheit. \\\\ \n"
    
    einheit=[]
    einheit_lsg=[]


    for i,e in enumerate(einheitenliste):
        einheit.append("$" + latex(zahlenliste[i]) + "\\," + "\\mathrm{" + (einheitenliste[i]) + "}" + "=$")

        ### Loesungen
        
        ## Einheit und Dimension trennen
        try:
            dim=int(e.split("^")[1])
            dimstr=(e.split("^")[1])
        except:
            dim=1
            dimstr=""

        e=e.split("^")[0]

        ## Ar
        if e == "a":
            einheit_lsg.append("$" + latex(zahlenliste[i]) + "\\," + "\\mathrm{" + (einheitenliste[i]) + "}" + "=" + latex(zahlenliste[i]) + "\\cdot 10^{2} " + "\\," + "\\mathrm{m^2} $")            

        ## Hektar
        elif e == "ha":
            einheit_lsg.append("$" + latex(zahlenliste[i]) + "\\," + "\\mathrm{" + (einheitenliste[i]) + "}" + "=" + latex(zahlenliste[i]) + "\\cdot 10^{4} " + "\\," + "\\mathrm{m^2} $")            

        ## Kilo allgemein
        elif e[0] == "k":
            einheit_lsg.append("$" + latex(zahlenliste[i]) + "\\," + "\\mathrm{" + (einheitenliste[i]) + "}" + "=" + latex(zahlenliste[i]) + "\\cdot 10^{" + latex(3*dim) + "} " + "\\," + "\\mathrm{" + latex(e[1]) + "^{" + latex(dimstr) + "}" + "}" + "$")


        ## Mega allgemein
        elif e[0] == "M":
            einheit_lsg.append("$" + latex(zahlenliste[i]) + "\\," + "\\mathrm{" + (einheitenliste[i]) + "}" + "=" + latex(zahlenliste[i]) + "\\cdot 10^{" + latex(6*dim) + "} " + "\\," + "\\mathrm{" + latex(e[1]) + "^{" + latex(dimstr) + "}" + "}" + "$")

        ## Giga allgemein
        elif e[0] == "G":
            einheit_lsg.append("$" + latex(zahlenliste[i]) + "\\," + "\\mathrm{" + (einheitenliste[i]) + "}" + "=" + latex(zahlenliste[i]) + "\\cdot 10^{" + latex(9*dim) + "} " + "\\," + "\\mathrm{" + latex(e[1]) + "^{" + latex(dimstr) + "}" + "}" + "$")

        ## dezi allgemein
        elif e[0] == "d":
            einheit_lsg.append("$" + latex(zahlenliste[i]) + "\\," + "\\mathrm{" + (einheitenliste[i]) + "}" + "=" + latex(zahlenliste[i]) + "\\cdot 10^{" + latex((-1)*dim) + "} " + "\\," + "\\mathrm{" + latex(e[1]) + "^{" + latex(dimstr) + "}" + "}" + "$")


        ## centi allgemein
        elif e[0] == "c":
            einheit_lsg.append("$" + latex(zahlenliste[i]) + "\\," + "\\mathrm{" + (einheitenliste[i]) + "}" + "=" + latex(zahlenliste[i]) + "\\cdot 10^{" + latex((-2)*dim) + "} " + "\\," + "\\mathrm{" + latex(e[1]) + "^{" + latex(dimstr) + "}" + "}" + "$")

        ## milli allgemein
        elif e[0] == "m":
            einheit_lsg.append("$" + latex(zahlenliste[i]) + "\\," + "\\mathrm{" + (einheitenliste[i]) + "}" + "=" + latex(zahlenliste[i]) + "\\cdot 10^{" + latex((-3)*dim) + "} " + "\\," + "\\mathrm{" + latex(e[1]) + "^{" + latex(dimstr) + "}" + "}" + "$")




    aufg=multicol(einheit,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(einheit_lsg,3)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg


def aufgPotenzMultaufgabe(potenzliste,lsg="n"):
    aufgtext="Schreibe ohne Potenz als Multiplikationsaufgabe. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for p in potenzliste:
        aufgabe="$" + latex(p.basis) + "^{" + latex(p.exponent) + "}=$"
        potenz.append(aufgabe)
        loesung="$" + latex(p.basis)
        for l in range(p.exponent-1):
            loesung+="\\cdot" + latex(p.basis)
        loesung+="$"
            

        potenz_lsg.append(aufgabe + loesung)

    aufg=multicol(potenz,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,3)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg


def aufgPotenzPotenzaufgabe(potenzliste,lsg="n"):
    aufgtext="Schreibe als Potenz. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for p in potenzliste:
        aufgabe="$" + latex(p.basis)
        for l in range(p.exponent-1):
            aufgabe+="\\cdot" + latex(p.basis)
        aufgabe+="=$"
        potenz.append(aufgabe)
            
        loesung="$" + latex(p.basis) + "^{" + latex(p.exponent) + "}$"

        potenz_lsg.append(aufgabe + loesung)

    aufg=multicol(potenz,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,3)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg




def aufgPotenzBruch(potenzliste,lsg="n"):
    aufgtext="Schreibe als Bruch. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for p in potenzliste:
        aufgabe="$" + latex(p.basis) + "^{" + latex(p.exponent) + "}=$"
        potenz.append(aufgabe)

        loesung="$\\frac{1}{" + latex(p.basis) + "^{" + latex(-p.exponent) + "}}$" 

        potenz_lsg.append(aufgabe + loesung)

    aufg=multicol(potenz,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,3)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg




def aufgPotenzWurzel(potenzliste,lsg="n"):
    aufgtext="Schreibe als Wurzel. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for p in potenzliste:
        aufgabe="$" + latex(p.basis) + "^{" + latex(p.exponent) + "}=$"
        potenz.append(aufgabe)

        loesung="$\\sqrt[" + latex(p.exponent.q) + "]{" + latex(p.basis) + "}^{\\," + latex(p.exponent.p) + "}$" 

        potenz_lsg.append(aufgabe + loesung)

    aufg=multicol(potenz,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,3)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg

def aufgPotenzWurzelPotenz(potenzliste,lsg="n"):
    aufgtext="Schreibe als Potenz. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for p in potenzliste:
        aufgabe="$\\sqrt[" + latex(p.exponent.q) + "]{" + latex(p.basis) + "}^{\\," + latex(p.exponent.p) + "}=$" 
        potenz.append(aufgabe)

        loesung="$" + latex(p.basis) + "^{" + latex(p.exponent) + "}$"
        potenz_lsg.append(aufgabe + loesung)

    aufg=multicol(potenz,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,3)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg




def aufgPotenzOhne(potenzliste,lsg="n"):
    aufgtext="Berechne mit dem Taschenrechner. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for p in potenzliste:
        potenz.append("$" + latex(p.basis) + "^{" + latex(p.exponent) + "}=$")
        potenz_lsg.append("$" + latex(p.basis) + "^{" + latex(p.exponent) + "}=" + latex(p.ergebnis) + "$")

    aufg=multicol(potenz,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,3)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg

def aufgPotenzFaktor(faktorliste,potenzliste,lsg="n"):
    aufgtext="Berechne mit dem Taschenrechner. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for i,p in enumerate(potenzliste):
        potenz.append(("$" + latex(faktorliste[i]) + "\\cdot" + latex(p.basis) + "^{" + latex(p.exponent) + "}=$").replace(".",","))

        potenz_lsg.append(("$" + latex(faktorliste[i]) + "\\cdot" + latex(p.basis) + "^{" + latex(p.exponent) + "}=" + latex(faktorliste[i]*p.ergebnis) + "$").replace(".",","))

    aufg=multicol(potenz,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,3)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg



def aufgPotenzAdd(potenzliste1,potenzliste2,lsg="n"):
    aufgtext="Berechne mit dem Taschenrechner. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for i,p in enumerate(potenzliste1):
        potenz.append("$" + latex(p.basis) + "^{" + latex(p.exponent) + "}" + "+" + latex(potenzliste2[i].basis) + "^{" + latex(potenzliste2[i].exponent) + "}=$")
        potenz_lsg.append("$" + latex(p.basis) + "^{" + latex(p.exponent) + "}" + "+" + latex(potenzliste2[i].basis) + "^{" + latex(potenzliste2[i].exponent) + "}=" + latex(p.ergebnis + potenzliste2[i].ergebnis) + "$")

    aufg=multicol(potenz,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,3)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg


def aufgPotenzFaktorAdd(faktorenliste1,potenzliste1,faktorenliste2,potenzliste2,lsg="n"):
    aufgtext="Berechne mit dem Taschenrechner. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for i,p in enumerate(potenzliste1):
        aufgabe="$" + latex(faktorenliste1[i]) + "\\cdot" + latex(p.basis) + "^{" + latex(p.exponent) + "}" + "+" + latex(faktorenliste2[i]) + "\\cdot" + latex(potenzliste2[i].basis) + "^{" + latex(potenzliste2[i].exponent) + "}=$"
        potenz.append(aufgabe)

        loesung="$" + latex((faktorenliste1[i] * (p.ergebnis)) + (faktorenliste2[i] * (potenzliste2[i].ergebnis))) + "$"
        potenz_lsg.append(aufgabe + loesung)

    aufg=multicol(potenz,2)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,2)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg

def aufgPotenzMult(potenzliste1,potenzliste2,lsg="n"):
    aufgtext="Multipliziere mit dem Taschenrechner. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for i,p in enumerate(potenzliste1):
        potenz.append("$" + latex(p.basis) + "^{" + latex(p.exponent) + "}" + "\\cdot" + latex(potenzliste2[i].basis) + "^{" + latex(potenzliste2[i].exponent) + "}=$")
        potenz_lsg.append("$" + latex(p.basis) + "^{" + latex(p.exponent) + "}" + "\\cdot" + latex(potenzliste2[i].basis) + "^{" + latex(potenzliste2[i].exponent) + "}=" + latex(p.ergebnis * potenzliste2[i].ergebnis) + "$")

    aufg=multicol(potenz,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,3)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg


def aufgPotenzMultGleicheBasis(potenzliste1,potenzliste2,lsg="n"):
    aufgtext="Schreibe als eine Potenz. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for i,p in enumerate(potenzliste1):
        aufgabe="$" + latex(p.basis) + "^{" + latex(p.exponent) + "}" + "\\cdot" + latex(potenzliste2[i].basis) + "^{" + latex(potenzliste2[i].exponent) + "}=$"
        potenz.append(aufgabe)

        loesung="$" + latex(p.basis) + "^{" + latex(p.exponent + potenzliste2[i].exponent) + "}$"

        potenz_lsg.append(aufgabe + loesung)

    aufg=multicol(potenz,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,3)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg


def aufgPotenzDivGleicheBasis(potenzliste1,potenzliste2,lsg="n"):
    aufgtext="Schreibe als eine Potenz. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for i,p in enumerate(potenzliste1):
        aufgabe="$\\frac{" + latex(p.basis) + "^{" + latex(p.exponent) + "}}" + "{" + latex(potenzliste2[i].basis) + "^{" + latex(potenzliste2[i].exponent) + "}}=$"
        potenz.append(aufgabe)

        loesung="$" + latex(p.basis) + "^{" + latex(p.exponent - potenzliste2[i].exponent) + "}$"

        potenz_lsg.append(aufgabe + loesung)

    aufg=multicol(potenz,3)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,3)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg



def aufgPotenzFaktorMult(faktorenliste1,potenzliste1,faktorenliste2,potenzliste2,lsg="n"):
    aufgtext="Multipliziere mit dem Taschenrechner. \\\\ \n"
    potenz=[]
    potenz_lsg=[]

    for i,p in enumerate(potenzliste1):
        aufgabe="$" + latex(faktorenliste1[i]) + "\\cdot" + latex(p.basis) + "^{" + latex(p.exponent) + "}" + "\\cdot" + latex(faktorenliste2[i]) + "\\cdot" + latex(potenzliste2[i].basis) + "^{" + latex(potenzliste2[i].exponent) + "}=$"
        potenz.append(aufgabe)

        
        loesung="$" + latex(faktorenliste1[i] * p.ergebnis * faktorenliste2[i] * potenzliste2[i].ergebnis) + "$"
        potenz_lsg.append(aufgabe + loesung)

    aufg=multicol(potenz,2)
    aufg=aufgtext+aufg
    aufg_lsg=multicol(potenz_lsg,2)
    aufg_lsg=aufgtext+aufg_lsg

    if lsg=="n":
        return aufg
    elif lsg=="a":
        return aufg_lsg








##### Negative Zahlen

### Zwei Zahlen addieren/subtrahieren
def aufgNegZahlenZwei(term1, term2, operator, lsg="n"):

    aufgtext="Berechne. \\\\ \n"
    
    aufgabe=[]
    aufgabe_lsg=[]

    for i,aufg in enumerate(term1):  
        a=term1[i] 
        b=term2[i]

        if operator == "+":
            expr = a+b
            aufgabe.append("$" + latex(a) + "+" + minusklammer(b) + "=$") 
            aufgabe_lsg.append("$" + latex(a) + "+" + minusklammer(b) + "=" + latex(expr) + "$")

        elif operator == "-":
            expr = a-b
            aufgabe.append("$" + latex(a) + "-" + minusklammer(b) + "=$") 
            aufgabe_lsg.append("$" + latex(a) + "-" + minusklammer(b) + "=" + latex(expr) + "$")



    aufg=multicol(aufgabe,3)
#    aufg=aufgtext+aufg
    aufg_lsg=multicol(aufgabe_lsg,3)
#    aufg_lsg=aufgtext+aufg_lsg

    if lsg == "n":
        return aufg
    else:
        return aufg_lsg




### Drei Zahlen addieren/Subtrahieren
def aufgNegZahlenDrei(term1, term2, term3, op1, op2, lsg="n"):

    aufgtext="Berechne. \\\\ \n"
    
    aufgabe=[]
    aufgabe_lsg=[]

    for i,aufg in enumerate(term1):  
        a=term1[i] 
        b=term2[i]
        c=term3[i]



        if op1 == "+":


            if op2 == "+":
                expr = a+b+c
                aufgabe.append("$" + latex(a) + "+" + minusklammer(b) + "+" + minusklammer(c) + "=$") 
                aufgabe_lsg.append("$" + latex(a) + "+" + minusklammer(b) + "+" + minusklammer(c) + "=" + latex(expr) + "$")

            if op2 == "-":
                expr = a+b-c
                aufgabe.append("$" + latex(a) + "+" + minusklammer(b) + "-" + minusklammer(c) + "=$") 
                aufgabe_lsg.append("$" + latex(a) + "+" + minusklammer(b) + "-" + minusklammer(c) + "=" + latex(expr) + "$")



        if op1 == "-":


            if op2 == "+":
                expr = a-b+c
                aufgabe.append("$" + latex(a) + "-" + minusklammer(b) + "+" + minusklammer(c) + "=$") 
                aufgabe_lsg.append("$" + latex(a) + "-" + minusklammer(b) + "+" + minusklammer(c) + "=" + latex(expr) + "$")

            if op2 == "-":
                expr = a-b-c
                aufgabe.append("$" + latex(a) + "-" + minusklammer(b) + "-" + minusklammer(c) + "=$") 
                aufgabe_lsg.append("$" + latex(a) + "-" + minusklammer(b) + "-" + minusklammer(c) + "=" + latex(expr) + "$")

            

    aufg=multicol(aufgabe,3)
#    aufg=aufgtext+aufg
    aufg_lsg=multicol(aufgabe_lsg,3)
#    aufg_lsg=aufgtext+aufg_lsg

    if lsg == "n":
        return aufg
    else:
        return aufg_lsg



def term(term):
    import re
    newterm=term.replace("**","^")
    latexterm=""
    regex=r'[0-9]'
    a=re.match("[0-9]","0")
    for i,zeichen in enumerate(newterm):
        if zeichen == "*":
            if (re.match("[0-9]",term[i+1])) or (term[i-1] == term[i+1]):
                latexterm+="\\cdot "
            else:
                latexterm+=""
        else:
            latexterm+=zeichen
    
    return latex(latexterm)
          



def term_lsg(term):
    term=expand(sympify(term))
    return latex(term)


def aufgTerme(aufgliste,spalten=3):
    aufgtext="Berechne. \\\\ \n"
    
    aufgaben=[]

    for aufg in aufgliste:
        aufgaben.append("$" + term(aufg) + "=$")
        
    aufg=multicol(aufgaben,spalten)

    return aufg


def aufgTerme_lsg(aufgliste,spalten=3):
    aufgtext="Berechne. \\\\ \n"
    
    aufgaben=[]

    for aufg in aufgliste:
        aufgaben.append("$" + term(aufg) + "=" + term_lsg(aufg) + "$")
        
    aufg=multicol(aufgaben,spalten)

    return aufg







