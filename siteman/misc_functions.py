"""
All misc static functions goes here.
import this file whereever need any of this functions
"""
from django.shortcuts import get_object_or_404
from . models import Projekt, Haus, Wohnung


def get_current_projekt(request):
    """
    return the project obj which is currently set in the session
    """
    try:
        projekt_id = request.session['current_projekt_id']   
        projekt = Projekt.objects.get(pk=projekt_id)
    except KeyError:
        projekt = None
    return projekt 

def get_current_haus(request):
    """
    return the haus obj which is currently set in the session
    """
    haus = get_object_or_404(Haus, pk=request.session['current_haus_id'])
    # try:
    #     haus_id = request.session['current_haus_id']   
    #     haus = Haus.objects.get(pk=haus_id)
    # except KeyError:
    #     haus = None
    return haus


def get_current_wohnung(request):
    """
    return the wohnung obj which is currently set in the session
    """
    wohnung = get_object_or_404(Wohnung, pk=request.session['current_wohnung_id'])
    # try:
    #     wohnung_id = request.session['current_wohnung_id']   
    #     wohnung = Wohnung.objects.get(pk=wohnung_id)
    # except KeyError:
    #     wohnung = None
    return wohnung 

def remove_current_wohnung(request):
    """
    remove currently set wohnung from the session
    """
    request.session['current_wohnung_id'] = None

def remove_current_haus(request):
    """
    remove currently set haus from the session
    """
    request.session['current_haus_id'] = None

