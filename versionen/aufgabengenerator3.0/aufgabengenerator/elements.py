#! /usr/bin/env python

## Author: Pasquale Franz
## Date: 26.01.2015


import random
from sympy import *
from sympy.abc import *
from functions import *
import re


class Aufgabe():
    ""
    
    
    




##### Hilfsfunktionen fuer Berechnungen
def normiereEinheit(einheit):
    if einheit == "ha":
        return 10**4
    elif einheit == "a":
        return 10**2
    
    elif einheit == "l":
        return 10**(-3)
        

    elif len(einheit.split("^")[0]) == 1:
        return 1

    else:
        try:
            dim=int(einheit.split("^")[1])
        except:
            dim=1

        praefix=einheit[0]

        if praefix == "k":
            return 10**(3*dim)

        elif praefix == "M":
            return 10**(6*dim)

        elif praefix == "G":
            return 10**(9*dim)

        elif praefix == "d":
            return 10**(-1*dim)

        elif praefix == "c":
            return 10**(-2*dim)

        elif praefix == "m":
            return 10**(-3*dim)


def normiereEinheitZehnerpotenz(einheit):
    if einheit == "ha":
        return "\\cdot 10^4"
    elif einheit == "a":
        return "\\cdot 10^2"

    elif einheit == "l":
        return "\\cdot 10^{-3}"


    elif len(einheit.split("^")[0]) == 1:
        return ""

    else:
        try:
            dim=int(einheit.split("^")[1])
        except:
            dim=1

        praefix=einheit[0]

        if praefix == "k":
            return "\\cdot 10^" + str(3*dim) 

        elif praefix == "M":
            return "\\cdot 10^" + str(6*dim)

        elif praefix == "G":
            return "\\cdot 10^" + str(9*dim)

        elif praefix == "d":
            return "\\cdot 10^" + str(-1*dim)

        elif praefix == "c":
            return "\\cdot 10^" + str(-2*dim)

        elif praefix == "m":
            return "\\cdot 10^" + str(-3*dim)

## Gibt den Exponenten zurueck
def normiereEinheitNurExponent(einheit):
    if einheit == "ha":
        return str(4)
    elif einheit == "a":
        return str(2)

    elif einheit == "l":
        return str(-3)


    elif len(einheit.split("^")[0]) == 1:
        return ""

    else:
        try:
            dim=int(einheit.split("^")[1])
        except:
            dim=1

        praefix=einheit[0]

        if praefix == "k":
            return str(3*dim)

        elif praefix == "M":
            return str(6*dim)

        elif praefix == "G":
            return str(9*dim)

        elif praefix == "d":
            return str(-1*dim)

        elif praefix == "c":
            return str(-2*dim)

        elif praefix == "m":
            return str(-3*dim)


def grundeinheit(einheit):
    if einheit == "ha" or einheit == "a": 
        return "m^2"
    elif einheit == "l":
        return "m^3"
    else:
        if len(einheit.split("^")[0]) == 1:
            return einheit.split("^")[0]
        else:
            return (einheit.split("^")[0])[1]



def einheitLatex(einheit):
    if " " in einheit:
        zahl=einheit.split(" ")[0]
        einheit=einheit.split(" ")[1]
    else:
        zahl=""
        einheit=einheit
        
    try:
        return zahl + "\\mathrm{\\," + einheit.split("^")[0] + "}^" + einheit.split("^")[1] 
    except: 
        return zahl + "\\mathrm{\\," + einheit + "}"



def einheitLatexBruch(einheit):
    z=re.split("[{}]",einheit)[1]
    n=re.split("[{}]",einheit)[3]

    bruch=einheit.replace(z,einheitLatex(z))
    bruch=einheit.replace(n,einheitLatex(n))
    
    return bruch



def einheitPraefix(einheit):
    if einheit == "ha" or einheit == "a":
        return ""
    else:
        if len(einheit)>1:
            return einheit[0]
        else:
            return ""


def einheitNorm(einheit):
    if einheit == "ha" or einheit == "a" or einheit == "l":
        return "m"
    else:
        if len(einheit.split("^")[0]) == 1:
            return einheit
        else:
            ge=""
            for i in range(len(einheit)):
                if i == 0:
                    continue
                else:
                    ge+=einheit[i]
            return ge


