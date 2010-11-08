import tweepy
from django.conf import settings
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response
from search.models import *
from blog.models import Entry
from video.models import *
from headlines.models import *


def search_results(request):

  if request.method == 'GET':
    return HttpResponseRedirect("/")

  search_string = request.POST.get("searchbox")
  if search_string:
    entries = Entry.objects.select_related().filter(
                Q(title__icontains=search_string) | 
                Q(body_markdown__icontains=search_string),status=1)

    videos = Video.objects.select_related().filter(
                Q(title__icontains=search_string) | 
                Q(details__icontains=search_string),isactive=1)

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
    'entries':entries,
    'videos':videos,
    'search_term':search_string,
    'headlines':headlines,
    #'tweets':tweets,
  })
  return render_to_response('search/results.html', variables)

