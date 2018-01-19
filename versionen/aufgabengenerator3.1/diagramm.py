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
    ft.write(latex(lsg,mode='inline'))
    ft.write('\n')


### NOW: Formatting the exercise sheet

### Latex opening

fp.write('\\documentclass[12pt]{article}\n\
\\usepackage[utf8]{inputenc}\n\
\\usepackage{pgf,tikz}\n\
\\usepackage{fancyhdr}\n\
\\usepackage{paralist} \n\
\\usepackage{amssymb}  \n\
\\usepackage{amsthm}   \n\
\\usepackage{multicol} \n\
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


fp.write('\documentclass[10pt]{article} \n
\usepackage{pgf,tikz}
\usetikzlibrary{arrows}
\pagestyle{empty}
% fixed exp function.
%
\makeatletter
\let\pgfmath@function@exp\relax % undefine old exp function
\pgfmathdeclarefunction{exp}{1}{%   
  \begingroup
    \pgfmath@xc=#1pt\relax
    \pgfmath@yc=#1pt\relax
    \ifdim\pgfmath@xc<-9pt
      \pgfmath@x=1sp\relax
    \else
      \ifdim\pgfmath@xc<0pt
        \pgfmath@xc=-\pgfmath@xc
      \fi
      \pgfmath@x=1pt\relax
      \pgfmath@xa=1pt\relax
      \pgfmath@xb=\pgfmath@x
      \pgfmathloop%
        \divide\pgfmath@xa by\pgfmathcounter
        \pgfmath@xa=\pgfmath@tonumber\pgfmath@xc\pgfmath@xa%
        \advance\pgfmath@x by\pgfmath@xa
      \ifdim\pgfmath@x=\pgfmath@xb
      \else
        \pgfmath@xb=\pgfmath@x
      \repeatpgfmathloop%
      \ifdim\pgfmath@yc<0pt
        \pgfmathreciprocal@{\pgfmath@tonumber\pgfmath@x}%
        \pgfmath@x=\pgfmathresult pt\relax
      \fi
    \fi
    \pgfmath@returnone\pgfmath@x%
  \endgroup
}
\makeatother

\begin{document}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
\draw[->,color=black] (0,0) -- (3,0);
\foreach \x in {1,2,3}
\draw[shift={(\x,0)},color=black] (0pt,2pt) -- (0pt,-2pt) node[below] {\footnotesize $\x$};
\draw[->,color=black] (0,0) -- (0,6);
\foreach \y in {1,2,3,4,5,6}
\draw[shift={(0,\y)},color=black] (2pt,0pt) -- (-2pt,0pt) node[left] {\footnotesize $\y$};
\draw[color=black] (0pt,-10pt) node[right] {\footnotesize $0$};
\clip(0,0) rectangle (3,6);
\draw[smooth,samples=100,domain=-4.3:7.38] plot(\x,{2^\x});
\end{tikzpicture}
\end{document}
');

fp.write('\\begin{document}\n')
fp.write('\\begin{flushleft}\n')










### Closing
fp.write('\n')
fp.write('\\end{flushleft} \n')
fp.write('\\end{document}')

ft.write('\n')
ft.write('\\end{flushleft} \n')
ft.write('\\end{document}')


fp.close()
ft.close()











 
