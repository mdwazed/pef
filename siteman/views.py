"""
main views to create db ORM
"""

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, ListView, UpdateView

from . import models, forms, misc_functions, default_creator
from .components import Haus_fl

import os


# Create your views here.

def home(request):
    return render(request, 'siteman/home.html')

def home_projekt(request):
    """
    display current project set in current session
    give option to set another running project in surrent session
    """
    # set selected project in session var if submitted
    if request.method == "POST":
        selected_projekt_id = request.POST['selected_projekt']
        request.session['current_projekt_id'] = selected_projekt_id
    # get the current project from session var
    projekt =  misc_functions.get_current_projekt(request)
    # get all running project to display in select option   
    projekts = models.Projekt.objects.filter(projekt_status=True) # status true means curently running projekt
    context = {
    'projekt' : projekt,
    'projekts' : projekts,
    }
    return render(request, 'siteman/home_projekt.html', context)

def projekt(request):
    """
    Add/edit project related information from projekt details page

    """
    projekt =  misc_functions.get_current_projekt(request)
    if request.method == 'POST':
        form = forms.ProjektForm(request.POST, instance=projekt)
        if form.is_valid():
            form.save()
    if projekt:
        projekt_form = forms.ProjektForm(instance=projekt)
    else:
        raise ValueError('Kein projekt selected!')

    context = {
    'form' : projekt_form,
    }
    return render(request, 'siteman/projekt.html', context)

"""
##############################################################################
#################### views related to haus only ##############################
##############################################################################
"""


def plans(request):
    """
    display all plans related to a haus 
    """
    haus = misc_functions.get_current_haus(request)
    # plans = get_list_or_404(models.Plan, haus=haus)
    plans = models.Plan.objects.filter(haus=haus)
    context = {
    'haus': haus,
    'plans': plans
    }
    return render(request,'siteman/haus/plans.html', context)

def upload_plan(request):
    haus = misc_functions.get_current_haus(request)

    if request.method == 'POST':
        
        form = forms.PlanUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            name = form.cleaned_data['name']
            components = form.cleaned_data['components']
            plan = request.FILES['plan']
            haus_pk = request.POST['haus']
            haus = get_object_or_404(models.Haus, pk=haus_pk)
            plan = models.Plan(haus=haus, name=name, components=components, plan=plan)
            plan.save()
            # return HttpResponse(request.FILES)
            return HttpResponseRedirect(reverse('siteman:plans'))
        else:
            return render(request, 'siteman/haus/plan_upload.html', {'form': form, 'haus': haus})
    form = forms.PlanUploadForm()
    context ={
    'form': form,
    'haus': haus,
    }
    return render(request, 'siteman/haus/plan_upload.html', context)

def haus(request):
    """
    display list of haus associated with selected project
    add haus to a project with defalult settings
    """

    if request.method == "POST":
        # print('posted')
        form = forms.AddHausForm(request.POST)
        # print(request.POST)  

        if form.is_valid():
            projekt_id =  request.session['current_projekt_id']
            haus_nr = form.cleaned_data['haus_nr']
            display_nr = form.cleaned_data['display_nr']            
            grundung = form.cleaned_data['grundung']
            aussenwande_eg_og_dg = form.cleaned_data['aussenwande_eg_og_dg']
            dach = form.cleaned_data['dach']
            fenster_beschattung = form.cleaned_data['fenster_beschattung']


            # 
            # get all selected options for default text generations
            # put them in dict and pass to the create default module 
            #in order to set the default values against each option.
            # 
            haus = models.Haus(haus_nr=haus_nr, display_nr=display_nr, projekt_id=projekt_id)
            haus.save()
            # key 'haus' determine in the default creator wheather the 'to be create' component is related to haus or not. 
            default_choices = {
            'haus' : haus,
            'grundung':grundung,
            'aussenwande_eg_og_dg':aussenwande_eg_og_dg,
            'dach':dach,
            'fenster_beschattung': fenster_beschattung,
            }
            #set defults values of all attributes of haus
            try:
                haus = default_creator.create_default_haus_components(default_choices)
                # save addl fields from default settings
                haus.save()
            except Exception as e:
                print('One or more haus components could not be created', e)    
            return HttpResponseRedirect(reverse('siteman:haus'))
        else:
            # print(forms.ValidationError)
            return render(request, 'siteman/haus.html', {'form':form})


    else:        
        projekt =  misc_functions.get_current_projekt(request)
        if not projekt:
            raise ValueError('Keine projekt selected!')
        hauser =  models.Haus.objects.filter(projekt=projekt).order_by('haus_nr')
        form = forms.AddHausForm()
        # print("-------creating unbounded add haus form------")
        context = {
        'projekt' : projekt,
        'hauser' : hauser,
        'form' : form,
        }         
        return render(request, 'siteman/haus.html', context)

