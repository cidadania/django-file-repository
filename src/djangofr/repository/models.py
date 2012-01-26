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

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

class Category(models.Model):

    """
    Category data model. This model stores possible categories or groups where
    we store the RepoFiles.
    
    :fields: name, description, pub_date, last_mod
    
    .. versionadded:: 0.1
    """
    name = models.CharField(_('Category name'), max_length=100,
        help_text=_('Name of the category. 100 chars maximum.'))
    description = models.TextField(_('Description'))
    pub_date = models.DateTimeField(auto_now_add=True)
    last_mod = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __unicode__(self):
         return self.name


class RepoFile(models.Model):

    """
    RepoFile data model. This model is meant to store all the files and information
    about the files.
    
    :fields: name, description, front, stored_file, category, public, allowed_users,
    tags, pub_date, last_mod, author
    
    **Methods:**
    
    **human_file_size**
      Returns the file size in human readable form, since the get_size method returns
      the byte count.
      
    .. versionadded:: 0.1
    """
    name = models.CharField(_('Name'), max_length=250,
        help_text=_('This will be the visible name of the file.'))
    description = models.TextField(_('Description of the file'))
    front = models.ImageField(upload_to='images/', blank=True, null=True)
    stored_file = models.FileField(upload_to='files/',
        verbose_name=_('File to upload'),
        help_text=_('Maximum file size is 25MB.'), blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name=_('Select the category'))
    public = models.BooleanField(_('Make public'),
        help_text=_('Selecting this will make the file available to public.'))
    allowed_users = models.ManyToManyField(User, blank=True, null=True,
        verbose_name=_('Allowed users'),
        help_text=_('Select the users that can see this file.'),
        related_name="allowed_users")
    tags = TaggableManager()
        
    pub_date = models.DateTimeField(auto_now_add=True)
    last_mod = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, blank=True, null=True, related_name="author")

    def human_file_size(self):
        print self.stored_file.size
        if self.stored_file.size < 1023:
            return str(self.stored_file.size) + " Bytes"
        elif self.stored_file.size >= 1024 and self.stored_file.size <= 1048575:
            return str(round(self.stored_file.size / 1024.0, 2)) + " KB"
        elif self.stored_file.size >= 1048576:
            return str(round(self.stored_file.size / 1024000.0, 2)) + " MB"

    class Meta:
         ordering = ['name']
         verbose_name = _('File')
         verbose_name_plural = _('Files')
         get_latest_by = 'pubdate'

    def __unicode__(self):
         return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('view-file', (), {
            'file_id': self.id})
