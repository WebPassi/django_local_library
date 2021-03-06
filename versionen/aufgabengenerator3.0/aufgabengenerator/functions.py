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
        self.streichen=False
    def anzeigen(self):
        if self.streichen==True:
            latex_str="$\\cancel{" + latex(self.name) + "(" + self.variable + ")=" + latex(self.expr) + "}$"
        else:
            latex_str="$" + latex(self.name) + "(" + self.variable + ")=" + latex(self.expr) + "$"
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
    def __init__(self,a,b,name="f",variable="x"):
        self.name=name
        self.variable=variable
        self.a=a
        self.b=b
        self.expr=a*x+b
        self.vonx=name + "(" + variable + ")"
        self.gleichung=self.vonx + "=" + latex(self.expr)
    def anzeigen(self):
        latex_str="$" + self.name + "(x)=" + latex(self.a) + "x+" + latex(self.b) + "$ \n"
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
    def __init__(self, f, a, b, c,streichen=False):
        if f=="n":
            self.a=a
            self.b=b
            self.c=c
            self.expr=self.a*(x**2)+self.b*x+self.c
            self.p=self.b/self.a
            self.q=self.c/self.a
            self.d=self.b/(-2*self.a)
            self.e=self.c-self.a*(self.d)**2
        if f=="s":
            self.a=a
            self.d=b
            self.e=c
            self.expr=self.a*((x-self.d)**2)+self.e
            self.b=-2*self.a*self.d
            self.c=self.a*self.d**2+self.e
        self.streichen=streichen
        self.name="f"
        self.variable="x"
    def delete0terms(term):
        if self.a == 0:
            return ""
        else:
            return latex(term)
    def normalform(self):
        return self.a * x**2 +  self.b * x + self.c

    def scheitelpunktform(self):
        return self.a * (x-self.d)**2 + self.e
#        return "a"

    def sp(self):
        string="$S(" + latex(self.d) + "|" + latex(self.e) + ")$"
        return string

    def symachse(self):
        string="$" + latex(self.variable) + "=" + latex(self.d) + "$" 
        return string

    def oeffnung(self):
        if self.a<0:
            return "unten"
        elif self.a>0:
            return "oben"

    def form(self):
        if abs(self.a)<1:
            return "gestaucht"
        elif abs(self.a)>1:
            return "gestreckt"
        else:
            return "normal"




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
        self.term1=term1
        self.term2=term2
        self.ls=term1.expr
        self.rs=term2.expr
        self.equation=Eq(self.ls,self.rs)

    def zeigeGlg(self):
        return latex(self.ls) + " = " + latex(self.rs)
    def zeigeGlgLatex(self):
        return "$" + latex(self.ls) + " = " + latex(self.rs) + "$"

    def zeigeLsg(self,ds="p"):
        if self.equation==True:
            if ds=="p":
                lsg="\\mathbb{R}"
                return latex(lsg)
            elif ds=="m":
                lsg="L=\\mathbb{R}"
                return latex(lsg)
            elif ds=="v":
                lsg="Alle Zahlen sind L\\\"osungen"
                return lsg
        elif self.equation==False:
            if ds=="p":
                lsg="\\{\\}"
                return latex(lsg)
            elif ds=="m":
                lsg="L=\\{\\}"
                return latex(lsg)
            elif ds=="v":
                lsg="Keine L\\\"osung"
                return lsg
        else:
            solution=solve(self.equation,x)
            if ds=="p":
                lsg=latex(solution[0])
                return lsg
            elif ds=="m":
                lsg="L=\\{" + latex(solution[0]) + "\\}"
                return lsg
            elif ds=="v":
                lsg=latex(x) + "=" + latex(solution[0])
                return latex(lsg)
        
    def rechenweg_alt(self):
        latexstr="\\begin{alignat}{4} \n"

        ls=self.ls
        rs=self.rs
        op=self.term1.b
        latexstr+="&" + latex(ls) + "&=&" + latex(rs) + "\\quad &|& " + latex(-op) + "\\\\ \n"

        ls=ls-op
        rs=rs-op
        op=self.term2.a*x
        latexstr+="&" + latex(ls) + "&=&" + latex(rs) + "\\quad &|& " + latex(-op) + "\\\\ \n"

        ls=ls-op
        rs=rs-op
        op=self.term1.a-self.term2.a
        latexstr+="&" + latex(ls) + "&=&" + latex(rs) + "\\quad &|& :" + latex(op) + "\\\\ \n"

        ls=ls/op
        rs=rs/op
        latexstr+="&" + latex(ls) + "&=&" + latex(rs) + "\\quad &&"

        latexstr+="\\end{alignat}"
        return latexstr