def set_current_haus(request, haus_id, redirect):
    """
    set this haus as curent haus in the session var.
    redirect to rohbau page
    """
    request.session['current_haus_id'] = haus_id
    if redirect == 'ubersicht':
        return HttpResponseRedirect(reverse('siteman:haus_ubersicht'))
    elif redirect == 'wohnungen':
        return HttpResponseRedirect(reverse('siteman:haus_wohnungen'))

def haus_ubersicht(request):
    """
    display summary information of the selected haus
    """
    haus = misc_functions.get_current_haus(request)
    context = {
    'haus' : haus,
    }
    return render(request, 'siteman/haus/ubersicht.html', context)


def haus_wohnungen(request):
    """
    list all wohnung of current haus and
    add new wohnung to the haus
    """
    # remove any set wohnung from sesion.
    # prevent action on worng wohnung incase going back through back button in borwser
    misc_functions.remove_current_wohnung(request)

    haus = misc_functions.get_current_haus(request)
    wohnung_list = models.Wohnung.objects.filter(haus=haus)
    if request.method == 'POST':
        form = forms.AddWohnungForm(request.POST)
        if form.is_valid():
            wohnung_nr = form.cleaned_data['wohnung_nr']
            clients_name =form.cleaned_data['clients_name']
            clients_address =form.cleaned_data['clients_address']
            clients_email =form.cleaned_data['clients_email']
            clients_tel =form.cleaned_data['clients_tel']
            wohnung = models.Wohnung(haus=haus, wohnung_nr=wohnung_nr, clients_name=clients_name, clients_tel=clients_tel, clients_email=clients_email, clients_address=clients_address)
            wohnung.save()
            # key 'wohnung' detrmine whether to be create components is related to wohnung or not.
            default_choices = {
            'wohnung': wohnung,
            }

            try:
                wohnung = default_creator.create_default_wohnung_components(default_choices)
                # save addl fields from default settings
                wohnung.save()
            except Exception as e:
                print('One or more wohnung components could not be created', e)

    form = forms.AddWohnungForm()
    context = {
    'haus': haus,
    'wohnung_list': wohnung_list,
    'form':form,
    }
    return render(request, 'siteman/haus/wohnungen.html', context)

def haus_delete(request, pk):
    """
    delete the corrasponsing house and all associated components of currently selected project.
    """
    haus = get_object_or_404(models.Haus, pk=pk)
    try:
        haus.delete()
        return HttpResponseRedirect(reverse('siteman:haus'))
    except Exception as e:
        return HttpResponse("failed to delete objets" + str(e))


def haus_rohbau(request):
    """
    description of rohbau of currently selected haus 
    """
    haus = misc_functions.get_current_haus(request)

    context = {
    'haus' : haus,
    }
    return render(request, 'siteman/haus/rohbau.html', context)

class HausRohbauUpdateView(UpdateView):
    model = models.Rohbau
    template_name = 'siteman/haus/rohbau_update.html'
    form_class = forms.RohbauModelForm

    def get_success_url(self):
        return reverse('siteman:haus_rohbau')

def haus_erdbau(request):
    """
    erdbau views of currently selected haus
    """
    haus = misc_functions.get_current_haus(request)
    context = {
    'haus' : haus,
    }
    return render(request, 'siteman/haus/erdbau.html', context)

