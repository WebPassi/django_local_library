#! /usr/bin/env python

## Author: Pasquale Franz
## Date: 26.01.2015

######
## Generate a table in latex-format with given values

from sympy import *
from sympy.abc import *
from elements import *

class Function:
    def __init__(self,strFunction):
        self.name="f"
        self.variable="x"
        self.expr=strFunction
    def anzeigen(self):
        latex_str="$" + latex(self.name) + "=" + latex(self.expr) + "$"
        return latex_str        
    def ywert(self,xwert):
        return self.expr.subs(x,xwert)
    def ylist(self,x):
        y=range(len(x))
        for index,item in enumerate(x):
            y[index]=self.ywert(x[index])
        return y
    def wertetabelle(self,xlist=range(-3,4)):
        return table(xlist,self.ylist(xlist))
    def graph(self):
        latexstr="\\draw[color=black] plot[smooth] function{" + str(self.expr) + "}; \n" 
        return latexstr
    def xwert(self,ywert):
        glg = Eq(self.expr,ywert)
        lsg = (solve(glg,x))
        return lsg
    def nullstelle(self):
        return self.xwert(0)
    def integral(self,a,b):
        myint ='(x,a,b)'
        aufgabe = Integral(self.expr,eval(myint))
        ### Stammfunktion
        stamm = integrate(self.expr)
        ### obere Grenze eingesetzt
        og = stamm.subs(x,a) 
        ### untere Grenze eingesetzt
        ug = stamm.subs(x,b) 
        ### exakte Loesung
        lsg = integrate(self.expr,eval(myint))
        latexstr=latex("$" + latex(aufgabe) + "$")
        return latexstr
    def randIntegral(self):
        a=random.randint(-4,-1)
        b=random.randint(1,4)
        myint ='(x,a,b)'
        aufgabe = Integral(self.expr,eval(myint))
        ### Stammfunktion
        stamm = integrate(self.expr)
        ### obere Grenze eingesetzt
        og = stamm.subs(x,a) 
        ### untere Grenze eingesetzt
        ug = stamm.subs(x,b) 
        ### exakte Loesung
        lsg = integrate(self.expr,eval(myint))
        latexstr=latex("$" + latex(aufgabe) + "$")
        return latexstr
class LinFunc(Function):
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.expr=a*x+b
    def anzeigen(self):
        latex_str="$f(x)=" + latex(self.a) + "x+" + latex(self.b) + "$ \n"
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

class QuadFunc(Function):
    def __init__(self, f, a, b, c):
        if f=="n":
            self.a=a
            self.b=b
            self.c=c
            self.expr=self.a*(x**2)+self.b*x+self.c
            self.d=self.b/(-2*self.a)
            self.e=self.c-self.a*(self.d)**2
        if f=="s":
            self.a=a
            self.d=b
            self.e=c
            self.expr=self.a*((x-self.d)**2)+self.e
            self.b=-2*self.a*self.d
            self.c=self.a*self.d**2+self.d
        self.name="f"
        self.variable="x"
    def delete0terms(term):
        if self.a == 0:
            return ""
        else:
            return latex(term)
    def normalform(self):
        return no1(self.a) + latex(x**2) +  no1(self.b) + latex(x) + no0(self.c)

    def sp(self):
        string="$S(" + latex(self.d) + "|" + latex(self.e) + ")$"
        return string

    def symachse(self):
        string="$" + latex(self.variable) + "=" + latex(self.d) + "$" 
        return string




class Term():
    def __init__(self,listexpr):
        self.liste=listexpr
        wert=0
        for expression in listexpr:
            wert+=expression
        self.expr=wert        
    def vereinfacheAusdruck(self):
        wert=0
        for expr in self.liste:
            wert+=expr
        return latex(wert)
    def test(self):
        return self.liste
    def zeigeAusdruck(self):
        strausdruck=""
        for index,expr in enumerate(self.liste):
            if index==0:
                strausdruck="(" + latex(expr) + ")"
            else:
                strausdruck+="+ (" +latex(expr) + ")"
        return strausdruck
    def anzeigenKlammer(self):
        return "(" + latex(self.expr) + ")"



class LinTerm():
    def __init__(self,a,b,factor=1):
        self.factor=factor
        self.a=a
        self.b=b
        self.expr=factor*(a*x+b)
    def ausdruck():
        return self.expr
    def zeigeLinTerm(self):
        if self.factor==1:
            return latex(self.expr)
        else:
            return latex(self.factor) + "(" + latex(self.a*x+self.b) + ")"
    
    


class axhochn(Function):
    def __init__(self):
        self.a=random.randint(1,10)
        self.n=random.randint(1,10)
        self.expr=self.a*x**self.n
    def random(self):
        a=random.randint(1,10)
        n=random.randint(1,10)
        self.expr=self.a*x**self.n

class polynom(Function):
    def __init__(self,n):
        self.expr=0
        for i in range(n):
            self.expr+=axhochn().expr

class Equation():
    def __init__(self,term1,term2):
        self.ls=term1.expr
        self.rs=term2.expr
        self.lsz=term1.zeigeLinTerm()
        self.rsz=term2.zeigeLinTerm()
        self.equation=Eq(self.ls,self.rs)
    def zeigeGlg(self):
        return latex(self.lsz) + " = " + latex(self.rsz)
    def zeigeLsg(self):
        solution=solve(self.equation,x)
        return latex(solution[0])
    

            

