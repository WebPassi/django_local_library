from django.conf.urls import patterns, url

from generator import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #url(r'^(?P<n>\d+)/$', views.detail, name='detail'),
    #url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),)
    url(r'auto_ab', views.auto_ab, name='auto_ab'),
    url(r'quad_glg', views.quad_glg, name='quad_glg'),
#    url(r'aufgabe', views.aufgabe, name='aufgabe'),
#    url(r'quadfunc', views.quadfunc, name='quadfunc'),


)


