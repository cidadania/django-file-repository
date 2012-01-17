from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

urlpatterns = patterns('djangofr.repository.views',

    url(r'^add/$', 'add_file', name='add-file'),
    
    url(r'^(?P<file_id>\d+)/delete/$', DeleteFile.as_view(), name='delete-file'),
    
    url(r'^(?P<file_id>\d+)/edit/$', 'edit_file', name='edit-file'),
    
    url(r'^(?P<file_id>\d+)', ViewFile.as_view(), name='view-file')
)
