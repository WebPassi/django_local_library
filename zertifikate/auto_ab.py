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
#import random


def ab_terme():
    strFileName="terme"
    strFileTex=strFileName + ".tex"
    strFilePdf=strFileName + ".pdf"
    datei=open(strFileName + ".tex",'w')
    terme=list(range(3))
    terme[0]=3*x
    terme[1]=-5*x
    terme[2]=8*x
    term=Term(terme)
#    aufg=makeSheet(makeExercise(latex(term.test()[2])))
    aufg=makeSheet(makeExercise(term.zeigeAusdruck()))
    datei.write(aufg)
    datei.close()
    os.system('pdflatex ' + strFileTex)
    os.system('evince ' + strFilePdf + '&')    


def ab_lin():
    strFileName="ab_lin"
    strFileTex=strFileName + ".tex"
    strFilePdf=strFileName + ".pdf"
    datei=open(strFileName + ".tex",'w')
    t1=LinTerm(3,-2)
    t2=LinTerm(4,-3)
    e=Equation(t1,t2)
    rw=e.rechenweg("v")
    aufg=makeExercise(rw)
#    aufg=makeExercise(glg)
    sheet=makeSheet(aufg)

    datei.write(sheet)
    datei.close()
    os.system('pdflatex ' + strFileTex)
    os.system('evince ' + strFilePdf + '&')



def ab_linglg():
    strFileName="lineare_gleichungen"
    strFileTex=strFileName + ".tex"
    strFilePdf=strFileName + ".pdf"
    datei=open(strFileName + ".tex",'w')
    
    anzahl_aufgaben=6
    anzahl_menge=9
    glgsymp = [[0 for spalte in range(anzahl_menge)] for zeile in range(anzahl_aufgaben)]
    glg = [[0 for spalte in range(anzahl_menge)] for zeile in range(anzahl_aufgaben)]
    lsg = [[0 for spalte in range(anzahl_menge)] for zeile in range(anzahl_aufgaben)]
    aufg = range(anzahl_aufgaben)
    ### Einfache lineare Gleichungen
    for i in range(anzahl_menge):
        linterm1=LinTerm(zufallZ0(-10,10),0)
        linterm2=LinTerm(0,zufallZ0(-10,10))
        glgsymp[0][i]=Equation(linterm1,linterm2)
        glg[0][i]=Equation(linterm1,linterm2).zeigeGlg()
        lsg[0][i]=glgsymp[0][i].zeigeLsg()
    multi=multicol(glg[0],3)    
    aufg[0]=makeExercise(multi)

    ### Rechts 0
    for i in range(anzahl_menge):
        linterm1=LinTerm(zufallZ0(-10,10),zufallZ(-10,10))
        linterm2=LinTerm(0,0)
        glgsymp[1][i]=Equation(linterm1,linterm2)
        glg[1][i]=Equation(linterm1,linterm2).zeigeGlg()
        lsg[1][i]=glgsymp[1][i].zeigeLsg()
    multi=multicol(glg[1],3)    
    aufg[1]=makeExercise(multi)

    ### Rechts Zahl
    for i in range(anzahl_menge):
        linterm1=LinTerm(zufallZ0(-10,10),zufallZ(-10,10))
        linterm2=LinTerm(0,zufallZ(-10,10))
        glgsymp[2][i]=Equation(linterm1,linterm2)
        glg[2][i]=Equation(linterm1,linterm2).zeigeGlg()
        lsg[2][i]=glgsymp[2][i].zeigeLsg()
    multi=multicol(glg[2],3)    
    aufg[2]=makeExercise(multi)

    ### Links Rechts
    for i in range(anzahl_menge):
        linterm1=LinTerm(zufallZ0(-10,10),zufallZ(-10,10))
        linterm2=LinTerm(zufallZ0(-10,10),zufallZ(-10,10))
        glgsymp[3][i]=Equation(linterm1,linterm2)
        glg[3][i]=Equation(linterm1,linterm2).zeigeGlg()
        lsg[3][i]=glgsymp[3][i].zeigeLsg()
    multi=multicol(glg[3],3)    
    aufg[3]=makeExercise(multi)

    ### Klammern links, Zahl rechts
    for i in range(anzahl_menge):
        linterm1=LinTerm(zufallZ0(-10,10),zufallZ(-10,10),zufallZ0(-10,10))
        linterm2=LinTerm(0, zufallZ(-10,10))
        glgsymp[4][i]=Equation(linterm1,linterm2)
        glg[4][i]=Equation(linterm1,linterm2).zeigeGlg()
        lsg[4][i]=glgsymp[4][i].zeigeLsg()
    multi=multicol(glg[4],3)    
    aufg[4]=makeExercise(multi)

    ### Klammern links, Klammer rechts
    for i in range(anzahl_menge):
        linterm1=LinTerm(zufallZ0(-10,10),zufallZ(-10,10),zufallZ0(-10,10))
        linterm2=LinTerm(zufallZ0(-10,10),zufallZ(-10,10),zufallZ0(-10,10))
        glgsymp[5][i]=Equation(linterm1,linterm2)
        glg[5][i]=Equation(linterm1,linterm2).zeigeGlg()
        lsg[5][i]=glgsymp[5][i].zeigeLsg()
    multi=multicol(glg[5],2)    
    aufg[5]=makeExercise(multi)

    
    ### Aufgabe zusammenstellen
    aufgaben=""
    for a in aufg:
        aufgaben+=a

    ### Loesungen
    loes=range(54)
    strloes=""
    index=0
    for i in range(6):
        for j in lsg[i]:
            loes[index]=j
            strloes+=scriptstyle(latex(loes[index])) + " , "
            index+=1    
    ### Loesungen zufall
    zufloes=zufallsliste(loes)
    strzufloes=""
    for i in zufloes:
        strzufloes+=scriptstyle(latex(i)) + " , "
    ab=makeSheet(aufgaben + strzufloes + "\\\\[0.2em] \n" + strloes)
    datei.write(ab)
    datei.close()
    os.system('pdflatex ' + strFileTex)
    os.system('evince ' + strFilePdf + '&')   