class HausErdbauUpdateView(UpdateView):
    model = models.Erdbau
    template_name = 'siteman/haus/erdbau_update.html'
    form_class = forms.ErdbauModelForm

    def get_success_url(self):
        return reverse('siteman:haus_erdbau')


def haus_dach(request):
    """
    erdbau views of currently selected haus
    """
    haus = misc_functions.get_current_haus(request)
    context = {
    'haus' : haus,
    }
    return render(request, 'siteman/haus/dach.html', context)

class HausDachUpdateView(UpdateView):
    model = models.Dach
    template_name = 'siteman/haus/dach_update.html'
    form_class = forms.DachModelForm

    def get_success_url(self):
        return reverse('siteman:haus_dach')

def haus_fenster(request):
    """
    erdbau views of currently selected haus
    """
    haus = misc_functions.get_current_haus(request)
    context = {
    'haus' : haus,
    }
    return render(request, 'siteman/haus/fenster.html', context)

class HausFensterUpdateView(UpdateView):
    model = models.Fenster
    template_name = 'siteman/haus/fenster_update.html'
    form_class = forms.FensterModelForm

    def get_success_url(self):
        return reverse('siteman:haus_fenster')

def haus_elektro(request):
    """
    erdbau views of currently selected haus
    """
    haus = misc_functions.get_current_haus(request)
    context = {
    'haus' : haus,
    }
    return render(request, 'siteman/haus/elektro.html', context)

class HausElektroUpdateView(UpdateView):
    model = models.Elektro
    template_name = 'siteman/haus/elektro_update.html'
    form_class = forms.ElektroModelForm

    def get_success_url(self):
        return reverse('siteman:haus_elektro')


def haus_sanitaer(request):
    """
    erdbau views of currently selected haus
    """
    haus = misc_functions.get_current_haus(request)
    context = {
    'haus' : haus,
    }
    return render(request, 'siteman/haus/sanitaer.html', context)

class HausSanitaerUpdateView(UpdateView):
    model = models.Sanitaer
    template_name = 'siteman/haus/sanitaer_update.html'
    form_class = forms.SanitaerModelForm

    def get_success_url(self):
        return reverse('siteman:haus_sanitaer')


def haus_innenputz(request):
    """
    erdbau views of currently selected haus
    """
    haus = misc_functions.get_current_haus(request)
    context = {
    'haus' : haus,
    }
    return render(request, 'siteman/haus/innenputz.html', context)

class HausInnenputzUpdateView(UpdateView):
    model = models.Innenputz
    template_name = 'siteman/haus/innenputz_update.html'
    form_class = forms.InnenputzModelForm

    def get_success_url(self):
        return reverse('siteman:haus_innenputz')

def haus_estrich(request):
    """
    erdbau views of currently selected haus
    """
    haus = misc_functions.get_current_haus(request)
    context = {
    'haus' : haus,
    }
    return render(request, 'siteman/haus/estrich.html', context)

class HausEstrichUpdateView(UpdateView):
    model = models.Estrich
    template_name = 'siteman/haus/estrich_update.html'
    form_class = forms.EstrichModelForm

    def get_success_url(self):
        return reverse('siteman:haus_estrich')

def haus_trockenbau(request):
    """
    erdbau views of currently selected haus
    """
    haus = misc_functions.get_current_haus(request)
    context = {
    'haus' : haus,
    }
    return render(request, 'siteman/haus/trockenbau.html', context)

class HausTrockenbauUpdateView(UpdateView):
    model = models.Trockenbau
    template_name = 'siteman/haus/trockenbau_update.html'
    form_class = forms.TrockenbauModelForm

    def get_success_url(self):
        return reverse('siteman:haus_trockenbau')

def haus_maler(request):
    """
    erdbau views of currently selected haus
    """
    haus = misc_functions.get_current_haus(request)
    context = {
    'haus' : haus,
    }
    return render(request, 'siteman/haus/maler.html', context)

