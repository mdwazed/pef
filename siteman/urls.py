from django.contrib import admin
from django.urls import path, include
# from django.shortcuts import include

from . import views

app_name = 'siteman'

urlpatterns = [
    path('', views.home, name='home'),
    path('home_projekt', views.home_projekt, name='home_projekt'),
    path('home_erganzung', views.home_erganzung, name='home_erganzung'),
    path('projekt/', views.projekt, name='projekt'),
    path('haus/', views.haus, name='haus'),
    path('set_current_haus/<int:haus_id>', views.set_current_haus, name='set_current_haus'),
    path('haus/delete/<int:pk>', views.haus_delete, name='haus_delete'), 
    path('haus_rohbau', views.haus_rohbau, name='haus_rohbau'), 
    path('haus_erdbau', views.haus_erdbau, name='haus_erdbau'), 
    path('haus_dach', views.haus_dach, name='haus_dach'), 
    path('haus_fenster', views.haus_fenster, name='haus_fenster'), 
    path('haus_elektro', views.haus_elektro, name='haus_elektro'), 
    path('haus_sanitaer', views.haus_sanitaer, name='haus_sanitaer'), 
    path('haus_innenputz', views.haus_innenputz, name='haus_innenputz'), 
    path('haus_estrich', views.haus_estrich, name='haus_estrich'), 
    path('haus_trockenbau', views.haus_trockenbau, name='haus_trockenbau'), 
    path('haus_maler', views.haus_maler, name='haus_maler'), 
    path('haus_aussenputz', views.haus_aussenputz, name='haus_aussenputz'), 
    path('haus_fliesenleger', views.haus_fliesenleger, name='haus_fliesenleger'), 
    path('haus_bodenbelaege', views.haus_bodenbelaege, name='haus_bodenbelaege'), 

    


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
    # path('gebaudeausrustung/', views.gebaudeausrustung, name='gebaudeausrustung'),
    path('rohinstallation/', views.rohinstallation, name='rohinstallation'),
    path('sanitarausstattung/', views.sanitarausstattung, name='sanitarausstattung'),
    path('elektroausstattung/', views.elektroausstattung, name='elektroausstattung'),
    path('entluftung/', views.entluftung, name='entluftung'),
    path('aufzuge/', views.aufzuge, name='aufzuge'),
]
