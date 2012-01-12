from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.
class RepoFile(models.Model):

    """
    """
    name = models.CharField(_('Name'), max_length=250,
        help_text=_('This will be the visible name of the file.'))
    stored_file = models.FileField(upload_to='/files',
        verbose_name=_('File to upload'),
        help_text=_('Maximum file size is 25MB.'))
    public = models.BooleanField(_('Public'))
    allowed_users = models.ForeignKey(User, blank=True, null=True,
        verbose_name=_('Select the users that can see this file.'))
    pubdate = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, blank=True, null=True)

    class Meta:
         ordering = ['name']
         verbose_name = _('File')
         verbose_name_plural = _('Files')
         get_latest_by = 'pubdate'

    def __unicode__(self):
         return self.name

#    @models.permalink
#    def get_absolute_url(self):
#        return ('space-index', (), {
#            'space_name': self.url})

