#! /usr/bin/env python

#! /usr/bin/env python

## Author: Pasquale Franz
## Date: 26.01.2015

######
## Generate a table in latex-format with given values
import os


from elements import *
from functions import *
from darstellung import *
from aufgaben import *
from zufall import *



def zertifikat_parabeln_potenzen():
    strFileName="zertifikat_parabeln_und_potenzen"
    strFileName_lsg="zertifikat_parabeln_und_potenzen_lsg"

    strFileTex=strFileName + ".tex"
    strFileTex_lsg=strFileName_lsg + ".tex"
    strFilePdf=strFileName + ".pdf"
    strFilePdf_lsg=strFileName_lsg + ".pdf"
    
    datei=open(strFileName + ".tex",'a')
    datei_lsg=open(strFileName_lsg + ".tex",'a')
    f=QuadFunc("s",-0.5,-1,2.5)
    
    aufg1=makeExercise(aufgWertetabelleGraph(f))
    aufg1_lsg=makeExercise(aufgWertetabelleGraph(f,"a"))

    # Funktionen in Liste definieren
    flist=[]
    for index in range(3):
        flist.append(QuadFunc("s",zufallQ0(-4,4),zufallZ(-2,2),zufallZ(-2,2)))
    for index,funktion in enumerate(flist):
        funktion.name="f_" + latex(index+1) 
    #numfunc=enumlist(erstelleFunktionsliste(flist))
    
    aufg2=makeExercise(aufgParabeleigenschaftenAllgemein(flist))
    aufg2_lsg=makeExercise(aufgParabeleigenschaftenAllgemein(flist,"a"))
    
#    aufg6=makeExercise(aufgFunktionaufstellen(flist))
#    aufg6_lsg=makeExercise(aufgFunktionaufstellen(flist,"a"))

    

    flist=[]
    for index in range(3):
        flist.append(QuadFunc("s",zufallQ0(-4,4),zufallZ(-2,2),zufallZ(-2,2)))
    for index,funktion in enumerate(flist):
        funktion.name="f_" + latex(index+1) 

    aufg3=makeExercise(aufgAuswahlGraph(flist))
    aufg3_lsg=makeExercise(aufgAuswahlGraph(flist,"a"))

    flist=[]
    for index in range(6):
        flist.append(QuadFunc("s",zufallZ0(-3,3),zufallZ(-3,3),zufallZ(-3,3)))
    for index,funktion in enumerate(flist):
        funktion.name="f_" + latex(index+1) 

    aufg6=makeExercise(aufgScheitelpunktform(flist))
    aufg6_lsg=makeExercise(aufgScheitelpunktform(flist,"a"))

    flist=[]
    for index in range(6):
        flist.append(QuadFunc("s",zufallZ0(-3,3),zufallZ(-2,2),zufallZ(-2,2)))
    for index,funktion in enumerate(flist):
        funktion.name="f_" + latex(index+1) 

    aufg5=makeExercise(aufgNormalform(flist))
    aufg5_lsg=makeExercise(aufgNormalform(flist,"a"))


    flist=[]
    for index in range(4):
        flist.append(QuadFunc("s",zufallQ0(-4,4),zufallZ(-2,2),zufallZ(-2,2)))
    for index,funktion in enumerate(flist):
        funktion.name="f_" + latex(index+1) 
