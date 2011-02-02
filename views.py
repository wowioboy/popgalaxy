from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.utils import simplejson
from django.core.validators import email_re
from django.contrib.auth.models import User
from django.db import IntegrityError

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


@login_required
def comment_form(request):
    return render_to_response('comments/comment_form.html', context_instance=RequestContext(request))



def remote_logout(request):
    dump = simplejson.dumps
    json = {}
    logout(request)
    return HttpResponse(dump(json), mimetype="application/json")

def remote_login(request):
    dump = simplejson.dumps
    json = {'success': False}

    user = authenticate(
        username=request.POST.get('username', '').lower(), 
        password=request.POST.get('password', '')
    )

    if user:
        login(request, user)
        json['success'] = True

    return HttpResponse(dump(json), mimetype="application/json")


def remote_signup(request):
    dump = simplejson.dumps
    json = {'success': False}

    signup_form = UserCreationForm(request.POST)

    if signup_form.is_valid():

        errors = extra_validation(request.POST)
        if errors:
            if errors.get('email', False):
                json['email'] = 'invalid'
            if errors.get('name', False):
                json['name'] = 'required'
        else:
            data = signup_form.cleaned_data
            name = request.POST['name'].strip().split(' ')
            fname = name[0]
            if len(name) > 0:
                del name[0]
                lname = ' '.join(name)
            else:
                lname = ''

            user = User.objects.create_user(username=data['username'].lower(), email=data['username'].lower(), password=data['password1'])
            user.first_name=fname
            user.last_name=lname
            user.save()
        
            user = authenticate(username=user.username, password=data['password1'])
            login(request, user)
            json['success'] = True
            

    else:
        errors = signup_form.errors
        if errors.get('username', False):
            if 'exists' in errors['username'][0]:
                json['username'] = 'exists'
            else:
                json['username'] = 'required'
        if errors.get('password1', False):
            json['password1'] = 'required'
        if errors.get('password2', False):
            if 'match' in errors['password2'][0]:
                json['password2'] = 'no_match'
            else:
                json['password2'] = 'required'
        
        errors = extra_validation(request.POST)
        if errors.get('email', False):
            json['email'] = 'invalid'
        if errors.get('name', False):
            json['name'] = 'required'

    return HttpResponse(dump(json), mimetype="application/json")


def extra_validation(data):
    errors = {}

    if not data.get('name', False):
        errors['name'] = 'missing'

    valid_email = email_re.match(data.get('username', ''))
    if not valid_email:
        errors['email'] = 'invalid'

    return errors
