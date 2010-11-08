from django.conf.urls.defaults import *
from tagging.views import tagged_object_list
from blog.models import Entry
from video.models import *
from video.views import *

urlpatterns = patterns('',
    (r'^(?P<slug>[a-zA-Z0-9_.-]+)/$',video_detail),
    (r'^$',video_list),
)

