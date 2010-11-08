from django.contrib import admin
from video.models import *

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'isactive', 'featured', 'carousel', 'drunkduck', 'wowio', 'wevolt', 'syndicate')           
    search_fields = ['title', 'body_markdown']
    list_filter = ('pub_date', 'featured', 'drunkduck', 'wowio', 'wevolt', 'syndicate')
    prepopulated_fields = {"slug" : ('title',)}

admin.site.register(Video, VideoAdmin)