from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from djangofr.taggit.managers import TaggableManager

class Category(models.Model):

    """
    """
    name = models.CharField(_('Category name'), max_length=100,
        help_text=_('Name of the category. 100 chars maximum.'))
    pub_date = models.DateTimeField(auto_now_add=True)
    last_mod = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __unicode__(self):
         return self.name


class RepoFile(models.Model):

    """
    """
    name = models.CharField(_('Name'), max_length=250,
        help_text=_('This will be the visible name of the file.'))
    description = models.TextField(_('Description of the file'))
    front = models.ImageField(upload_to='images/', blank=True, null=True)
    stored_file = models.FileField(upload_to='files/',
        verbose_name=_('File to upload'),
        help_text=_('Maximum file size is 25MB.'), blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name=_('Select the category'))
    public = models.BooleanField(_('Make public'),
        help_text=_('Selecting this will make the file available to public.'))
    allowed_users = models.ManyToManyField(User, blank=True, null=True,
        verbose_name=_('Allowed users'),
        help_text=_('Select the users that can see this file.'),
        related_name="allowed_users")
    tags = TaggableManager()
        
    pub_date = models.DateTimeField(auto_now_add=True)
    last_mod = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, blank=True, null=True, related_name="author")

    def human_file_size(self):
        print self.stored_file.size
        if self.stored_file.size < 1023:
            return str(self.stored_file.size) + " Bytes"
        elif self.stored_file.size >= 1024 and self.stored_file.size <= 1048575:
            return str(round(self.stored_file.size / 1024.0, 2)) + " KB"
        elif self.stored_file.size >= 1048576:
            return str(round(self.stored_file.size / 1024000.0, 2)) + " MB"

    class Meta:
         ordering = ['name']
         verbose_name = _('File')
         verbose_name_plural = _('Files')
         get_latest_by = 'pubdate'

    def __unicode__(self):
         return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('view-file', (), {
            'file_id': self.id})
