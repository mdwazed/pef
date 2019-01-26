from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'siteman/home.html')

def home_projekt(request):
    return render(request, 'siteman/home_projekt.html')
def project(request):
    return render(request, 'siteman/project.html')
def haus(request):
    return render(request, 'siteman/haus.html')
def wohnung(request):
    return render(request, 'siteman/wohnung.html')
def rohbau(request):
    return render(request, 'siteman/rohbau.html')
def wande(request):
    return render(request, 'siteman/wande.html')
def abdictung(request):
    return render(request, 'siteman/abdictung.html')
def decken(request):
    return render(request, 'siteman/decken.html')
def versorgung(request):
    return render(request, 'siteman/versorgung.html')
def erweiterter(request):
    return render(request, 'siteman/erweiterter.html')


def home_erganzung(request):
    return render(request, 'siteman/home_erganzung.html')
def erg_haus(request):
    return render(request, 'siteman/erg_haus.html')
def erg_wohnung(request):
    return render(request, 'siteman/erg_wohnung.html') 
def erg_rohbau(request):
    return render(request, 'siteman/erg_rohbau.html')
def erg_wande(request):
    return render(request, 'siteman/erg_wande.html') 
def erg_abdictung(request):
    return render(request, 'siteman/erg_abdictung.html') 
def erg_decken(request):
    return render(request, 'siteman/erg_decken.html') 
def erg_versorgung(request):
    return render(request, 'siteman/erg_versorgung.html')
def erg_erweiterter(request):
    return render(request, 'siteman/erg_erweiterter.html')


def home_progress(request):
    return render(request, 'siteman/home_progress.html')



