from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'django-fr.views.view_site_index', name='home'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^user/', include('registration.backends.default.urls')),

    url(r'^i18n/', include('django.conf.urls.i18n')),
    
)
