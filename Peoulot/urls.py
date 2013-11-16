from django.conf.urls import *
from django.contrib.auth.decorators import login_required, permission_required

from JJL.Peoulot.views import ListPeoulot, LirePeoula, ajouterModifier

urlpatterns = patterns('JJL.Peoulot.views',
    url(r'^$', login_required(ListPeoulot.as_view()), name='liste'),
    url(r'^toutes/$', login_required(ListPeoulot.as_view()), {'toutes' : True}, name='toutes'),
    url(r'^lire/(?P<pk>\d+)$', login_required(LirePeoula.as_view()), name='lire'),
    url(r'^ajouter/$', permission_required('Peoulot.add_peoula', raise_exception=True)(ajouterModifier), name='ajouter'),
    url(r'^modifier/(?P<pk>\d+)$', permission_required('Peoulot.change_peoula', raise_exception=True)(ajouterModifier), name='modifier'),
)