def ab_linfunc():
    strFileName="lineare_funktionen"
    strFileTex=strFileName + ".tex"
    strFilePdf=strFileName + ".pdf"
    datei=open(strFileName + ".tex",'w')

    flist=[]
    flist.append(LinFunc(1,0))
    for index in range(3):
        lf=LinFunc(1,zufallZ0(-6,6))
        flist.append(lf)
    numfunc=enumlist(erstelleFunktionsliste(flist))
    graph=zeichneGraph(flist,0.3)
    elemente=teileBlatt(numfunc,graph,0.3,0.7)
    aufg1=makeExercise(elemente)
    
    flist=[]
    flist.append(LinFunc(1,0))
    for index in range(3):
        flist.append(LinFunc(zufallQ0(-4,4),0))
    numfunc=enumlist(erstelleFunktionsliste(flist))
    graph=zeichneGraph(flist,0.3)
    elemente=teileBlatt(numfunc,graph,0.3,0.7)
    aufg2=makeExercise(elemente)

    flist=[]
    flist.append(LinFunc(1,0))
    for index in range(3):
        flist.append(LinFunc(zufallQ0(-4,4),zufallZ0(-6,6)))
    numfunc=enumlist(erstelleFunktionsliste(flist))
    graph=zeichneGraph(flist,0.3)
    elemente=teileBlatt(numfunc,graph,0.3,0.7)
    aufg3=makeExercise(elemente)

    flist=[]
    flist.append(LinFunc(1,0))
    for index in range(3):
        flist.append(LinFunc(zufallQ0(-4,4),zufallZ0(-6,6)))
#    numfunc=enumlist(erstelleFunktionsliste(flist))
    graph=zeichneGraph(flist,0.8)
#    elemente=teileBlatt(0.3,0.7,numfunc,graph)
    aufg4=makeExercise(graph)

    ab=makeSheet(aufg1+aufg2+aufg3+aufg4)
    datei.write(ab)
    
    datei.close()
    os.system('pdflatex ' + strFileTex)
    os.system('evince ' + strFilePdf + '&') 



