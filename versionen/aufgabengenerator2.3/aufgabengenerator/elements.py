#! /usr/bin/env python

## Author: Pasquale Franz
## Date: 26.01.2015

######
## Generate a table in latex-format with given values

from sympy.abc import *
#from skelet import Skelet


def preambel():
    str="\\documentclass[12pt]{article}\n\
\\usepackage[utf8]{inputenc}\n\
\\usepackage{paralist} \n\
\\usepackage{amssymb}  \n\
\\usepackage{amsthm}   \n\
\\usepackage{multicol} \n\
\\usepackage[left=1.5cm,right=1.5cm,top=0cm,bottom=0cm]{geometry} \n\
\\usepackage{amsmath}  \n\
\\usepackage{pgf,tikz} \n\
\\usetikzlibrary{arrows} \n\
\\pagestyle{empty} \n\
\\newtheoremstyle{note} \n\
{16pt}  % Platz zwischen Kopf und voherigem Text \n\
{16pt}  % und nachfolgendem Text \n\
{}     % Schriftart des Koerpers \n\
{}     % mit \parindent Einzug \n\
{\\bf}  % Schriftart des Kopfes \n\
{:}     % Nach Bedarf z.B. Doppelpunkt nach dem Kopf \n\
{0.5em} % Platz zwischen Kopf und Koerper \n\
{}     % Kopfname \n\n\
\\theoremstyle{note} \n\
\\newtheorem{aufgabe}{Aufgabe} \n\n\n\n"
    return str

def math(latexexpr):
    return "$" + latexexpr + "$"

def mmath(latexexpr):
    return "\\[" + latexexpr + "\\]"

def scriptstyle(latexexpr):
    return "$ \\scriptstyle" + latexexpr + "$"

        

def makeExercise(aufgabe):
    str="\\begin{aufgabe} ~ \\\\ \n"
    str+=aufgabe
    str+="\\end{aufgabe} \n"
    return str

def makeSheet(exercises):
    str=preambel()
    str+="\\begin{document} \n\
    \\begin{flushleft}\n"
    str+=exercises
    str+="\\end{flushleft} \n\
    \\end{document}"
    return str

def teileBlatt(links,rechts,inhalt1,inhalt2):
    str1="\\begin{minipage}{" + str(links-0.1) + "\\textwidth} \n"
    str2=inhalt1
    str3="\\end{minipage} \n"
    str4="\\begin{minipage}{0.1\\textwidth} \n ~ \\end{minipage} \n"
    str5="\\begin{minipage}{" + str(rechts-0.1) + "\\textwidth} \n"
    str6=inhalt2
    str7="\\end{minipage} \n\n"
    return str1+str2+str3+str4+str5+str6+str7


def table(x,y):
    latex_str='\\begin{tabular}{'
    appear=1
    for i in x:
        latex_str+='c'
        if appear < len(x):
            latex_str+='|'
        appear+=1
    latex_str+='}\n'
    appear=1
    for i in x:
        latex_str+=str(i)
        if appear < len(x):
            latex_str+='&'
        appear+=1
    latex_str+='\\\\ \\hline \n'
    appear=1
    for i in y:
        latex_str+=str(i)
        if appear < len(y):
            latex_str+='&'
        appear+=1
    latex_str+='\n\\end{tabular} \n\n'
    return latex_str

def zeichneGraph(funktionenliste,scale=1):
        str1="""\\definecolor{cqcqcq}{rgb}{0.75,0.75,0.75} 
\\begin{tikzpicture}[scale=""" + str(scale) + """][line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm] 
\\draw [color=cqcqcq,dash pattern=on 2pt off 2pt, xstep=1.0cm,ystep=1.0cm] (-6.33,-6.57) grid (6.29,6.53); 
\\draw[->,color=black] (-6.33,0) -- (6.29,0); 
\\foreach \\x in {-6,-4,-2,2,4,6} 
\\draw[shift={(\\x,0)},color=black] (0pt,2pt) -- (0pt,-2pt) node[below] {\\footnotesize $\\x$}; 
\\draw[color=black] (6,0.07) node [anchor=south west] { x}; 
\\draw[->,color=black] (0,-6.57) -- (0,6.53); 
\\foreach \\y in {-6,-4,-2,2,4,6} 
\\draw[shift={(0,\\y)},color=black] (2pt,0pt) -- (-2pt,0pt) node[left] {\\footnotesize $\\y$}; 
\\draw[color=black] (0.09,6.17) node [anchor=west] { y}; 
\\draw[color=black] (0pt,-10pt) node[right] {\\footnotesize $0$}; 
\\clip(-6.33,-6.57) rectangle (6.29,6.53);"""
        str2=""
        for funktion in funktionenliste:
            str2+="\\draw [domain=-6.33:6.29] plot(\\x,{(" + str(funktion.a) + "*\\x+" + str(funktion.b) + "}); \n"
        str3="\\end{tikzpicture} \n\
\\hspace{1cm}"
        return str1 + str2 + str3

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
         
def enumlist(inhaltsliste):
    latex_str="\\begin{enumerate}[a)] \n"
    for inhalt in inhaltsliste:
        latex_str+='\\item \n'
        latex_str+=inhalt
        latex_str+='\n'
    latex_str+='\\end{enumerate} \n'
    return latex_str
   


