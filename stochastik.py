#! /usr/bin/env python
# -*- coding: utf-8 -*-

## Author: Pasquale Franz
## Date: 03.06.2014

######
## The python-script generates a latex output which, (after compiling with pdflatex) creates random exercise sheets with solution.
## The implented functions (exercises) so far:
## Linear equations:
##   linfunc(): ax+b=c
##   linfunc0(): ax+b=0 
## Quadratical equations:
##   quadfunc(): ax2+bx+c=0
##   quadfuncnormal(): x2+bx+c=0
##   quadfuncnormalsym(): x2+c=0
##   quadfuncsym(): ax2+c=0
##   quadfunchomo(): ax2+bx=0

import random
from sympy import * 
#from sympy import Integral, latex

# erklaere alle buchstaben neutzbaren zu sympy symbolen:
from sympy.abc import *
from collections import Counter

from elements import *

def binomial(n,k):
    return factorial(n) // factorial(k) // factorial(n-k)
 
def binomial_write(n="",k=""):
    if n == "":
        n = random.randint(10,20)
    if k == "":
        k = random.randint(0,10)

    fp.write("$\\binom{" + latex(n) + "}{" + latex(k) + "}=$")
    ft.write("$\\binom{" + latex(n) + "}{" + latex(k) + "}=" + latex(binomial(n,k)) + "$")

### Kenngroessen: genau 3 (k1) von 8 (n1) gelbe und 2 (k2) von 10 (n2) rote Kugeln 
def lotto(n1="",n2="",k1="",k2=""):
    if n1 == "":
        n1 = random.randint(5,10)
    if n2 == "":
        n2 = random.randint(5,10)
    if k1 == "":
        k1 = random.randint(0,5)
    if k2 == "":
        k2 = random.randint(0,5)

    n = n1+n2
    k = k1+k2
    fp.write("$\\frac{\\binom{" + latex(n1) + "}{" + latex(k1) + "}\cdot \\binom{" + latex(n2) + "}{" + latex(k2) + "}}{\\binom{" + latex(n) + "}{" + latex(k) + "}}=$")
    ft.write("$\\frac{\\binom{" + latex(n1) + "}{" + latex(k1) + "}\cdot \\binom{" + latex(n2) + "}{" + latex(k2) + "}}{\\binom{" + latex(n) + "}{" + latex(k) + "}}=" + latex((binomial(n1,k1)*binomial(n2,k2) / binomial(n,k)*100).evalf(3)) + "\\%$")

### Kenngroessen: genau 3 (k1) von 8 (n1) gelbe, 2 (k2) von 10 (n2) rote und 7 (k3) von 15 (n3) schwarze Kugeln 
def lottodrei(n1="",n2="",n3="",k1="",k2="",k3=""):
    if n1 == "":
        n1 = random.randint(5,10)
    if n2 == "":
        n2 = random.randint(5,10)
    if n3 == "":
        n3 = random.randint(5,10)
    if k1 == "":
        k1 = random.randint(0,5)
    if k2 == "":
        k2 = random.randint(0,5)
    if k3 == "":
        k3 = random.randint(0,5)

    n = n1+n2+n3
    k = k1+k2+k3
    fp.write("$\\frac{\\binom{" + latex(n1) + "}{" + latex(k1) + "}\cdot \\binom{" + latex(n2) + "}{" + latex(k2) + "}\cdot \\binom{" + latex(n3) + "}{" + latex(k3) + "}}{\\binom{" + latex(n) + "}{" + latex(k) + "}}=$")
    ft.write("$\\frac{\\binom{" + latex(n1) + "}{" + latex(k1) + "}\cdot \\binom{" + latex(n2) + "}{" + latex(k2) + "}\cdot \\binom{" + latex(n3) + "}{" + latex(k3) + "}}{\\binom{" + latex(n) + "}{" + latex(k) + "}}=" + latex((binomial(n1,k1)*binomial(n2,k2) / binomial(n,k)*100).evalf(3)) + "\\%$")

def bernoullip(n="",p="",k=""):
    if n == "":
        n = random.randint(0,10)
    if k == "":
        k = random.randint(0,n)
    if p == "":
        p = Float(random.random()).evalf(4)

    ft.write("$n=" + latex(n) + "$, $p=" + latex(p) + "$, $k=" + latex(k) + "$ \\\\ \n")
    ft.write("$P(X=" + latex(k) + ")=$\\\\ $\\binom{" + latex(n) + "}{" + latex(k) + "}\\cdot" + latex(p) + "^{" + latex(k) + "}\\cdot" + latex(1-p) + "^{" + latex(n-k) + "}=$ \\\\ \n")
    ft.write("$" + latex((binomial(n,k)*(p**k)*(1-p)**(n-k)*100).evalf(4)) + "\\%$")
    