def einheitDim(einheit):
    if einheit == "ha": 
        return 4
    elif einheit == "a":
        return 2
    elif einheit == "l":
        return -3
    else:
        try:
            dim=int(einheit.split("^")[1])
        except:
            dim=1
        return dim


def einheitenRechnerDiv(einheit1,einheit2):
    if einheit1 == "" and einheit2 == "":
        return ""

    elif einheit1 == "":
        return "\\frac{1}{" + einheit2 + "}"

    elif einheit2 == "":
        return einheit1

    elif grundeinheit(einheit1) == grundeinheit(einheit2):
        if einheitDim(einheit1) == einheitDim(einheit2):
            return ""

        elif einheitDim(einheit1) > einheitDim(einheit2):
            if einheitDim(einheit1)-einheitDim(einheit2) == 1:
                return grundeinheit(einheit1)
            else:
                return grundeinheit(einheit1) + "^" + latex(int(einheitDim(einheit1)-einheitDim(einheit2)))
 
        elif einheitDim(einheit1) < einheitDim(einheit2):
            if einheitDim(einheit1)-einheitDim(einheit2) == -1:
                return "\\frac{1}{" + grundeinheit(einheit1) + "}"
            else:
                return "\\frac{1}{" + grundeinheit(einheit1) + "^" + latex(int(einheitDim(einheit2)-einheitDim(einheit1))) + "}"

    else:
        return "\\frac{" + einheit1 + "}{" + einheit2 + "}"

        
    



def loeseGlg(term1,term2):
    glg=Eq(term1,term2)
    lsg=solve(glg,x)
    return lsg

def berechneNullstellen(funktion):
    return funktion.nullstelle()


def header(title,klasse):
    latexstr="\\usepackage{fancyheadings} \n\
\\pagestyle{fancy} \n\
\\headheight1.6cm \n\
\\lhead{" + klasse + "} \n\
\\chead{" + latex(title) +"} \n\
\\rhead{\includegraphics[scale=0.5]{logo.png}} \n\
\\lfoot{} \n\
\\cfoot{} \n\
\\rfoot{} \n"
    return latexstr


### Die Praeambel einer Latex-Datei
### Hier koennen grundlegende Einstellungen des Layouts getroffen werden.
def preambel(title,klasse):
    str="\\documentclass[12pt,fleqn]{article}\n\
\\usepackage[utf8]{inputenc}\n\
\\usepackage{paralist} \n\
\\usepackage{amssymb}  \n\
\\usepackage{amsthm}   \n\
\\usepackage{eurosym} \n\
\\usepackage{multicol} \n\
\\usepackage[left=1.5cm,right=1.5cm,top=1.5cm,bottom=0.5cm]{geometry} \n"
    str+=header(title,klasse)
    str+="\\usepackage{amsmath}  \n\
\\usepackage{cancel} \n\
\\usepackage{pgf,tikz} \n\
\\usetikzlibrary{arrows} \n\
\\newtheoremstyle{aufg} \n\
{16pt}  % Platz zwischen Kopf und voherigem Text \n\
{16pt}  % und nachfolgendem Text \n\
{}     % Schriftart des Koerpers \n\
{}     % mit \parindent Einzug \n\
{\\bf}  % Schriftart des Kopfes \n\
{:}     % Nach Bedarf z.B. Doppelpunkt nach dem Kopf \n\
{0.5em} % Platz zwischen Kopf und Koerper \n\
{}     % Kopfname \n\n\
\\theoremstyle{aufg} \n\
\\newtheorem{aufgabe}{Aufgabe} \n\n\n\n\
\\newtheoremstyle{bsp} \n\
{16pt}  % Platz zwischen Kopf und voherigem Text \n\
{16pt}  % und nachfolgendem Text \n\
{}     % Schriftart des Koerpers \n\
{}     % mit \parindent Einzug \n\
{\\em}  % Schriftart des Kopfes \n\
{:}     % Nach Bedarf z.B. Doppelpunkt nach dem Kopf \n\
{0.5em} % Platz zwischen Kopf und Koerper \n\
{}     % Kopfname \n\n\
\\theoremstyle{bsp} \n\
\\newtheorem{beispiel}{Beispiel} \n\n\n\n"
    return str


