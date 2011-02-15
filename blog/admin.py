from django.contrib import admin
from blog.models import *
from tinymce.widgets import TinyMCE

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date','carousel','enable_comments', 'status')           
    search_fields = ['title', 'body_markdown']
    list_filter = ('pub_date', 'enable_comments', 'status')
    prepopulated_fields = {"slug" : ('title',)}
    fieldsets = (
		(None, {'fields': ('carousel', 'status', 'title', 'subtitle', 'carousel_text', 'carousel_subtext', 'leadin_markdown', 'body_markdown', ('pub_date', 'enable_comments'), 'thumbnail', 'tags', 'slug')}),
    )
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})}, 
    }

admin.site.register(Entry, EntryAdmin)
