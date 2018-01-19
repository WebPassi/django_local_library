#! /usr/bin/env python

from sympy import * 
#from sympy import Integral, latex

# erklaere alle buchstaben neutzbaren zu sympy symbolen:
from sympy.abc import *



### note: um einen \ mit write() zu erzeugen muss  \\ getippt werden.



f = open('texoutput.tex', 'w')

f.write('%This is a sympy to latex test.\n\n\n');

f.write('\\documentclass[12pt]{article}\n\
\\usepackage[utf8]{inputenc}\n\
\\usepackage{pgf,tikz}\n\
\\usepackage{fancyhdr}\n\
\\usepackage{paralist} \n\
\\usepackage{amssymb}  \n\
\\usepackage{amsthm}   \n\
\\usepackage{amsmath}  \n\n\n\n');

f.write('\\begin{document}\n')

#SymPy-Ausdruck a als String 


#Potenzen
expr='2**3'
string=latex(eval(expr));
f.write(string);

#string=latex(expr)+'='+latex(exp) \\\\';
#f.write(string);f.write('\n');f.write('\n');




#Bsp 1 - Integral
expr='x**2'; # expression to integrate
var='x';

string=latex(Integral(expr,eval(var))); # prints ausgangsformel
string=string+'=';
string=string+latex(integrate(expr,eval(var)));# prints result of integration
string=string+' \\\\'; #end latex line
f.write('{\\bf Bsp1:}\n');
f.write(string); #write to fille
f.write('\n');  # newline in outputfile
f.write('\n');  # another new, empty line




#Bsp 2 -Integral
expr='1/x + x**5'; # expression to integrate
string=latex(Integral(expr,eval(var)))+'='+latex(integrate(expr,eval(var)))+' \\\\';
f.write('{\\bf Bsp2:}\n');
f.write(string);f.write('\n');f.write('\n');


#Bsp 3 - Stammfkt.
expr='x**2';
var='(x,a,b)';    # integral ueber x von a nach b
string=latex(Integral(expr,eval(var)))+'='+latex(integrate(expr,eval(var)))+' \\\\';
f.write('{\\bf Bsp3:}\n');f.write(string);f.write('\n');f.write('\n');


#Bsp 4 - Stammfkt.
expr='x**2';
var='(x,a,2)';
string=latex(Integral(expr,eval(var)))+'='+latex(integrate(expr,eval(var)))+' \\\\';
f.write('{\\bf Bsp4:}\n');f.write(string);f.write('\n');f.write('\n');


#Bsp 5 - Stammfkt.
expr='x**2';
var='(x,1,2)';   
string=latex(Integral(expr,eval(var)))+'='+latex(integrate(expr,eval(var)))+' \\\\';
f.write('{\\bf Bsp5:}\n');f.write(string);f.write('\n');f.write('\n');


f.write('\\end{document}')


f.close()










 
