from django.conf.urls import include, url

from django.conf import settings
from django.conf.urls.static import static

from JJL.Peoulot.views import ListPeoulot
from JJL.views import login_view, logout_view, home

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', home, name='login'),
    url(r'^login/$', login_view, name='validate'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^peoulot/', include('JJL.Peoulot.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
