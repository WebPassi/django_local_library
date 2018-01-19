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




def test_vermischte_Aufgaben():
    strFileName="test_pauli"
    strFileName_lsg=strFileName + "_lsg"

    strFileTex=strFileName + ".tex"
    strFileTex_lsg=strFileName_lsg + ".tex"
    strFilePdf=strFileName + ".pdf"
    strFilePdf_lsg=strFileName_lsg + ".pdf"
    
    os.system('rm ' + strFileTex)
    os.system('rm ' + strFileTex_lsg)



    datei=open(strFileName + ".tex",'a')
    datei_lsg=open(strFileName_lsg + ".tex",'a')



    aufg=[]
    lsg=[]


    ### Aufgabe 1


    a1=Aufgabe()

    term=[]
    term_lsg=[]

    for i in range(3):
        var1=str(zufallN(20))
        var2=str(zufallN(20))
        op=random.choice(["+","-"])
        vnam=random.choice(["x","y","a","b"])

        term.append(var1 + "*" + vnam + op + var2  + "*" + vnam)


    a1.punkte=3
    a1.aufgabe=makeExercise(aufgTerme(term), str(a1.punkte))
    a1.lsg=makeExercise(aufgTerme_lsg(term), str(a1.punkte))

    aufg.append(a1.aufgabe)
    lsg.append(a1.lsg)


    ### Aufgabe 2
    a2=Aufgabe()

    term=[]
    term_lsg=[]

    for i in range(2):
        var1=str(zufallN(20))
        var2=str(zufallN(20))
        var3=str(zufallN(20))
        var4=str(zufallN(20))
        op1=random.choice(["+","-"])
        op2=random.choice(["+","-"])
        op3=random.choice(["+","-"])
        
        auswahl=[]
        auswahl.append(random.choice(["x","y","a","b"]))
        auswahl.append(random.choice(["x","y","a","b"]))


        term.append(var1 + "*" + random.choice(auswahl) + op1 + var2  + "*" + random.choice(auswahl) + op2 + var3 + "*" + random.choice(auswahl) + op3 + var4 + "*" + random.choice(auswahl) )


    a2.punkte=4
    a2.aufgabe=makeExercise(aufgTerme(term,2), str(a2.punkte))
    a2.lsg=makeExercise(aufgTerme_lsg(term,2), str(a2.punkte))
    
    aufg.append(a2.aufgabe)
    lsg.append(a2.lsg)


    ### Aufgabe 3
    a3=Aufgabe()

    term=[]
    term_lsg=[]

    var1=str(zufallN(20))
    var2=str(zufallN(20))
    var3=str(zufallN(20))
    var4=str(zufallN(20))
    op1=random.choice(["+","-"])
    op2=random.choice(["+","-"])
    op3=random.choice(["+","-"])

    varnam=random.choice(["x","y","a","b"])

    term.append(var1 + "*(" + var2  + "*" + varnam + op1 + var3 + ")")


    var1=str(zufallN(20))
    var2=str(zufallN(20))
    var3=str(zufallN(20))
    var4=str(zufallN(20))
    op1=random.choice(["+","-"])
    op2=random.choice(["+","-"])
    op3=random.choice(["+","-"])

    varnam=random.choice(["x","y","a","b"])

    term.append("(" + var1 + "*" + varnam + op + var2 + ")" + "*(" + var3 + "*" + varnam + op + var4 + ")")



    a3.punkte=5
    a3.aufgabe=makeExercise(aufgTerme(term,2), str(a3.punkte))
    a3.lsg=makeExercise(aufgTerme_lsg(term,2), str(a3.punkte))
    
    aufg.append(a3.aufgabe)
    lsg.append(a3.lsg)



    ### Aufgabe 4

    a4=Aufgabe()

    glg=[]
    glg_lsg=[]

    t1=LinTerm(zufallZ0(-3,3),0)
    t2=LinTerm(0,zufallZ0(-3,3))
    glg.append("$" + aufgGlg(t1,t2) + "$")
    glg_lsg.append("$" + aufgGlg(t1,t2) + "$" + "\\\\" + "$x=" + aufgGlg_lsg(t1,t2) + "$")

    t1=LinTerm(zufallZ0(-3,3),zufallZ0(-3,3))
    t2=LinTerm(0,zufallZ0(-3,3))
    glg.append("$" + aufgGlg(t1,t2) + "$")
    glg_lsg.append("$" + aufgGlg(t1,t2) + "$" + "\\\\" + "$x=" + aufgGlg_lsg(t1,t2) + "$")


    t1=LinTerm(zufallZ0(-3,3),zufallZ0(-3,3))
    t2=LinTerm(zufallZ0(-3,3),zufallZ0(-3,3))
    glg.append("$" + aufgGlg(t1,t2) + "$")
    glg_lsg.append("$" + aufgGlg(t1,t2) + "$" + "\\\\" + "$x=" + aufgGlg_lsg(t1,t2) + "$")

    
    a4.punkte=6
    a4.aufgabe=makeExercise(multicol(glg,3), str(a4.punkte))
    a4.lsg=makeExercise(multicol(glg_lsg,3), str(a4.punkte))

    aufg.append(a4.aufgabe)
    lsg.append(a4.lsg)
    


    a5=Aufgabe()
    
    ta=Textaufgabe.objects.filter(name="Kreditzinsen")[0]
    
    a5.punkte=4

    gw=str(zufallN(9)*1000)
    p=str(zufallN(7))
    namensliste=["Uli","Manfred","Herr Stein"]
    name=random.choice(namensliste)
    a5.aufgabe=makeExercise(ta.erzeugeAufgabe([name,gw,p]), str(a5.punkte))
    a5.lsg=makeExercise(ta.erzeugeAufgabe([name,gw,p])+ta.loesung([name,gw,p]), str(a5.punkte))

    aufg.append(a5.aufgabe)
    lsg.append(a5.lsg)


    a6=Aufgabe()
    
    ta=Textaufgabe.objects.filter(name="Kreditzinsen")[1]
    
    a6.punkte=4

    gw=str(zufallZ(330000,350000)/100.0)
    pwplus=str(zufallZ(350000,370000)/100.0)

