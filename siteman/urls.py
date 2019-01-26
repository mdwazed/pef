from django.contrib import admin
from django.urls import path, include
# from django.shortcuts import include

from . import views

app_name = 'siteman'

urlpatterns = [
    path('', views.home, name='home'),
    path('home_projekt', views.home_projekt, name='home_projekt'),
    path('home_erganzung', views.home_erganzung, name='home_erganzung'),
    path('project/', views.project, name='project'),
    path('haus/', views.haus, name='haus'),
    path('erg_haus/', views.erg_haus, name='erg_haus'),
    path('wohnung/', views.wohnung, name='wohnung'),
    path('erg_wohnung/', views.erg_wohnung, name='erg_wohnung'),
    path('rohbau/', views.rohbau, name='rohbau'),
    path('erg_rohbau/', views.erg_rohbau, name='erg_rohbau'),
    path('wande/', views.wande, name='wande'),
    path('erg_wande/', views.erg_wande, name='erg_wande'),
    path('abdictung/', views.abdictung, name='abdictung'),
    path('erg_abdictung/', views.erg_abdictung, name='erg_abdictung'),
    path('decken/', views.decken, name='decken'),
    path('erg_decken/', views.erg_decken, name='erg_decken'),
    path('versorgung/', views.versorgung, name='versorgung'),
    path('erg_versorgung/', views.erg_versorgung, name='erg_versorgung'),
    path('erweiterter/', views.erweiterter, name='erweiterter'),    
    path('erg_erweiterter/', views.erg_erweiterter, name='erg_erweiterter'),
    path('home_progress/', views.home_progress, name='home_progress'),
]
