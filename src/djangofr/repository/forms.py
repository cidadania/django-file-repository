from django.forms import ModelForm

from repository.models import RepoFile

class RepoFileForm(ModelForm):
    
    """
    ModelForm for RepoFile. In this case all they fields are needed in the form
    except the author, so we got rid of it.
    
    :versionadded: 0.2b
    """
    class Meta:
        model = RepoFile
        exclude = ('author')

