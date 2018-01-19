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
from textaufgaben.models import *



def zertifikat_parabeln_potenzen():
    strFileName="zertifikat_parabeln_und_potenzen"
    strFileName_lsg=strFileName + "_lsg"

    strFileTex=strFileName + ".tex"
    strFileTex_lsg=strFileName_lsg + ".tex"
    strFilePdf=strFileName + ".pdf"
    strFilePdf_lsg=strFileName_lsg + ".pdf"
    
    os.system('rm ' + strFileTex)
    os.system('rm ' + strFileTex_lsg)



    datei=open(strFileName + ".tex",'w')
    datei_lsg=open(strFileName_lsg + ".tex",'w')
    

    ### Grundniveau
    gn="\\begin{center} \\begin{framed} Grundniveau \\end{framed} \\end{center}"





    ### Aufgabe 1
    ### Parabeleigenschaften
    a1=Aufgabe()

    flist=[]
    for index in range(2):
        flist.append(QuadFunc("s",1,zufallZ(-2,2),zufallZ(-2,2)))
    for index,funktion in enumerate(flist):
        funktion.name="f_" + latex(index+1) 
    
    a1.punkte=6
    a1.aufgabe=makeExercise(aufgParabeleigenschaften(flist), str(a1.punkte))
    a1.lsg=makeExercise(aufgParabeleigenschaften(flist,"a"), str(a1.punkte))
    




    ### Aufgabe 2
    ### Potenzen

    a2=Aufgabe()

    potenzen=[]
    faktoren=[]
    for i in range(3):
        potenzen.append(Potenz(10,zufallZ(-5,5)))
        faktoren.append(zufallZ(-20,20))

    a2.punkte=3
    a2.aufgabe=makeExercise(aufgZehnerpotenzFaktor(faktoren,potenzen), str(a2.punkte))
    a2.lsg=makeExercise(aufgZehnerpotenzFaktor(faktoren,potenzen,"a"), str(a2.punkte))
    


    gn=grundniveau([a1,a2])
    gn_lsg=grundniveau([a1,a2],"a")





    ### Aufgabe 1
    ### Parabel zeichnen
    a3=Aufgabe()

    f=QuadFunc("n",1,zufallZ0(-3,3),zufallZ0(-3,3))
    

    a3.punkte=7
    a3.aufgabe=makeExercise(aufgWertetabelleGraph(f), str(a3.punkte))
    a3.lsg=makeExercise(aufgWertetabelleGraph(f,"a"), str(a3.punkte))






    ### Aufgabe 4
    ### Einheiten,Potenzen

    a4=Aufgabe()

    einheiten=[]
    zahlen=[]
    for index in range(3):
        einheiten.append("GB")
        zahlen.append(zufallN(100))
        

    a4.punkte=3
    a4.aufgabe=makeExercise(aufgZehnerpotenzEinheiten(zahlen,einheiten), str(a4.punkte))
    a4.lsg=makeExercise(aufgZehnerpotenzEinheiten(zahlen,einheiten,"a"), str(a4.punkte))

    

    a5=Aufgabe()
    
    ta=Textaufgabe.objects.all()[0]
    
    a5.punkte=4
    a5.aufgabe=makeExercise(ta.erzeugeAufgabe(["6 GB", "2 MB"]), str(a5.punkte))
    a5.lsg=makeExercise(ta.erzeugeAufgabe(["6 GB", "2 MB"])+ta.loesung(["6 GB", "2 MB"]), str(a5.punkte))



    a6=Aufgabe()
    
    ta=Textaufgabe.objects.all()[1]
    
    a6.punkte=4
    v1="200000 l"
    v2="0.01 mm"
    a6.aufgabe=makeExercise(ta.erzeugeAufgabe([v1, v2]), str(a6.punkte))
    a6.lsg=makeExercise(ta.erzeugeAufgabe([v1, v2])+ta.loesung([v1, v2]), str(a6.punkte))



    a7=Aufgabe()
    
    ta=Textaufgabe.objects.all()[2]
    
    a7.punkte=4
    v="20 ha"
    a7.aufgabe=makeExercise(ta.erzeugeAufgabe([v]), str(a7.punkte))
    a7.lsg=makeExercise(ta.erzeugeAufgabe([v])+ta.loesung([v]), str(a7.punkte))



    sn=standardniveau([a3,a5,a6,a7])
    sn_lsg=standardniveau([a3,a5,a6,a7],"a")



    ### Erhoehtes Niveau
    a8=Aufgabe()
    a8.punkte=4

    f=[QuadFunc("n",1,-4,3)]
    a8.aufgabe=makeExercise(aufgScheitelpunktform(f),str(a8.punkte))
    a8.lsg=makeExercise(aufgScheitelpunktform(f,"a"),str(a8.punkte))



    hn=highniveau([a8])
    hn_lsg=highniveau([a8],"a")


    
    sheet=makeZertifikat(gn+sn+hn,"Parabeln und Potenzen",32)

    sheet_lsg=makeZertifikat(gn_lsg+sn_lsg+hn_lsg,"Parabeln und Potenzen", 32)

    datei.write(sheet)
    datei.close()

    datei_lsg.write(sheet_lsg)
    datei_lsg.close()
    os.system('pdflatex --shell-escape ' + strFileTex)
    os.system('pdflatex --shell-escape ' + strFileTex_lsg)
#    os.system('evince ' + strFilePdf + '&')        
    os.system('evince ' + strFilePdf_lsg + '&')    