def ab_quadglg():
    strFileName="quadratische_gleichungen"
    strFileTex=strFileName + ".tex"
    strFilePdf=strFileName + ".pdf"
    datei=open(strFileName + ".tex",'w')
    
    anzahl_aufgaben=6
    anzahl_menge=9
    glgsymp = [[0 for spalte in range(anzahl_menge)] for zeile in range(anzahl_aufgaben)]
    glg = [[0 for spalte in range(anzahl_menge)] for zeile in range(anzahl_aufgaben)]
    lsg = [[0 for spalte in range(anzahl_menge)] for zeile in range(anzahl_aufgaben)]
    aufg = range(anzahl_aufgaben)
    ### Einfache lineare Gleichungen
    for i in range(anzahl_menge):
        term1=QuadFunc("n", 1, zufallZ0(-10,10),0)
        term2=QuadFunc("n", 1, 2,3)
        glgsymp[0][i]=Equation(term1,term2)
        glg[0][i]=Equation(term1,term2).zeigeGlgLatex()
        lsg[0][i]=glgsymp[0][i].zeigeLsg()
    multi=multicol(glg[0],3)    
    aufg[0]=makeExercise(multi)

    ab=makeSheet(aufg[0])
    datei.write(ab)
    datei.close()
    os.system('pdflatex ' + strFileTex)
    os.system('evince ' + strFilePdf + '&')   





def ab_quadfunc_alt():
    strFileName="sheet"
    strFileTex=strFileName + ".tex"
    strFilePdf=strFileName + ".pdf"
    datei=open(strFileName + ".tex",'w')
    f=QuadFunc("n",zufallQ(-5,5),zufallQ(-9,9),zufallZ(-9,9))
    func=math(zeigeFunktion(f))
    aufg=makeExercise(func)
    ab=makeSheet(aufg)
    g=QuadFunc(Rational(1,5),Rational(1,5),Rational(1,5))
    testexpr=latex(g.expr) 
    datei.write(testexpr + "\n")
    datei.write(bruch(testexpr))
    #datei.write(ab)
    datei.close()
    #os.system('pdflatex ' + strFileTex)
    #os.system('evince ' + strFilePdf + '&')    

def ab_quadfunc():
    strFileName="ab1_normalparabel"
    strFileName_lsg="ab1_normalparabel_lsg"
    strFileTex=strFileName + ".tex"
    strFileTex_lsg=strFileName_lsg + ".tex"
    strFilePdf=strFileName + ".pdf"
    strFilePdf_lsg=strFileName_lsg + ".pdf"
    datei=open(strFileName + ".tex",'w')
    datei_lsg=open(strFileName_lsg + ".tex",'w')

    # Funktionen in Liste definieren
    flist=[]
    for index in range(3):
        flist.append(QuadFunc("s",1,zufallZ(-3,3),zufallZ(-3,3)))
    for index,funktion in enumerate(flist):
        funktion.name="f_" + latex(index+1) 
    #numfunc=enumlist(erstelleFunktionsliste(flist))
    
    aufg2=makeExercise(aufgParabeleigenschaften(flist))
    aufg2_lsg=makeExercise(aufgParabeleigenschaften(flist,"a"))
    
    aufg6=makeExercise(aufgFunktionaufstellen(flist))
    aufg6_lsg=makeExercise(aufgFunktionaufstellen(flist,"a"))

    
    flist=[]
    for index in range(6):
        flist.append(QuadFunc("s",1,zufallZ(-2,2),zufallZ(-2,2)))
    for index,funktion in enumerate(flist):
        funktion.name="f_" + latex(index+1) 
    
    aufg5=makeExercise(aufgGraph(flist))
    aufg5_lsg=makeExercise(aufgGraph(flist,"a"))


    flist=[]
    for index in range(3):
        flist.append(QuadFunc("s",1,zufallZ(-2,2),zufallZ(-2,2)))
    for index,funktion in enumerate(flist):
        funktion.name="f_" + latex(index+1) 
    aufg3=makeExercise(aufgAuswahlGraph(flist))
    aufg3_lsg=makeExercise(aufgAuswahlGraph(flist,"a"))

    flist=[]
    for index in range(4):
        flist.append(QuadFunc("s",1,zufallZ(-2,2),zufallZ(-2,2)))
    for index,funktion in enumerate(flist):
        funktion.name="f_" + latex(index+1) 
    aufg4=makeExercise(aufgAuswahlFunktion(flist))
    aufg4_lsg=makeExercise(aufgAuswahlFunktion(flist,"a"))
    
    sheet=makeSheet(aufg1+aufg2+aufg3+aufg4+aufg5+aufg6)
    sheet_lsg=makeSheet(aufg1_lsg+aufg2_lsg+aufg3_lsg+aufg4_lsg+aufg5_lsg+aufg6_lsg)