def binomial_pdf(n="",p="",k=""):
    if n == "":
        n = random.randint(21,29)
    if p == "":
        #p = Float(random.random()).evalf(4)
        p = random.choice([0.3,0.4,0.6,0.7])
    if k == "":
        k = int(n*p)
        #k=random.randint(0,n)

    aufgabe="$n=" + latex(n) + "$, $p=" + latex(p) + "$, $k=" + latex(k) + "$"
    lsg="$" + latex((binomial(n,k)*(p**k)*(1-p)**(n-k)*100).evalf(4)) + "$"
    lsg_2="$P(X=" + latex(k) + ")=\\binom{" + latex(n) + "}{" + latex(k) + "}\\cdot" + latex(p) + "^{" + latex(k) + "}\\cdot" + latex(1-p) + "^{" + latex(n-k) + "}=" + latex((binomial(n,k)*(p**k)*(1-p)**(n-k)*100).evalf(4)) + "$"
    return [aufgabe,lsg,lsg_2,aufgabe + "\\\\ \n" + lsg_2]


def binomial_cdf(n="",p="",k1=0,k2=0):
    if n == "":
        n = random.choice([20,50,80,100])

    if p == "":
        #p = Float(random.random()/2.0).evalf(4)
        p = random.choice([0.1,0.5,0.25,0.4,Rational(1,3),Rational(1,6)])



    if k1 == 0 and k2 == 0:
        art = random.choice([0,1,2])
    elif k1 == 0:
        art=0;
    elif k2 == 0:
        art=1;
    else:
        art=2

    if art == 0:
        k1 == 0
        #k2 = random.randint(0,n)
        k2 = int(n*p)
    elif art == 1:
        #k1 = random.randint(0,n)
        k1 = int(n*p)
        k2 = n
    elif art == 2:
        #k1 = random.randint(0,n)
        #k2 = random.randint(k1,n)
        k1=int(n*p-sqrt(n*p*(1-p)))
        k2=int(n*p+sqrt(n*p*(1-p)))

    verbal = random.choice([False,True])
    


    if art == 2: 
        aufgabe="$n=" + latex(n) + "$, $p=" + latex(p) + "$, " + "$" + latex(k1) + "\\leq k \\leq " + latex(k2) + "$"
    elif art == 1:
        if verbal == False:
            aufgabe="$n=" + latex(n) + "$, $p=" + latex(p) + "$, " + "$" + latex(k1) + "\\leq k $"
        elif verbal == True:
            aufgabe="$n=" + latex(n) + "$, $p=" + latex(p) + "$, " + "$k$ mindestens " + math(latex(k1))

    elif art == 0:
        if verbal == False:
            aufgabe="$n=" + latex(n) + "$, $p=" + latex(p) + "$, " + "$k \\leq " + latex(k2) + "$"
        if verbal == True:
            aufgabe="$n=" + latex(n) + "$, $p=" + latex(p) + "$, " + "$k$ höchstens " + math(latex(k2))


    lsg=0
    for k in range(k1,k2+1):
        lsg += (binomial(n,k)*(p**k)*(1-p)**(n-k)*100).evalf(4)

    lsg=math(latex(lsg))
    
    if art == 2:
        lsg_2="$P(" + latex(k1) + "\\leq X \\leq " + latex(k2) + ")=$ " + latex(lsg)
    elif art == 0:
        lsg_2="$P(X \\leq " + latex(k2) + ")=$ " + latex(lsg)

    elif art == 1:
        lsg_2="$P(" + latex(k1) + "\\leq X)=$ " + latex(lsg)

    return [aufgabe,lsg,lsg_2,aufgabe + "\\\\ \n" + lsg_2]


def aufg_bernoulli(aufgabentext="Bestimmen Sie die Wahrscheinlichkeiten der Bernoulli-Experimente mit den folgenden Kenngrößen und Trefferangaben.",anzahl=3,verbal=False):
    aufgabe=aufgabentext + "\\\\ \n"
    

    aufgaben=[]
    loesungen=[]
    binom=[]
    binom.append(binomial_pdf())
    #aufgaben.append(binom[0])
    #loesungen.append(binom[2])

    for i in range(anzahl-1):
        binom.append(binomial_cdf())
        #aufgaben.append(binom[0])
        #loesungen.append(binom[2])


    aufgaben=[]
    loesungen=[]
    for i in binom:
        aufgaben.append(i[0])
        loesungen.append(i[3])



    aufgabe = makeExercise(aufgabe=multicol(aufgaben,2),punkte="8",aufgabentext=aufgabentext)

    loesung = makeExercise(multicol(loesungen,2))

    #return [aufgabe,loesung]
    return binom



