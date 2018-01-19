#! /usr/bin/env python

## Author: Pasquale Franz
## Date: 26.01.2015


import random
from sympy import *
from sympy.abc import *
from functions import *
import re


##### Hilfsfunktionen fuer Berechnungen

def loeseGlg(term1,term2):
    glg=Eq(term1,term2)
    lsg=solve(glg,x)
    return lsg

def berechneNullstellen(funktion):
    return funktion.nullstelle()


def header():
    latexstr="\\usepackage{fancyheadings} \n\
\\pagestyle{fancy} \n\
\\headheight1.6cm \n\
\\lhead{} \n\
\\chead{Prozentrechnung} \n\
\\rhead{\includegraphics[scale=0.5]{/home/pfranz/hbo/logo.png}} \n\
\\lfoot{} \n\
\\cfoot{} \n\
\\rfoot{} \n"
    return latexstr


### Die Praeambel einer Latex-Datei
### Hier koennen grundlegende Einstellungen des Layouts getroffen werden.
def preambel():
    str="\\documentclass[12pt,fleqn]{article}\n\
\\usepackage[utf8]{inputenc}\n\
\\usepackage{paralist} \n\
\\usepackage{amssymb}  \n\
\\usepackage{amsthm}   \n\
\\usepackage{eurosym} \n\
\\usepackage{multicol} \n\
\\usepackage[left=1.5cm,right=1.5cm,top=1.5cm,bottom=0.5cm]{geometry} \n"
    str+=header()
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
def makeExercise(aufgabe):
    latexstr="\\begin{aufgabe} ~ \\\\ \n"
    latexstr+=aufgabe
    latexstr+="\\end{aufgabe} \n"
    return latexstr

def makeExample(aufgabe):
    latexstr="\\begin{beispiel} ~ \\\\ \n"
    latexstr+=aufgabe
    latexstr+="\\end{beispiel} \n"
    return latexstr

### Erstellt aus dem uebergebenen Parameter ein Latex-Dokument
### Eingabe und Ausgabe: Latex-Ausdruck
def makeSheet(exercises):
    latexstr=preambel()
    latexstr+="\\begin{document} \n\
    \\begin{flushleft}\n"
    latexstr+="Name: \\hspace{12cm} Datum:"
    latexstr+=exercises
    latexstr+="\\end{flushleft} \n\
    \\end{document}"
    return latexstr


##### Zahlen

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


        













