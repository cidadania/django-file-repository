from django.forms import ModelForm

from repository.models import RepoFile

class RepoFileForm(ModelForm):
    
    """
    """
    class Meta:
        model = RepoFile
        exclude = ('author')

