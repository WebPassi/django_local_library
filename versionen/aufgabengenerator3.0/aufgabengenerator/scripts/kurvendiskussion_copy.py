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



### note: um einen \ mit write() zu erzeugen muss  \\ getippt werden.


### Create file with exercises 
fp = open('pupil.tex', 'w')
### Create file lehrer.tex with solutions
ft = open('teacher.tex', 'w')

### Integrale

#init_printing()

def integralpot():
    n = random.randint(1,7)
    lb = random.randint(1,10)-5
    lu = random.randint(1,10)-5
    if lb > lu:
        tmp = lu
        lu = lb
        lb = tmp
    func=x**n
    myint ='(x,lb,lu)'
    aufgabe = Integral(func,eval(myint))
    stamm = integrate(func)
    og = stamm.subs(x,lu) 
    ug = stamm.subs(x,lb) 
#    lsg = latex(integrate(func,eval(myint)).evalf(2),mode='inline')
#    lsg = latex(integrate(func,eval(myint)))
    lsg = integrate(func,eval(myint))
    fp.write(latex(aufgabe,mode="inline"))
#    ft.write(aufgabe + "= \\\\ \\[" + stamm + '=' + lsg + "\\]")
#    lsg=Float(lsg,5)
#    ft.write(str(lsg))
    if "/" not in str(lsg):
        lsg = latex(integrate(func,eval(myint)))
    else: 
        lsg = latex(integrate(func,eval(myint)).evalf(5))  
#        lsg = latex(float(integrate(func,eval(myint)))  
    ft.write(latex(aufgabe,mode="inline") + "$=$ \\\\" + "$[" + latex(stamm) +  "]_{\scriptscriptstyle" + str(lb) + "}^{\scriptscriptstyle" + str(lu) + "}=(" + latex(og) + ")-(" + latex(ug) + ")=" + lsg + "$")
    




### Functions

## ax+b=0
def linfunc0():
    # Random Numbers for a,b, but a not = 0
    a = random.randint(1,10)-5
    if a==0:
        a=1
    b = random.randint(1,10)-5

    
    # Linear Expression
    linexpr=a*x+b
    # Equation 
    glg = Eq(linexpr,0)
    # Solution
    lsg = solve(glg,x)

    # Don't write the solution in pupil's file
    fp.write(latex(glg,mode='inline'))
    fp.write('\\\\')
    fp.write('\n')

    ft.write(latex(glg,mode='inline'))
    ft.write('\\\\')
    ft.write('\n')
    ft.write('{\\tiny $x=$' + latex(lsg[0],mode='inline') + '}')
    ft.write('\n')

def linfunc():
    # Random Numbers for a,b, but a not = 0
    a = random.randint(1,10)-5
    if a==0:
        a=1
    b = random.randint(1,10)-5
    c = random.randint(1,10)-5

    # Linear Expression
    linexpr=a*x+b
    # Equation
    glg = Eq(linexpr,c)
    # Solution
    lsg = solve(glg,x)

    # Don't write the solution in pupil file
    fp.write(latex(glg,mode='inline'))
    fp.write('\\\\')
    fp.write('\n')

    ft.write(latex(glg,mode='inline'))
    ft.write('\\\\')
    ft.write('\n')
    ft.write('{\\tiny $x=$' + latex(lsg[0],mode='inline') + '}')
    ft.write('\n')



def quadfunc():
    # Random Numbers for a,b and c but a not = 0
    a = random.randint(1,10)-5
    if a==0:
        a=1
    b = random.randint(1,10)-5
    c = random.randint(1,10)-5
    
    # Quadratical Expression
    quadexpr=a*x**2+b*x+c
    # Equation
    glg = Eq(quadexpr,0)
    # Solution
    lsg = (solve(glg,x))


    # Don't write solution in pupil's file
    fp.write(latex(glg,mode='inline'))
    fp.write('\\\\')

    ft.write(latex(glg,mode='inline'))
    ft.write('\\\\')
    # A complex solution is replaced with no solution
    if "I" not in str(lsg):
        ft.write('\n')
        ft.write('{\\tiny $x_1=$' +  latex(lsg[0].evalf(2),mode='inline') + '}')
        try:
            ft.write('{\\tiny   ,     $x_2=$' + latex(lsg[1].evalf(2),mode='inline') + '}')
        except IndexError:
            ft.write('')
        ft.write('\n')
    else:
        ft.write('\n')
        ft.write('{\\tiny Keine Lösung}')
        ft.write('\n')


