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


def efuncpotpol():
    a=random.randint(1,10)-5
    if a == 0:
        a=-5
    b=random.randint(1,10)-5
    if b == 0:
        b=-5
    m=random.randint(1,1)
    n=random.randint(1,1)
    func=a*(x**m)*exp(b*(x**n))
    abl=diff(func,x,1)
    abl2=diff(func,x,2)
    ablfactor=simplify(abl)
    abl2factor=simplify(abl2)
    fp.write("$f(x)=$" + latex(func,mode='inline'))
    ft.write("$f(x)=$" + latex(func,mode='inline') + "\\\\ \n")
    ft.write("$f'(x)=$" + latex(abl,mode='inline') + "\\\\ \n")
    ft.write("$f'(x)=$" + latex(ablfactor,mode='inline') + "\\\\ \n")
    #ft.write("$f''(x)=$" + latex(abl2,mode='inline') + "\\\\ \n")

def binomial(n,k):
    return factorial(n)*1.0 // factorial(k) // factorial(n-k)
 
def binomial_write():
    n = random.randint(10,20)
    k = random.randint(0,10)
    fp.write("$\\binom{" + latex(n) + "}{" + latex(k) + "}=$")
    ft.write("$\\binom{" + latex(n) + "}{" + latex(k) + "}=" + latex(binomial(n,k)) + "$")

def lotto():
    n1 = random.randint(5,10)
    n2 = random.randint(5,10)
    k1 = random.randint(0,5)
    k2 = random.randint(0,5)
    n = n1+n2
    k = k1+k2
    fp.write("$\\frac{\\binom{" + latex(n1) + "}{" + latex(k1) + "}\cdot \\binom{" + latex(n2) + "}{" + latex(k2) + "}}{\\binom{" + latex(n) + "}{" + latex(k) + "}}=$")
    ft.write("$\\frac{\\binom{" + latex(n1) + "}{" + latex(k1) + "}\cdot \\binom{" + latex(n2) + "}{" + latex(k2) + "}}{\\binom{" + latex(n) + "}{" + latex(k) + "}}=" + latex((binomial(n1,k1)*binomial(n2,k2) / binomial(n,k)*100).evalf(3)) + "\\%$")

def lottodrei():
    n1 = random.randint(5,10)
    n2 = random.randint(5,10)
    n3 = random.randint(5,10)
    k1 = random.randint(0,5)
    k2 = random.randint(0,5)
    k3 = random.randint(0,5)
    n = n1+n2+n3
    k = k1+k2+k3
    fp.write("$\\frac{\\binom{" + latex(n1) + "}{" + latex(k1) + "}\cdot \\binom{" + latex(n2) + "}{" + latex(k2) + "}\cdot \\binom{" + latex(n3) + "}{" + latex(k3) + "}}{\\binom{" + latex(n) + "}{" + latex(k) + "}}=$")
    ft.write("$\\frac{\\binom{" + latex(n1) + "}{" + latex(k1) + "}\cdot \\binom{" + latex(n2) + "}{" + latex(k2) + "}\cdot \\binom{" + latex(n3) + "}{" + latex(k3) + "}}{\\binom{" + latex(n) + "}{" + latex(k) + "}}=" + latex((binomial(n1,k1)*binomial(n2,k2) / binomial(n,k)*100).evalf(3)) + "\\%$")

def bernoullip():
    n = random.randint(0,10)
    k = random.randint(0,10)
    if k>n:
        tmp = n
        n = k
        k = tmp
    p = Float(random.random()).evalf(2)
    ft.write("$n=" + latex(n) + "$, $p=" + latex(p) + "$, $k=" + latex(k) + "$ \\\\ \n")
    ft.write("$P(X=" + latex(k) + ")=$\\\\ $\\binom{" + latex(n) + "}{" + latex(k) + "}\\cdot" + latex(p) + "^{" + latex(k) + "}\\cdot" + latex(1-p) + "^{" + latex(n-k) + "}=$ \\\\ \n")
    ft.write("$" + latex((binomial(n,k)*(p**k)*(1-p)**(n-k)*100).evalf(2)) + "\\%$")
    




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
fp.write('\\begin{aufgabe} ~ \\ \n')
fp.write('\\begin{multicols}{3} \n')
fp.write('\\begin{enumerate}[a)] \n')

ft.write('\\begin{aufgabe} ~ \\ \n')
ft.write('\\begin{multicols}{3} \n')
ft.write('\\begin{enumerate}[a)] \n')

for i in range(1,4):
    fp.write('\\item ')
    ft.write('\\item ')
##### Which exercise
    binomial_write() 
#####
    fp.write('\n')
    ft.write('\n')

fp.write('\\end{enumerate} \n')
fp.write('\\end{multicols} \n')
fp.write('\\end{aufgabe}')
fp.write('\\vspace{1em}')

ft.write('\\end{enumerate} \n')
ft.write('\\end{multicols} \n')
ft.write('\\end{aufgabe}')
ft.write('\\vspace{1em}')

### Aufgabe 2: 
fp.write('\\begin{aufgabe} ~ \\ \n')
fp.write('\\begin{multicols}{3} \n')
fp.write('\\begin{enumerate}[a)] \n')

