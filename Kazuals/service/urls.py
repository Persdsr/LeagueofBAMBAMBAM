from django.urls import path
from . import views

urlpatterns = [
    path('splash_quize/', views.splash_quiz, name='splash_quiz'),
]