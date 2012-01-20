:mod:`repository` --- Repository
================================

:mod:`repository.admin` --- Administration
------------------------------------------

.. automodule:: repository.admin

.. autoclass:: CategoryAdmin(admin.ModelAdmin)
    :members:

.. autoclass:: RepoFileAdmin(admin.ModelAdmin)
    :members:
    
:mod:`repository.models` --- Data models
----------------------------------------

.. automodule:: repository.models

.. autoclass:: Category(models.Model)
    :members:

.. autoclass:: RepoFile(models.Model)
    :members:

:mod:`repository.forms` --- Forms
---------------------------------

.. automodule:: repository.forms

.. autoclass:: RepoFileForm(ModelForm)
    :members:

:mod:`repository.urls` --- URLs
-------------------------------

add/
  Adds a new file to the repository
  
  :reverse: add_file

cat/<cat_id>
  Shows the documents in a specific category.
  
  :values: cat_id (Category ID)
  :reverse: category_view

myfiles/
  Shows the private files a user has.
  
  :reverse: my_files

<file_id>/delete
<file_id>/edit
  Delete or edit the file with <file_id>
  
  :values: file_id
  
<file_id>/
  View detailed info about a particular file.
  
  :values: file_id
  
:mod:`repository.views` --- Views
---------------------------------

.. automodule:: repository.views

.. autofunction:: index(request)

.. autoclass:: ViewFile(DetailView)
    :members:

.. autofunction:: add_file(request)

.. autofunction:: edit_file(request, file_id)

.. autoclass:: DeleteFile(DeleteView)
    :members:

.. autofunction:: cat_show(request, cat_id)

.. autofunction:: user_files(request)