def quadfuncnormal():
    # Random Numbers for a,b and c but a not = 0
    a = 1
    b = random.randint(1,10)-5
    c = random.randint(1,10)-5

    # Quadratical Expression
    quadexpr=a*x**2+b*x+c
    # Equation
    glg = Eq(quadexpr,0)
    # Solution
    lsg = (solve(glg,x))

    # Don't write solution in pupil's file
    fp.write(latex(glg,mode='inline'))
    fp.write('\\\\')

    ft.write(latex(glg,mode='inline'))
    ft.write('\\\\')
    # A complex solution is replaced with no solution
    if "I" not in str(lsg):
        ft.write('\n')
        ft.write('{\\tiny $x_1=$' +  latex(lsg[0].evalf(2),mode='inline') + '}')
        try:
            ft.write('{\\tiny   ,     $ x_2=$' + latex(lsg[1].evalf(2),mode='inline') + '}')
        except IndexError:
            ft.write('')
        ft.write('\n')
    else:
        ft.write('\n')
        ft.write('{\\tiny Keine Lösung}')
        ft.write('\n')

def quadfuncnormalsym():
    # Random Numbers for a,b and c but a not = 0
    a = 1
    b = 0
    c = random.randint(1,50)-40

    # Quadratical Expression
    quadexpr=a*x**2+b*x+c
    # Equation
    glg = Eq(quadexpr,0)
    # Solution
    lsg = (solve(glg,x,real=True))

    # Don't write solution in pupil's file
    fp.write(latex(glg,mode='inline'))
    fp.write('\\\\')

    ft.write(latex(glg,mode='inline'))
    ft.write('\\\\')
    # A complex solution is replaced with no solution
    if "I" not in str(lsg):
        ft.write('\n')
        ft.write('{\\tiny $x_1=$' +  latex(lsg[0].evalf(2),mode='inline') + '}')
        try:
            ft.write('{\\tiny   ,     $ x_2=$' + latex(lsg[1].evalf(2),mode='inline') + '}')
        except IndexError:
            ft.write('')
        ft.write('\n')
    else:
        ft.write('\n')
        ft.write('{\\tiny Keine Lösung}')
        ft.write('\n')

def quadfuncsym():
    # Random Numbers for a,b and c but a not = 0
    a = random.randint(1,10)-5
    if a==0:
        a=1
    b = 0
    c = random.randint(1,10)-9

    # Quadratical Expression
    quadexpr=a*x**2+b*x+c
    # Equation
    glg = Eq(quadexpr,0)
    # Solution
    lsg = (solve(glg,x))

    # Don't write solution in pupil's file
    fp.write(latex(glg,mode='inline'))
    fp.write('\\\\')
    
    ft.write(latex(glg,mode='inline'))
    ft.write('\\\\')
    # A complex solution is replaced with no solution
    if "I" not in str(lsg):
        ft.write('\n')
        ft.write('{\\tiny $x_1=$' +  latex(lsg[0].evalf(2),mode='inline') + '}')
        try:
            ft.write('{\\tiny   ,     $ x_2=$' + latex(lsg[1].evalf(2),mode='inline') + '}')
        except IndexError:
            ft.write('')
        ft.write('\n')
    else:
        ft.write('\n')
        ft.write('{\\tiny Keine Lösung}')
        ft.write('\n')

def quadfunchomo():
    # Random Numbers for a,b and c but a not = 0
    a = random.randint(1,10)-5
    if a==0:
        a=1
    b = random.randint(1,10)-5
    c = 0

    # Quadratical Expression
    quadexpr=a*x**2+b*x+c
    # Equation
    glg = Eq(quadexpr,c)
    # Solution
    lsg = (solve(glg,x))

    # Don't write solution in pupil's file
    fp.write(latex(glg,mode='inline'))
    fp.write('\\\\')

    ft.write(latex(glg,mode='inline'))
    ft.write('\\\\')
    # A complex solution is replaced with no solution
    if "I" not in str(lsg):
        ft.write('\n')
        ft.write('{\\tiny $x_1=$' +  latex(lsg[0].evalf(2),mode='inline') + '}')
        try:
            ft.write('{\\tiny   ,   $ x_2=$' + latex(lsg[1].evalf(2),mode='inline') + '}')
        except IndexError:
            ft.write('')
        ft.write('\n')
    else:
        ft.write('\n')
        ft.write('{\\tiny Keine Lösung}')
        ft.write('\n')


