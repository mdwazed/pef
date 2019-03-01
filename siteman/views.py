from django.shortcuts import render
from django.http import HttpResponse

from .models import (Projekt, Haus, Wohnung,) 
from .forms import (ProjektForm, AddHausForm,)
from . import misc_functions, default_creator

# Create your views here.

def home(request):
    return render(request, 'siteman/home.html')

def home_projekt(request):
    """
    display project set in current session
    allow set another running project in surrent session
    """
    # set selected project in session var
    if request.method == "POST":
        selected_projekt_id = request.POST['selected_projekt']
        request.session['current_projekt_id'] = selected_projekt_id
    # get the current project from session var
    projekt =  misc_functions.get_current_projekt(request)
    # get all running project to display in select option   
    projekts = Projekt.objects.filter(projekt_status=True)
    context = {
    'projekt' : projekt,
    'projekts' : projekts,
    }
    return render(request, 'siteman/home_projekt.html', context)

def projekt(request):
    """
    Add/edit project related information.

    """
    projekt =  misc_functions.get_current_projekt(request)
    if request.method == 'POST':
        form = ProjektForm(request.POST, instance=projekt)
        if form.is_valid():
            form.save()
    if projekt:
        projekt_form = ProjektForm(instance=projekt)
    else:
        raise ValueError('Keine projekt selected!')

    context = {
    'form' : projekt_form,
    }
    return render(request, 'siteman/projekt.html', context)

def haus(request):
    """
    display list of haus associated with selected project
    add haus to a project with defalult values
    """

    if request.method == "POST":
        # print('posted')
        form = AddHausForm(request.POST)
        if form.is_valid():

            haus_nr = form.cleaned_data['haus_nr']
            display_nr = form.cleaned_data['display_nr']            
            projekt_id =  request.session['current_projekt_id']
            # 
            # get all selected options for default text generations
            # put them in dict and pass to the create default module 
            # 
            default_choices = {
            'haus_nr' : haus_nr,
            'display_nr' : display_nr,
            'projekt_id' : projekt_id,

            }
            # init_haus = Haus(haus_nr=haus_nr, display_nr=display_nr, projekt_id=projekt_id)
            #set defults values of all attributes of haus
            haus = default_creator.create_default_haus(default_choices)
            haus.save()

    projekt =  misc_functions.get_current_projekt(request)
    if not projekt:
        raise ValueError('Keine projekt selected!')
    hauser =  Haus.objects.filter(projekt=projekt).order_by('haus_nr')
    form = AddHausForm()
    context = {
    'projekt' : projekt,
    'hauser' : hauser,
    'form' : form,
    }         

    return render(request, 'siteman/haus.html', context)

def haus_delete(request, pk):
    """
    delete the corrasponsing house and all associated components of currently selected project.
    """

    return HttpResponse('delete this haus'+ str(pk))

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
# def gebaudeausrustung(request):
#     return render(request, 'siteman/rohinstallation.html')
def rohinstallation(request):
    return render(request, 'siteman/rohinstallation.html')
    # return HttpResponse('response returned')
def sanitarausstattung(request):
    return render(request, 'siteman/sanitarausstattung.html')
def elektroausstattung(request):
    return render(request, 'siteman/elektroausstattung.html')
def entluftung(request):
    return render(request, 'siteman/entluftung.html')
def aufzuge(request):
    return render(request, 'siteman/aufzuge.html')



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