def kreuze_mengen(mengen):
    ### Tupel fuer jedes Element der ersten Menge erzeugen
    if not type(mengen[0][0]) is tuple:
        for i,element in enumerate(mengen[0]):
            mengen[0][i]=(element,)
            

    if len(mengen) == 1:
        return mengen[0]

    elif len(mengen) == 2:
        alte_kombinationen=mengen[0]
        neue_kombinationen=[]
        for kombination in alte_kombinationen:
            for element in mengen[1]:
                neue_kombinationen.append(kombination + (element,))

        return neue_kombinationen
        

    elif len(mengen) > 2:
        alte_kombinationen=mengen[0]
        neue_kombinationen=[]
        for kombination in alte_kombinationen:
            for element in mengen[1]:
                neue_kombinationen.append(kombination + (element,))

        mengen.pop(0)
        mengen[0]=neue_kombinationen
        
        return kreuze_mengen(mengen)
    else:
        return ""


def ergebnismenge(kugeln="",zuege="",zuruecklegen="",reihenfolge=""):
    ### Kugeln zufaellig bereit stellen
    if kugeln == "":
        anzahl_arten=random.randint(1,5)

        arten=["g","b","v","s","r","w","l","o"]
        art=[]
        anzahl=[]
        for i in list(range(anzahl_arten)):
            art_zuf=random.choice(arten)
            art.append(art_zuf)
            anzahl.append(random.randint(1,5))
            arten.remove(art_zuf)

        kugeln_dict=dict(zip(art,anzahl))

        ### Kugeln als Liste: b,b,b,r,r,..
        kugeln = []

        for item in kugeln_dict.items():
            for anz in list(range(item[1])):
                kugeln.append(item[0])

    if type(kugeln) is dict:
        kugeln_dict=kugeln
        ### Kugeln als Liste: b,b,b,r,r,..
        kugeln = []

        for item in kugeln_dict.items():
            for anz in list(range(item[1])):
                kugeln.append(item[0])


    ### zufallige Anzahl der Zuege
    if zuege == "":
        zuege=random.randint(2,2)


    ### Prinzip 1: Mit Zuruecklegen, mit Reihenfolge
    if zuruecklegen == "mZ" and reihenfolge == "mR":

        kugeln_set=set(kugeln)
        
        hilfsmengen=[]
        for zug in list(range(zuege)):
            hilfsmengen.append(list(kugeln_set))        

        ergebnismenge=kreuze_mengen(hilfsmengen)

        return set(ergebnismenge)


    ### Prinzip 2: Mit Zuruecklegen, ohne Reihenfolge
    if zuruecklegen == "mZ" and reihenfolge == "oR":

        kugeln_set=set(kugeln)
        
        hilfsmengen=[]
        for zug in list(range(zuege)):
            hilfsmengen.append(list(kugeln_set))        

        ergebnismenge=kreuze_mengen(hilfsmengen)

        for i,ergebnis in enumerate(ergebnismenge):
            ergebnis_list=list(ergebnis)
            ### sortieren
            ergebnis_list.sort()
            ### gleiche Eintraege loeschen
            ergebnismenge[i]=tuple(ergebnis_list)

        return set(ergebnismenge)



    ### Prinzip 3: Ohne Zuruecklegen, mit Reihenfolge
    if zuruecklegen == "oZ" and reihenfolge == "mR":

        kugeln_set=set(kugeln)
        
        hilfsmengen=[]
        for zug in list(range(zuege)):
            hilfsmengen.append(list(kugeln_set))        

        ergebnismenge=kreuze_mengen(hilfsmengen)

        ergebnismenge_oZ=[]
        for i,kombinationen in enumerate(ergebnismenge):
            auftreten=Counter(kombination for kombination in kombinationen)
            weniger=True
            for symbol in kugeln_dict:
                if auftreten.get(symbol) > kugeln_dict.get(symbol):
                    weniger=False
            if weniger == True:
                ergebnismenge_oZ.append(kombinationen)

        return set(ergebnismenge_oZ)




    ### Prinzip 3: Ohne Zuruecklegen, ohne Reihenfolge
    if zuruecklegen == "oZ" and reihenfolge == "oR":

        kugeln_set=set(kugeln)
        
        hilfsmengen=[]
        for zug in list(range(zuege)):
            hilfsmengen.append(list(kugeln_set))        

        ergebnismenge=kreuze_mengen(hilfsmengen)

        ergebnismenge_oZ=[]
        for i,kombinationen in enumerate(ergebnismenge):
            auftreten=Counter(kombination for kombination in kombinationen)
            weniger=True
            for symbol in kugeln_dict:
                if auftreten.get(symbol) > kugeln_dict.get(symbol):
                    weniger=False
            if weniger == True:
                ergebnismenge_oZ.append(kombinationen)

        ergebnismenge=ergebnismenge_oZ

        for i,ergebnis in enumerate(ergebnismenge):
            ergebnis_list=list(ergebnis)
            ### sortieren
            ergebnis_list.sort()
            ### gleiche Eintraege loeschen
            ergebnismenge[i]=tuple(ergebnis_list)


        return set(ergebnismenge)

    