### algebra

def binom1():
    a = random.randint(1,10)
    b = random.randint(1,10)
    expr = (a*x+b)**2
    lsg = expr.expand()
    fp.write(latex(expr,mode='inline'))
    fp.write(' = ')
    fp.write('\\\\')
    ft.write(latex(expr,mode='inline'))
    ft.write(' = ')
    ft.write('\n')
    ft.write('\\\\')
    ft.write(latex(lsg,mode='inline'))

def binom2():
    a = random.randint(1,10)
    b = random.randint(1,10)-11
    expr = (a*x+b)**2
    lsg = expr.expand()
    fp.write(latex(expr,mode='inline'))
    fp.write(' = ')
    fp.write('\\\\')
    ft.write(latex(expr,mode='inline'))
    ft.write(' = ')
    ft.write('\n')
    ft.write('\\\\')
    ft.write(latex(lsg,mode='inline'))

def binom3():
    a = random.randint(1,10)
    b = random.randint(1,10)
    expr = (a*x+b)*(a*x-b)
    lsg = expr.expand()
    fp.write(latex(expr,mode='inline'))
    fp.write(' = ')
    fp.write('\\\\')
    ft.write(latex(expr,mode='inline'))
    ft.write(' = ')
    ft.write('\n')
    ft.write('\\\\')
    ft.write(latex(lsg,mode='inline'))

def mult_out():
    a = random.randint(1,10)-5
    if a == 0:
        a=1
    b = random.randint(1,10)-5
    if b == 0:
        b=1
    c = random.randint(1,10)-5
    if c == 0:
        c=1
    d = random.randint(1,10)-5
    if d == 0:
        d=1
    expr = (a*x+b)*(c*x+d)
    lsg = expr.expand()
    fp.write(latex(expr,mode='inline'))
    fp.write(' = ')
    fp.write('\\\\')
    ft.write(latex(expr,mode='inline'))
    ft.write(' = ')
    ft.write('\n')
    ft.write('\\\\')
    ft.write(latex(lsg,mode='inline'))

def factorize1():
    a = random.randint(1,10)-5
    if a == 0:
        a=1
    b = random.randint(1,10)-5
    if b == 0:
        b=1
    expr = a*x*(x+b)
    lsg = expr.expand()
    fp.write(latex(lsg,mode='inline'))
    fp.write(' = ')
    fp.write('\\\\')
    ft.write(latex(lsg,mode='inline'))
    ft.write(' = ')
    ft.write('\n')
    ft.write('\\\\')
    ft.write(latex(expr,mode='inline'))

def factorize2():
    a = random.randint(1,10)-5
    if a == 0:
        a=1
    b = random.randint(1,10)-5
    if b == 0:
        b=1
    c = random.randint(1,10)-5
    if c == 0:
        c=1
    expr = a*x*(x**2+b*x+c)
    lsg = expr.expand()
    fp.write(latex(lsg,mode='inline'))
    fp.write(' = ')
    fp.write('\\\\')
    ft.write(latex(lsg,mode='inline'))
    ft.write(' = ')
    ft.write('\n')
    ft.write('\\\\')
    ft.write(latex(expr,mode='inline'))



### Doesn't work yet
def terme():
    a = random.randint(1,10)-5
    if a == 0:
        a=1
    b = random.randint(1,10)
    if b == 0:
        b=1
    c = random.randint(1,10)
    if c == 0:
        c=1
    d = random.randint(1,10)
    if d == 0:
        d=1
    expr1 = a*x**2
    expr2 = c*x
    expr3 = b*x**2
    expr4 = d*x
    expr = expr1+expr2+expr3-expr4
    fp.write(latex(latex(expr1) + '+' + latex(expr2) + '+' + latex(expr3) + '-' + latex(expr4),mode='inline'))
    fp.write(' = ')
    fp.write('\\\\')

    ft.write(latex(latex(expr1) + '+' + latex(expr2) + '+' + latex(expr3) + '-' + latex(expr4),mode='inline'))
    ft.write(' = ')
    ft.write('\\\\')
    ft.write(latex(expr,mode='inline'))
 
