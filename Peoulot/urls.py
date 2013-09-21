from django.conf.urls import *
from django.contrib.auth.decorators import login_required

from JJL.Peoulot.views import ListPeoulot, LirePeoula, ajouterModifier

urlpatterns = patterns('JJL.Peoulot.views',
    url(r'^$', login_required(ListPeoulot.as_view()), name='liste'),
    url(r'^lire/(?P<pk>\d+)$', login_required(LirePeoula.as_view()), name='lire'),
    url(r'^ajouter/$', login_required(ajouterModifier), name='ajouter'),
    url(r'^modifier/(?P<pk>\d+)$', login_required(ajouterModifier), name='modifier'),
)