#    namensliste=["Uli","Manfred","Herr Stein"]
#    name=random.choice(namensliste)
    a6.aufgabe=makeExercise(ta.erzeugeAufgabe([gw,pwplus]), str(a6.punkte))
    a6.lsg=makeExercise(ta.erzeugeAufgabe([gw,pwplus])+ta.loesung([gw,pwplus]), str(a6.punkte))

    aufg.append(a6.aufgabe)
    lsg.append(a6.lsg)






    a7=Aufgabe()
    
    ta=Textaufgabe.objects.filter(name="Kreditzinsen")[2]
    
    a7.punkte=4

    pw=str(zufallZ(100,300)*1000)
    p=str(zufallN(7))
    namensliste=["Deutschland","Hamburg","Berlin"]
    name=random.choice(namensliste)
    a7.aufgabe=makeExercise(ta.erzeugeAufgabe([name,p,pw,name]), str(a7.punkte))
    a7.lsg=makeExercise(ta.erzeugeAufgabe([name,p,pw,name])+ta.loesung([name,p,pw,name]), str(a7.punkte))

    aufg.append(a7.aufgabe)
    lsg.append(a7.lsg)


    punkte=a1.punkte+a2.punkte+a3.punkte+a4.punkte+a5.punkte+a6.punkte+a7.punkte


    
    sheet=makeTest(exercises=aufg, kurs="WA Pauli",title="Schriftliche Arbeit", punkte=punkte)

    sheet_lsg=makeTest(exercises=lsg, kurs="WA Pauli",title="Schriftliche Arbeit", punkte=punkte)


    datei.write(sheet)
    datei.close()

    datei_lsg.write(sheet_lsg)
    datei_lsg.close()
    os.system('pdflatex --shell-escape ' + strFileTex)
    os.system('pdflatex --shell-escape ' + strFileTex_lsg)
#    os.system('evince ' + strFilePdf + '&')        
    os.system('evince ' + strFilePdf_lsg + '&')    







