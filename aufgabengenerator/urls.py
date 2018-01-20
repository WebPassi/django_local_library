#from django.conf.urls import url
from django.contrib import admin

from django.urls import include, path

app_name="aufgabengenerator"

urlpatterns = [
    # Examples:
    # url(r'^$', 'aufgabengenerator.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^generator/', include('generator.urls', namespace="generator")),

    path(r'^admin/', admin.site.urls),

    path(r'^generator/', include('generator.urls')),


]
