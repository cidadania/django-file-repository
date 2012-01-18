from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from repository.models import RepoFile, Category

def view_site_index(request):

    """
    This is the main site view. All the public repository objects are shown here.
    We also get the categories context to filter them in the template.
    
    :contexts: files, categories
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
        
    return render_to_response('site_index.html', {'file': files,'categories':categories},
        context_instance=RequestContext(request))
