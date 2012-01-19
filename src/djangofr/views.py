from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView

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

def cat_show(request, cat_id):

    """
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
        
    return render_to_response('category_list.html', {'current_category': cat,
                                                     'file': files,
                                                     'categories': categories},
                                      context_instance=RequestContext(request))
                                    
                    
def user_files(request):

    """
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
        
    return render_to_response('user_files.html', {'file':files},
                              context_instance=RequestContext(request))
