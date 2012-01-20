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

from django.forms import ModelForm

from repository.models import RepoFile

class RepoFileForm(ModelForm):
    
    """
    ModelForm for RepoFile. In this case all they fields are needed in the form
    except the author, so we got rid of it.
    
    :rtype: HTML Form
    
    .. versionadded:: 0.2b
    """
    class Meta:
        model = RepoFile
        exclude = ('author')

