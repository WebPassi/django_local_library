from django.http import HttpResponse
from django.template import RequestContext, loader



from sympy import *
from sympy.abc import *
from funktionen import Function

#l=Function(x*x)
#l1=LinFunc(1,2)
#a=tester()
def index(request):
#    return HttpResponse(l.ywert(2))
    t=Function(x*x)
    wert=t.ywert(3)
    template=loader.get_template('generator/index.html')
    context=RequestContext(request, {
        'Funktionswert': wert,
    })
    return HttpResponse(template.render(context))


def aufgabe(request):
    return HttpResponse("Hello, world. %s" % n)


