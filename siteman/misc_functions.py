"""
All misc static functions goes here.
import this file whereever need any of this functions
"""

from .models import Projekt, Haus

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

