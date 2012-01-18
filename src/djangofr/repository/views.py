from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from djangofr.repository.models import Category, RepoFile

class ViewFile(DetailView):

    """
    Returns the file object. If the file is not public and the user is
    """
    context_object_name = 'file'
    template_name = 'repository/file_detail.html'
    
    def get_object(self):
        fileid = self.kwargs['file_id']
        file_object = get_object_or_404(RepoFile, pk=fileid)
        
        if not file_object.public:
            if self.request.user.is_anonymous():
                self.template_name = 'errors/not_allowed.html'
                return RepoFile.objects.none()
            for i in file_object.allowed_users.all():
                if i == self.request.user:
                    return file_object
            if self.request.user.is_staff:
                return file_object
            
            self.template_name = 'errors/not_allowed.html'
            return RepoFile.objects.none()
            
        return file_object

    def get_context_data(self, **kwargs):
        context = super(ViewFile, self).get_context_data(**kwargs)
        return context

def add_file(request):

    """
    """
    pass


def edit_file(request, file_id):

    """
    """
    pass


class DeleteFile(DeleteView):

    """
    """
    context_object_name = 'file'
    success_url = '/'
    
    def dispatch(self, *args, **kwargs):
        return super(DeleteFile, self).dispatch(*args, **kwargs)

    def get_object(self):
        return get_object_or_404(RepoFile, url = self.kwargs['file_id'])
