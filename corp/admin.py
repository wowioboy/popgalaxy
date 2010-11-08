from django.contrib import admin
from corp.models import *

class CorporateAdmin(admin.ModelAdmin):
    list_display = ('section',)           
    search_fields = ['section', 'details_markdown']
    list_filter = ('section',)

admin.site.register(Corporate, CorporateAdmin)