class HausMalerUpdateView(UpdateView):
    model = models.Maler
    template_name = 'siteman/haus/maler_update.html'
    form_class = forms.MalerModelForm

    def get_success_url(self):
        return reverse('siteman:haus_maler')

def haus_aussenputz(request):
    """
    erdbau views of currently selected haus
    """
    haus = misc_functions.get_current_haus(request)
    context = {
    'haus' : haus,
    }
    return render(request, 'siteman/haus/aussenputz.html', context)

class HausAussenputzUpdateView(UpdateView):
    model = models.Aussenputz
    template_name = 'siteman/haus/aussenputz_update.html'
    form_class = forms.AussenputzModelForm

    def get_success_url(self):
        return reverse('siteman:haus_aussenputz')

def haus_fliesenleger(request):
    """
    erdbau views of currently selected haus
    """
    haus = misc_functions.get_current_haus(request)
    context = {
    'haus' : haus,
    }
    return render(request, 'siteman/haus/fliesenleger.html', context)

class HausFliesenlegerUpdateView(UpdateView):
    model = models.Fliesenleger
    template_name = 'siteman/haus/fliesenleger_update.html'
    form_class = forms.FliesenlegerModelForm

    def get_success_url(self):
        return reverse('siteman:haus_fliesenleger')

def haus_bodenbelaege(request):
    """
    erdbau views of currently selected haus
    """
    haus = misc_functions.get_current_haus(request)
    context = {
    'haus' : haus,
    }
    return render(request, 'siteman/haus/bodenbelaege.html', context)

class HausBodenbelaegeUpdateView(UpdateView):
    model = models.Bodenbelaege
    template_name = 'siteman/haus/bodenbelaege_update.html'
    form_class = forms.BodenbelaegeModelForm

    def get_success_url(self):
        return reverse('siteman:haus_bodenbelaege')

def haus_schreiner(request):
    """
    erdbau views of currently selected haus
    """
    haus = misc_functions.get_current_haus(request)
    context = {
    'haus' : haus,
    }
    return render(request, 'siteman/haus/schreiner.html', context)

class HausSchreinerUpdateView(UpdateView):
    model = models.Schreiner
    template_name = 'siteman/haus/schreiner_update.html'
    form_class = forms.SchreinerModelForm

    def get_success_url(self):
        return reverse('siteman:haus_schreiner')

def haus_schlosser(request):
    """
    erdbau views of currently selected haus
    """
    haus = misc_functions.get_current_haus(request)
    context = {
    'haus' : haus,
    }
    return render(request, 'siteman/haus/schlosser.html', context)

class HausSchlosserUpdateView(UpdateView):
    model = models.Schlosser
    template_name = 'siteman/haus/schlosser_update.html'
    form_class = forms.SchlosserModelForm

    def get_success_url(self):
        return reverse('siteman:haus_schlosser')

def haus_schliessanlage(request):
    """
    erdbau views of currently selected haus
    """
    haus = misc_functions.get_current_haus(request)
    context = {
    'haus' : haus,
    }
    return render(request, 'siteman/haus/schliessanlage.html', context)

class HausSchliessanlageUpdateView(UpdateView):
    model = models.Schliessanlage
    template_name = 'siteman/haus/schliessanlage_update.html'
    form_class = forms.SchliessanlageModelForm

    def get_success_url(self):
        return reverse('siteman:haus_schliessanlage')

def haus_sicherheitstechnik(request):
    """
    erdbau views of currently selected haus
    """
    haus = misc_functions.get_current_haus(request)
    context = {
    'haus' : haus,
    }
    return render(request, 'siteman/haus/sicherheitstechnik.html', context)

class HausSicherheitstechnikUpdateView(UpdateView):
    model = models.Sicherheitstechnik
    template_name = 'siteman/haus/sicherheitstechnik_update.html'
    form_class = forms.SicherheitstechnikModelForm

    def get_success_url(self):
        return reverse('siteman:haus_sicherheitstechnik')

