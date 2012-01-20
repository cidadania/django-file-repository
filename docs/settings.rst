Settings
========

djangofr does noeed some extra settings apart from the defaults in settings.py
We tell you here which are they.

**ACCOUNT_ACTIVATION_DAYS**
  This value sets the valid tiome of an activation key after it was sent. If
  the user does not activate the account in that time, the key expires.
  
  :default: 7

**EMAIL_HOST** | **EMAIL_PORT** | EMAIL_HOST_USER | EMAIL_HOST_PASSWORD
  This values are for sending the validation email to the users.
  
  :default: None
  
.. warning: We recommend using a non-SSL or non-certified connection due to
            technical issues.

**LOGIN_URL**, **LOGIN_REDIRECT_URL**, **LOGOUT_URL**
  This values tell django where to search for the login, logout and redirect URLs
  Usually you will want this with the default value, since to modify it you have
  to modify the application URLs.
  
  :defaults: - /user/login
             - /user/logout
             - /
  
**FORCE_LOWERCASE_TAGS**
  Forces the tags to be stored and managed in lowercase form. This is useful,
  unless you want for any reason manage case sensitive urls.
  
  :default: True
