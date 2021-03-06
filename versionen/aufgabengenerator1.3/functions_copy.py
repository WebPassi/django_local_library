#! /usr/bin/env python

## Author: Pasquale Franz
## Date: 26.01.2015

######
## Generate a table in latex-format with given values

from sympy import latex
from sympy.abc import *
from elements import *

#from skelet import Skelet

class Function:
    def __init__(self,function):
        self.expr=function
    def ywert(self,xwert):
        return self.expr.subs(x,xwert)
    def ylist(self,x):
        y=range(len(x))
        for index,item in enumerate(x):
            y[index]=self.ywert(x[index])
        return y
    def wertetabelle(self,xlist=range(-3,4)):
        return table(xlist,self.ylist(xlist))


class LinFunc(Function):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def anzeigen(self):
        latex_str="$f(x)=" + latex(self.a) + "x+" + latex(self.b) + "$ \\\\ \n"
        return latex_str
    def ywert(self,x):
        return self.a*x+self.b
    def graph_zeichnen(self):
        str1="""\\definecolor{cqcqcq}{rgb}{0.75,0.75,0.75} 
\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm] 
\\draw [color=cqcqcq,dash pattern=on 2pt off 2pt, xstep=1.0cm,ystep=1.0cm] (-3.33,-3.57) grid (3.29,3.53); 
\\draw[->,color=black] (-3.33,0) -- (3.29,0); 
\\foreach \\x in {-3,-2,-1,1,2,3} 
\\draw[shift={(\\x,0)},color=black] (0pt,2pt) -- (0pt,-2pt) node[below] {\\footnotesize $\\x$}; 
\\draw[color=black] (3,0.07) node [anchor=south west] { x}; 
\\draw[->,color=black] (0,-3.57) -- (0,3.53); 
\\foreach \\y in {-3,-2,-1,1,2,3} 
\\draw[shift={(0,\\y)},color=black] (2pt,0pt) -- (-2pt,0pt) node[left] {\\footnotesize $\\y$}; 
\\draw[color=black] (0.09,3.17) node [anchor=west] { y}; 
\\draw[color=black] (0pt,-10pt) node[right] {\\footnotesize $0$}; 
\\clip(-3.33,-3.57) rectangle (3.29,3.53);""" 
        str2="\\draw [domain=-3.33:3.29] plot(\\x,{(" + str(self.a) + "*\\x+" + str(self.b) + "}); \n"
        str3="\\end{tikzpicture} \n\
\\hspace{1cm}"
        latex_str=str1 + str2 + str3
        return latex_str



class Parabel(Function):
    def __init__(self, xs, ys, a):
        self.d=xs
        self.e=ys
        self.a=a
        self.expr=self.a*(x-self.d)**2+self.e
        

"""
    def modelParabel(self):
        quadf=self.a*(x-self.d)**2+self.e
        lf = open('datei.tex','a')
        lf.write("$p(x)=" + latex(quadf) + "$ \\\\ \n")
        lf.write("Wertetabelle: \\\\ \n\n")
        self.wertetabelle([-2,-1,0,1,2])
#        lf.write("Scheitelpunkt: $S(" + latex(self.d) + "|" + latex(self.e) + ")$ \\\\ \n")
#        lf.write("Normalform: \\\\ \n")
#        lf.write("$p(x)=" + latex(quadf.expand()) + "$")

#        lf.write("\\[ p(x)=" + latex(self.a) + "(x-" + latex(self.d) + ")^2+" + latex(self.e) + "\\] \n")
"""
