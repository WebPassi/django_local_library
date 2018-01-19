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
### Zufallsvariablen fuer den Grad der Funktion, unterer Grenze, obere Grenze
    n = random.randint(1,7)
    lb = random.randint(1,10)-5
    lu = random.randint(1,10)-5
### Grenzen bei Bedarf vertauschen
    if lb > lu:
        tmp = lu
        lu = lb
        lb = tmp
### Funktion
    func=x**n
### Integralaufgabe
    myint ='(x,lb,lu)'
    aufgabe = Integral(func,eval(myint))
### Stammfunktion
    stamm = integrate(func)
### obere Grenze eingesetzt
    og = stamm.subs(x,lu) 
### untere Grenze eingesetzt
    ug = stamm.subs(x,lb) 
### exakte Loesung
    lsg = integrate(func,eval(myint))
##### Latex
    fp.write(latex(aufgabe,mode="inline"))
### Nur als Dezimalzahl schreiben, wenn die Loesung ein Bruch ist
    if "/" not in str(lsg):
        lsg = latex(integrate(func,eval(myint)))
    else: 
        lsg = latex(integrate(func,eval(myint)).evalf(5))  
    ft.write(latex(aufgabe,mode="inline") + "$=$ \\\\" + "$[" + latex(stamm) +  "]_{\scriptscriptstyle" + str(lb) + "}^{\scriptscriptstyle" + str(lu) + "}=(" + latex(og) + ")-(" + latex(ug) + ")=" + lsg + "$")

def integralpotneg():
### Zufallsvariablen fuer den Grad der Funktion, unterer Grenze, obere Grenze
    n = random.randint(1,10)-5
    if n==-1:
        n=-5
    lb = random.randint(1,10)-5
    lu = random.randint(1,10)-5
### Grenzen bei Bedarf vertauschen
    if lb > lu:
        tmp = lu
        lu = lb
        lb = tmp
### Funktion
    func=x**n
### Integralaufgabe
    myint ='(x,lb,lu)'
    aufgabe = Integral(func,eval(myint))
### Stammfunktion
    stamm = integrate(func)
### obere Grenze eingesetzt
    og = stamm.subs(x,lu) 
### untere Grenze eingesetzt
    ug = stamm.subs(x,lb) 
### exakte Loesung
    lsg = integrate(func,eval(myint))
##### Latex
    fp.write(latex(aufgabe,mode="inline"))
### Nur als Dezimalzahl schreiben, wenn die Loesung ein Bruch ist
    if "/" not in str(lsg):
        lsg = latex(integrate(func,eval(myint)))
    else: 
        lsg = latex(integrate(func,eval(myint)).evalf(5))  
    ft.write(latex(aufgabe,mode="inline") + "$=$ \\\\" + "$[" + latex(stamm) +  "]_{\scriptscriptstyle" + str(lb) + "}^{\scriptscriptstyle" + str(lu) + "}=(" + latex(og) + ")-(" + latex(ug) + ")=" + lsg + "$")


def integralpotfaktor():
### Zufallsvariablen fuer den Faktor, den Grad der Funktion, unterer Grenze, obere Grenze
    a = random.randint(1,10)-5
    if a==0:
        a=1
    n = random.randint(1,7)
    lb = random.randint(1,10)-5
    lu = random.randint(1,10)-5
### Grenzen bei Bedarf vertauschen
    if lb > lu:
        tmp = lu
        lu = lb
        lb = tmp
### Funktion
    func=a*x**n
### Integralaufgabe
    myint ='(x,lb,lu)'
    aufgabe = Integral(func,eval(myint))
### Stammfunktion
    stamm = integrate(func)
### obere Grenze eingesetzt
    og = stamm.subs(x,lu) 
### untere Grenze eingesetzt
    ug = stamm.subs(x,lb) 
### exakte Loesung
    lsg = integrate(func,eval(myint))
##### Latex
    fp.write(latex(aufgabe,mode="inline"))
