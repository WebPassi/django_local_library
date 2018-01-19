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

from terme import *

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
    #gn="\\begin{center} \\begin{framed} Grundniveau \\end{framed} \\end{center}"




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





def zertifikat_kreis_koerper():
    strFileName="zertifikat_kreis_und_koerper"
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
    #gn="\\begin{center} \\begin{framed} Grundniveau \\end{framed} \\end{center}"

    a1=Aufgabe()
    
    ta=Textaufgabe.objects.get(name="Kreis")
    
    a1.punkte=4
    a1.aufgabe=makeExercise(ta.erzeugeAufgabe(["57 m"]), str(a1.punkte))
    #a1.lsg=makeExercise(ta.erzeugeAufgabe(["57 m"]), str(a1.punkte))


    a2=Aufgabe()
    
    ta=Textaufgabe.objects.get(name="Zylinder")
    
    a2.punkte=9

    r=zufallN(20)
    h=zufallN(10)
    a2.aufgabe=makeExercise(ta.erzeugeAufgabe([str(r) + " cm", str(h) + " cm"]), str(a2.punkte))
    #a2.lsg=makeExercise(ta.erzeugeAufgabe(["57 m"]), str(a2.punkte))



    gn=grundniveau([a1,a2])
    #gn_lsg=grundniveau([a1],"a")






    ### Erhoehtes Niveau

    a3=Aufgabe()
    
    ta=Textaufgabe.objects.get(name="Zusammengesetzt")
    
    a3.punkte=11

    rho=round(zufallR(),1)
    einheit="g/cm^3"
    a3.aufgabe=makeExercise(ta.erzeugeAufgabe([str(rho).replace(".",",") + " " + einheit]), str(a3.punkte))
    #a3.lsg=makeExercise(ta.erzeugeAufgabe(["57 m"]), str(a3.punkte))



    a4=Aufgabe()
    
    ta=Textaufgabe.objects.get(name="Kugel")
    
    a4.punkte=5

    d=zufallZ(15,25)
    einheit="cm"
    a4.aufgabe=makeExercise(ta.erzeugeAufgabe([str(d) + " " + einheit]), str(a4.punkte))
    #a4.lsg=makeExercise(ta.erzeugeAufgabe(["57 m"]), str(a3.punkte))



    sn=standardniveau([a3,a4])
    #sn_lsg=standardniveau([a2],"a")




    a5=Aufgabe()
    
    ta=Textaufgabe.objects.get(name="PyramideKegel")
    
    a5.punkte=6

    s=zufallZ(10,15)
    h=zufallZ(10,15)
    einheit="cm"
    a5.aufgabe=makeExercise(ta.erzeugeAufgabe([str(s) + " " + einheit,str(h) + " " + einheit]), str(a5.punkte))
    #a5.lsg=makeExercise(ta.erzeugeAufgabe(["57 m"]), str(a3.punkte))




    hn=highniveau([a5])
    #hn_lsg=highniveau([a3],"a")



    gesamtpunkte=a1.punkte + a2.punkte + a3.punkte + a4.punkte + a5.punkte
    
    sheet=makeZertifikat(gn+sn+hn,"Kreis und K\\\"orper",str(gesamtpunkte))

    #sheet_lsg=makeZertifikat(gn_lsg+sn_lsg+hn_lsg,"Parabeln und Potenzen", 32)

    datei.write(sheet)
    datei.close()

    #datei_lsg.write(sheet_lsg)
    datei_lsg.close()
    os.system('pdflatex --shell-escape ' + strFileTex)
    #os.system('pdflatex --shell-escape ' + strFileTex_lsg)
    os.system('evince ' + strFilePdf + '&')        
    #os.system('evince ' + strFilePdf_lsg + '&')    






def test_vermischte_Aufgaben():
    ### Dateinamen angeben
    strFileName="test_WA_Pauli"
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







def test_terme():
    ### Dateinamen angeben
    strFileName="test_stz_v3"
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


    teilaufgaben=[]
    teilaufgaben.append(aufg_terme_addieren())
    teilaufgaben.append(aufg_terme_addieren(['a'],art="dezimal"))
    teilaufgaben.append(aufg_terme_addieren(['v'],laenge=3))
    teilaufgaben.append(aufg_terme_addieren(['x','y'],laenge=5))
    teilaufgaben.append(aufg_terme_addieren(['a','b','c'],laenge=9,art="dezimal"))

    a1.punkte=10
    a1.aufgabe=makeExercise(enumlist([ta[0] for ta in teilaufgaben]), str(a1.punkte))
    a1.lsg=makeExercise(enumlist([ta[2] for ta in teilaufgaben]), str(a1.punkte))

    aufg.append(a1.aufgabe)
    lsg.append(a1.lsg)



    punkte=a1.punkte




    ### Aufgabe 2


    a2=Aufgabe()


    teilaufgaben=[]
    teilaufgaben.append(aufg_eine_klammer(['','ganz'],['x','ganz'],['','ganz'],position="hinten"))

    teilaufgaben.append(aufg_eine_klammer(['','ganz'],['x','ganz'],['','ganz'],position="vorne"))

    teilaufgaben.append(aufg_eine_klammer(['','ganz',[-7,-2]],['a','dezimal'],['','dezimal'],position="hinten"))

    teilaufgaben.append(aufg_eine_klammer(['a','ganz'],['b','ganz'],['c','ganz'],position="vorne"))

    teilaufgaben.append(aufg_term_fix('(2a-3b)*3 - 2*(-1.5a+4b)'))


    a2.punkte=10
    a2.aufgabe=makeExercise(enumlist([ta[0] for ta in teilaufgaben]), str(a1.punkte))
    a2.lsg=makeExercise(enumlist([ta[2] for ta in teilaufgaben]), str(a1.punkte))

    aufg.append(a2.aufgabe)
    lsg.append(a2.lsg)



    punkte=a1.punkte + a2.punkte


    
    sheet=makeTest(exercises=aufg, kurs="MA Stz v3",title="Schriftliche Arbeit", punkte=punkte,zeit=20)

    sheet_lsg=makeTest(exercises=lsg, kurs="MA Stz v3",title="Schriftliche Arbeit", punkte=punkte,zeit=20)


    datei.write(sheet)
    datei.close()

    datei_lsg.write(sheet_lsg)
    datei_lsg.close()
    os.system('pdflatex --shell-escape ' + strFileTex)
    os.system('pdflatex --shell-escape ' + strFileTex_lsg)
#    os.system('evince ' + strFilePdf + '&')        
    os.system('evince ' + strFilePdf_lsg + '&')    







