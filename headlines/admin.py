from django.contrib import admin
from headlines.models import *

class HeadlineAdmin(admin.ModelAdmin):
    list_display = ('title','isactive',)           
    search_fields = ['title']

admin.site.register(Headline, HeadlineAdmin)