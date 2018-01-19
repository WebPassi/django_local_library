#import os
from django.shortcuts import render
from django.http import HttpResponse

from sympy import *
from sympy.abc import *
from funktionen import Function
from klausur import *

#l=Function(x*x)
#l1=LinFunc(1,2)
#a=tester()



def index(request):
    context={'bla': ""}
    return render(request,'generator/index.html',context)

def auto_ab(request):
    context={'bla': ""}
    return render(request,'generator/auto_ab.html',context)

def quad_glg(request):
    meinTest()
#    os.system('pdflatex sheet.tex')
#    os.system('evince sheet.pdf')
    return HttpResponse("<h1>Viele Quadratische Gleichungen</h1>")


#def aufgabe(request):
#    t=Function(x*x)
#    wert=t.ywert(3)
#    context={'Funktionswert': wert}
#    return render(request,'generator/aufgabe.html',context)





