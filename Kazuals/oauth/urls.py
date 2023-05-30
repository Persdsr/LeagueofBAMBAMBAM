
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.Logout, name='logout')
]
