import os
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.contrib import admin
from blog.views import *
from video.views import *
from search.views import *
from corp.views import *
from headlines.views import *
from feeds import LatestBlogFeed, LatestVideoFeed

admin.autodiscover()
urlpatterns = patterns('',
    # Example:
    # (r'^popgalaxy/', include('popgalaxy.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '/usr/local/tinymce/jscripts/tiny_mce' },),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    (r'^tagging_autocomplete/', include('tagging_autocomplete.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
)
urlpatterns += patterns('',
    (r'^$',home_page),
    (r'^blog/feed/$', LatestBlogFeed()),
    (r'^video/feed/$', LatestVideoFeed()),
    (r'^blog/',include('blog.urls')),
    (r'^video/',include('video.urls')),
    (r'^search/$',search_results),
    (r'^about/$',about),
)
"""
urlpatterns += patterns('',
    (r'^profile/(\w+)/$', profile_page),
    (r'^account/(\w+)/$', account_page),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^passwordchange/$','django.contrib.auth.views.password_change'),
    (r'^logout/$', logout_page),
    (r'^register/$', register_page),
    (r'^register/success/$', direct_to_template, {'template': 'registration/register_success.html'}),
)
"""