def haus_aussenanlagern(request):
    """
    erdbau views of currently selected haus
    """
    haus = misc_functions.get_current_haus(request)
    context = {
    'haus' : haus,
    }
    return render(request, 'siteman/haus/aussenanlagern.html', context)

class HausAussenanlagernUpdateView(UpdateView):
    model = models.Aussenanlagern
    template_name = 'siteman/haus/aussenanlagern_update.html'
    form_class = forms.AussenanlagernModelForm

    def get_success_url(self):
        return reverse('siteman:haus_aussenanlagern')

"""
##############################################################################
###################  views related to wohnung ################################
##############################################################################
"""
def set_current_wohnung(request, wohnung_id):
    """
    set this wohnung as curent wohnung in the session var.
    redirect to wohnung ubersicht  page
    """
    # print(wohnung_id)
    request.session['current_wohnung_id'] = wohnung_id
    return HttpResponseRedirect(reverse('siteman:wohnung_ubersicht'))

def wohnung_plans(request):
    """
    display all plans related to a wohnung
    """
    wohnung = misc_functions.get_current_wohnung(request)
    # plans = get_list_or_404(models.Plan, haus=haus)
    plans = models.WohnungPlan.objects.filter(wohnung=wohnung)
    context = {
    'wohnung': wohnung,
    'plans': plans
    }
    return render(request,'siteman/wohnung/plans.html', context)

def upload_wohnung_plan(request, component):
    """
    upload wohnung related plan and image
    """
    wohnung = misc_functions.get_current_wohnung(request)

    if request.method == 'POST':
        
        form = forms.WohnungPlanUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            name = form.cleaned_data['name']
            # file_name, file_ext = os.path.splitext(name) 
            # print(file_name + file_ext)
            # if file_ext != 'pdf' or 

            components = form.cleaned_data['components']
            # components = component
            plan = request.FILES['plan']
            wohnung_pk = request.POST['wohnung']
            wohnung = get_object_or_404(models.Wohnung, pk=wohnung_pk)
            plan = models.WohnungPlan(wohnung=wohnung, name=name, components=components, plan=plan)
            plan.save()
            # return HttpResponse(request.FILES)
            return HttpResponseRedirect(reverse('siteman:wohnung_plans'))
        else:
            context ={
            'form': form,
            'wohnung': wohnung,
            'components': component,
            }
            return render(request, 'siteman/wohnung/plan_upload.html', context)

    form = forms.WohnungPlanUploadForm()
    context ={
    'form': form,
    'wohnung': wohnung,
    'components': component,
    }
    return render(request, 'siteman/wohnung/plan_upload.html', context)


def wohnung_delete(request, pk):
    """
    delete the corrasponsing wohnung and all associated components of currently selected haus.
    """
    wohnung = get_object_or_404(models.Wohnung, pk=pk)
    try:
        wohnung.delete()
        return HttpResponseRedirect(reverse('siteman:haus_wohnungen'))
    except Exception as e:
        return HttpResponse("failed to delete objets" + str(e))


def wohnung_ubersicht(request):
    """
    display summary information of the selected wohnung
    """
    wohnung = misc_functions.get_current_wohnung(request)
    context = {
    'wohnung' : wohnung,
    }
    return render(request, 'siteman/wohnung/ubersicht.html', context)

def wohnung_fenster(request):
    """
    display fenster information of the selected wohnung
    """
    wohnung = misc_functions.get_current_wohnung(request)
    plans = models.WohnungPlan.objects.filter(wohnung=wohnung)
    context = {
    'wohnung' : wohnung,
    'plans': plans,
    }
    return render(request, 'siteman/wohnung/fenster.html', context)

class WohnungFensterUpdateView(UpdateView):
    model = models.Fenster
    template_name = 'siteman/wohnung/fenster_update.html'
    form_class = forms.WohnungFensterModelForm

    def get_success_url(self):
        return reverse('siteman:wohnung_fenster')

