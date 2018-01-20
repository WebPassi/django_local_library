from django.shortcuts import *
from django.http import HttpResponse
from django.template.loader import render_to_string
#from jinja2 import Environment, PackageLoader

import os
import re


import sys
from io import StringIO
import contextlib

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


from glob import glob
from pathlib import Path
import shutil

import subprocess

from shutil import copyfile


import numpy as np

from sympy import *
from sympy.abc import *
from functions import Function
from auto_ab import *
from elements import *
from zufall import *

from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application

transformations = (standard_transformations + (implicit_multiplication_application,))


from terme import *
from geometrie3d import *
from stochastik import *

#from operator import itemgetter, attrgetter

#generator_dir="/home/pfranz/aufgabengenerator"

user='frz'
#act_dir='/home/pfranz/aufgabengenerator/user/frz/tmp'
act_dir='user/frz/tmp'




def index(request):
    context={'bla': ""}
    return render(request,'generator/index.html',context)

def auto_ab(request):
    context={'bla': ""}
    return render(request,'generator/auto_ab.html',context)

def quad_glg(request):
    ab_quadglg()
    return HttpResponse("<h1>Viele Quadratische Gleichungen</h1>")

def lin_glg(request):
    ab_linglg()
    with open('ab_linglg.pdf','rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'inline'
    return response


def lin_func(request):
    ab_linfunc()
    with open('lineare_funktionen_komplett.pdf','rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        #response['Content-Disposition'] = 'inline'
    return response



def terme(request):
    ab_terme()
    with open('ab_terme_komplett.pdf','rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'inline'
    return response

    
def normalparabel(request):
    ab_normalparabel()
    with open('ab1_normalparabel_komplett.pdf','rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'inline'
    return response


def parabel(request):
    ab_allgemeine_parabel()
    with open('ab2_allgemeine_parabel_komplett.pdf','rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'inline'
    return response


def scheitelpunktform(request):
    ab_scheitelpunktform()
    with open('ab_scheitelpunktform.pdf','rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'inline'
    return response



def prozentrechnung(request):
    ab_prozentrechnung()
    with open('ab_prozentrechnung.pdf','rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'inline'
    return response


def linFunc_os(request):
    ab_linFunc_os()
    with open('ab_lineare_Funktionen_os_komplett.pdf','rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'inline'
    return response


def pdf_view(request):
    with open('ab2_allgemeine_parabel_lsg.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'inline'
    return response

def aufgTemp():
    f=open("xxx.tex","w")
    env = Environment(loader=PackageLoader('generator', 'templates/generator'))
    template = env.get_template('lgs.tex')
    menge=range(24)
    aufg=[1,2]
    f.write(template.render({'menge':menge, 'aufgaben':aufg}))


def zertifikat_parabeln_potenzen(request):
    zertifikat_parabeln_potenzen()
    return HttpResponse("<h1>Zertifikat Parabeln und Potenzen</h1>")













def neues_projekt(request,projektname="tmp"):
    #os.chdir('/home/pfranz/aufgabengenerator/')

    #os.removedirs('../tmp/')

    #os.chdir('../')
    #shutil.rmtree('tmp/')

    try:
        del request.session['nummer']
    except:
        pass
    try:
        user=request.session['user']
    except:
        user="frz"
        
    #user_dir=generator_dir + '/user/' + user

    user_dir=user

    os.chdir(../user_dir)

    shutil.rmtree('tmp/')

    return manuell_ab(request)



def projekt_laden(request):
    try:
        user=request.session['user']
    except:
        user="frz"
        

    #user_dir=generator_dir + '/user/' + user
    user_dir=user
    os.chdir(user_dir)
    projekte=glob('*')
    context={
        'projekte': projekte,
    }
    return render(request,'generator/projekt_laden.html',context)



def projekt_loeschen(request):
    try:
        user=request.session['user']
    except:
        user="frz"
        

    #user_dir=generator_dir + '/user/' + user
    user_dir=user
    os.chdir(user_dir)
    projekte=glob('*')
    context={
        'projekte': projekte,
    }
    return render(request,'generator/projekt_loeschen.html',context)

def projekt_loeschen_submit(request,projektname):
    #os.chdir('/home/pfranz/aufgabengenerator/')

    #os.removedirs('../tmp/')

    #os.chdir('../')
    #shutil.rmtree('tmp/')

    #del request.session['nummer']

    try:
        user=request.session['user']
    except:
        user="frz"
        
    #user_dir=generator_dir + '/user/' + user
    user_dir=user

    os.chdir(user_dir)

    shutil.rmtree(projektname)

    return projekt_loeschen(request)




def projekt_speichern(request,projekt=""):
    try:
        user=request.session['user']
    except:
        user="frz"
        
    #user_dir=generator_dir + '/user/' + user
    user_dir=user

    #return HttpResponse(os.getcwd())


    try:
        projekt=request.POST['projektname']
    except:
        pass


    if projekt == "":
        return render(request,'generator/projekt_speichern.html')
    else:
        shutil.copytree('./', '../' + projekt)
        os.chdir('../' + projekt)
        return manuell_ab(request)







def manuell_ab(request,projektname=""):
    try:
        user=request.session['user']
    except:
        user="frz"
        
    if projektname == "":
        projektname="tmp"


    ### User Verzeichnis
    #projekt_dir=generator_dir + '/user/' + user + '/' + projektname
    projekt_dir=user + '/' + projektname


    try:
        os.mkdir(projekt_dir)
    except OSError:
        pass

    os.chdir(projekt_dir)

    try:
        os.system('touch ' +  'tmp' + '.kpt')
    except:
        pass
        
    create_skelet(request)

    os.system('pdflatex --shell-escape ' + 'tmp' + '.tex')

    os.system('pdflatex --shell-escape ' + 'tmp_lsg' + '.tex')


    context={
        'projektname': projektname,
    }

    #return render(request,'generator/manuell_ab.html',context)
    return render(request,'generator/manuell_ab.html')


def konzept(request):
    ## Konzept einlesen
    konzept=open('tmp' + '.kpt','r')
    aufgaben_konzept=konzept.readlines()
    konzept.close()

    ## Aufgaben einlesen
    aufgaben=[]
    for a in aufgaben_konzept:
        a_name=a.split(',')[0].replace('\n','')

        try:
            a_temp=open(a_name + '.tpl','r').read()
            aufgaben.append(a_temp)
        except:
            aufgaben=[]

    context={
        'aufgaben': aufgaben,
        'ab': 'tmp.pdf',
        'lsg': 'tmp_lsg.pdf',
    }
    return render(request,'generator/konzept.html',context)


def create_skelet(request):
    #konzept=open(projektname + '.kpt','r')
    #skelet=open(projektname + '.tex','w')
    konzept=open('tmp' + '.kpt','r').readlines()

    arbeitsblatt=open('tmp' + '.tex','w')

    #latexstr=open('/home/pfranz/aufgabengenerator/vorlagen/geometrie3d.tex').read()
    latexstr=open('vorlagen/geometrie3d.tex').read()


    latexstr+="\\begin{document} \n" 

    for topic in konzept:
        latexstr+="\\input{" + topic.split(',')[0].replace('\n','') + "} \n" 
        
    latexstr+="\\end{document} \n"

    arbeitsblatt.write(latexstr)

    arbeitsblatt.close()


    ##### Loesungsblatt
    loesung=open('tmp_lsg' + '.tex','w')

    #latexstr=open('/home/pfranz/aufgabengenerator/vorlagen/geometrie3d.tex').read()
    latexstr=open('vorlagen/geometrie3d.tex').read()

    latexstr+="\\begin{document} \n" 

    for topic in konzept:
        latexstr+="\\input{" + topic.split(',')[0].replace('\n','') + "_lsg" + "} \n" 
        
    latexstr+="\\end{document} \n"

    loesung.write(latexstr)

    loesung.close()


    

def output(request):
    #create_skelet(request)
    #os.system('pdflatex --shell-escape ' + projektname + '.tex')
    #return output_direkt(request,projektname)
    return output_direkt(request,'tmp')
    #return HttpResponse("hallo")


def output_direkt(request,name):
    if not '.' in name:
        name=name + '.pdf'

    with open(name,'rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'inline'
        return response


def aufgabe_loeschen(request):
    konzept=open('tmp' + '.kpt','r')
    aufgaben=konzept.readlines()
    konzept.close()

    aufgabe=aufgaben[len(aufgaben)-1].replace("\n","").split(',')[0]
    #aufgabe=aufgaben[0].replace("\n","")
    os.remove(aufgabe + ".tex")
    os.remove(aufgabe + "_lsg.tex")

    del aufgaben[len(aufgaben)-1]

    konzept=open('tmp' + '.kpt','w')
    konzept.writelines(aufgaben)
    konzept.close()

    return manuell_ab(request)




def uebersicht_aufgaben(request,nummer=""):
    context={'bla': nummer}
    request.session['nummer']=nummer
    return render(request,'generator/uebersicht_aufgaben.html',context)

def aufgabenwahl(request):
    aufgabenbereich=request.POST['aufgabenbereich']

    if aufgabenbereich == "terme_addieren":
        context={'aufgabenbereich': aufgabenbereich}
        return render(request,'generator/terme_addieren_einstellungen.html',context)

    elif aufgabenbereich == "terme_eine_klammer":
        context={'aufgabenbereich': aufgabenbereich}
        return render(request,'generator/terme_eine_klammer_einstellungen.html',context)

    elif aufgabenbereich == "prozente":
        context={'aufgabenbereich': aufgabenbereich}
        return render(request,'generator/prozente_einstellungen.html',context)

    elif aufgabenbereich == "ordnen":
        context={'aufgabenbereich': aufgabenbereich}
        return render(request,'generator/ordnen_einstellungen.html',context)

    elif aufgabenbereich == "pythagoras":
        context={'aufgabenbereich': aufgabenbereich}
        return render(request,'generator/pythagoras_einstellungen.html',context)

    elif aufgabenbereich == "trigonometrie":
        context={'aufgabenbereich': aufgabenbereich}
        return render(request,'generator/trigonometrie_einstellungen.html',context)

    elif aufgabenbereich == "geraden_lagebeziehung":
        context={'aufgabenbereich': aufgabenbereich}
        return render(request,'generator/geraden_lagebeziehung_einstellungen.html',context)
        #return geraden_lagebeziehung(request)


    elif aufgabenbereich == "ebene_3Punktform":
        context={'aufgabenbereich': aufgabenbereich}
        return render(request,'generator/aufgaben_einstellungen.html',context)

    elif aufgabenbereich == "ebene_normalform":
        context={'aufgabenbereich': aufgabenbereich}
        return render(request,'generator/aufgaben_einstellungen.html',context)

    elif aufgabenbereich == "winkel_vektoren":
        context={'aufgabenbereich': aufgabenbereich}
        return render(request,'generator/aufgaben_einstellungen.html',context)

    ### Stochastik
    elif aufgabenbereich == "binomial":
        context={'aufgabenbereich': aufgabenbereich}
        return render(request,'generator/bernoulli_einstellungen.html',context)

    
    else:
        context={
            'aufgabenbereich': aufgabenbereich,
            'name': "terme",
        }
        #return render(request,'generator/freie_aufgabe.html',context)
        return freie_aufgabe(request)



def freie_aufgabe(request):
    return render(request,'generator/freie_aufgabe.html')




def freie_aufgabe_berechnen(nummer):
    aufgabenname='a' + str(nummer)
    aufgabe=open(aufgabenname + '.tpl').read()

    ##############################
    ##############################
    ##### Konkrete Aufgabe aus Templates erstellen

    ### Aufgabe
    templatedatei=open(aufgabenname + '.tpl','r')
    inhalt=templatedatei.read()

    latexdatei=open(aufgabenname + '.tex','w')

    ### Loesung
    loesungstemplatedatei=open(aufgabenname + '_lsg.tpl','r')
    loesung=loesungstemplatedatei.read()

    loesungslatexdatei=open(aufgabenname + '_lsg.tex','w')

    ##############################
    ##############################
    ##### Variablen, muessen in der Aufgabe mit {{varname}} definiert werden.
    ##### Terme werden in der Aufgabe und in der Loesung ausgewertet.

    ### Muster
    muster = r"{{[a-zA-Z0-9_+-/\*()]+}}"

    import re
    ### Eingabe Original {{ a }}, {{a*b}}
    terme_orig=re.findall(muster,aufgabe)
    ersetzung=terme_orig[:]

    terme_orig_lsg=re.findall(muster,loesung)
    ersetzung_lsg=terme_orig_lsg[:]

    ### Variablen als Tuple speichern
    variablen_tuples = [ ( v.split(',')[0].replace('\n',''), v.split(',')[1].replace('\n',''), v.split(',')[2].replace('\n',''), v.split(',')[3].replace('\n','') ) for v in open(aufgabenname + '.var','r').readlines()  ]     

    ### Variablen der Laenge absteigend sortieren
    variablen = sorted(variablen_tuples, key=lambda var: -len(var[0]))

    ### Informationen Variablendatei *.var
    for var in variablen:
        ### Zufallszahl bereitstellen 
        var_name=var[0]
 
        ## Zahl, Vektor, Funktion, ...
        var_spez=var[1]

        ## R,Q,QBruch,QDez,Z,N, ...
        var_raum=var[2]

        ## Zahlenbereich von wo bis wo
        var_bereich=var[3]
        ug=var_bereich.split(';')[0].replace('[','')
        og=var_bereich.split(';')[1].replace(']','')
        
        wert=zufallZ(int(ug),int(og))

        ### ersetzt {{a*b}} durch {{3*7}}
        for i,ers in enumerate(ersetzung):
            ersetzung[i]=ers.replace(var_name,str(wert))

        ### ersetzt {{a*b}} durch {{3*7}}
        for i,ers in enumerate(ersetzung_lsg):
            ersetzung_lsg[i]=ers.replace(var_name,str(wert))


    ### ersetzt {{3*7}} durch 21
    for i,t_orig in enumerate(terme_orig):
        ersetzung[i]=str(parse_expr(ersetzung[i].replace('{{','').replace('}}','').replace(' ','')))

        inhalt=inhalt.replace(t_orig,ersetzung[i])


    for i,t_orig_lsg in enumerate(terme_orig_lsg):
        ersetzung_lsg[i]=str(parse_expr(ersetzung_lsg[i].replace('{{','').replace('}}','').replace(' ','')))

        loesung=loesung.replace(t_orig_lsg,ersetzung_lsg[i])

  
    latexdatei.write(makeExercise(inhalt))
    
    loesungslatexdatei.write(makeExercise(loesung))

 
    ### Aufraeumen
    templatedatei.close()
    latexdatei.close()

    loesungstemplatedatei.close()
    loesungslatexdatei.close()




def auto_aufgabe_berechnen(nummer):
    aufgabenname="a" + nummer 
    

    texfile=open(aufgabenname + '.tex','w')
    texfile_lsg=open(aufgabenname + '_lsg.tex','w')
    texfile_lsg_skizze=open(aufgabenname + '_lsg_skizze.tex','w')

    befehl='print(' + open(aufgabenname + '.tpl').readlines()[0].replace('\n','') + ')'

    with stdoutIO() as s:
        exec(befehl)

        aufgabe=s.getvalue().replace("['","").replace("']","").split(',')[0]
        aufgabe=aufgabe.replace('\\\\','\\').replace('\\n','')
        texfile.write(aufgabe)

        aufgabe=s.getvalue().replace("['","").replace("']","").split(',')[1]
        aufgabe=aufgabe.replace('\\\\','\\').replace('\\n','').replace("'","")
        texfile_lsg.write(aufgabe)

        aufgabe=s.getvalue().replace("['","").replace("']","").split(',')[2]
        aufgabe=aufgabe.replace('\\\\','\\').replace('\\n','').replace("'","")
        texfile_lsg_skizze.write(aufgabe)


    texfile.close()
    texfile_lsg.close()
    texfile_lsg_skizze.close()












def freie_aufgabe_erstellen(request):
    import re
    ### Eingaben der Aufgabe und Loesung abfragen
    aufgabe=request.POST['aufgabe']
    loesung=request.POST['loesung']


    nummer=request.session['nummer']
    ##### Nummer vergeben / Position
    if nummer == "":
        konzept=open('tmp' + '.kpt','r').readlines()
        nummer=str(len(konzept)+1)
        request.session['nummer']=nummer

    aufgabenname="a" + nummer

    ##### Konzept anpassen
    konzept=open('tmp' + '.kpt','a')
    konzept.write(aufgabenname + ",frei \n")
    konzept.close()




    ##### Templatedateien bereitstellen
    ### oeffnen
    a_templ=open(aufgabenname + '.tpl','w')
    lsg_templ=open(aufgabenname + '_lsg.tpl','w')

    ### schreiben
    a_templ.write(aufgabe)
    lsg_templ.write(loesung)

    
    ### schliessen
    a_templ.close()
    lsg_templ.close()


    ##############################
    ##############################
    ##### Variablen bereitstellen, in Datei schreiben
    #muster_var = r"{{[ ]*[a-zA-Z0-9_]+[ ]*}}"
    muster_var = r"{{[a-zA-Z0-9_]+}}"

    variablendatei=open(aufgabenname + '.var','w')

    variablen_orig=re.findall(muster_var,aufgabe)

    variablen=[]
    for var_orig in variablen_orig:
        variablen.append(var_orig.replace('{','').replace('}','').replace(' ',''))
    variablen=set(variablen)
    var_spez="Zahl"
    var_raum="N"
    
    for var in variablen:
        variablendatei.write(var.split(',')[0] + ',' + var_spez + "," + var_raum + "," + '[1;7]' + '\n')
        
    variablendatei.close()



    freie_aufgabe_berechnen(nummer)

    return manuell_ab(request)



    
def aufgabe_neu_berechnen(request,nummer):
    if ',frei' in open('tmp' + '.kpt').readlines()[int(nummer)-1]:
        freie_aufgabe_berechnen(nummer)

    else:
        auto_aufgabe_berechnen(nummer)




    return manuell_ab(request)





def erstelle_zertifikat(request,dateiname="tmp.tex",name="",punkte="",enote="",gnote=""):
    name="Wahrscheinlichkeit 1"
    punkte="30"
    enote=3
    gnote=2


    context={
        'name': name,
        'punkte': punkte,
        'enote':enote,
        'gnote':gnote,
    }

    zertifikat_konkret= render_to_string('generator/zertifikat.tex',context)

    texdatei=open(dateiname,'w')
    
    texdatei.write(zertifikat_konkret)

    texdatei.close()

    os.system('pdflatex --shell-escape ' + dateiname)

    return output_direkt(request,dateiname.split('.')[0] + '.pdf')



############################## 
###       Aufgaben
############################## 


#### Zahlen ordnen
def zahlen_ordnen(request):
    aufgabentext=request.POST['aufgabentext']
    anzahl=int(request.POST['anzahl'])
    zahlenbereich=request.POST['zahlenbereich']
    von=int(request.POST['von'])
    bis=int(request.POST['bis'])
    stellen=int(request.POST['stellen'])
    
    zahlen=[]
    i=1
    while i <= anzahl:
        if zahlenbereich == "Z":
            zahlen.append(zufallZ(von,bis))
        elif zahlenbereich == "dezimal":
            zahlen.append(zufallR(von,bis,stellen))
        i+=1

    konzept=open('tmp' + '.kpt','r').readlines()
    aufgabenname="a" + str(len(konzept)+1) 
    konzept=open('tmp' + '.kpt','a')
    konzept.write(aufgabenname + "\n")
    konzept.close()

    texdatei=open(aufgabenname + '.tex','w')
    texdatei_lsg=open(aufgabenname + '_lsg.tex','w')
    
    

    texdatei.write(makeExercise(aufg_zahlen_ordnen(zahlen,aufgabe=aufgabentext)))
    texdatei_lsg.write(makeExercise(aufg_zahlen_ordnen_lsg(zahlen)))







    texdatei.close()
    texdatei_lsg.close()


    konzept=open('tmp' + '.kpt','a')
    konzept.write(aufgabenname + "\n")

    konzept.close()


    return manuell_ab(request)



def aufgabe_terme_addieren(request):
    aufgabentext=request.POST['aufgabentext']
    anzahl=request.POST['anzahl']
    variablen=request.POST['variablen'].split(',')
    ug=1
    og=int(request.POST['og'])
    laenge=int(request.POST['laenge'])
    anzahl=int(request.POST['anzahl'])
    spalten=int(request.POST['spalten'])


    nummer=request.session['nummer']
    ##### Nummer vergeben / Position
    if nummer == "":
        konzept=open('tmp' + '.kpt','r').readlines()
        nummer=str(len(konzept)+1)
        request.session['nummer']=nummer

    aufgabenname="a" + nummer

    ##### Konzept anpassen
    konzept=open('tmp' + '.kpt','a')
    konzept.write(aufgabenname + "\n")
    konzept.close()
    

    template=open(aufgabenname + '.tpl','w')
    var_list="["
    for v in variablen:
        #var_list += '"' + v + '"'
        var_list += '"' + v + '"' + ','
    var_list += "]"

    template.write('aufg_terme_addieren(variablen=' + var_list + ',art=' + '"ganz"' + ',runden=' + "2" + ',intervall=[' + str(ug) + ',' + str(og) + '],laenge=' + str(laenge) + ',aufgabentext="' + aufgabentext + '",anzahl=' + str(anzahl) + ',spalten=' + str(spalten) + ')')
    template.close()



    aufgabe=aufg_terme_addieren(variablen=variablen,art="ganz",runden=2,intervall=[ug,og],laenge=laenge,aufgabentext=aufgabentext,anzahl=anzahl,spalten=spalten)


    texdatei=open(aufgabenname + '.tex','w')
    texdatei_lsg=open(aufgabenname + '_lsg.tex','w')
    texdatei_lsg_skizze=open(aufgabenname + '_lsg_skizze.tex','w')
    


    texdatei.write(aufgabe[0])
    texdatei_lsg.write(aufgabe[1])
    texdatei_lsg_skizze.write(aufgabe[2])

    #texdatei.write(makeExercise(enumlist(aufgaben),aufgabentext=aufgabentext))

    texdatei.close()
    texdatei_lsg.close()
    texdatei_lsg_skizze.close()


    return manuell_ab(request)





def terme_eine_klammer(request):
    aufgabentext=request.POST['aufgabentext']
    anzahl=request.POST['anzahl']
    variable=request.POST['variablen']
    ug=1
    og=int(request.POST['og'])
    laenge=int(request.POST['laenge'])
    anzahl=int(request.POST['anzahl'])
    spalten=int(request.POST['spalten'])

    aufgaben=[]

    i=1
    while i <= anzahl:
        aufgaben.append(aufg_eine_klammer(eins=["","ganz",[ug,og]],zwei=["x","ganz",[ug,og]],drei=["","ganz",[ug,og]])[0])
        i+=1


    konzept=open('tmp' + '.kpt','r')
    aufgaben_konzept=konzept.readlines()
    konzept.close()
    
    aufgabenname="a" + str(len(aufgaben_konzept)+1) 

    texdatei=open(aufgabenname + '.tex','w')
    texdatei_lsg=open(aufgabenname + '_lsg.tex','w')
    


    texdatei.write(makeExercise(multicol(aufgaben,spalten),aufgabentext=aufgabentext))

    texdatei.close()


    konzept=open('tmp' + '.kpt','a')
    konzept.write(aufgabenname + "\n")

    konzept.close()


    return manuell_ab(request)






def pythagoras(request):
    aufgabentext=request.POST['aufgabentext']
    anzahl=int(request.POST['anzahl'])
    #variable=request.POST['variablen']
    #ug=1
    #og=int(request.POST['og'])
    #laenge=int(request.POST['laenge'])
    #anzahl=int(request.POST['anzahl'])
    #spalten=int(request.POST['spalten'])

    aufgaben=[]

    a=zufallN(9)
    b=zufallN(9)
    gamma=90
    aufgaben.append(aufgPythagoras(a=a,b=b,gamma=gamma))

    a=zufallZ(6,13)
    b=zufallN(5)
    alpha=90
    aufgaben.append(aufgPythagoras(a=a,b=b,alpha=alpha))



    konzept=open('tmp' + '.kpt','r')
    aufgaben_konzept=konzept.readlines()
    konzept.close()
    
    aufgabenname="a" + str(len(aufgaben_konzept)+1) 

    texdatei=open(aufgabenname + '.tex','w')
    texdatei_lsg=open(aufgabenname + '_lsg.tex','w')
    


    texdatei.write(makeExercise(enumlist(aufgaben),aufgabentext=aufgabentext))

    texdatei.close()


    konzept=open('tmp' + '.kpt','a')
    konzept.write(aufgabenname + "\n")

    konzept.close()


    return manuell_ab(request)



def trigonometrie(request):
    aufgabentext=request.POST['aufgabentext']
    anzahl=int(request.POST['anzahl'])
    #variable=request.POST['variablen']
    #ug=1
    #og=int(request.POST['og'])
    #laenge=int(request.POST['laenge'])
    #anzahl=int(request.POST['anzahl'])
    #spalten=int(request.POST['spalten'])

    aufgaben=[]

    a=zufallN(9)
    b=zufallN(9)
    gamma=90
    aufgaben.append(aufgTrigonometrie(a=a,b=b,gamma=gamma))

    a=zufallZ(6,13)
    beta=zufallN(60)
    alpha=90
    aufgaben.append(aufgTrigonometrie(a=a,alpha=alpha,beta=beta))



    konzept=open('tmp' + '.kpt','r')
    aufgaben_konzept=konzept.readlines()
    konzept.close()
    
    aufgabenname="a" + str(len(aufgaben_konzept)+1) 

    texdatei=open(aufgabenname + '.tex','w')
    texdatei_lsg=open(aufgabenname + '_lsg.tex','w')
    


    texdatei.write(makeExercise(enumlist(aufgaben),aufgabentext=aufgabentext))

    texdatei.close()


    konzept=open('tmp' + '.kpt','a')
    konzept.write(aufgabenname + "\n")

    konzept.close()


    return manuell_ab(request)




def geraden_lagebeziehung(request):
    #aufgabentext=request.POST['aufgabentext']

    #anzahl=int(request.POST['anzahl'])
    #variable=request.POST['variablen']
    #ug=1
    #og=int(request.POST['og'])
    #laenge=int(request.POST['laenge'])
    #anzahl=int(request.POST['anzahl'])
    #spalten=int(request.POST['spalten'])


    sv=[0,0,0]
    rv=[0,0,0]

    sv[0]=zufallZ0(-4,4)
    sv[1]=zufallZ0(-4,4)
    #sv[2]=zufallZ(-5,5)
    sv[2]=0

    rv[0]=zufallZ0(-4,4)
    #rv[1]=zufallZ(-5,5)
    rv[1]=0
    rv[2]=zufallZ0(-4,4)



    aufgabentext="Untersuchen Sie die Lagebeziehung zwischen " + gerade3d_latex(sv,rv) + "\\\\ und den folgenden Geraden:"

    sv=np.array(sv)
    rv=np.array(rv)

    aufgaben=[]
    aufgaben.append(gerade_identisch(sv,rv))
    #aufgaben.append(gerade_schnitt(sv,rv))
    aufgaben.append(gerade_parallel(sv,rv))
    aufgaben.append(gerade_windschief(sv,rv))

    random.shuffle(aufgaben)


    konzept=open('tmp' + '.kpt','r')
    aufgaben_konzept=konzept.readlines()
    konzept.close()
    
    aufgabenname="a" + str(len(aufgaben_konzept)+1) 

    texdatei=open(aufgabenname + '.tex','w')
    texdatei_lsg=open(aufgabenname + '_lsg.tex','w')
    


    texdatei.write(makeExercise(enumlist(aufgaben),aufgabentext=aufgabentext))

    texdatei.close()


    konzept=open('tmp' + '.kpt','a')
    konzept.write(aufgabenname + "\n")

    konzept.close()


    return manuell_ab(request)







def ebene_3Punktform(request):
    aufgabentext=request.POST['aufgabentext']
    #anzahl=int(request.POST['anzahl'])
    zahlenbereich=request.POST['zahlenbereich']
    von=int(request.POST['von'])
    bis=int(request.POST['bis'])
    stellen=int(request.POST['stellen'])
    
    nummer=request.session['nummer']
    ##### Nummer vergeben / Position
    if nummer == "":
        konzept=open('tmp' + '.kpt','r').readlines()
        nummer=str(len(konzept)+1)
        request.session['nummer']=nummer

    aufgabenname="a" + nummer

    ##### Konzept anpassen
    konzept=open('tmp' + '.kpt','a')
    konzept.write(aufgabenname + "\n")
    konzept.close()
    

    template=open(aufgabenname + '.tpl','w')

    template.write('aufg_ebene_3Punktform(art=' + zahlenbereich + ',runden=' + str(stellen) + ',intervall=' + '[' + str(von) + ',' + str(bis) + ']' + ',aufgabentext="' + aufgabentext + '")')
    template.close()





    #aufgaben.append(gerade_identisch(sv,rv))
    #aufgaben.append(gerade_schnitt(sv,rv))
    #aufgaben.append(gerade_parallel(sv,rv))
    #aufgaben.append(gerade_windschief(sv,rv))

    #random.shuffle(aufgaben)

    aufgabe_komplett=aufg_ebene_3Punktform(art=zahlenbereich,runden=stellen,intervall=[von,bis],aufgabentext=aufgabentext)

    aufgabe=aufgabe_komplett[0]
    loesung=aufgabe_komplett[1]



    texdatei=open(aufgabenname + '.tex','w')
    texdatei_lsg=open(aufgabenname + '_lsg.tex','w')
    texdatei_lsg_skizze=open(aufgabenname + '_lsg_skizze.tex','w')
    


    texdatei.write(aufgabe)
    texdatei_lsg.write(loesung)
    #texdatei_lsg_skizze.write(aufgabe[2])

    #texdatei.write(makeExercise(enumlist(aufgaben),aufgabentext=aufgabentext))

    texdatei.close()
    texdatei_lsg.close()
    texdatei_lsg_skizze.close()


    return manuell_ab(request)



def winkel_vektoren(request):
    aufgabentext=request.POST['aufgabentext']
    #anzahl=int(request.POST['anzahl'])
    zahlenbereich=request.POST['zahlenbereich']
    von=int(request.POST['von'])
    bis=int(request.POST['bis'])
    stellen=int(request.POST['stellen'])
    
    nummer=request.session['nummer']
    ##### Nummer vergeben / Position
    if nummer == "":
        konzept=open('tmp' + '.kpt','r').readlines()
        nummer=str(len(konzept)+1)
        request.session['nummer']=nummer

    aufgabenname="a" + nummer

    ##### Konzept anpassen
    konzept=open('tmp' + '.kpt','a')
    konzept.write(aufgabenname + "\n")
    konzept.close()
    

    template=open(aufgabenname + '.tpl','w')

    template.write('aufg_winkel_vektoren(art=' + zahlenbereich + ',runden=' + str(stellen) + ',intervall=' + '[' + str(von) + ',' + str(bis) + ']' + ',aufgabentext="' + aufgabentext + '")')
    template.close()





    #aufgaben.append(gerade_identisch(sv,rv))
    #aufgaben.append(gerade_schnitt(sv,rv))
    #aufgaben.append(gerade_parallel(sv,rv))
    #aufgaben.append(gerade_windschief(sv,rv))

    #random.shuffle(aufgaben)

    aufgabe_komplett=aufg_winkel_vektoren(art=zahlenbereich,runden=stellen,intervall=[von,bis],aufgabentext=aufgabentext)

    aufgabe=aufgabe_komplett[0]
    loesung=aufgabe_komplett[1]



    texdatei=open(aufgabenname + '.tex','w')
    texdatei_lsg=open(aufgabenname + '_lsg.tex','w')
    texdatei_lsg_skizze=open(aufgabenname + '_lsg_skizze.tex','w')
    


    texdatei.write(aufgabe)
    texdatei_lsg.write(loesung)
    #texdatei_lsg_skizze.write(aufgabe[2])

    #texdatei.write(makeExercise(enumlist(aufgaben),aufgabentext=aufgabentext))

    texdatei.close()
    texdatei_lsg.close()
    texdatei_lsg_skizze.close()


    return manuell_ab(request)



def ebene_normalform(request):
    aufgabentext=request.POST['aufgabentext']
    #anzahl=int(request.POST['anzahl'])
    zahlenbereich=request.POST['zahlenbereich']
    von=int(request.POST['von'])
    bis=int(request.POST['bis'])
    stellen=int(request.POST['stellen'])
    
    nummer=request.session['nummer']
    ##### Nummer vergeben / Position
    if nummer == "":
        konzept=open('tmp' + '.kpt','r').readlines()
        nummer=str(len(konzept)+1)
        request.session['nummer']=nummer

    aufgabenname="a" + nummer

    ##### Konzept anpassen
    konzept=open('tmp' + '.kpt','a')
    konzept.write(aufgabenname + "\n")
    konzept.close()
    

    template=open(aufgabenname + '.tpl','w')

    template.write('aufg_ebene_3Punktform(art=' + zahlenbereich + ',runden=' + str(stellen) + ',intervall=' + '[' + str(von) + ',' + str(bis) + ']' + ',aufgabentext="' + aufgabentext + '")')
    template.close()





    #aufgaben.append(gerade_identisch(sv,rv))
    #aufgaben.append(gerade_schnitt(sv,rv))
    #aufgaben.append(gerade_parallel(sv,rv))
    #aufgaben.append(gerade_windschief(sv,rv))

    #random.shuffle(aufgaben)


    aufgabe_komplett=ebene_normalform_latex()
    aufgabe=makeExercise(aufgabe_komplett[0],aufgabentext=aufgabentext)
    loesung=makeExercise(aufgabe_komplett[1],aufgabentext=aufgabentext)




    texdatei=open(aufgabenname + '.tex','w')
    texdatei_lsg=open(aufgabenname + '_lsg.tex','w')
    texdatei_lsg_skizze=open(aufgabenname + '_lsg_skizze.tex','w')
    


    texdatei.write(aufgabe)
    texdatei_lsg.write(loesung)
    #texdatei_lsg_skizze.write(aufgabe[2])

    #texdatei.write(makeExercise(enumlist(aufgaben),aufgabentext=aufgabentext))

    texdatei.close()
    texdatei_lsg.close()
    texdatei_lsg_skizze.close()


    return manuell_ab(request)



#### Stochastik
def binomial(request):
    aufgabentext=request.POST['aufgabentext']
    anzahl=int(request.POST['anzahl'])
    verbal=""
    
    nummer=request.session['nummer']
    ##### Nummer vergeben / Position
    if nummer == "":
        konzept=open('tmp' + '.kpt','r').readlines()
        nummer=str(len(konzept)+1)
        request.session['nummer']=nummer

    aufgabenname="a" + nummer

    ##### Konzept anpassen
    konzept=open('tmp' + '.kpt','a')
    konzept.write(aufgabenname + "\n")
    konzept.close()
    

    template=open(aufgabenname + '.tpl','w')

    template.write('"aufgabentext="' + aufgabentext + ',"anzahl="' + str(anzahl) + ',"verbal="' + str(verbal) + ')')
    template.close()


    #return HttpResponse(aufg_bernoulli(aufgabentext=aufgabentext,anzahl=anzahl))


    texdatei=open(aufgabenname + '.tex','w')
    texdatei_lsg=open(aufgabenname + '_lsg.tex','w')
    texdatei_lsg_skizze=open(aufgabenname + '_lsg_skizze.tex','w')
    
    aufgaben=[]
    loesungen=[]
    for i in aufg_bernoulli(aufgabentext=aufgabentext,anzahl=anzahl): 
        aufgaben.append(i[0])
        loesungen.append(i[3])

    #return HttpResponse(aufgaben)

    texdatei.write(makeExercise(aufgabe=multicol(aufgaben,2),punkte="24",aufgabentext=aufgabentext))
    texdatei_lsg.write(makeExercise(aufgabe=multicol(loesungen,2),punkte="24",aufgabentext=aufgabentext))



    texdatei.close()
    texdatei_lsg.close()
    texdatei_lsg_skizze.close()


    return manuell_ab(request)