#    sheet=makeSheet(aufg1+aufg2+aufg3)
    datei.write(sheet)
    datei.close()

    datei_lsg.write(sheet_lsg)
    datei_lsg.close()
    os.system('pdflatex --shell-escape ' + strFileTex)
    os.system('pdflatex --shell-escape ' + strFileTex_lsg)
#    os.system('evince ' + strFilePdf + '&')        
    os.system('evince ' + strFilePdf_lsg + '&')        

    



def ab_integral():
    strFileName="sheet"
    strFileTex=strFileName + ".tex"
    strFilePdf=strFileName + ".pdf"
    datei=open(strFileName + ".tex",'w')

    func=range(2)
    func1=polynom(1)
    func2=polynom(2)
    multi=multicol([func1.randIntegral(),func2.randIntegral()],2)
    aufg=makeExercise(multi)
    sheet=makeSheet(aufg)
    
    datei.write(sheet)
    datei.close()
    os.system('pdflatex ' + strFileTex)
    os.system('evince ' + strFilePdf + '&')

def ab_normalparabel():
    strFileName="ab1_normalparabel"
    strFileName_lsg="ab1_normalparabel_lsg"
    strFileTex=strFileName + ".tex"
    strFileTex_lsg=strFileName_lsg + ".tex"
    strFilePdf=strFileName + ".pdf"
    strFilePdf_lsg=strFileName_lsg + ".pdf"
    datei=open(strFileName + ".tex",'w')
    datei_lsg=open(strFileName_lsg + ".tex",'w')
    f=QuadFunc("n",1,0,-3)
    
    aufg1=makeExercise(aufgWertetabelleGraph(f))
    aufg1_lsg=makeExercise(aufgWertetabelleGraph(f,"a"))

    # Funktionen in Liste definieren
    flist=[]
    for index in range(3):
        flist.append(QuadFunc("s",1,zufallZ(-3,3),zufallZ(-3,3)))
    for index,funktion in enumerate(flist):
        funktion.name="f_" + latex(index+1) 
    #numfunc=enumlist(erstelleFunktionsliste(flist))
    
    aufg2=makeExercise(aufgParabeleigenschaften(flist))
    aufg2_lsg=makeExercise(aufgParabeleigenschaften(flist,"a"))
    
    aufg6=makeExercise(aufgFunktionaufstellen(flist))
    aufg6_lsg=makeExercise(aufgFunktionaufstellen(flist,"a"))

    
    flist=[]
    for index in range(6):
        flist.append(QuadFunc("s",1,zufallZ(-2,2),zufallZ(-2,2)))
    for index,funktion in enumerate(flist):
        funktion.name="f_" + latex(index+1) 
    
    aufg5=makeExercise(aufgGraph(flist))
    aufg5_lsg=makeExercise(aufgGraph(flist,"a"))


    flist=[]
    for index in range(3):
        flist.append(QuadFunc("s",1,zufallZ(-2,2),zufallZ(-2,2)))
    for index,funktion in enumerate(flist):
        funktion.name="f_" + latex(index+1) 
    aufg3=makeExercise(aufgAuswahlGraph(flist))
    aufg3_lsg=makeExercise(aufgAuswahlGraph(flist,"a"))

    flist=[]
    for index in range(4):
        flist.append(QuadFunc("s",1,zufallZ(-2,2),zufallZ(-2,2)))
    for index,funktion in enumerate(flist):
        funktion.name="f_" + latex(index+1) 
    aufg4=makeExercise(aufgAuswahlFunktion(flist))
    aufg4_lsg=makeExercise(aufgAuswahlFunktion(flist,"a"))
    
    sheet=makeSheet(aufg1+aufg2+aufg3+aufg4+aufg5+aufg6)
    sheet_lsg=makeSheet(aufg1_lsg+aufg2_lsg+aufg3_lsg+aufg4_lsg+aufg5_lsg+aufg6_lsg)
