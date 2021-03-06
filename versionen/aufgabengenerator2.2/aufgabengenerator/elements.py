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
            