### Die Praeambel einer Latex-Datei
### Hier koennen grundlegende Einstellungen des Layouts getroffen werden.
def zertifikat(title,klasse):
    str=open("zertifikate/zertifikat.tex").read()
    return str





### Gibt einen Ausdruck im einfachen Mathemodus aus
def math(latexexpr):
    return "$" + latexexpr + "$"

### Gibt einen Ausdruck im abgesetzten Mathemodus aus
def mmath(latexexpr):
    return "\\[" + latexexpr + "\\]"

### Kleine Schrift
def scriptstyle(latexexpr):
    return "$ \\scriptstyle" + latexexpr + "$"

        
### Erstellt eine Aufgabe in der Latex-Umgebung aufgabe
### Eingabe und Ausgabe: Latex-Ausdruck
def makeExercise(aufgabe,punkte=""):
    if punkte == "":
        latexstr="\\begin{aufgabe} ~ \\\\ \n"
        latexstr+=aufgabe
        latexstr+="\\end{aufgabe} \n"
    else:
        latexstr="\\begin{aufgabe}\\framebox{\\qquad/" + punkte + "} ~ \\\\ \n"
        latexstr+=aufgabe
        latexstr+="\\end{aufgabe} \n"
    
    return latexstr

def makeExample(aufgabe):
    latexstr="\\begin{beispiel} ~ \\\\ \n"
    latexstr+=aufgabe
    latexstr+="\\end{beispiel} \n"
    return latexstr


def grundniveau(aufgaben,lsg="n"):
    punkte=0
    for a in aufgaben:
        punkte+=a.punkte

    if lsg == "n":
        latexstr="\\begin{center} \\begin{framed} Grundniveau (" + str(punkte) + " Punkte) \\end{framed} \\end{center}"
        for a in aufgaben:
            latexstr+=a.aufgabe

        latexstr+="\n \\clearpage \n"



    if lsg == "a":
        latexstr="\\begin{center} \\begin{framed} Grundniveau (" + str(punkte) + " Punkte) \\end{framed} \\end{center}"
        for a in aufgaben:
            latexstr+=a.lsg
    
        latexstr+="\n \\clearpage \n"

    return latexstr


def standardniveau(aufgaben,lsg="n"):
    punkte=0
    for a in aufgaben:
        punkte+=a.punkte

    if lsg == "n":
        latexstr="\\begin{center} \\begin{framed} Standardniveau (" + str(punkte) + " Punkte) \\end{framed} \\end{center}"
        for a in aufgaben:
            latexstr+=a.aufgabe



    if lsg == "a":
        latexstr="\\begin{center} \\begin{framed} Standardniveau (" + str(punkte) + " Punkte) \\end{framed} \\end{center}"
        for a in aufgaben:
            latexstr+=a.lsg
    
        
    return latexstr



def highniveau(aufgaben,lsg="n"):
    punkte=0
    for a in aufgaben:
        punkte+=a.punkte

    if lsg == "n":
        latexstr="\\begin{center} \\begin{framed} Erh\\\"ohtes Niveau (" + str(punkte) + " Punkte) \\end{framed} \\end{center}"
        for a in aufgaben:
            latexstr+=a.aufgabe

    if lsg == "a":
        latexstr="\\begin{center} \\begin{framed} Erh\\\"ohtes Niveau (" + str(punkte) + " Punkte) \\end{framed} \\end{center}"
        for a in aufgaben:
            latexstr+=a.lsg
    
    return latexstr





### Erstellt aus dem uebergebenen Parameter ein Latex-Dokument
### Eingabe und Ausgabe: Latex-Ausdruck
def makeSheet(exercises,title="",klasse=""):
    latexstr=zertifikat(title,klasse)
    latexstr+="\\begin{document} \n\
    \\begin{flushleft}\n"
    latexstr+="\\begin{center}" + title + "\\end{center}"

    if type(exercises) is not list:
        latexstr+=exercises
    else:
        for ex in exercises:
            latexstr+=ex
        
    latexstr+="\\end{flushleft} \n\
\\end{document}"
    return latexstr