#    sheet=makeSheet(aufg1+aufg2+aufg3)
    datei.write(sheet)
    datei.close()

    datei_lsg.write(sheet_lsg)
    datei_lsg.close()
    os.system('pdflatex --shell-escape ' + strFileTex)
    os.system('pdflatex --shell-escape ' + strFileTex_lsg)
#    os.system('evince ' + strFilePdf + '&')        
    os.system('evince ' + strFilePdf_lsg + '&')        

def ab_allgemeine_parabel():
    strFileName="ab2_allgemeine_parabel"
    strFileName_lsg="ab2_allgemeine_parabel_lsg"
    strFileTex=strFileName + ".tex"
    strFileTex_lsg=strFileName_lsg + ".tex"
    strFilePdf=strFileName + ".pdf"
    strFilePdf_lsg=strFileName_lsg + ".pdf"
    datei=open(strFileName + ".tex",'w')
    datei_lsg=open(strFileName_lsg + ".tex",'w')
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
    aufg4=makeExercise(aufgAuswahlFunktion(flist))
    aufg4_lsg=makeExercise(aufgAuswahlFunktion(flist,"a"))
    
    sheet=makeSheet(aufg1+aufg2+aufg3+aufg4+aufg5+aufg6)
    sheet_lsg=makeSheet(aufg1_lsg+aufg2_lsg+aufg3_lsg+aufg4_lsg+aufg5_lsg+aufg6_lsg)
#    sheet=makeSheet(aufg1+aufg2+aufg3)
    datei.write(sheet)
    datei.close()

    datei_lsg.write(sheet_lsg)
    datei_lsg.close()
    os.system('pdflatex --shell-escape ' + strFileTex)
    os.system('pdflatex --shell-escape ' + strFileTex_lsg)
    os.system('evince ' + strFilePdf + '&')        
#    os.system('evince ' + strFilePdf_lsg + '&')        

def ab_scheitelpunktform():
    strFileName="ab_scheitelpunktform"
    strFileTex=strFileName + ".tex"
    strFilePdf=strFileName + ".pdf"
    datei=open(strFileName + ".tex",'w')

    f=QuadFunc("n",1, zufallZ(-5,5),zufallZ(-5,5)) 
    aufg=makeExercise(quadErg(f))
    sheet=makeSheet(aufg)
    datei.write(sheet)
    datei.close()
    os.system('pdflatex ' + strFileTex)
    os.system('evince ' + strFilePdf + '&')

