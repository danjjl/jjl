from django.conf.urls import *

from JJL.Peoulot.views import ListPeoulot, LirePeoula, ajouterModifier

urlpatterns = patterns('JJL.Peoulot.views',
    url(r'^$', ListPeoulot.as_view(), name='liste'),
    url(r'^lire/(?P<pk>\d+)$', LirePeoula.as_view(), name='lire'),
    url(r'^ajouter/$', ajouterModifier, name='ajouter'),
    url(r'^modifier/(?P<pk>\d+)$', ajouterModifier, name='modifier'),
)
