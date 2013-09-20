from django.conf.urls import *

from django.conf import settings
from django.conf.urls.static import static

from JJL.Peoulot.views import ListPeoulot

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', ListPeoulot.as_view(), name='liste'),
    (r'^peoulot/', include('JJL.Peoulot.urls')),
    # Examples:
    # url(r'^$', 'JJL.views.home', name='home'),
    # url(r'^JJL/', include('JJL.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