def wohnung_elektro(request):
    """
    display elektro information of the selected wohnung
    """
    wohnung = misc_functions.get_current_wohnung(request)
    plans = models.WohnungPlan.objects.filter(wohnung=wohnung)
    context = {
    'wohnung' : wohnung,
    'plans': plans,
    }
    return render(request, 'siteman/wohnung/elektro.html', context)

class WohnungElektroUpdateView(UpdateView):
    model = models.Elektro
    template_name = 'siteman/wohnung/elektro_update.html'
    form_class = forms.WohnungElektroModelForm

    def get_success_url(self):
        return reverse('siteman:wohnung_elektro')

def wohnung_raumbuch_elektro(request):
    """
    display raumbuch elektro information of the selected wohnung
    """
    wohnung = misc_functions.get_current_wohnung(request)
    plans = models.WohnungPlan.objects.filter(wohnung=wohnung)
    context = {
    'wohnung' : wohnung,
    'plans': plans,
    }
    return render(request, 'siteman/wohnung/raumbuch_elektro.html', context)

class WohnungRaumbuchElektroUpdateView(UpdateView):
    model = models.Raumbuch_elektro
    template_name = 'siteman/wohnung/raumbuch_elektro_update.html'
    form_class = forms.WohnungRuambuchElektroModelForm

    def get_success_url(self):
        return reverse('siteman:wohnung_raumbuch_elektro')

def wohnung_sanitaer(request):
    """
    display sanitar information of the selected wohnung
    """
    wohnung = misc_functions.get_current_wohnung(request)
    plans = models.WohnungPlan.objects.filter(wohnung=wohnung)
    context = {
    'wohnung' : wohnung,
    'plans': plans,
    }
    return render(request, 'siteman/wohnung/sanitaer.html', context)

class WohnungSanitaerUpdateView(UpdateView):
    model = models.Sanitaer
    template_name = 'siteman/wohnung/sanitaer_update.html'
    form_class = forms.WohnungSanitaerModelForm

    def get_success_url(self):
        return reverse('siteman:wohnung_sanitaer')

def wohnung_innenputz(request):
    """
    display innenputz information of the selected wohnung
    """
    wohnung = misc_functions.get_current_wohnung(request)
    plans = models.WohnungPlan.objects.filter(wohnung=wohnung)
    context = {
    'wohnung' : wohnung,
    'plans': plans,
    }
    return render(request, 'siteman/wohnung/innenputz.html', context)

class WohnungInnenputzUpdateView(UpdateView):
    model = models.Innenputz
    template_name = 'siteman/wohnung/innenputz_update.html'
    form_class = forms.WohnungInnenputzModelForm

    def get_success_url(self):
        return reverse('siteman:wohnung_innenputz')

def wohnung_estrich(request):
    """
    display estrich information of the selected wohnung
    """
    wohnung = misc_functions.get_current_wohnung(request)
    plans = models.WohnungPlan.objects.filter(wohnung=wohnung)
    context = {
    'wohnung' : wohnung,
    'plans': plans,
    }
    return render(request, 'siteman/wohnung/estrich.html', context)

class WohnungEstrichUpdateView(UpdateView):
    model = models.Estrich
    template_name = 'siteman/wohnung/estrich_update.html'
    form_class = forms.WohnungEstrichModelForm

    def get_success_url(self):
        return reverse('siteman:wohnung_estrich')

def wohnung_trockenbau(request):
    """
    display trockenbau information of the selected wohnung
    """
    wohnung = misc_functions.get_current_wohnung(request)
    plans = models.WohnungPlan.objects.filter(wohnung=wohnung)
    context = {
    'wohnung' : wohnung,
    'plans': plans,
    }
    return render(request, 'siteman/wohnung/trockenbau.html', context)

class WohnungTrockenbauUpdateView(UpdateView):
    model = models.Trockenbau
    template_name = 'siteman/wohnung/trockenbau_update.html'
    form_class = forms.WohnungTrockenbauModelForm

    def get_success_url(self):
        return reverse('siteman:wohnung_trockenbau')

