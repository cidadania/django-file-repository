django-file-repository
======================

This program is a simple file storage platform.

How to install
--------------

Standalone development
......................

To use djangofr alone (in development mode) just download the code and execute:
::
  ./manage.py syncdb
  
After building the database and creating the administration user you have to run::

  ./manage.py runserver

Et voilà!

Standalone stable
.................

Not written yet.

Pluggable
.........

The other way is to use djangofr as a pluggable application, in which case you will
have to copy the **repository** directory onto your project and create an url
to manage the repo.

.. warning:: This secion has to be extended.

Documentation
-------------

You can find all the djangofr documentation in: http://django-file-repository.rtfd.org/

Questions/Contact
-----------------

You can contact me at oscar.carballal@cidadania.coop if you have any questions about djangofr