### Nur als Dezimalzahl schreiben, wenn die Loesung ein Bruch ist
    if "/" not in str(lsg):
        lsg = latex(integrate(func,eval(myint)))
    else: 
        lsg = latex(integrate(func,eval(myint)).evalf(5))  
    ft.write(latex(aufgabe,mode="inline") + "$=$ \\\\" + "$[" + latex(stamm) +  "]_{\scriptscriptstyle" + str(lb) + "}^{\scriptscriptstyle" + str(lu) + "}=(" + latex(og) + ")-(" + latex(ug) + ")=" + lsg + "$")

def integralpotfaktorneg():
### Zufallsvariablen fuer den Faktor, den Grad der Funktion, unterer Grenze, obere Grenze
    a = random.randint(1,10)-5
    if a==0:
        a=-5
    n = random.randint(1,10)-5
    if n==-1:
        a=-5
    lb = random.randint(1,10)-5
    lu = random.randint(1,10)-5
### Grenzen bei Bedarf vertauschen
    if lb > lu:
        tmp = lu
        lu = lb
        lb = tmp
### Funktion
    func=a*x**n
### Integralaufgabe
    myint ='(x,lb,lu)'
    aufgabe = Integral(func,eval(myint))
### Stammfunktion
    stamm = integrate(func)
### obere Grenze eingesetzt
    og = stamm.subs(x,lu) 
### untere Grenze eingesetzt
    ug = stamm.subs(x,lb) 
### exakte Loesung
    lsg = integrate(func,eval(myint))
##### Latex
    fp.write(latex(aufgabe,mode="inline"))
### Nur als Dezimalzahl schreiben, wenn die Loesung ein Bruch ist
    if "/" not in str(lsg):
        lsg = latex(integrate(func,eval(myint)))
    else: 
        lsg = latex(integrate(func,eval(myint)).evalf(5))  
    ft.write(latex(aufgabe,mode="inline") + "$=$ \\\\" + "$[" + latex(stamm) +  "]_{\scriptscriptstyle" + str(lb) + "}^{\scriptscriptstyle" + str(lu) + "}=(" + latex(og) + ")-(" + latex(ug) + ")=" + lsg + "$")

def integralpotsum():
### Zufallsvariablen fuer den Faktor, den Grad der Funktion, unterer Grenze, obere Grenze
    a1 = random.randint(1,10)-5
    if a1==0:
        a1=1
    n1 = random.randint(1,7)
    a2 = random.randint(1,10)-5
    if a2==0:
        a2=1
    n2 = random.randint(1,7)
### Grenzen
    lb = random.randint(1,10)-5
    lu = random.randint(1,10)-5
### Funktionen
    func1=a1*x**n1
    func2=a2*x**n2
    func=func1+func2
### Grenzen bei Bedarf vertauschen
    if lb > lu:
        tmp = lu
        lu = lb
        lb = tmp
### Integralaufgabe
    myint ='(x,lb,lu)'
    aufgabe = Integral(func,eval(myint))
### Stammfunktion
    stamm = integrate(func)
### obere Grenze eingesetzt
    og = stamm.subs(x,lu) 
### untere Grenze eingesetzt
    ug = stamm.subs(x,lb) 
### exakte Loesung
    lsg = integrate(func,eval(myint))
##### Latex
    fp.write(latex(aufgabe,mode="inline"))
### Nur als Dezimalzahl schreiben, wenn die Loesung ein Bruch ist
    if "/" not in str(lsg):
        lsg = latex(integrate(func,eval(myint)))
    else: 
        lsg = latex(integrate(func,eval(myint)).evalf(5))  
    ft.write(latex(aufgabe,mode="inline") + "$=$ \\\\" + "$[" + latex(stamm) +  "]_{\scriptscriptstyle" + str(lb) + "}^{\scriptscriptstyle" + str(lu) + "}=(" + latex(og) + ")-(" + latex(ug) + ")=" + lsg + "$")

def integralpotsumv():
### Zufallsvariablen fuer die Anzahl der Funktionen, den Faktor, den Grad der Funktion, unterer Grenze, obere Grenze
    summanden = random.randint(1,3)
    a=range(summanden)
    n=range(summanden)
    function=range(summanden)
    func=0
    for i in a:
        a[i] = random.randint(1,10)-5
        if a[i]==0:
            a[i]=1
        n[i] = random.randint(1,7)
        function[i]=a[i]*x**n[i]
        func=func+function[i]
