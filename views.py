# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView

def home(request):
    if request.user.is_authenticated():
        return redirect('liste')
    else:
        return render_to_response('login.html', {
            'pageTitle' : 'Log In',
        }, context_instance=RequestContext(request))

def login_view(request):
    username = request.POST.get('nom')
    password = request.POST.get('mdp')
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        messages.success(request, u'Tu as été connecté en tant que ' + username + u'. Bonnes péoulot.')
    else:
        messages.warning(request, u'Oh :o Tu t\'es trompé dans le mot de passe ou dans le nom d\'utilisateur.')
    return redirect('login')

def logout_view(request):
    logout(request)
    messages.info(request, u'Bye Bye, tu as été déconnecté.')
    return redirect('login')
