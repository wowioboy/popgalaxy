import tweepy
from django.conf.urls.defaults import *
from django.conf import settings
from tagging.views import tagged_object_list
from blog.models import Entry
from blog.views import *
from headlines.models import *

headlines = Headline.objects.filter(isactive=1)
"""
auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_SECRET)
api = tweepy.API(auth)
pop_timeline = api.user_timeline()
dd_timeline = api.user_timeline('drunkduck')
wv_timeline = api.user_timeline('wevoltonline')
mentions = api.mentions()
tweets = {
  'pop_timeline':pop_timeline,
  'dd_timeline':dd_timeline,
  'wv_timeline':wv_timeline,
  'mentions':mentions
}
"""

entries = Entry.objects.order_by('-pub_date','title').filter(status=1)
data_dict = {
	'queryset': entries,
	'date_field': 'pub_date',
    #'extra_context':{'tweets':tweets,'headlines':headlines},
}

urlpatterns = patterns('django.views.generic.date_based',
    (r'(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 'object_detail', dict(data_dict, template_name='blog/entry.html')),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 'object_detail', dict(data_dict, template_name='blog/entry.html')),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$','archive_day',dict(data_dict,template_name='blog/index.html')),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$','archive_month', dict(data_dict, template_name='blog/index.html')),
    (r'^(?P<year>\d{4})/$','archive_year', dict(data_dict, template_name='blog/index.html')),
    (r'^$',blog),
)