ft.write('\\begin{aufgabe} ~ \\ \n')
ft.write('\\begin{multicols}{3} \n')
ft.write('\\begin{enumerate}[a)] \n')

for i in range(1,4):
    fp.write('\\item ')
    ft.write('\\item ')
##### Which exercise
    lotto()
##### 
    fp.write('\n')
    ft.write('\n')

fp.write('\\end{enumerate} \n')
fp.write('\\end{multicols} \n')
fp.write('\\end{aufgabe}')
fp.write('\\vspace{1em}')

ft.write('\\end{enumerate} \n')
ft.write('\\end{multicols} \n')
ft.write('\\end{aufgabe}')
ft.write('\\vspace{1em}')

### Aufgabe 3: 
fp.write('\\begin{aufgabe} ~ \\ \n')
fp.write('\\begin{multicols}{3} \n')
fp.write('\\begin{enumerate}[a)] \n')

ft.write('\\begin{aufgabe} ~ \\ \n')
ft.write('\\begin{multicols}{3} \n')
ft.write('\\begin{enumerate}[a)] \n')

for i in range(1,4):
    fp.write('\\item ')
    ft.write('\\item ')
##### Which exercise
    lottodrei() 
#####
    fp.write('\n')
    ft.write('\n')
fp.write('\\end{enumerate} \n')
fp.write('\\end{multicols} \n')
fp.write('\\end{aufgabe}')
fp.write('\\vspace{1em}')

ft.write('\\end{enumerate} \n')
ft.write('\\end{multicols} \n')
ft.write('\\end{aufgabe}')
ft.write('\\vspace{1em}')

### Aufgabe 4:  
fp.write('\\begin{aufgabe} ~ \\ \n')
fp.write('\\begin{multicols}{3} \n')
fp.write('\\begin{enumerate}[a)] \n')

ft.write('\\begin{aufgabe} ~ \\ \n')
ft.write('\\begin{multicols}{3} \n')
ft.write('\\begin{enumerate}[a)] \n')

for i in range(1,4):
    fp.write('\\item ')
    ft.write('\\item ')
##### Which exercise
    bernoullip() 
#####
    fp.write('\n')
    ft.write('\n')
fp.write('\\end{enumerate} \n')
fp.write('\\end{multicols} \n')
fp.write('\\end{aufgabe}')
fp.write('\\vspace{1em}')

ft.write('\\end{enumerate} \n')
ft.write('\\end{multicols} \n')
ft.write('\\end{aufgabe}')
ft.write('\\vspace{1em}')

### Aufgabe 5: 
fp.write('\\begin{aufgabe} ~ \\ \n')
fp.write('\\begin{multicols}{3} \n')
fp.write('\\begin{enumerate}[a)] \n')

ft.write('\\begin{aufgabe} ~ \\ \n')
ft.write('\\begin{multicols}{3} \n')
ft.write('\\begin{enumerate}[a)] \n')

for i in range(1,4):
    fp.write('\\item ')
    ft.write('\\item ')
##### Which exercise
    linfunc0() 
#####
    fp.write('\n')
    ft.write('\n')
fp.write('\\end{enumerate} \n')
fp.write('\\end{multicols} \n')
fp.write('\\end{aufgabe}')
fp.write('\\vspace{1em}')

ft.write('\\end{enumerate} \n')
ft.write('\\end{multicols} \n')
ft.write('\\end{aufgabe}')
ft.write('\\vspace{1em}')

### Aufgabe 6: 
fp.write('\\begin{aufgabe} ~ \\ \n')
fp.write('\\begin{multicols}{3} \n')
fp.write('\\begin{enumerate}[a)] \n')

ft.write('\\begin{aufgabe} ~ \\ \n')
ft.write('\\begin{multicols}{3} \n')
ft.write('\\begin{enumerate}[a)] \n')

for i in range(1,4):
    fp.write('\\item ')
    ft.write('\\item ')
##### Which exercise
    efuncpotpol()
##### 
    fp.write('\n')
    ft.write('\n')
fp.write('\\end{enumerate} \n')
fp.write('\\end{multicols} \n')
fp.write('\\end{aufgabe}')
fp.write('\\vspace{1em}')

ft.write('\\end{enumerate} \n')
ft.write('\\end{multicols} \n')
ft.write('\\end{aufgabe}')
ft.write('\\vspace{1em}')

### Aufgabe 7: 
fp.write('\\begin{aufgabe} ~ \\ \n')
fp.write('\\begin{multicols}{3} \n')
fp.write('\\begin{enumerate}[a)] \n')

ft.write('\\begin{aufgabe} ~ \\ \n')
ft.write('\\begin{multicols}{3} \n')
ft.write('\\begin{enumerate}[a)] \n')

for i in range(1,4):
    fp.write('\\item ')
    ft.write('\\item ')
##### Which exercise
    efuncpotpol()
##### 
    fp.write('\n')
    ft.write('\n')
fp.write('\\end{enumerate} \n')
fp.write('\\end{multicols} \n')
fp.write('\\end{aufgabe}')
fp.write('\\vspace{1em}')

ft.write('\\end{enumerate} \n')
ft.write('\\end{multicols} \n')
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











 
