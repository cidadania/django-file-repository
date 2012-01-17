from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from djangofr.repository.models import Category, RepoFile

class CategoryAdmin(admin.ModelAdmin):

    """
    """
    list_display = ('name', 'pub_date', 'last_mod')
    search_fields = ('name',)
    
class RepoFileAdmin(admin.ModelAdmin):

    """
    """
    list_display = ('name', 'category', 'description', 'public', 'pub_date')
    search_fields = ('name', 'category', 'description')
    
#    fieldsets = [
#        (None, {'fields':
#            [('name', 'category'), 'description']}),
#            
#        (None, {'fields':
#            [('front', 'stored_file')]})
#            
#        (None, {'fields':
#            ['public', 'allowed_users']}),
#    ]
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(RepoFile, RepoFileAdmin)
