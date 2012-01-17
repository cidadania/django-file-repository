from django.shortcuts import render_to_response
from django.template import RequestContext

from repository.models import RepoFile, Category

def view_site_index(request):

    """
    This is the main site view. All the public repository objects are shown here.
    We also get the categories context to filter them in the template.
    
    :contexts: files, categories
    """
    files = RepoFile.objects.filter(public=True)
    categories = Category.objects.all()
    
    return render_to_response('site_index.html', {'file': files,'categories':categories},
        context_instance=RequestContext(request))