def efunceinfach():
    a=random.randint(1,10)-5
    if a == 0:
        a=-5
    b=random.randint(1,10)-5
    if b == 0:
        b=-5
    func=a*exp(b*x)
    abl=diff(func,x,1)
    abl2=diff(func,x,2)
    fp.write("$f(x)=$" + latex(func,mode='inline'))
    ft.write("$f(x)=$" + latex(func,mode='inline') + "\\\\ \n")
    ft.write("$f'(x)=$" + latex(abl,mode='inline') + "\\\\ \n")
    ft.write("$f''(x)=$" + latex(abl2,mode='inline') + "\\\\ \n")

def efuncpot():
    a=random.randint(1,10)-5
    if a == 0:
        a=-5
    b=random.randint(1,10)-5
    if b == 0:
        b=-5
    n=random.randint(1,4)
    func=a*exp(b*(x**n))
    abl=diff(func,x,1)
    abl2=diff(func,x,2)
    fp.write("$f(x)=$" + latex(func,mode='inline'))
    ft.write("$f(x)=$" + latex(func,mode='inline') + "\\\\ \n")
    ft.write("$f'(x)=$" + latex(abl,mode='inline') + "\\\\ \n")
    ft.write("$f''(x)=$" + latex(abl2,mode='inline') + "\\\\ \n")

def efuncpotpol():
    a=random.randint(1,10)-5
    if a == 0:
        a=-5
    b=random.randint(1,10)-5
    if b == 0:
        b=-5
    m=random.randint(1,4)
    n=random.randint(1,4)
    func=a*(x**m)*exp(b*(x**n))
    abl=diff(func,x,1)
    abl2=diff(func,x,2)
    ablfactor=simplify(abl)
    abl2factor=simplify(abl2)
    fp.write("$f(x)=$" + latex(func,mode='inline'))
    ft.write("$f(x)=$" + latex(func,mode='inline') + "\\\\ \n")
    ft.write("$f'(x)=$" + latex(abl,mode='inline') + "\\\\ \n")
    ft.write("$f'(x)=$" + latex(ablfactor,mode='inline') + "\\\\ \n")
    ft.write("$f''(x)=$" + latex(abl2,mode='inline') + "\\\\ \n")

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
    


def efuncpotpolkd():
    a=random.randint(1,10)-5
    if a == 0:
        a=-5
    b=random.randint(1,10)-5
    if b == 0:
        b=-5
    m=random.randint(1,4)
    n=random.randint(1,4)
    func=a*(x**m)*exp(b*(x**n))
    abl=diff(func,x,1)
    abl2=diff(func,x,2)
    ablfactor=simplify(abl)
    abl2factor=simplify(abl2)
    glgns = Eq(func,0)
    lsgns = makereal(solve(glgns,x,real=True))
    glgextr = Eq(abl,0)
    lsgextr = makereal(solve(glgextr,x,real=True))
    fp.write("$f(x)=$" + latex(func,mode='inline'))
### Funktion und Ableitung
    ft.write("Funktion und Ableitung: \n")
    ft.write("\\begin{align*} \n")
    ft.write("f(x)&=" + latex(func) + "\\\\ \n")
    ft.write("f'(x)&=" + latex(abl) + "\\\\ \n")
    ft.write("f'(x)&=" + latex(ablfactor) + "\\\\ \n")
    ft.write("f''(x)&=" + latex(abl2) + "\\\\ \n")
    ft.write("\\end{align*} \n")
### Nullstellen
    ft.write("Nullstellen: \n")
    ft.write("\\begin{align*} \n")
    ft.write("f(x)&=0 \\\\ \n")
    ft.write(latex(func)  + "&=0 \n")
    ft.write("\\end{align*} \n")
    for index in range(len(lsgns)):
        try:
            ft.write("$x_" + str(index+1) + "=" + latex(lsgns[index].evalf(2)) + "$ \\quad")
        except IndexError:
            ft.write('')
    ft.write("\\\\ \n")
