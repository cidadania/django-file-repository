from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'djangofr.views.view_site_index', name='home'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^user/', include('registration.backends.default.urls')),

    url(r'^i18n/', include('django.conf.urls.i18n')),

    # Static content #### FOR DEVELOPMENT!! ####
    (r'^uploads/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'uploads'}),
    
    # Static content #### FOR DEVELOPMENT!! ####
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'static'}),
)

if settings.DEBUG:
    # Serve static files
    urlpatterns += staticfiles_urlpatterns()