### Grenzen
    lb = random.randint(1,10)-5
    lu = random.randint(1,10)-5
### Grenzen bei Bedarf vertauschen
    if lb > lu:
        tmp = lu
        lu = lb
        lb = tmp
### Integralaufgabe
    myint ='(x,lb,lu)'
    aufgabe = Integral(func,eval(myint))
### Stammfunktion
    stamm = integrate(func)
### obere Grenze eingesetzt
    og = stamm.subs(x,lu) 
### untere Grenze eingesetzt
    ug = stamm.subs(x,lb) 
### exakte Loesung
    lsg = integrate(func,eval(myint))
##### Latex
    fp.write(latex(aufgabe,mode="inline"))
### Nur als Dezimalzahl schreiben, wenn die Loesung ein Bruch ist
    if "/" not in str(lsg):
        lsg = latex(integrate(func,eval(myint)))
    else: 
        lsg = latex(integrate(func,eval(myint)).evalf(5))  
    ft.write(latex(aufgabe,mode="inline") + "$=$ \\\\" + "$[" + latex(stamm) +  "]_{\scriptscriptstyle" + str(lb) + "}^{\scriptscriptstyle" + str(lu) + "}=(" + latex(og) + ")-(" + latex(ug) + ")=" + lsg + "$")
    

def integralpotsumvneg():
### Zufallsvariablen fuer die Anzahl der Funktionen, den Faktor, den Grad der Funktion, unterer Grenze, obere Grenze
    summanden = random.randint(1,3)
    a=range(summanden)
    n=range(summanden)
    function=range(summanden)
    func=0
    for i in a:
        a[i] = random.randint(1,10)-5
        if a[i]==0:
            a[i]=1
        n[i] = random.randint(1,10)-5
        if n[i]==-1:
            n[i]=-5
        function[i]=a[i]*x**n[i]
        func=func+function[i]
### Grenzen
    lb = random.randint(1,10)-5
    lu = random.randint(1,10)-5
### Grenzen bei Bedarf vertauschen
    if lb > lu:
        tmp = lu
        lu = lb
        lb = tmp
### Integralaufgabe
    myint ='(x,lb,lu)'
    aufgabe = Integral(func,eval(myint))
### Stammfunktion
    stamm = integrate(func)
### obere Grenze eingesetzt
    og = stamm.subs(x,lu) 
### untere Grenze eingesetzt
    ug = stamm.subs(x,lb) 
### exakte Loesung
    lsg = integrate(func,eval(myint))
##### Latex
    fp.write(latex(aufgabe,mode="inline"))
### Nur als Dezimalzahl schreiben, wenn die Loesung ein Bruch ist
    if "/" not in str(lsg):
        lsg = latex(integrate(func,eval(myint)))
    else: 
        lsg = latex(integrate(func,eval(myint)).evalf(5))  
    ft.write(latex(aufgabe,mode="inline") + "$=$ \\\\" + "$[" + latex(stamm) +  "]_{\scriptscriptstyle" + str(lb) + "}^{\scriptscriptstyle" + str(lu) + "}=(" + latex(og) + ")-(" + latex(ug) + ")=" + lsg + "$")


def kubischflaeche():
# Nullstellen
    n1=random.randint(1,5)-6
    n2=0
    n3=random.randint(1,5)
# Faktor
    a=random.randint(1,10)-5
    if a==0:
        a=-5
# Funktion
    funcfactor=a*(x-n1)*(x-n2)*(x-n3)
    func=expand(funcfactor)
    lsg=integrate(func,x,n1,n2)
    ft.write("$$f(x)=" + latex(func) + "$$ \n")
    ft.write("$$A=" + latex(Integral(func,x,n1,n2)) + "=" + latex(lsg) + "$$ \n")
    



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
\\usepackage[left=1.5cm,right=1.5cm,top=0.5cm,bottom=0.5cm]{geometry} \n\
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
    integralpot() 
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
    integralpotfaktor() 
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
    integralpotsum() 
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
    integralpotsumv() 
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

"""
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
    integralpotsumv() 
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
"""

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
    linfunc()
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
    quadfunc()
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
    quadfunc()
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











 
