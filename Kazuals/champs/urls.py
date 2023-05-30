
from django.contrib import admin
from django.urls import path, include

from champs import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('champs/', views.ChampsView.as_view(), name='champs'),
    path('guide/<slug:guide_slug>/<slug:champion_id>/', views.ChampionBuild.as_view(), name='detail_guide'),
    path('champion/<slug:champion_slug>/', views.champion_info, name='champion_info'),
    path('build_create/', views.CreateBuild.as_view(), name='build_create')
]
