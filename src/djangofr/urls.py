# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Cidadanía Coop.
# Written by: Oscar Carballal Prego <oscar.carballal@cidadania.coop>
#
# This file is part of django-file-repository.
#
# django-file-repository is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with django-file-repository.  If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'repository.views.index', name='home'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^user/', include('registration.backends.default.urls')),

    url(r'^i18n/', include('django.conf.urls.i18n')),
    
    url(r'^repo/', include('repository.urls')),
    
    # Media content #### FOR DEVELOPMENT!! ####
    (r'^uploads/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'uploads'}),
    
    # Static content #### FOR DEVELOPMENT!! ####
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'static'}),
)

if settings.DEBUG:
    # Serve static files
    urlpatterns += staticfiles_urlpatterns()