### Erstellt aus dem uebergebenen Parameter ein Latex-Dokument
### Eingabe und Ausgabe: Latex-Ausdruck
def makeZertifikat(exercises,title,punkte,zeit=45,hilfsmittel=["TR","FS"]):
    
    ### Legende, Formelsammlung fuer FS, ...
    for i,hm in enumerate(hilfsmittel):
        if hm == "TR":
            hilfsmittel[i]="nicht programmierf\\\"ahiger Taschenrechner"
        elif hm == "FS":
            hilfsmittel[i]="Formelsammlung"
        else:
            hilfsmittel[i]=hm

    latexstr=zertifikat(title,klasse="")
    latexstr+="\\begin{document} \n\
    \\begin{flushleft}\n"

    latexstr+="\\begin{center}{Schriftliche Arbeit zum Erwerb eines Zertifikats im Fach Mathematik}\\end{center} \n"
    latexstr+="\\begin{center}{\\Large " + title + "}\\end{center} \n\
\\renewcommand{\\arraystretch}{2.15} \n\
\\begin{tabular}{|p{10cm}|p{2cm}|p{2cm}|p{2cm}|} \n\
\\hline \n\
\\hspace{2cm} Punkte von \\qquad" + str(punkte) + "\\qquad Punkten erreicht & \\hspace{1.2cm} NP & G & E \\\\ \n\
\\hline \n\
\\end{tabular} \\\\[1em]    \n"

    latexstr+="{\\bf Hilfsmittel: }" + hilfsmittel[0] + ", " + hilfsmittel[1] + "\\\\ \n"
    latexstr+="{\\bf Zeit: }" + str(zeit) + " Minuten" + "\\\\ \n"

    latexstr+="\\begin{center} {\\bf Bearbeite so viele Aufgaben wie m\\\"oglich.} \\end{center}"


    if type(exercises) is not list:
        latexstr+=exercises
    else:
        for ex in exercises:
            latexstr+=ex


    latexstr+="\\end{flushleft} \n\
    \\end{document}"
    return latexstr





##### Zahlen

def makereal(field):
    i=0
    for index in range(len(field)):
        try:
            if "I" in str(field[index]):
                continue
            else:
                i+=1
        except IndexError:
            break
    liste=range(i)
    j=0
    for index in range(len(field)):
        try:
            if "I" in str(field[index]):
                continue
            else:
                liste[j]=field[index]
                j+=1
        except IndexError:
            break
    return liste


def vorzeichenpro(zahl):
    if zahl > 0:
        if zahl == 1:
            return ""
        else:
            return latex(zahl)
    elif zahl < 0:
        if zahl == -1:
            return "-"
        else:
            return latex(zahl)
    else:
        return ""

def vorzeichensum(zahl):
    if zahl > 0:
        return "+" 
    elif zahl < 0:
        return "-"
    else:
        return ""

def vorzeichensumpro(zahl):
    if zahl > 0:
        if zahl == 1:
            return "+"
        else:
            return "+" + latex(zahl)
    elif zahl < 0:
        if zahl == -1:
            return "-"
        else:
            return latex(zahl)
    else:
        return ""

def minusklammer(zahl):
    if zahl < 0:
        return "(" + latex(zahl) + ")"
    else:
        return latex(zahl)


### Gibt die Summanden eines Polynoms als Liste zurueck 
def zerlegung(expr):
    sum=expr.split(r"[+,-]")
    return sum
    
### Bruchdarstellung mit separiertem x
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

### Nummeriert die uebergebenen Funktionen und benennt sie entsprechend (z.B. f_1,...) 
### Eingabe: Liste von Funktionstermen
### Ausgabe: Liste von Funktionsgleichungen: z.B. f_1(x)=x, f_2(x)= ...
def erstelleFunktionsliste(funktionsliste,name="f"):
    enumfunktion=list(range(len(funktionsliste)))
    for index,funktion in enumerate(funktionsliste):
        funktion.name=latex(name) + "_" + latex(index+1)
        enumfunktion[index]="$" + latex(funktion.name) + "(x)=" + latex(funktion.expr) + "$"
    return enumfunktion

def nummeriereFunktionen(funktionsliste,name="f"):
    enumfunktion=list(range(len(funktionsliste)))
    for index,funktion in enumerate(funktionsliste):
        funktion.name=latex(name) + "_" + latex(index+1)
    return funktionsliste