### Gilt nur fuer a,b,c,d ungleich null
    def rechenweg(self,ds="p"):
        if ds=="p":
            latexstr="\\begin{alignat*}{7} \n"
            op=self.term1.b
            latexstr+=vorzeichenpro(self.term1.a) + "&" + latex(x) + "&&" + vorzeichensum(self.term1.b) + latex(abs(self.term1.b)) + "&&=" + "&\;" + vorzeichenpro(self.term2.a) + "&" + latex(x) + "&\;&" + vorzeichensum(self.term2.b) + "&\;&" + latex(abs(self.term2.b)) + "& \quad &|" + vorzeichensum(-op) + latex(abs(-op)) + "\\\\ \n"

            op=self.term2.a
            latexstr+=vorzeichenpro(self.term1.a) + "&" + latex(x) + "&&" + "&&=" + "&" + vorzeichenpro(self.term2.a) + "&" + latex(x) + "&&" + vorzeichensum(self.term2.b-self.term1.b) + "&&" + latex(abs(self.term2.b-self.term1.b)) + "&&|" + vorzeichensum(-op) + latex(abs(-op)) + latex(x) + "\\\\ \n"

            op=self.term1.a-self.term2.a
            latexstr+=vorzeichenpro(self.term1.a-self.term2.a) + "&" + latex(x) + "&&" + "&&=" + "&&" + "&&" + vorzeichensum(self.term2.b-self.term1.b) + "&&" + latex(abs(self.term2.b-self.term1.b)) + "&&|" + ":" + minusklammer(op) + "\\\\ \n"

            latexstr+="&" + latex(x) + "&&" + "&&=" + "&&" + "&&" + "&&" + self.zeigeLsg() + "&& \n"

            latexstr+="\\end{alignat*}"
            return latexstr

        if ds=="v":
            latexstr="\\begin{alignat*}{8} \n"
            op=self.term1.b
            latexstr+=vorzeichenpro(self.term1.a) + "&" + latex(x) + "&&" + vorzeichensum(self.term1.b) + latex(abs(self.term1.b)) + "&&=" + "&\;" + vorzeichenpro(self.term2.a) + "&" + latex(x) + "&\;&" + vorzeichensum(self.term2.b) + "&\;&" + latex(abs(self.term2.b)) + "& \quad &|" + vorzeichensum(-op) + latex(abs(-op)) + "&\qquad &" + "\\text{Zahlen nach rechts}" + "\\\\ \n" 

            op=self.term2.a
            latexstr+=vorzeichenpro(self.term1.a) + "&" + latex(x) + "&&" + "&&=" + "&" + vorzeichenpro(self.term2.a) + "&" + latex(x) + "&&" + vorzeichensum(self.term2.b-self.term1.b) + "&&" + latex(abs(self.term2.b-self.term1.b)) + "&&|" + vorzeichensum(-op) + latex(abs(-op)) + latex(x) + "&&" + "\\text{$x$-se nach links}" + "\\\\ \n"

            op=self.term1.a-self.term2.a
            latexstr+=vorzeichenpro(self.term1.a-self.term2.a) + "&" + latex(x) + "&&" + "&&=" + "&&" + "&&" + vorzeichensum(self.term2.b-self.term1.b) + "&&" + latex(abs(self.term2.b-self.term1.b)) + "&&|" + ":" + minusklammer(op) + "&&" + "\\text{Durch Fakor vor dem $x$ teilen}" + "\\\\ \n"

            latexstr+="&" + latex(x) + "&&" + "&&=" + "&&" + "&&" + "&&" + self.zeigeLsg() + "&& \n"

            latexstr+="\\end{alignat*}"
            return latexstr


            

class Potenz():
    def __init__(self,basis,exponent):
        self.basis=basis
        self.exponent=exponent
        self.ergebnis=(self.basis)**(self.exponent)

    def ergebnis(self):
        return self.ergebnis

    def darsPotenz():
        return "$" + basis + "^{" + exponent + "}=$"
    def darsDezimal():
        return "$" + latex() + "=$"


        