def ab_prozentrechnung():
    strFileName="ab_prozentrechnung"
    strFileTex=strFileName + ".tex"
    strFilePdf=strFileName + ".pdf"
    datei=open(strFileName + ".tex",'w')

    ### Beispiel 1
    gw=5500
    eh="\\euro"
    ps=6
    ds="p"
    rechenweg1=makeExample(bspProzentwert(ps,ds,gw,eh))

    loes=[]
    gw=listZufallszahlenN(9,5000)
    eh=["g","kg","m","km","ml","t","\\euro~","cm$^2$","m$^3$"]
    ps=listZufallszahlenZ(9,0,100)
    ds=["p","p","p","p","p","p","p","p","p"]

    aufg1=makeExercise(aufgProzentwert(ps,ds,gw,eh))
    ### Loesungen
    for i,dummy in enumerate(ps):
        loes.append(runden(prozentwert(gw[i],ps[i]),5))

    ### Beispiel 2
    pw=2100
    eh="\\euro"
    gw=7500
    rechenweg2=makeExample(bspProzentsatz(pw,gw,eh))
    gw=listZufallszahlenZ(9,3000,5000)
    eh=["g","kg","m","km","ml","t","\\euro~","cm$^2$","m$^3$"]
    pw=listZufallszahlenZ(9,0,3000)
    aufg2=makeExercise(aufgProzentsatz(pw,gw,eh))
    ### Loesungen
    for i,dummy in enumerate(ps):
        loes.append(runden(prozentsatz(gw[i],pw[i])*100,5))

    ### Beispiel 3
    pw=2100
    eh="\\euro"
    ps=45
    ds="p"
    rechenweg3=makeExample(bspGrundwert(pw,eh,ps,ds))
    pw=listZufallszahlenN(9,5000)
    eh=["g","kg","m","km","ml","t","\\euro~","cm$^2$","m$^3$"]
    ps=listZufallszahlenZ(9,0,100)
    ds=["p","p","p","p","p","p","p","p","p"]
    aufg3=makeExercise(aufgGrundwert(pw,eh,ps,ds))
    ### Loesungen
    for i,dummy in enumerate(ps):
        loes.append(runden(grundwert(pw[i],ps[i]),5))

    ### Loesungen zufall
    zufloes=zufallsliste(loes)
    strzufloes=""
    for i in zufloes:
        strzufloes+=scriptstyle(latex(deutsch(i))) + " | "
#    ab=makeSheet(aufgaben + strzufloes + "\\\\[0.2em] \n" + strloes)
    sheet=makeSheet(rechenweg1 + aufg1 + rechenweg2 + aufg2 + rechenweg3 + aufg3 + strzufloes)
    datei.write(sheet)
    datei.close()
    os.system('pdflatex ' + strFileTex)
    os.system('evince ' + strFilePdf + '&')


def ab_linFunc_os():

    strFileName="ab_lineare_Funktionen_os"
    strFileTex=strFileName + ".tex"
    strFilePdf=strFileName + ".pdf"
    datei=open(strFileName + ".tex",'w')

    strFileNameL="ab_lineare_Funktionen_os_lsg"
    strFileTexL=strFileNameL + ".tex"
    strFilePdfL=strFileNameL + ".pdf"
    dateiL=open(strFileNameL + ".tex",'w')

    datum=" 04.09.15 \\\\[2em]"

    f=LinFunc(zufallQ0(-4,4),zufallZ0(-3,3),"f")
    g=LinFunc(zufallQ0(-4,4),zufallZ0(-3,3),"g")
    x1=zufallZ(-5,5)
    x2=zufallZ(-5,5)
    y1=g.ywert(x1)
    y2=g.ywert(x2)

    text="Gegeben ist die Funktion " + latex(f.name) + " mit"
    text+="\\[" + latex(f.gleichung) + "\\; . \\]"

    ### ta=Teilaufgaben und Loesung, pa=Teilaufgaben
    ta=[]
    pa=[]

    aufg="Bestimmen Sie die Nullstellen von $" + f.name + "$. \\\\ \n"
    lsg=aufgNullstelle(f)
    ta.append(aufg+lsg)
    pa.append(aufg)

    aufg="Zeichnen Sie den Graphen von $" + latex(f.name) + "$. \\\\ \n"
    lsg=f.graph_zeichnen()
    ta.append(aufg+lsg)
    pa.append(aufg)

    ## Funktionswert
    xw=zufallZ0(-5,5)
    aufg="Bestimmen Sie den Funktionswert an der Stelle " + "$x=" + latex(xw) + "$. \\\\ \n" 
    lsg=aufgyStelle(f,xw)
    ta.append(aufg+lsg)
    pa.append(aufg)

    yw=zufallZ0(-5,5)
    aufg="Bestimmen Sie, an welcher Stelle die Funktion den Wert " + "$y=" + latex(yw) + "$ annimmt. \\\\ \n" 
    lsg=aufgxStelle(f,yw)
    lsg+="\\clearpage"
    ta.append(aufg+lsg)
    pa.append(aufg)


    aufg="Untersuchen Sie die Steigung von $" + latex(f.name) + "$ sowohl qualitativ (fallend/steigend) als auch quantitativ. Geben Sie hierzu auch die Steigung in Prozent und den Steigungswinkel an. \\\\ \n"
    lsg=aufgSteigungGerade(f)
    ta.append(aufg+lsg)
    pa.append(aufg)

    aufg="Gegeben ist eine weitere Funktion $" + latex(g.name) + "$, deren Graph durch die Punkte $A(" + latex(x1) + "|" + latex(y1) + ")$ und $B(" + latex(x2) + "|" + latex(y2) + ")$ verl\\\"auft. Bestimmen Sie die Funktionsgleichung von $" + latex(g.name) + "$. \\\\ \n"   
    lsg=aufgGeradeAufstellen(g,x1,x2)
    ta.append(aufg+lsg)
    pa.append(aufg)

    aufg="Untersuchen Sie, ob sich $" + latex(f.name) + "$ und $" + latex(g.name) + "$ schneiden und bestimmen Sie gegebenenfalls den Schnittpunkt. \\\\ \n"
    lsg=aufgSchnittpunktGeraden(f,g)
    ta.append(aufg+lsg)
    pa.append(aufg)

    aufg="Bestimmen Sie den Schnittwinkel zwischen $" + latex(f.name) + "$ und $" + latex(g.name) + "$. \\\\ \n"
    lsg=aufgSchnittwinkelGeraden(f,g)
    ta.append(aufg+lsg)
    pa.append(aufg)

    
    aufgkt=enumlist(ta)
    aufgkp=enumlist(pa)
    
    sheett=makeSheet(datum+text+aufgkt,"Lineare Funktionen","MA-1")
    sheetp=makeSheet(datum+text+aufgkp,"Lineare Funktionen","MA-1")

    datei.write(sheetp)
    datei.close()

    dateiL.write(sheett)
    dateiL.close()

    os.system('pdflatex ' + strFileTex)
    os.system('pdflatex ' + strFileTexL)

    os.system('evince ' + strFilePdf + '&')    


