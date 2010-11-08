import os
import sys

sys.path.append('/home/pop/public_html/popgalaxy')
sys.path.append('/usr/lib/python2.5/site-packages/django/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
