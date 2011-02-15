#import tweepy
from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response
from video.models import *
from blog.models import *
from headlines.models import *


def video_list(request):

  videos = Video.objects.filter(isactive=1).order_by('-pub_date')
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
    'videos':videos,
    'headlines': headlines,
  })
  return render_to_response('video/list.html', variables)


def video_detail(request,slug):

  video = Video.objects.get(slug=slug)
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
  variables = RequestContext(request, {
    'video': video,
    'headlines': headlines,
  })
  return render_to_response('video/detail.html', variables)
