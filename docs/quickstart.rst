Quickstart
==========

To start using django-file-repository (*djangofr* from now on) right away you
can use the default installation.

Download
--------

You can download *djangofr* from GitHub:

Stable::

    http://github.com/cidadania/django-file-repository/downloads

Development::

    git clone git://github.com/cidadania/django-file-repository.git

Configuration
-------------

The only parameters required to work with *djangofr* are:

.. warning:: Currently *djangofr* does not support SSL or certificated servers.
             Support will be included in the future.

.. note:: If you will not allow user registration you can skip the configuration
          step.

**EMAIL_HOST**
 This is your SMTP server.
 
 :default: localhost
    
**EMAIL_PORT**
  Port for your server.
  
  :default: 25
     
**EMAIL_HOST_USER**
  Your email user.
  
  :default: None
     
**EMAIL_HOST_PASSWORD**
  Your email password.
  
  :default: None
  
Build database and start working!
---------------------------------

After that, you will only have to run this commands::

    ./manage.py syncdb (to make the database tables)

    and after it
    
    ./manage.py runserver (it will start the development server on port 8000)
    
The instructions for deployment in production servers are pretty well explained
in the `django documentation <https://docs.djangoproject.com/en/dev/howto/deployment/>`_
