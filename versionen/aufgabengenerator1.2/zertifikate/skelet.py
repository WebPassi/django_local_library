#! /usr/bin/env python

## Author: Pasquale Franz
## Date: 26.01.2015

######
## Just the skelet of a latex file


# erklaere alle buchstaben neutzbaren zu sympy symbolen:
from sympy.abc import *

from zinsen.models import Aufgabe

import re

import random

### note: um einen \ mit write() zu erzeugen muss  \\ getippt werden.

class Skelet:
    def head(self):
        lf = open('datei.tex','w')
        lf.write('\
\\documentclass[12pt]{article}\n\
\\usepackage[utf8]{inputenc}\n\
\\usepackage{paralist} \n\
\\usepackage{amssymb}  \n\
\\usepackage{amsthm}   \n\
\\usepackage{multicol} \n\
\\usepackage[left=1.5cm,right=1.5cm,top=0.8cm,bottom=1cm]{geometry} \n\
\\usepackage{amsmath}  \n\
\\begin{document}\n\
\\begin{flushleft}\n')
        lf.close()
    def end(self):
        lf = open('datei.tex','a')
        lf.write('\
\\end{flushleft}\n\
\\end{document}')
        lf.write('\n')
        lf.close()
    def body(self,aufgabe):
        lf = open('datei.tex','a')
        lf.write(aufgabe.write())
        lf.write('\n')
        lf.close()

class AAufgabe:
    def __init__(self,text,bereich,inhalt,schwierigkeit,punkte):
        self.text=text
        self.bereich=bereich
        self.inhalt=inhalt
        self.schwierigkeit=schwierigkeit
        self.punkte=punkte
        self.muster = r"#\[[^(\]#)]*\]#"
    def write(self):
        return '\\begin{aufgabe} ~ \\\\ \n' + self.text + '\\\\ \n \\end{aufgabe} \\\\ \n'

class Zinsen(AAufgabe):
    def __init__(self,aufgabe):
        self.text=aufgabe.text
        self.inhalt=aufgabe.inhalt
        self.muster=aufgabe.muster
        self.gw=0
        self.pw=0
        self.p=0
    def plaintext(self):
        text = re.split(self.muster,self.text)
        return text
    def hole_werte(self):
        info = re.findall(self.muster,self.text)
        for werte in info:
            tmp = werte.replace('#[','').replace(']#','')
            wert = tmp.split(',')
            if wert[0] == "G":
                if wert[1] == "N":
                    print wert[2]
                    print wert[3]
                    self.gw=random.randint(int(wert[2]),int(wert[3]))
                elif wert[1] == "R":
                    self.gw=random.random()*(float(wert[3])-float(wert[2]))+float(wert[2])
                self.text=self.text.replace(werte,str(self.gw))                
            elif wert[0] == "W":
                if wert[1] == "N":
                    self.pw=random.randint(int(wert[2]),int(wert[3]))
                elif wert[1] == "R":
                    self.pw=random.random()*(float(wert[3])-float(wert[2]))+float(wert[2])
                self.text=self.text.replace(werte,str(self.pw))
            elif wert[0] == "p":
                if wert[1] == "N":
                    self.p=random.randint(int(wert[2]),int(wert[3]))
                elif wert[1] == "R":
                    self.p=random.random()*(float(wert[3])-float(wert[2]))+float(wert[2])
                self.text=self.text.replace(werte,str(self.p))
    def werte(self):
        werte = re.findall(self.muster,self.text)
        return werte    
    def zeige(self):
        print self.text
        lf = open('datei.tex','a')
        lf.write(str(self.plaintext()[0]))
        lf.write(str(self.werte()))
        lf.close()














 