### Nummeriert die uebergebenen Funktionen und benennt sie entsprechend (z.B. f_1,...) 
### Eingabe: Liste von Funktionstermen
### Ausgabe: Liste von Funktionsnamen: z.B. f_1, f_2, ...
def erstelleNamensliste(funktionsliste,name="f"):
    enumfunktion=list(range(len(funktionsliste)))
    for index,funktion in enumerate(funktionsliste):
        funktion.name=latex(name) + "_" + latex(index+1)
        enumfunktion[index]=math(latex(funktion.name))
    return enumfunktion

### Darstellung von den Loesungen einer Gleichung
### Keine komplexen Zahlen
def zeigeErgebnisQuad(solset):
    if "I" in str(solset[0]):
        #math="$L={}"
        anzeige="Keine Nullstelle"
    elif len(solset)==1:
        anzeige="$x=" + latex(solset[0]) + "$"
    elif "sqrt" in str(solset[0]):
        anzeige="$x_1\\approx " + latex(deutsch(runden(solset[0],2))) + "\\quad " + "x_2\\approx" + latex(deutsch(runden(solset[1],2))) + "$"
        anzeige="$x_1\\approx " + latex(deutsch(runden(solset[0],2))) + "\\quad " + "x_2\\approx" + latex(deutsch(runden(solset[1],2))) + "$"
    else:
        anzeige="$x_1=" + latex(solset[0]) + "\\quad " + "x_2=" + latex(solset[1]) + "$"
    return anzeige

### Rundet eine Zahl auf die gewuenschte Nachkommastelle
def runden(evalzahl,nks):
    if "0." in str(evalzahl.evalf(2)):
        return evalzahl.evalf(nks)
    else:
        return evalzahl.evalf(nks+1)   

### Deutsche Darstellung von Kommazahlen
### Ersetzt Punkt durch Komma
def deutsch(kommazahl):
    try:
        return re.sub('\.',',\hspace{-1pt}',str(kommazahl))
    except:
        return kommazahl

### nimmt letzte Zahl in Liste auf
def intervall(a,b):
    liste=list(range(a,b))
    liste.append(b)
    return liste


##### Listen

### Ruft die multicols-Umgebung von Latex auf
### Eingabe: inhalt als Liste von Latex-Ausdruecken, spaltenanzahl
def multicol(inhalt,spalten):
    latex_str='\\begin{multicols}{' + str(spalten) + '} \n'
    latex_str+='\\begin{enumerate}[a)] \n'
    for inh in inhalt:
        latex_str+='\\item \n'
        latex_str+=inh
        latex_str+='\n'
    latex_str+='\\end{enumerate} \n'
    latex_str+='\\end{multicols} \n'
    return latex_str
         
### Ruft die enumerate-Umgebung von Latex auf
### Eingabe: inhalt als Liste von Latex-Ausdruecken
def enumlist(inhaltsliste):
    latex_str="\\begin{enumerate}[a)] \n"
    for inhalt in inhaltsliste:
        latex_str+='\\item \n'
        latex_str+=inhalt
        latex_str+='\n'
    latex_str+='\\end{enumerate} \n'
    return latex_str

##### Tabellen

### Eine Tabelle mit Gitter ohne Eintraege
def plain_table(n,m):
    x=list(range(n))
    y=list(range(m))
    latex_str='\\begin{tabular}{'
    # Tabellendesign
    appear=1
    for i in x:
        latex_str+='c'
        if appear < len(x):
            latex_str+='|'
        appear+=1
    latex_str+='}\n'
    # Eintraege
    trennlinie=1
    for j in y:
        appear=1
        for i in x:
            latex_str+=""
            if appear < len(x):
                latex_str+='&'
            appear+=1
        if trennlinie < len(y):
            latex_str+='\\\\ \\hline \n'
        trennlinie+=1
    latex_str+='\n\\end{tabular} \n\n'
    return latex_str

### Erstellt eine Latex-Tabelle aus der uebergebenen Matrix
def table(matrix,stretch=1.0):
    zeilenanz=len(matrix)-1
    spaltenanz=len(matrix[0])-1
    latex_str="\\renewcommand{\\arraystretch}{" + latex(stretch) + "} \n"
    latex_str+='\\begin{tabular}{'
    for j,dump in enumerate(matrix[0]):
        latex_str+='c'
        if j < spaltenanz:
            latex_str+='|'
    latex_str+='}\n'
    for i,zeile in enumerate(matrix):
        for j,eintrag in enumerate(zeile):
            if j < spaltenanz:
                latex_str+=str(eintrag) + " & "
            else: 
                latex_str+=str(eintrag)
        if i < zeilenanz:
            latex_str+='\\\\ \\hline \n'
        else:
            latex_str+='\\\\ \n' 
    latex_str+='\n\\end{tabular} \n\n'    
    return latex_str

    