def ab_vektoren():
    strFileName="terme"
    strFileTex=strFileName + ".tex"
    strFilePdf=strFileName + ".pdf"
    datei=open(strFileName + ".tex",'w')


    anz=3
    vectors=[]
    for i in range(anz):
        vectors.append(matrix([zufallN(10),zufallN(10),zufallN(10)]))
    
    aufgVektor_norm(vectors)

    datei.write("ende")

    datei.close()
    os.system('pdflatex ' + strFileTex)
    os.system('evince ' + strFilePdf + '&')    


def ab_lgs():
    strFileName="lgs"
    strFileTex=strFileName + ".tex"
    strFilePdf=strFileName + ".pdf"
    datei=open(strFileName + ".tex",'w')


    



def zertifikat_parabeln_potenzen():
    strFileName="zertifikat_parabeln_und_potenzen"
    strFileName_lsg="zertifikat_parabeln_und_potenzen_lsg"
    os.system('cp templates/' + strFileName + '.tex ./')
    os.system('cp templates/' + strFileName + ' ' + strFileName_lsg + '.tex ./')

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
    aufg4=makeExercise(aufgAuswahlFunktion(flist))
    aufg4_lsg=makeExercise(aufgAuswahlFunktion(flist,"a"))
    
    sheet=makeSheet(aufg1+aufg2+aufg3+aufg4+aufg5+aufg6)
    sheet_lsg=makeSheet(aufg1_lsg+aufg2_lsg+aufg3_lsg+aufg4_lsg+aufg5_lsg+aufg6_lsg)
#    sheet=makeSheet(aufg1+aufg2+aufg3)
    datei.write(sheet)
    datei.close()

    datei_lsg.write(sheet_lsg)
    datei_lsg.close()
    os.system('pdflatex --shell-escape ' + strFileTex)
    os.system('pdflatex --shell-escape ' + strFileTex_lsg)
    os.system('evince ' + strFilePdf + '&')        
#    os.system('evince ' + strFilePdf_lsg + '&')        
