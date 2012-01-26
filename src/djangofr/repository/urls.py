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
from django.conf import settings

from repository.views import DeleteFile, ViewFile

urlpatterns = patterns('repository.views',

    url(r'^add/$', 'add_file', name='add_file'),
    
    url(r'^cat/(?P<cat_id>\d+)/', 'cat_show', name='category_view'),

    url(r'^myfiles/', 'user_files', name='my_files'),
    
    url(r'^(?P<file_id>\d+)/delete/$', DeleteFile.as_view(), name='delete_file'),
    
    url(r'^(?P<file_id>\d+)/edit/$', 'edit_file', name='edit_file'),
    
    url(r'^(?P<file_id>\d+)', ViewFile.as_view(), name='view_file')
)
