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

#################################################
# SPECIFIC DJANGO-FILE-REPOSITORY CONFIGURATION #
#################################################

# Customization
REPOSITORY_NAME = "MyRepo"

# django-registration settings
ACCOUNT_ACTIVATION_DAYS = 7
#EMAIL_HOST=""
#EMAIL_PORT=
#EMAIL_HOST_USER=""
#EMAIL_HOST_PASSWORD=""

# django-auth settings
LOGIN_URL="/user/login"
LOGIN_REDIRECT_URL="/"
LOGOUT_URL="/user/logout"

# django-tagging settings
FORCE_LOWERCASE_TAGS = True

# Set the available languages in the platform
LANGUAGES = (
    ('es', 'Espanol'),
    ('en', 'English'),
    ('gl', 'Galego'),
)

##################################
# STANDARD DJANGO PROJECT CONFIG #
##################################

# Get the current working directory
import os
cwd = os.path.dirname(os.path.realpath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    #('AdminName', 'admin@email.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db/sqlite.db',
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost.
        'PORT': '',                      # Set to empty string for default.
    }
}

# i18n and l10n configuration
TIME_ZONE = 'Europe/Madrid'
LANGUAGE_CODE = 'es-es'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

# Media and static files directories
MEDIA_ROOT = cwd + '/uploads/'
MEDIA_URL = '/uploads'
STATIC_ROOT = cwd + '/static/'
STATIC_URL = '/static'
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATICFILES_DIRS = (
    (cwd + '/static_files/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'mzr2%=l*+p87^9t1x@0km^ej*ge0+32v657d)lp@sh$i)sms4g'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'djangofr.urls'

TEMPLATE_DIRS = (
    (cwd + '/templates/')
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'djangofr.repository',
    'taggit',
    'registration',
)



# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
