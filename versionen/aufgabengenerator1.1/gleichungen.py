#! /usr/bin/env python

## Author: Pasquale Franz
## Date: 03.06.2014

######
## The python-script generates a latex output which, (after compiling with pdflatex) creates random exercise sheets with solution.
## The implented functions (exercises) so far:
## Linear equations:
##   linfunc(): ax+b=c
##   linfunc0(): ax+b=0 
## Quadratical equations:

import random
from sympy import * 
#from sympy import Integral, latex

# erklaere alle buchstaben neutzbaren zu sympy symbolen:
from sympy.abc import *



### note: um einen \ mit write() zu erzeugen muss  \\ getippt werden.



f = open('lehrer.tex', 'w')

f.write('%This is a sympy to latex test.\n\n\n');

f.write('\\documentclass[12pt]{article}\n\
\\usepackage[utf8]{inputenc}\n\
\\usepackage{pgf,tikz}\n\
\\usepackage{fancyhdr}\n\
\\usepackage{paralist} \n\
\\usepackage{amssymb}  \n\
\\usepackage{amsthm}   \n\
\\usepackage{multicol} \n\
\\pagestyle{empty} \n\
\\usepackage[left=1.5cm,right=1.5cm,top=0.8cm,bottom=1cm]{geometry} \n\
\\usepackage{amsmath}  \n\n\n\n');

f.write('\\newtheoremstyle{note} \n\
{16pt}  % Platz zwischen Kopf und voherigem Text \n\
{16pt}  % und nachfolgendem Text \n\
{}     % Schriftart des Koerpers \n\
{}     % mit \parindent Einzug \n\
{\\bf}  % Schriftart des Kopfes \n\
{:}     % Nach Bedarf z.B. Doppelpunkt nach dem Kopf \n\
{0.5em} % Platz zwischen Kopf und Koerper \n\
{}     % Kopfname \n\n\
\\theoremstyle{note} \n\
\\newtheorem{aufgabe}{Aufgabe} \n\n\n\n');


f.write('\\begin{document}\n')
f.write('\\begin{flushleft}\n')

#SymPy-Ausdruck a als String 

def linfunc0():
    a = random.randint(1,10)-5
    if a==0:
        a=1
    b = random.randint(1,10)-5
    linexpr=a*x+b
    glg = Eq(linexpr,0)
    lsg = solve(glg,x)
    f.write(latex(glg,mode='inline'))
    f.write('\\\\')
    f.write('\n')
    f.write(latex(lsg,mode='inline'))
    f.write('\n')

def linfunc():
    a = random.randint(1,10)-5
    if a==0:
        a=1
    b = random.randint(1,10)-5
    c = random.randint(1,10)-5
    linexpr=a*x+b
    glg = Eq(linexpr,c)
    lsg = solve(glg,x)
    f.write(latex(glg,mode='inline'))
    f.write('\\\\')
    f.write('\n')
    f.write(latex(lsg,mode='inline'))
    f.write('\n')


def terme():
    a = random.randint(1,10)-5
    #b = random.randint(1,10)-5
    termexpr = a**y+2*a*y
    glg = expand(termexpr)
    lsg = solve(glg,x)
    f.write(latex(glg,mode='inline'))
    f.write('\\\\')
    if "I" not in str(lsg):
        f.write('\n')
        f.write(latex(lsg,mode='inline'))
        f.write('\n')
    else:
        f.write('\n')
        f.write('No solution')
        f.write('\n')
 


def quadfunc():
    a = random.randint(1,10)-5
    if a==0:
        a=1
    b = random.randint(1,10)-5
    c = random.randint(1,10)-5
    quadexpr=a*x**2+b*x+c
    glg = Eq(quadexpr,0)
    lsg = solve(glg,x)
    f.write(latex(glg,mode='inline'))
    f.write('\\\\')
    if "I" not in str(lsg):
        f.write('\n')
        f.write(latex(lsg,mode='inline'))
        f.write('\n')
    else:
        f.write('\n')
        f.write('No solution')
        f.write('\n')


def quadfuncnormal():
    a = 1
    b = random.randint(1,10)-5
    c = random.randint(1,10)-5
    quadexpr=a*x**2+b*x+c
    glg = Eq(quadexpr,0)
    lsg = solve(glg,x)
    f.write(latex(glg,mode='inline'))
    f.write('\\\\')
    if "I" not in str(lsg):
        f.write('\n')
        f.write(latex(lsg,mode='inline'))
        f.write('\n')
    else:
        f.write('\n')
        f.write('No solution')
        f.write('\n')

def quadfuncnormalsym():
    a = 1
    b = 0
    c = random.randint(1,50)-40
    quadexpr=a*x**2+b*x+c
    glg = Eq(quadexpr,0)
    lsg = solve(glg,x,real=True)
    f.write(latex(glg,mode='inline'))
    f.write('\\\\')
    if "I" not in str(lsg):
        f.write('\n')
        f.write(latex(lsg,mode='inline'))
        f.write('\n')
    else:
        f.write('\n')
        f.write('No solution')
        f.write('\n')

