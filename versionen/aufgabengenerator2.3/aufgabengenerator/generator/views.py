#import os
from django.shortcuts import render
from django.http import HttpResponse

from sympy import *
from sympy.abc import *
from functions import Function
from auto_ab import *

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
    ab_quadfunc()
    return HttpResponse("<h1>Viele Quadratische Gleichungen</h1>")

def lin_glg(request):
    ab_linglg()
    return HttpResponse("<h1>Viele Lineare Gleichungen</h1>")

def lin_func(request):
    ab_linfunc()
    return HttpResponse("<h1>Viele Lineare Funktionen</h1>")

def terme(request):
    ab_terme()
    return HttpResponse("<h1>Viele Terme</h1>")
    

#def aufgabe(request):
#    t=Function(x*x)
#    wert=t.ywert(3)
#    context={'Funktionswert': wert}
#    return render(request,'generator/aufgabe.html',context)





