from django.shortcuts import render_to_response
from django.template import RequestContext

from repository.models import RepoFile, Category

def view_site_index(request):

    """
    """
    files = RepoFile.objects.filter(public=True)
    categories = Category.objects.all()
    
    return render_to_response('site_index.html', {'file': files,'categories':categories},
        context_instance=RequestContext(request))
