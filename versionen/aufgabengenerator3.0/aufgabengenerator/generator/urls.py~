from django.conf.urls import patterns, url

from generator import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #url(r'^(?P<n>\d+)/$', views.detail, name='detail'),
    #url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),)
    url(r'auto_ab', views.auto_ab, name='auto_ab'),
    url(r'quad_glg', views.quad_glg, name='quad_glg'),
    url(r'lin_glg', views.lin_glg, name='lin_glg'),
    url(r'lin_func', views.lin_func, name='lin_func'),
    url(r'terme', views.terme, name='terme'),
    url(r'normalparabel', views.normalparabel, name='normalparabel'),
    url(r'parabel', views.parabel, name='parabel'),
    url(r'scheitelpunktform', views.scheitelpunktform, name='scheitelpunktform'),
    url(r'linFunc_os', views.linFunc_os, name='linFunc_os'),
    url(r'prozentrechnung', views.prozentrechnung, name='prozentrechnung'),

    url(r'manuell_ab', views.manuell_ab, name='manuell_ab'),
    url(r'rechenaufgabe', views.rechenaufgabe, name='rechenaufgabe'),
    url(r'aufgabenbereich', views.aufgabenbereich, name='aufgabenbereich'),


#    url(r'aufgabe', views.aufgabe, name='aufgabe'),
#    url(r'quadfunc', views.quadfunc, name='quadfunc'),


)


