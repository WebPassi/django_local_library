#! /usr/bin/env python
# -*- coding: utf-8 -*-

## Author: Pasquale Franz
## Date: 22.11.2017

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

### Gradmass
from mpmath import *

# erklaere alle buchstaben neutzbaren zu sympy symbolen:
from sympy.abc import *
from collections import Counter

def dreieck_berechnen(a="",b="",c="",alpha="",beta="",gamma=""):
    ### sss
    if not (a == "" or b == "" or c == ""):
        a_berechnet=a
        b_berechnet=b
        c_berechnet=c
        alpha_berechnet=degrees(acos(float((a**2-b**2-c**2)*1.0/(-2*b*c))))
        beta_berechnet=degrees(acos(float((b**2-a**2-c**2)*1.0/(-2*a*c))))
        gamma_berechnet=180-alpha_berechnet-beta_berechnet

    ### sws
    if not (a == "" or b == "" or gamma == ""):
        a_berechnet=a
        b_berechnet=b
        gamma_berechnet=gamma
        c_berechnet=sqrt(a**2+b**2-2*a*b*cos(radians(gamma)))
        alpha_berechnet=degrees(asin(a*1.0/c_berechnet*sin(radians(gamma))))
        beta_berechnet=180-alpha_berechnet-gamma

    if not (a == "" or c == "" or beta == ""):
        a_berechnet=a
        c_berechnet=c
        beta_berechnet=beta
        b_berechnet=sqrt(a**2+c**2-2*a*c*cos(radians(beta)))
        alpha_berechnet=degrees(asin(a*1.0/b_berechnet*sin(radians(beta))))
        gamma_berechnet=180-alpha_berechnet-beta

    if not (b == "" or c == "" or alpha == ""):
        b_berechnet=b
        c_berechnet=c
        alpha_berechnet=alpha
        a_berechnet=sqrt(b**2+c**2-2*b*c*cos(radians(alpha)))
        beta_berechnet=degrees(asin(b*1.0/a_berechnet*sin(radians(alpha))))
        gamma_berechnet=180-alpha-beta_berechnet

        
    ### wsw
    ## a gegeben
    if not (a == "" or alpha == "" or beta == ""):
        a_berechnet=a
        alpha_berechnet=alpha
        beta_berechnet=beta
        gamma_berechnet=180-alpha-beta
        b_berechnet=a*1.0/sin(radians(alpha))*sin(radians(beta))
        c_berechnet=a*1.0/sin(radians(alpha))*sin(radians(gamma_berechnet))

    if not (a == "" or alpha == "" or gamma == ""):
        a_berechnet=a
        alpha_berechnet=alpha
        gamma_berechnet=gamma
        beta_berechnet=180-alpha-gamma
        b_berechnet=a*1.0/sin(radians(alpha))*sin(radians(beta_berechnet))
        c_berechnet=a*1.0/sin(radians(alpha))*sin(radians(gamma))

    if not (a == "" or beta == "" or gamma == ""):
        a_berechnet=a
        beta_berechnet=beta
        gamma_berechnet=gamma
        alpha_berechnet=180-beta-gamma
        b_berechnet=a*1.0/sin(radians(alpha_berechnet))*sin(radians(beta_berechnet))
        c_berechnet=a*1.0/sin(radians(alpha_berechnet))*sin(radians(gamma))

    ## b gegeben
    if not (b == "" or alpha == "" or beta == ""):
        b_berechnet=b
        alpha_berechnet=alpha
        beta_berechnet=beta
        gamma_berechnet=180-alpha-beta
        a_berechnet=b*1.0/sin(radians(beta))*sin(radians(alpha))
        c_berechnet=a_berechnet*1.0/sin(radians(alpha))*sin(radians(gamma_berechnet))

    if not (b == "" or alpha == "" or gamma == ""):
        b_berechnet=b
        alpha_berechnet=alpha
        gamma_berechnet=gamma
        beta_berechnet=180-alpha-gamma
        a_berechnet=b*1.0/sin(radians(beta_berechnet))*sin(radians(alpha))
        c_berechnet=a_berechnet*1.0/sin(radians(alpha))*sin(radians(gamma))

    if not (b == "" or beta == "" or gamma == ""):
        b_berechnet=b
        beta_berechnet=beta
        gamma_berechnet=gamma
        alpha_berechnet=180-beta-gamma
        a_berechnet=b*1.0/sin(radians(beta))*sin(radians(alpha_berechnet))
        c_berechnet=a_berechnet*1.0/sin(radians(alpha_berechnet))*sin(radians(gamma))


    ## c gegeben
    if not (c == "" or alpha == "" or beta == ""):
        c_berechnet=c
        alpha_berechnet=alpha
        beta_berechnet=beta
        gamma_berechnet=180-alpha-beta
        a_berechnet=c*1.0/sin(radians(gamma_berechnet))*sin(radians(alpha))
        b_berechnet=a_berechnet*1.0/sin(radians(alpha))*sin(radians(beta))

    if not (c == "" or alpha == "" or gamma == ""):
        c_berechnet=c
        alpha_berechnet=alpha
        gamma_berechnet=gamma
        beta_berechnet=180-alpha-gamma
        a_berechnet=c*1.0/sin(radians(gamma))*sin(radians(alpha))
        b_berechnet=a_berechnet*1.0/sin(radians(alpha))*sin(radians(beta_berechnet))

    if not (c == "" or beta == "" or gamma == ""):
        c_berechnet=c
        beta_berechnet=beta
        gamma_berechnet=gamma
        alpha_berechnet=180-beta-gamma
        a_berechnet=c*1.0/sin(radians(gamma))*sin(radians(alpha_berechnet))
        b_berechnet=a_berechnet*1.0/sin(radians(alpha_berechnet))*sin(radians(beta))






    return [a_berechnet,b_berechnet,c_berechnet,alpha_berechnet,beta_berechnet,gamma_berechnet]
    #return acos(0)