def quadfuncsym():
    a = random.randint(1,10)-5
    if a==0:
        a=1
    b = 0
    c = random.randint(1,10)-9
    quadexpr=a*x**2+b*x+c
    glg = Eq(quadexpr,0)
    lsg = solve(glg,x)
    f.write(latex(glg,mode='inline'))
    f.write('\\\\')
    if "I" not in str(lsg):
        f.write('\n')
        f.write(latex(lsg,mode='inline'))
        f.write('\n')
    else:
        f.write('\n')
        f.write('No solution')
        f.write('\n')

def quadfunchomo():
    a = random.randint(1,10)-5
    if a==0:
        a=1
    b = random.randint(1,10)-5
    c = 0
    quadexpr=a*x**2+b*x+c
    glg = Eq(quadexpr,c)
    lsg = solve(glg,x)
    f.write(latex(glg,mode='inline'))
    f.write('\\\\')
    if "I" not in str(lsg):
        f.write('\n')
        f.write(latex(lsg,mode='inline'))
        f.write('\n')
    else:
        f.write('\n')
        f.write('No solution')
        f.write('\n')


### Aufgabe 1: Lineare Funktionen gleich 0
f.write('\\begin{aufgabe} ~ \\ \n')

f.write('\\begin{multicols}{3} \n')
f.write('\\begin{enumerate}[a)] \n')

for i in range(1,4):
    f.write('\\item ')
    linfunc0() 
    f.write('\n')
f.write('\\end{enumerate} \n')
f.write('\\end{multicols} \n')
f.write('\\end{aufgabe}')
f.write('\\vspace{1em}')

### Aufgabe 2: Lineare Funktionen 
f.write('\\begin{aufgabe} ~ \\ \n')

f.write('\\begin{multicols}{3} \n')
f.write('\\begin{enumerate}[a)] \n')

for i in range(1,4):
    f.write('\\item ')
    linfunc() 
    f.write('\n')
f.write('\\end{enumerate} \n')
f.write('\\end{multicols} \n')
f.write('\\end{aufgabe}')
f.write('\\vspace{1em}')

### Aufgabe 3: Quadratische Funktionen a=1, b=0 
f.write('\\begin{aufgabe} ~ \\ \n')

f.write('\\begin{multicols}{3} \n')
f.write('\\begin{enumerate}[a)] \n')

for i in range(1,4):
    f.write('\\item ')
    quadfuncnormalsym() 
    f.write('\n')
f.write('\\end{enumerate} \n')
f.write('\\end{multicols} \n')
f.write('\\end{aufgabe}')
f.write('\\vspace{1em}')

### Aufgabe 4: Quadratische Funktionen b=0 
f.write('\\begin{aufgabe} ~ \\ \n')

f.write('\\begin{multicols}{3} \n')
f.write('\\begin{enumerate}[a)] \n')

for i in range(1,4):
    f.write('\\item ')
    quadfuncsym() 
    f.write('\n')
f.write('\\end{enumerate} \n')
f.write('\\end{multicols} \n')
f.write('\\end{aufgabe}')
f.write('\\vspace{1em}')

### Aufgabe 5: Quadratische Funktionen c=0 
f.write('\\begin{aufgabe} ~ \\ \n')

f.write('\\begin{multicols}{3} \n')
f.write('\\begin{enumerate}[a)] \n')

for i in range(1,4):
    f.write('\\item ')
    quadfunchomo() 
    f.write('\n')
f.write('\\end{enumerate} \n')
f.write('\\end{multicols} \n')
f.write('\\end{aufgabe}')
f.write('\\vspace{1em}')

### Aufgabe 6: Quadratische Funktionen a=1 
f.write('\\begin{aufgabe} ~ \\ \n')

f.write('\\begin{multicols}{3} \n')
f.write('\\begin{enumerate}[a)] \n')

for i in range(1,4):
    f.write('\\item ')
    quadfuncnormal() 
    f.write('\n')
f.write('\\end{enumerate} \n')
f.write('\\end{multicols} \n')
f.write('\\end{aufgabe}')
f.write('\\vspace{1em}')

"""
### Aufgabe 7: Terme
f.write('\\begin{aufgabe} ~ \\ \n')

f.write('\\begin{multicols}{3} \n')
f.write('\\begin{enumerate}[a)] \n')

for i in range(1,4):
    f.write('\\item ')
    terme() 
    f.write('\n')
f.write('\\end{enumerate} \n')
f.write('\\end{multicols} \n')
f.write('\\end{aufgabe}')
f.write('\\vspace{1em}')
"""






f.write('\n')
f.write('\\end{flushleft} \n')
f.write('\\end{document}')


f.close()











 
