# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect

def login_view(request):
    username = request.POST['nom']
    password = request.POST['mdp']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            messages.success(request, u'Tu as été connecté en tant que ' + username + u'. Bonnes péoulot.')
            return redirect('liste')
        else:
            messages.warning(request, u'Ce compte a été désactivé. Il faudra se connecter avec un autre compte')
            return redirect('login')
    else:
        messages.warning(request, u'Oh :o Tu t\'es trompé dans le mot de passe ou dans le nom d\'utilisateur.')
        return redirect('login')

def logout_view(request):
    logout(request)
    messages.info(request, u'Bye Bye, tu as été déconnecté.')
    return redirect('login')
