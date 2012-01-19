from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from repository.models import Category, RepoFile
from repository.forms import RepoFileForm


def index(request):

    """
    This is the main application view. All the public repository objects are
    shown here. We also get the categories context to show them in the template.
    
    :contexts: file, categories
    """
    file_list = RepoFile.objects.filter(public=True)
    paginator = Paginator(file_list, 16, orphans=3)
    categories = Category.objects.all()
 
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        files = paginator.page(page)
    except (EmptyPage, InvalidPage):
        files = paginator.page(paginator.num_pages)
        
    return render_to_response('repository/repofile_index.html', {'file': files,'categories':categories},
        context_instance=RequestContext(request))


class ViewFile(DetailView):

    """
    Returns the file object. If the file is not public and the user is not in the
    allowed_users field the view returns a 'not allowed' error. Incase the user
    is allowed ot is an admin, the view returns the file.
    
    :context: file
    """
    context_object_name = 'file'
    template_name = 'repository/repofile_detail.html'
    
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
    Creates a new RepoFile object. The form is modified during validation to
    store the author.
    
    :context: form
    """
    file_form = RepoFileForm(request.POST or None)
    
    if request.user.is_staff:
        if request.method == 'POST':
            if file_form.is_valid():
                file_form_uncommited = file.form.save(commit=False)
                file_form_uncommited.author = request.user
                file_form_uncommited.save()
                
                return redirect('/')
    else:
        return render_to_response('errors/not_allowed.html',
                                  context_instance=RequestContext(request))
    
    return render_to_response('repository/repofile_add.html', {'form':file_form},
                              context_instance=RequestContext(request))


def edit_file(request, file_id):

    """
    """
    pass


class DeleteFile(DeleteView):

    """
    This view deletes the file the admin selects. It uses the default template
    for the class view.
    """
    context_object_name = 'file'
    success_url = '/'
    
    @method_decorator(permission_required('repofiles.delete_repofile'))
    def dispatch(self, *args, **kwargs):
        return super(DeleteFile, self).dispatch(*args, **kwargs)

    def get_object(self):
        return get_object_or_404(RepoFile, pk = self.kwargs['file_id'])
        

def cat_show(request, cat_id):

    """
    Shows all the files inside a specific category. This only includes the public
    files.
    
    :context: file, categories, current_category
    """
    # Current selected category
    cat = get_object_or_404(Category, pk=cat_id)
    # Get all categories
    categories = Category.objects.all()
    # Get files in current category
    file_list = RepoFile.objects.filter(category=cat_id).filter(public=True)
    paginator = Paginator(file_list, 16, orphans=3)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        files = paginator.page(page)
    except (EmptyPage, InvalidPage):
        files = paginator.page(paginator.num_pages)
        
    return render_to_response('repository/category_list.html', {'current_category': cat,
                                                     'file': files,
                                                     'categories': categories},
                                      context_instance=RequestContext(request))
                                    
                    
def user_files(request):

    """
    Show all the private files where the user has access. This does not include
    the public files. This view is paginated every 16 objects. If a page
    contains only 3 objects, they're added to the last page.
    
    :context: file
    """
    file_list = RepoFile.objects.filter(allowed_users__id=request.user.id)

    paginator = Paginator(file_list, 16, orphans=3)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        files = paginator.page(page)
    except (EmptyPage, InvalidPage):
        files = paginator.page(paginator.num_pages)
        
    return render_to_response('repository/repofile_user_files.html', {'file':files},
                              context_instance=RequestContext(request))