### Erstellt eine Latex-Tabelle mit Kopf- und Seitenbeschriftung
### Eingabe: kopf und links als Liste
def cross_table(kopf,links,stretch=1.0):
    matrix = [ [""] * (len(kopf)+1) for i in range(len(links)+1)]
    for i,zeile in enumerate(matrix):
        for j,eintrag in enumerate(zeile):
            if i == 0:
                if j == 0:
                    matrix[i][j]=""
                else:
                    matrix[i][j]=kopf[j-1]
            else:
                if j == 0:
                    matrix[i][0]=links[i-1]
    return table(matrix,stretch)

### Wertetabelle
def erstelleWertetabelle(funktion,bereich=list(range(-3,4))):
    intervall=bereich
    x=[]
    y=[]
    for i in intervall:
        x.append(i)
        y.append(runden(funktion.ywert(i),1))
#        y.append(funktion.ywert(i))
    matrix=[x,y]
    return table(matrix)

##### minipage

### Eingabe: links+rechts=1 (z.B. 0.4 und 0.6), inhalt1/2 Latex-Ausdruck
def teileBlatt(inhalt1,inhalt2,links=0.5,rechts=0.5):
    latexstr="\\begin{minipage}{" + latex(links-0.1) + "\\textwidth} \n"
    latexstr+=inhalt1
    latexstr+="\\end{minipage} \n"
    latexstr+="\\begin{minipage}{0.1\\textwidth} \n ~ \\end{minipage} \n"
    latexstr+="\\begin{minipage}{" + latex(rechts-0.1) + "\\textwidth} \n"
    latexstr+=inhalt2
    latexstr+="\\end{minipage} \n\n"
    return latexstr

##### Graphen und Funktionen

def zeigeFunktionsgleichung(funktionsliste,abstand=0):
    if type(funktionsliste) is not list:
        funktionsliste=[funktionsliste]
    latexstr="\\vspace{1em} \n"
    for f in funktionsliste:
        latexstr+=f.anzeigen() + "\\\\[" + latex(abstand) + "em] \n"
    return latexstr

### Notwendige Ersetzungen fuer die Skalierung der Achsen 
def pgflist(a,b):
    numlist=str(range(a,b))
    pgfstr=""
    ## Ersetzt eckige durch geschweifte Klammern
    str1=re.sub(r'\]',r'}',re.sub(r'\[',r'{',numlist))
    ## Spart die Null aus
    str1=re.sub(r',0,','',str1)
    str1=re.sub(r'0,','',str1)
    str1=re.sub(r',0','',str1)
    ## Schreibt die letzte Skalierung
    str1=re.sub(r'}',', ' + latex(b) + '}',str1)
    pgfstr+=str1
    pgfstr+=""
    return pgfstr


