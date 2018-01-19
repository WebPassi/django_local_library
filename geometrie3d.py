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
import numpy as np

### Gradmass
from mpmath import *

# erklaere alle buchstaben neutzbaren zu sympy symbolen:
from sympy.abc import *
from collections import Counter
from zufall import *

def punkt3d_latex(koordinaten=[1,1,1],name="P"):
    return name + "( " + str(koordinaten[0]) + "\\,|\\," + str(koordinaten[1]) + "\\,|\\," + str(koordinaten[2]) + ")"


def vektor3d_latex(koordinaten=[0,0,0],name="v"):
    return "\\vec{" + name + "}=\\Vekd{" + str(koordinaten[0]) + "}{" + str(koordinaten[1]) + "}{" + str(koordinaten[2]) + "}"  


def gerade3d_latex(sv,rv,name="g",parameter="r"):
    gerade="\\vec{x}=\\Vekd{" + str(sv[0]) + "}{" + str(sv[1]) + "}{" + str(sv[2]) + "} + " + parameter + "\\Vekd{" + str(rv[0]) + "}{" + str(rv[1]) + "}{" + str(rv[2]) + "}" 
    return math(name + ": " + gerade)


def ebene_parameter_latex(sv,rv1,rv2,name="E",parameter=["r","s"]):
    ebene="\\vec{x}=\\Vekd{" + str(sv[0]) + "}{" + str(sv[1]) + "}{" + str(sv[2]) + "} + " + parameter[0] + "\\Vekd{" + str(rv1[0]) + "}{" + str(rv1[1]) + "}{" + str(rv1[2]) + "}+ " + parameter[1] + "\\Vekd{" + str(rv2[0]) + "}{" + str(rv2[1]) + "}{" + str(rv2[2]) + "}" 
    return math(name + ": " + ebene)



def ebene_normalform_latex(sv="",nv="",name="E"):
    von=-5
    bis=5
    if sv == "":
        sv=[0,0,0]
        sv[0]=zufallZ0(von,bis)
        sv[1]=zufallZ0(von,bis)
        sv[2]=zufallZ0(von,bis)


    if nv == "":
        nv=[0,0,0]
        nv[0]=zufallZ0(von,bis)
        nv[1]=zufallZ0(von,bis)
        nv[2]=zufallZ0(von,bis)

    ebene_normal="(\\vec{x} - \\Vekd{" + str(sv[0]) + "}{" + str(sv[1]) + "}{" + str(sv[2]) + "}) \\cdot \\Vekd{" + str(nv[0]) + "}{" + str(nv[1]) + "}{" + str(nv[2]) + "} = 0 " 

    ebene_koord = latex(nv[0]) + "x_1 + " + latex(nv[1]) + "x_2 + " + latex(nv[2]) + "x_3" + " = " + latex(np.dot(sv,nv))

    return [mmath(name + ": " + ebene_normal), mmath(name + ": " + ebene_koord)]






def gerade_identisch(sv,rv):
    r=zufallZ01(-2,2)
    sv2=sv+r*rv

    k=zufallZ01(-2,2)
    rv2=k*rv

    return gerade3d_latex(sv2,rv2,"i")


def gerade_parallel(sv,rv,name="p"):
    r=zufallZ01(-2,2)
    sv2=sv+rv+r*np.array([1,0,-1])

    k=zufallZ01(-2,2)
    rv2=k*rv

    return gerade3d_latex(sv2,rv2,"p")



def gerade_schnitt(sv,rv):
    r=zufallZ0(-2,2)
    sv2=sv+r*rv

    k=zufallZ01(-2,2)
    rv2=rv+k*np.array([1,0,-1])

    return gerade3d_latex(sv2,rv2,"s")



def gerade_windschief(sv,rv):
    r=zufallZ01(-2,2)
    sv2=sv+r*(rv+np.array([1,0,-1]))


    rv2=np.cross(sv2-sv,rv)

    return gerade3d_latex(sv2,rv2,"w")



###### Ebenen
def aufg_ebene_3Punktform(art="ganz",runden=2,intervall=[2,7],aufgabentext="Geben Sie eine Ebene $E$ in Parameterform an, welche die folgenden drei Punkte enthält.  ",anzahl=1,spalten=1):

    ### Aufgabe
    von=intervall[0]
    bis=intervall[1]
    stellen=runden

    p1=[0,0,0]
    p2=[0,0,0]
    p3=[0,0,0]
    if art == "Z":
        p1[0]=zufallZ0(von,bis)
        p1[1]=zufallZ0(von,bis)
        p1[2]=0

        p2[0]=zufallZ0(von,bis)
        p2[1]=0
        p2[2]=zufallZ0(von,bis)

        p3[0]=zufallZ0(von,bis)
        p3[1]=0
        p3[2]=zufallZ0(von,bis)
    elif art == "dezimal":
        p1[0]=zufallR(von,bis,stellen)
        p1[1]=zufallR(von,bis,stellen)
        p1[2]=0

        p2[0]=zufallR(von,bis,stellen)
        p2[1]=0
        p2[2]=zufallR(von,bis,stellen)

        p3[0]=zufallR(von,bis,stellen)
        p3[1]=0
        p3[2]=zufallR(von,bis,stellen)


    aufgabe=makeExercise(mmath(punkt3d_latex(p1,"P_1") + " \\quad,\\quad " + punkt3d_latex(p2,"P_2") + " \\quad,\\quad " + punkt3d_latex(p1,name="P_3")),aufgabentext=aufgabentext)


                

    #### Lösung
    sv=np.array(p1)
    rv1=np.array(p2) - np.array(p1)
    rv2=np.array(p3) - np.array(p1)

    loesung=makeExercise(ebene_parameter_latex(sv,rv1,rv2),aufgabentext=aufgabentext)
    

    return [aufgabe,loesung]




##### Winkel
def aufg_winkel_vektoren(art="ganz",runden=2,intervall=[2,7],aufgabentext="",anzahl=1,spalten=1):

    ### Aufgabe
    von=intervall[0]
    bis=intervall[1]
    stellen=runden

    p1=[0,0,0]
    p2=[0,0,0]
    if art == "Z":
        p1[0]=zufallZ0(von,bis)
        p1[1]=zufallZ0(von,bis)
        p1[2]=0

        p2[0]=zufallZ0(von,bis)
        p2[1]=0
        p2[2]=zufallZ0(von,bis)

    elif art == "dezimal":
        p1[0]=zufallR(von,bis,stellen)
        p1[1]=zufallR(von,bis,stellen)
        p1[2]=0

        p2[0]=zufallR(von,bis,stellen)
        p2[1]=0
        p2[2]=zufallR(von,bis,stellen)


    aufgabe=makeExercise(mmath(vektor3d_latex(p1,"u_1") + " \\quad,\\quad " + vektor3d_latex(p2,"u_2")),aufgabentext=aufgabentext)


                

    #### Lösung
    u1=np.array(p1)
    u2=np.array(p2)


    loesung=makeExercise(str(winkel_zwischen_vektoren(u1,u2))) 
    

    #return [aufgabe,loesung]
    return [aufgabe,loesung]



def winkel_zwischen_vektoren(u1,u2):
    dot = np.dot(u1,u2)
    abs1 = np.sqrt((u1*u1).sum())
    abs2 = np.sqrt((u2*u2).sum())

    cos_angle = dot / abs1 / abs2
    
    angle_rad = np.arccos(cos_angle)
    
    angle_deg = angle_rad * 360 / 2 / np.pi

    return angle_deg