def dreieck_zeichnen(a="",b="",c="",alpha="",beta="",gamma=""):
    dreieck_berechnen(a,b,c,alpha,beta,gamma)
    latexstr="\\documentclass[12pt,fleqn]{article}  \n\
\\usepackage[utf8]{inputenc}  \n\
\\usepackage{paralist}  \n\
\\usepackage{amssymb}   \n\
\\usepackage{amsthm}    \n\
\\usepackage{eurosym}  \n\
\\usepackage{multicol}  \n\
\\usepackage[ngerman]{babel}  \n\
\\usepackage{tkz-euclide}  \n\
\\usetkzobj{all}  \n\
\\usepackage[left=1.5cm,right=1.5cm,top=1.5cm,bottom=0.5cm]{geometry}  \n\
\\usepackage{amsmath}   \n\
\\usepackage{cancel}  \n\
\\usepackage{pgf,tikz}  \n\
\\usetikzlibrary{arrows}  \n\
\\newtheoremstyle{aufg}  \n\
{16pt}  % Platz zwischen Kopf und voherigem Text  \n\
{16pt}  % und nachfolgendem Text  \n\
{}     % Schriftart des Koerpers  \n\
{}     % mit \\parindent Einzug  \n\
{\\bf}  % Schriftart des Kopfes  \n\
{:}     % Nach Bedarf z.B. Doppelpunkt nach dem Kopf  \n\
{0.5em} % Platz zwischen Kopf und Koerper  \n\
{}     % Kopfname  \n\
\\theoremstyle{aufg}  \n\
\\newtheorem{aufgabe}{Aufgabe}  \n\
\\newtheoremstyle{bsp}  \n\
{16pt}  % Platz zwischen Kopf und voherigem Text  \n\
{16pt}  % und nachfolgendem Text  \n\
{}     % Schriftart des Koerpers  \n\
{}     % mit \parindent Einzug  \n\
{\\em}  % Schriftart des Kopfes  \n\
{:}     % Nach Bedarf z.B. Doppelpunkt nach dem Kopf  \n\
{0.5em} % Platz zwischen Kopf und Koerper  \n\
{}     % Kopfname  \n\
\\theoremstyle{bsp}  \n\
\\newtheorem{beispiel}{Beispiel}  \n\
\\begin{document} \n\
\\begin{flushleft} \n\
\\section{9. Jahrgang} \n\
{\\bf Bestimme die fehlende Seite.} \n\
\\begin{minipage}{7cm} \n\
\\begin{tikzpicture}[rotate=180] \n\
\\coordinate (O) at (0,0); \n\
\\coordinate (A) at (4,0); \n\
\\coordinate (B) at (0,2); \n\
\\draw (O)--(A) node[midway,sloped, above]{a}; \n\
\\draw (A)--(B) node[rotate=0,midway,sloped, below]{7cm}; \n\
\\draw (B)--(O) node[rotate=180,midway,sloped, below]{3cm}; \n\
\\tkzMarkAngle[ size=0.65cm](A,O,B) \n\
\\tkzLabelAngle[pos = 0.35](A,O,B){$\\cdot$} \n\
\\tkzMarkAngle[ size=1.4cm](B,A,O) \n\
\\tkzLabelAngle[pos = 1](B,A,O){$\\alpha$} \n\
\\tkzMarkAngle[ size=0.65cm](O,B,A) \n\
\\tkzLabelAngle[pos = 0.35](O,B,A){$\\beta$} \n\
\\end{tikzpicture} \n\
\\end{minipage} \n\
\\begin{minipage}{7cm} \n\
\\begin{tikzpicture}[rotate=220] \n\
\\coordinate (O) at (0,0); \n\
\\coordinate (A) at (4,0); \n\
\\coordinate (B) at (0,2); \n\
\\draw (O)--(A) node[rotate=40,midway,sloped, above]{3cm}; \n\
\\draw (A)--(B) node[rotate=220,midway,sloped, above]{x}; \n\
\\draw (B)--(O) node[rotate=220,midway,sloped, above]{5cm}; \n\
\\tkzMarkAngle[ size=0.65cm](A,O,B) \n\
\\tkzLabelAngle[pos = 0.35](A,O,B){$\\cdot$} \n\
\\tkzMarkAngle[ size=1.4cm](B,A,O) \n\
\\tkzLabelAngle[pos = 1.1](B,A,O){$60^\\circ$} \n\
\\tkzMarkAngle[ size=0.8cm](O,B,A) \n\
\\tkzLabelAngle[pos = 0.5](O,B,A){$\\beta$} \n\
\\end{tikzpicture} \n\
\\end{minipage} \n\
\\end{flushleft} \n\
\\end{document} \n\ "

    f=open('test.tex','w')
    f.write(latexstr)
    f.close()

    return latexstr
