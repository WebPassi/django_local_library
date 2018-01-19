#! /usr/bin/env python

## Author: Pasquale Franz
## Date: 26.01.2015

######
## Generate a table in latex-format with given values

from sympy.abc import *
#from skelet import Skelet


class Skelet:
    def head(self):
        str="\\documentclass[12pt]{article}\n\
\\usepackage[utf8]{inputenc}\n\
\\usepackage{paralist} \n\
\\usepackage{amssymb}  \n\
\\usepackage{amsthm}   \n\
\\usepackage{multicol} \n\
\\usepackage[left=1.5cm,right=1.5cm,top=0.8cm,bottom=1cm]{geometry} \n\
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
\\newtheorem{aufgabe}{Aufgabe} \n\n\n\n\
\\begin{document}\n\
\\begin{flushleft}\n"
        return str
    def end():
        str="\\end{flushleft} \\\\ \n\
\\end{document}"
        return str


class Table:
    def centered(self,x,y):
        lf = open('tabelle.tex','a')
        lf.write('\\begin{tabular}{')
        appear=1
        for i in x:
            lf.write('c')
            if appear < len(x):
                lf.write('|')
            appear+=1
        lf.write('}\n')
        appear=1
        for i in x:
            lf.write(str(i))
            if appear < len(x):
                lf.write('&')
            appear+=1
        lf.write('\\\\ \\hline \n')
        appear=1
        for i in y:
            lf.write(str(i))
            if appear < len(y):
                lf.write('&')
            appear+=1
        lf.write('\\end{tabular} \n\n \\vspace{0.5cm}')

class Multicol:
    def col(self,aufgabe):
        lf = open('datei.tex','a')
        lf.write('\\begin{aufgabe} ~ \\ \n')
        lf.write('\\begin{multicols}{2} \n')
        lf.write('\\begin{enumerate}[a)] \n')
        for i in range(1,3):
            lf.write('\\item ')
            lf.write('test')
            aufgabe.graph_zeichnen()
            lf.write('\n')
        lf.write('\\end{enumerate} \n')
        lf.write('\\end{multicols} \n')
        lf.write('\\end{aufgabe}')
            


