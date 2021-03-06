from django.conf.urls import include, url
from django.http import HttpResponseRedirect
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import fileupload.views
admin.autodiscover()

urlpatterns = [
    url(r'^$', lambda x: HttpResponseRedirect('/ui/about')),
    url(r'^upload/', include('fileupload.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ui/', include('userinterface.urls')),
    url(r'^fetch/$', fileupload.views.analyze),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