### Zeichnet einen Graph   
def zeichneGraph(funktionsliste,dars="allinone",name="y",scale=1,xmin=-3,xmax=3,ymin=-3,ymax=3):
    if type(funktionsliste) is not list:
        funktionsliste=[funktionsliste]
    if dars=="allinone":
        latexstr="\\definecolor{cqcqcq}{rgb}{0.75,0.75,0.75} \n"
        latexstr+="\\begin{tikzpicture}[domain=" + latex(xmin) + ":" + latex(xmax) + ",scale=" + str(scale) + "][line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]" 
        
        # Koordinatengitter
        tol2=0.0
        latexstr+="\\draw[color=cqcqcq,dash pattern=on 2pt off 2pt, xstep=1.0cm,ystep=1.0cm] (" + latex(xmin-tol2) + "," + latex(xmin-tol2) + ") grid (" + latex(xmax+tol2) + "," + latex(ymax+tol2) + "); \n"   
        
        # Achsen
        tolachsen=0.0
        latexstr+="\\draw[->] (" + latex(xmin-tolachsen) + ",0) -- (" + latex(xmax+tolachsen) + ",0) node[below] {\\footnotesize $x$}; \n"
        latexstr+="\\foreach \\x in " + pgflist(xmin,xmax-1) + "\n"
        latexstr+="\\draw[shift={(\\x,0)},color=black] (0pt,2pt) -- (0pt,-2pt) node[below] {\\footnotesize $\\x$};" 
        
        latexstr+="\\draw[->,color=black] (0," + latex(ymin-tolachsen) + ") -- (0," + latex(ymax+tolachsen) + ") node[right] {\\footnotesize $y$}; \n"
        latexstr+="\\foreach \\y in " + pgflist(ymin,ymax-1) + "\n"
        latexstr+="\\draw[shift={(0,\\y)},color=black] (2pt,0pt) -- (-2pt,0pt) node[left] {\\footnotesize $\\y$}; \n" 
        latexstr+="\\draw[color=black] (0pt,-10pt) node[right] {\\footnotesize $0$}; \n"
        
        # Graph
        latexstr+="\\begin{scope} \n"
        tol1=0
        latexstr+="\\clip (" + latex(xmin-tol1) + "," + latex(ymin-tol1) + ") rectangle (" + latex(xmax+tol1) + "," + latex(ymax+tol1) + "); \n"
        for f in funktionsliste:
            latexstr+=f.graph()
            if name=="y":
                latexstr+="\\draw (" + latex(f.d+0.5) + "," + latex(f.e+0.2) + ") node[right] {" + "$\\scriptscriptstyle " + latex(f.name) + "$}; \n"

        latexstr+="\\end{scope} \n"
        latexstr+="\\end{tikzpicture}"
    
    elif dars=="normal":
        latexstr=""
        for f in funktionsliste:
            latexstr+="\\definecolor{cqcqcq}{rgb}{0.75,0.75,0.75} \n"
            latexstr+="\\begin{tikzpicture}[domain=" + latex(xmin) + ":" + latex(xmax) + ",scale=" + str(scale) + "][line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]" 
            
            # Koordinatengitter
            tol2=0.0
            latexstr+="\\draw[color=cqcqcq,dash pattern=on 2pt off 2pt, xstep=1.0cm,ystep=1.0cm] (" + latex(xmin-tol2) + "," + latex(xmin-tol2) + ") grid (" + latex(xmax+tol2) + "," + latex(ymax+tol2) + "); \n"   
            
            # Achsen
            tolachsen=0.0
            latexstr+="\\draw[->] (" + latex(xmin-tolachsen) + ",0) -- (" + latex(xmax+tolachsen) + ",0) node[below] {\\footnotesize $x$}; \n"
            latexstr+="\\foreach \\x in " + pgflist(xmin,xmax-1) + "\n"
            latexstr+="\\draw[shift={(\\x,0)},color=black] (0pt,2pt) -- (0pt,-2pt) node[below] {\\footnotesize $\\x$};" 
            
            latexstr+="\\draw[->,color=black] (0," + latex(ymin-tolachsen) + ") -- (0," + latex(ymax+tolachsen) + ") node[right] {\\footnotesize $y$}; \n"
            latexstr+="\\foreach \\y in " + pgflist(ymin,ymax-1) + "\n"
            latexstr+="\\draw[shift={(0,\\y)},color=black] (2pt,0pt) -- (-2pt,0pt) node[left] {\\footnotesize $\\y$}; \n" 
            latexstr+="\\draw[color=black] (0pt,-10pt) node[right] {\\footnotesize $0$}; \n"
            
            # Graph
            latexstr+="\\begin{scope} \n"
            tol1=0
            latexstr+="\\clip (" + latex(xmin-tol1) + "," + latex(ymin-tol1) + ") rectangle (" + latex(xmax+tol1) + "," + latex(ymax+tol1) + "); \n"
            latexstr+=f.graph()
            if name=="y":
                latexstr+="\\draw (" + latex(f.d+0.5) + "," + latex(f.e+0.2) + ") node[right] {" + "$\\scriptscriptstyle " + latex(f.name) + "$}; \n"
            
            # Graph streichen
            if f.streichen==True:
                latexstr+="\\draw (" + latex(xmin) + "," + latex(ymin) + ") -- (" + latex(xmax) + "," + latex(ymax) + "); \n"
            
            latexstr+="\\end{scope} \n"
            latexstr+="\\end{tikzpicture}"
    return latexstr


        













