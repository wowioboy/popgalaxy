from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response
from corp.models import *

def about(request):

  content = Corporate.objects.get(section='about')
  variables = RequestContext(request, {
    'content':content
  })
  return render_to_response('corp/about.html', variables)

