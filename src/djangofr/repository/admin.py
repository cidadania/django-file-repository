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

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from repository.models import Category, RepoFile

class CategoryAdmin(admin.ModelAdmin):

    """
    Category model administration.
    
    :list_display: name, pub_date, last_mod
    :search_fields: name
    
    .. versionadded:: 0.2b
    """
    list_display = ('name', 'pub_date', 'last_mod')
    search_fields = ('name',)
    
class RepoFileAdmin(admin.ModelAdmin):

    """
    RepoFile administration model. At save time we change the author to the
    current user (even if the user selected another author) and save. The user
    change is meant to be edited in file edit.
    
    :display: name, category, description, public, pub_date
    :search_fields: name, category, description
    
    .. versionadded:: 0.2b
    """
    list_display = ('name', 'category', 'description', 'public', 'pub_date')
    search_fields = ('name', 'category', 'description')
    
#    fieldsets = [
#        (None, {'fields':
#            [('name', 'category'), 'description']}),
#            
#        (None, {'fields':
#            [('front', 'stored_file')]})
#            
#        (None, {'fields':
#            ['public', 'allowed_users']}),
#    ]
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(RepoFile, RepoFileAdmin)
