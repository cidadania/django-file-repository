django-file-repository
======================

Current version: 0.2.1

This program is a file storage platform.

Features
--------

 * Public & private files
 * Categories & Tagging
 * i18n (currently spanish, galician and english)
 * User registration and personal zone

  *Future Features*
   * Cover image based on file content (if not, put generic filetype icon)
   * Persistent URLs
   * Online Multimedia viewer based on HTML5


Requirements
------------

 * django-registration
 * django-taggit

.. note:: Django-file-repository uses the latest version of
          django-registration, which is not available through pip
          or easy_install. You can download it from:

          https://bitbucket.org/ubernostrum/django-registration

How to install
--------------

Standalone
..........

To use djangofr alone (in development mode) just download the code and execute:
::
  ./manage.py syncdb
  
After building the database and creating the administration user you have to run::

  ./manage.py runserver

Et voilà!

Pluggable
.........

The other way is to use django-file-repository is as a pluggable application,
in which case you will have to install it through the *pip* or *easy_install*
commands.

**Note** The pluggable version comes with no templates. For possible example
templates you can download this project and study/use the templates there.

.. warning:: The cheese shop version can be outdated. If it's the case, please
             leave am issue here.

Documentation
-------------

You can find all the djangofr documentation in: http://django-file-repository.rtfd.org/

Questions/Contact
-----------------

You can contact me at oscar.carballal@cidadania.coop if you have any questions about djangofr
