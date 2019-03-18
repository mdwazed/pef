from django.contrib import admin
from django.urls import path, include
# from django.shortcuts import include

from . import views

app_name = 'siteman'

urlpatterns = [
    path('', views.home, name='home'),
    path('home_projekt', views.home_projekt, name='home_projekt'),
    path('projekt/', views.projekt, name='projekt'),
    path('haus/', views.haus, name='haus'),
    path('set_current_haus/<int:haus_id>/<slug:redirect>', views.set_current_haus, name='set_current_haus'),
    path('haus/delete/<int:pk>', views.haus_delete, name='haus_delete'), 
    path('haus_ubersicht', views.haus_ubersicht, name='haus_ubersicht'), 
    path('haus_wohnungen', views.haus_wohnungen, name='haus_wohnungen'), 

    path('haus_rohbau', views.haus_rohbau, name='haus_rohbau'), 
    path('haus_rohbau_update/<int:pk>', views.HausRohbauUpdateView.as_view(), name='haus_rohbau_update'), 
    path('haus_erdbau', views.haus_erdbau, name='haus_erdbau'), 
    path('haus_erdbau_update/<int:pk>', views.HausErdbauUpdateView.as_view(), name='haus_erdbau_update'),
    path('haus_dach', views.haus_dach, name='haus_dach'), 
    path('haus_dach_update/<int:pk>', views.HausDachUpdateView.as_view(), name='haus_dach_update'), 
    path('haus_fenster', views.haus_fenster, name='haus_fenster'), 
    path('haus_fenster_update/<int:pk>', views.HausFensterUpdateView.as_view(), name='haus_fenster_update'),
    path('haus_elektro', views.haus_elektro, name='haus_elektro'), 
    path('haus_elektro_update/<int:pk>', views.HausElektroUpdateView.as_view(), name='haus_elektro_update'),
    path('haus_sanitaer', views.haus_sanitaer, name='haus_sanitaer'), 
    path('haus_sanitaer_update/<int:pk>', views.HausSanitaerUpdateView.as_view(), name='haus_sanitaer_update'),
    path('haus_innenputz', views.haus_innenputz, name='haus_innenputz'), 
    path('haus_innenputz_update/<int:pk>', views.HausInnenputzUpdateView.as_view(), name='haus_innenputz_update'),
    path('haus_estrich', views.haus_estrich, name='haus_estrich'), 
    path('haus_estrich_update/<int:pk>', views.HausEstrichUpdateView.as_view(), name='haus_estrich_update'),
    path('haus_trockenbau', views.haus_trockenbau, name='haus_trockenbau'), 
    path('haus_trockenbau_update/<int:pk>', views.HausTrockenbauUpdateView.as_view(), name='haus_trockenbau_update'),
    path('haus_maler', views.haus_maler, name='haus_maler'), 
    path('haus_maler_update/<int:pk>', views.HausMalerUpdateView.as_view(), name='haus_maler_update'),
    path('haus_aussenputz', views.haus_aussenputz, name='haus_aussenputz'), 
    path('haus_aussenputz_update/<int:pk>', views.HausAussenputzUpdateView.as_view(), name='haus_aussenputz_update'),
    path('haus_fliesenleger', views.haus_fliesenleger, name='haus_fliesenleger'), 
    path('haus_fliesenleger_update/<int:pk>', views.HausFliesenlegerUpdateView.as_view(), name='haus_fliesenleger_update'),
    path('haus_bodenbelaege', views.haus_bodenbelaege, name='haus_bodenbelaege'), 
    path('haus_bodenbelaege_update/<int:pk>', views.HausBodenbelaegeUpdateView.as_view(), name='haus_bodenbelaege_update'),
    path('haus_schreiner', views.haus_schreiner, name='haus_schreiner'), 
    path('haus_schreiner_update/<int:pk>', views.HausSchreinerUpdateView.as_view(), name='haus_schreiner_update'),
    path('haus_schlosser', views.haus_schlosser, name='haus_schlosser'), 
    path('haus_schlosser_update/<int:pk>', views.HausSchlosserUpdateView.as_view(), name='haus_schlosser_update'),
    path('haus_schliessanlage', views.haus_schliessanlage, name='haus_schliessanlage'), 
    path('haus_schliessanlage_update/<int:pk>', views.HausSchliessanlageUpdateView.as_view(), name='haus_schliessanlage_update'),
    path('haus_sicherheitstechnik', views.haus_sicherheitstechnik, name='haus_sicherheitstechnik'), 
    path('haus_sicherheitstechnik_update/<int:pk>', views.HausSicherheitstechnikUpdateView.as_view(), name='haus_sicherheitstechnik_update'),
    path('haus_aussenanlagern', views.haus_aussenanlagern, name='haus_aussenanlagern'), 
    path('haus_aussenanlagern_update/<int:pk>', views.HausAussenanlagernUpdateView.as_view(), name='haus_aussenanlagern_update'),

    path('set_current_wohnung/<int:wohnung_id>', views.set_current_wohnung, name='set_current_wohnung'),
    path('wohnung/delete/<int:pk>', views.wohnung_delete, name='wohnung_delete'), 
    path('wohnung_ubersicht', views.wohnung_ubersicht, name='wohnung_ubersicht'), 
    path('wohnung_fenster', views.wohnung_fenster, name='wohnung_fenster'), 
    path('wohnung_fenster_update/<int:pk>', views.WohnungFensterUpdateView.as_view(), name='wohnung_fenster_update'),
    path('wohnung_elektro', views.wohnung_elektro, name='wohnung_elektro'), 
    path('wohnung_elektro_update/<int:pk>', views.WohnungElektroUpdateView.as_view(), name='wohnung_elektro_update'),
    path('wohnung_raumbuch_elektro', views.wohnung_raumbuch_elektro, name='wohnung_raumbuch_elektro'), 
    path('wohnung_raumbuch_elektro_update/<int:pk>', views.WohnungRaumbuchElektroUpdateView.as_view(), name='wohnung_raumbuch_elektro_update'),
    path('wohnung_sanitaer', views.wohnung_sanitaer, name='wohnung_sanitaer'), 
    path('wohnung_sanitaer_update/<int:pk>', views.WohnungSanitaerUpdateView.as_view(), name='wohnung_sanitaer_update'),









]