def wohnung_maler(request):
    """
    display maler information of the selected wohnung
    """
    wohnung = misc_functions.get_current_wohnung(request)
    plans = models.WohnungPlan.objects.filter(wohnung=wohnung)
    context = {
    'wohnung' : wohnung,
    'plans': plans,
    }
    return render(request, 'siteman/wohnung/maler.html', context)

class WohnungMalerUpdateView(UpdateView):
    model = models.Maler
    template_name = 'siteman/wohnung/maler_update.html'
    form_class = forms.WohnungMalerModelForm

    def get_success_url(self):
        return reverse('siteman:wohnung_maler')

def wohnung_fliesenleger(request):
    """
    display fliesenleger information of the selected wohnung
    """
    wohnung = misc_functions.get_current_wohnung(request)
    plans = models.WohnungPlan.objects.filter(wohnung=wohnung)
    context = {
    'wohnung' : wohnung,
    'plans': plans,
    }
    return render(request, 'siteman/wohnung/fliesenleger.html', context)

class WohnungFliesenlegerUpdateView(UpdateView):
    model = models.Fliesenleger
    template_name = 'siteman/wohnung/fliesenleger_update.html'
    form_class = forms.WohnungFliesenlegerModelForm

    def get_success_url(self):
        return reverse('siteman:wohnung_fliesenleger')

def wohnung_bodenbelaege(request):
    """
    display fliesenleger information of the selected wohnung
    """
    wohnung = misc_functions.get_current_wohnung(request)
    plans = models.WohnungPlan.objects.filter(wohnung=wohnung)
    context = {
    'wohnung' : wohnung,
    'plans': plans,
    }
    return render(request, 'siteman/wohnung/bodenbelaege.html', context)

class WohnungBodenbelaegeUpdateView(UpdateView):
    model = models.Bodenbelaege
    template_name = 'siteman/wohnung/bodenbelaege_update.html'
    form_class = forms.WohnungBodenbelaegeModelForm

    def get_success_url(self):
        return reverse('siteman:wohnung_bodenbelaege')

def wohnung_schreiner(request):
    """
    display schreiner/turen information of the selected wohnung
    """
    wohnung = misc_functions.get_current_wohnung(request)
    plans = models.WohnungPlan.objects.filter(wohnung=wohnung)
    context = {
    'wohnung' : wohnung,
    'plans': plans,
    }
    return render(request, 'siteman/wohnung/schreiner.html', context)

class WohnungSchreinerUpdateView(UpdateView):
    model = models.Schreiner
    template_name = 'siteman/wohnung/schreiner_update.html'
    form_class = forms.WohnungSchreinerModelForm

    def get_success_url(self):
        return reverse('siteman:wohnung_schreiner')

def wohnung_schlosser(request):
    """
    display schlosser information of the selected wohnung
    """
    wohnung = misc_functions.get_current_wohnung(request)
    plans = models.WohnungPlan.objects.filter(wohnung=wohnung)
    context = {
    'wohnung' : wohnung,
    'plans': plans,
    }
    return render(request, 'siteman/wohnung/schlosser.html', context)

class WohnungSchlosserUpdateView(UpdateView):
    model = models.Schlosser
    template_name = 'siteman/wohnung/schlosser_update.html'
    form_class = forms.WohnungSchlosserModelForm

    def get_success_url(self):
        return reverse('siteman:wohnung_schlosser')

def wohnung_schliessanlage(request):
    """
    display schliessanlage information of the selected wohnung
    """
    wohnung = misc_functions.get_current_wohnung(request)
    plans = models.WohnungPlan.objects.filter(wohnung=wohnung)
    context = {
    'wohnung' : wohnung,
    'plans': plans,
    }
    return render(request, 'siteman/wohnung/schliessanlage.html', context)

class WohnungSchliessanlageUpdateView(UpdateView):
    model = models.Schliessanlage
    template_name = 'siteman/wohnung/schliessanlage_update.html'
    form_class = forms.WohnungSchliessanlageModelForm

    def get_success_url(self):
        return reverse('siteman:wohnung_schliessanlage')