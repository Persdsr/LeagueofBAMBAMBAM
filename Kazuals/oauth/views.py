import json

from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView

from champs.models import Build
from champs.service.items_on_db import get_all_items
from .forms import CustomUserCreationForm, LoginUserForm


class RegisterUser(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'oauth/register.html'


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'oauth/login.html'
    success_url = reverse_lazy('home')


def Logout(request):
    logout(request)
    return redirect('home')