### Extrempunkte notwendige Bedingung
    ft.write("Extrempunkte (Notwendige Bedingung:) \n")
    ft.write("\\begin{align*} \n")
    ft.write("f'(x)&=0 \\\\ \n")
    ft.write(latex(ablfactor)  + "&=0 \n")
    ft.write("\\end{align*} \n")
    for index in range(len(lsgextr)):
        try:
            ft.write("$x_" + str(index+1) + "=" + latex(lsgextr[index].evalf(2)) + "$ \\quad")
        except IndexError:
            ft.write('')
    ft.write("\\\\ \n")
### Funktionswerte 
    ft.write("Funktionswerte: \\\\ \n")
    for index in range(len(lsgextr)):
        try:
            ft.write("$f(" + latex(lsgextr[index].evalf(2)) + ")=" + latex(func.subs(x,lsgextr[index].evalf(2))) + "$ \\quad")
        except IndexError:
            ft.write("\\\\ \n")    
### Extrempunkte notwendige Bedingung
    for index in range(len(lsgextr)):
        try:    
            ft.write("$$f''(" + latex(lsgextr[index].evalf(2)) + ")=" + latex(abl2.subs(x,lsgextr[index]).evalf(2)))
            if abl2.subs(x,lsgextr[index]) > 0:
                ft.write("> 0 $$")
                ft.write("$\\Rightarrow$ Tiefpunkt bei $T(" + latex(lsgextr[index].evalf(2)) + "|" + latex(func.subs(x,lsgextr[index]).evalf(2)) + ")$ \\\\ \n")  
            elif abl2.subs(x,lsgextr[0]) < 0:
                ft.write("< 0 $$")
                ft.write("$\\Rightarrow$ Hochpunkt bei $H(" + latex(lsgextr[index].evalf(2)) + "|" + latex(func.subs(x,lsgextr[index]).evalf(2)) + ")$ \\\\ \n")  
            elif abl2.subs(x,lsgextr[index]) == 0:
                ft.write("$$")
                ft.write("$\\Rightarrow$ Keine Entscheidung moeglich. \\\\ \n")
        except IndexError:
            ft.write("")        
    

### NOW: Formatting the exercise sheet

### Latex opening

fp.write('\\documentclass[12pt]{article}\n\
\\usepackage[utf8]{inputenc}\n\
\\usepackage{paralist} \n\
\\usepackage{amssymb}  \n\
\\usepackage{amsthm}   \n\
\\usepackage{multicol} \n\
\\pagestyle{empty} \n\
\\usepackage[left=1.5cm,right=1.5cm,top=0.8cm,bottom=1cm]{geometry} \n\
\\usepackage{amsmath}  \n\n\n\n');

fp.write('\\newtheoremstyle{note} \n\
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


fp.write('\\begin{document}\n')
fp.write('\\begin{flushleft}\n')

ft.write('\\documentclass[12pt]{article}\n\
\\usepackage[utf8]{inputenc}\n\
\\usepackage{paralist} \n\
\\usepackage{amssymb}  \n\
\\usepackage{amsthm}   \n\
\\usepackage{multicol} \n\
\\pagestyle{empty} \n\
\\usepackage[left=1.5cm,right=1.5cm,top=0.8cm,bottom=1cm]{geometry} \n\
\\usepackage{amsmath}  \n\n\n\n');

ft.write('\\newtheoremstyle{note} \n\
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


ft.write('\\begin{document}\n')
ft.write('\\begin{flushleft}\n')



## Linear equations:
##   linfunc(): ax+b=c
##   linfunc0(): ax+b=0 
## Quadratical equations:
##   quadfunc(): ax2+bx+c=0
##   quadfuncnormal(): x2+bx+c=0
##   quadfuncnormalsym(): x2+c=0
##   quadfuncsym(): ax2+c=0
##   quadfunchomo(): ax2+bx=0

### Aufgabe 1: 
fp.write('\\begin{aufgabe} ~  \n')
ft.write('\\begin{aufgabe} ~  \n')
efuncpotpolkd() 
fp.write('\n')
ft.write('\n')

fp.write('\\end{aufgabe}')
fp.write('\\vspace{1em}')

ft.write('\\end{aufgabe}')
ft.write('\\vspace{1em}')



### Closing
fp.write('\n')
fp.write('\\end{flushleft} \n')
fp.write('\\end{document}')

ft.write('\n')
ft.write('\\end{flushleft} \n')
ft.write('\\end{document}')


fp.close()
ft.close()











 
