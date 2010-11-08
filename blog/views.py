import tweepy
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from django.core import serializers
from django.utils import encoding
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.conf import settings
from itertools import chain
from blog.models import *
from blog.forms import *
from video.models import *
from headlines.models import *

########################################
def home_page(request):

  data_range = 4
  video = Video.objects.get(isactive=1,featured=1)
  carousel_video = Video.objects.filter(isactive=1,carousel=1)
  #carousel_blog = Entry.objects.filter(status=1,carousel=1)[:data_range].values('carousel_text','carousel_subtext','slug','thumbnail')
  headlines = Headline.objects.filter(isactive=1)

  
  tweets = {}
  auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
  auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_SECRET)
  api = tweepy.API(auth)
  pop_timeline = api.user_timeline() # PG's timeline
  #mentions = api.mentions()	# PG's @mentions
  dd_timeline = api.user_timeline('drunkduck') # DD's tweets
  wowio_timeline = api.user_timeline('wowio') # WOWIO's tweets
  wv_timeline = api.user_timeline('wevoltonline') # WEVolt's tweets
  tweets = {
    'pop_timeline':pop_timeline,
    'dd_timeline':dd_timeline,
    'wv_timeline':wv_timeline,
    'wowio_timeline':wowio_timeline,
    #'mentions':mentions
  }
  
  variables = RequestContext(request,{
    'featured_video':video,
    'carousel_video':carousel_video,
    'headlines':headlines,
    'tweets':tweets,
  })
  return render_to_response('homepage.html',variables)


########################################
def blog(request):

  entries_range = 5
  entries = Entry.objects.order_by('-pub_date','title').filter(status=1)
  headlines = Headline.objects.filter(isactive=1)

  """
  auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
  auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_SECRET)
  api = tweepy.API(auth)
  pop_timeline = api.user_timeline() # PG's timeline
  mentions = api.mentions()	# PG's @mentions
  dd_timeline = api.user_timeline('drunkduck') # DD's tweets
  wv_timeline = api.user_timeline('wevoltonline') # WEVolt's tweets
  tweets = {
    'pop_timeline':pop_timeline,
    'dd_timeline':dd_timeline,
    'wv_timeline':wv_timeline,
    'mentions':mentions
  }
  """
  variables = RequestContext(request, {
    'entries_range': range(entries_range),
    'entries': entries,
    'headlines':headlines,
  })
  return render_to_response('blog/index.html', variables)

########################################
def blog_entry(request, slug):

  entry = Entry.objects.filter(slug=slug)
  headlines = Headline.objects.filter(isactive=1)
  """
  auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
  auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_SECRET)
  api = tweepy.API(auth)
  pop_timeline = api.user_timeline() # PG's timeline
  mentions = api.mentions()	# PG's @mentions
  dd_timeline = api.user_timeline('drunkduck') # DD's tweets
  wv_timeline = api.user_timeline('wevoltonline') # WEVolt's tweets
  tweets = {
    'pop_timeline':pop_timeline,
    'dd_timeline':dd_timeline,
    'wv_timeline':wv_timeline,
    'mentions':mentions
  }
  """
  variables = RequestContext(request,{
    'entry':entry,
    'headlines':headlines,
  })
  return render_to_response('blog/entry.html',variables)
