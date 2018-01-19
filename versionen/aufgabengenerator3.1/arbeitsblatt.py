#! /usr/bin/env python

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
\\usepackage{amsmath}  \n\n\n\n');

f.write('\\begin{document} \n')

#SymPy-Ausdruck a als String 

menge = 10

unten=-10
oben=10


# negative Zahlen


for i in range(1,menge):  
    a = random.randrange(unten,oben)
    b = random.randrange(unten,oben)
    expr = a + b
    if b < 0:
        aufgabe = latex(a) + '+(' + latex(b) + ')='
        ergebnis = latex(expr)
        string = aufgabe + ergebnis
    else:
        aufgabe = latex(a) + '+' + latex(b) + '='
        ergebnis = latex(expr)
        string = aufgabe + ergebnis
    print string
    f.write(string)














f.write('\\end{document}')


f.close()










 
