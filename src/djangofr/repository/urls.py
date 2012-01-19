from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from djangofr.repository.views import DeleteFile, ViewFile

urlpatterns = patterns('djangofr.repository.views',

    url(r'^add/$', 'add_file', name='add_file'),
    
    url(r'^cat/(?P<cat_id>\d+)/', 'cat_show', name='category_view'),

    url(r'^myfiles/', 'user_files', name='my_files'),
    
    url(r'^(?P<file_id>\d+)/delete/$', DeleteFile.as_view(), name='delete_file'),
    
    url(r'^(?P<file_id>\d+)/edit/$', 'edit_file', name='edit_file'),
    
    url(r'^(?P<file_id>\d+)', ViewFile.as_view(), name='view_file')
)
