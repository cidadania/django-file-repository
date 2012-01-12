from django.conf.urls.defaults import patterns, include, url

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'django-fr.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^i18n/', include('django.conf.urls.i18n')),

)
