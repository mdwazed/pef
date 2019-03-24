"""
All froms of app siteman resides here
"""
# from django import forms
from django import forms
from django.contrib.admin import widgets 


from . import models



class ProjektForm(forms.ModelForm):
    """
    form to display and edit projects basic data
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['projekt_name'].widget.attrs.update({'class': 'special'})
        self.fields['projekt_name'].widget.attrs.update(size='80')
        self.fields['projekt_addresse'].widget.attrs.update(size='80')
        self.fields['projekt_stadt'].widget.attrs.update(size='80')
        self.fields['projekt_nutzungstyp'].widget.attrs.update(size='80')
        self.fields['projekt_energetischer_standard'].widget.attrs.update(size='20')
        self.fields['projekt_beschreibung'].widget.attrs.update(cols='80', rows='5')
        # self.fields['projekt_anfangsdatum'].widget = widgets.AdminDateWidget()

    class Meta:
        model = models.Projekt
        fields = ['projekt_name', 'projekt_addresse', 'projekt_stadt', 'projekt_nutzungstyp', 'projekt_anfangsdatum', 'projekt_enddatum', 'projekt_energetischer_standard', 'projekt_beschreibung',]
        widgets = {
            # 'projekt_beschreibung': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
            'projekt_anfangsdatum' : forms.SelectDateWidget(empty_label="-"),
            'projekt_enddatum' : forms.SelectDateWidget(empty_label="-"),
        }

class PlanUploadForm(forms.ModelForm):
    """
    upload pdf plan
    """
    # haus_qs = models.objects.filter(haus=haus)
    # haus = forms.ModelChoiceField(queryset=, widget=forms.HiddenInput())
    class Meta:
        model = models.Plan
        fields = ['name', 'components', 'plan',]

"""
########################################################################
########################  Haus Form ###################################
########################################################################
"""
class AddHausForm(forms.Form):
    """
    get choices options from models.choice field to generate custom 
    defalut text.
    """
    qs_grundung = models.ChoiceFields.objects.filter(option_type='gr')
    choices_grundung = [(x.option, x.display) for x in qs_grundung]
    qs_aussenwande_ab_eg = models.ChoiceFields.objects.filter(option_type='aw_eg_og_dg')
    choices_aussenwande_ab_eg = [(x.option, x.display) for x in qs_aussenwande_ab_eg]
    qs_dach = models.ChoiceFields.objects.filter(option_type='dach')
    choices_dach = [(x.option, x.display) for x in qs_dach]
    qs_fenster_beschattung = models.ChoiceFields.objects.filter(option_type='fenster_beschattung')
    choices_fenster_beschattung = [(x.option, x.display) for x in qs_fenster_beschattung]


    haus_nr = forms.CharField(label='Haus Nr.', max_length=10)
    display_nr = forms.CharField(label='Display Nr.', max_length=10)
    grundung = forms.ChoiceField(label='Grundung', choices=choices_grundung)
    aussenwande_eg_og_dg = forms.ChoiceField(label='Aussenwande ab EG', choices=choices_aussenwande_ab_eg)
    dach = forms.ChoiceField(label='Dach', choices=choices_dach)
    fenster_beschattung = forms.ChoiceField(label='Fenster Beschattung', choices=choices_fenster_beschattung)

    


class ErdbauModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['projekt_name'].widget.attrs.update({'class': 'special'})
        self.fields['erdbau'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Erdbau
        fields = ['erdbau', 'sonstiges', 'fundamentplan']
       
class RohbauModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['projekt_name'].widget.attrs.update({'class': 'special'})
        self.fields['grundung'].widget.attrs.update(cols='80', rows='5')
        self.fields['geschossdecken'].widget.attrs.update(cols='80', rows='5')
        self.fields['aussenwande_kellergeschoss'].widget.attrs.update(cols='80', rows='5')
        self.fields['aussenwande_eg_og_dg'].widget.attrs.update(cols='80', rows='5')
        self.fields['tragendeinnenwande'].widget.attrs.update(cols='80', rows='5')
        self.fields['nichttragendeinnenwande'].widget.attrs.update(cols='80', rows='5')
        self.fields['tiefgaragenrampe'].widget.attrs.update(cols='80', rows='5')
        self.fields['installationschachte'].widget.attrs.update(cols='80', rows='5')
        self.fields['dach'].widget.attrs.update(cols='80', rows='5')
        self.fields['treppen'].widget.attrs.update(cols='80', rows='5')
        self.fields['balkon'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Rohbau
        fields = ['grundung', 'geschossdecken', 'aussenwande_kellergeschoss', 'aussenwande_eg_og_dg',
        'tragendeinnenwande', 'nichttragendeinnenwande', 'tiefgaragenrampe', 'installationschachte', 'dach', 'treppen', 'balkon', 'sonstiges']

class DachModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['projekt_name'].widget.attrs.update({'class': 'special'})
        self.fields['dach'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Dach
        fields = ['dach', 'sonstiges']

class FensterModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['projekt_name'].widget.attrs.update({'class': 'special'})
        self.fields['algemeine_information'].widget.attrs.update(cols='80', rows='5')
        self.fields['beschattung'].widget.attrs.update(cols='80', rows='5')
        self.fields['kellergeschoss'].widget.attrs.update(cols='80', rows='5')
        self.fields['erdgeschoss'].widget.attrs.update(cols='80', rows='5')
        self.fields['regelgeschoss'].widget.attrs.update(cols='80', rows='5')
        self.fields['dachgeschoss'].widget.attrs.update(cols='80', rows='5')
        self.fields['treppenhaus'].widget.attrs.update(cols='80', rows='5')
        self.fields['tiefgarage'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Fenster
        fields = [ 'algemeine_information', 'beschattung','kellergeschoss', 'erdgeschoss', 'regelgeschoss', 'dachgeschoss', 'treppenhaus',
                    'tiefgarage', 'sonstiges']

class ElektroModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['projekt_name'].widget.attrs.update({'class': 'special'})
        self.fields['elektro'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Elektro
        fields = ['elektro', 'sonstiges']

class SanitaerModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['projekt_name'].widget.attrs.update({'class': 'special'})
        self.fields['heizung'].widget.attrs.update(cols='80', rows='5')
        self.fields['entwasserung'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Sanitaer
        fields = ['heizung', 'entwasserung', 'sonstiges' ]

class InnenputzModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['projekt_name'].widget.attrs.update({'class': 'special'})
        self.fields['innenputz_bad'].widget.attrs.update(cols='80', rows='5')
        self.fields['innenputz_wohnraueme'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Innenputz
        fields = ['innenputz_bad', 'innenputz_wohnraueme', 'sonstiges']

class EstrichModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['projekt_name'].widget.attrs.update({'class': 'special'})
        self.fields['daemmplatten'].widget.attrs.update(cols='80', rows='5')
        self.fields['estrich'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Estrich
        fields = ['daemmplatten', 'estrich', 'sonstiges' ]

class TrockenbauModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['projekt_name'].widget.attrs.update({'class': 'special'})
        self.fields['wande'].widget.attrs.update(cols='80', rows='5')
        self.fields['decken'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Trockenbau
        fields = ['wande', 'decken', 'sonstiges' ]

class MalerModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['projekt_name'].widget.attrs.update({'class': 'special'})
        self.fields['tapete'].widget.attrs.update(cols='80', rows='5')
        self.fields['farbe'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Maler
        fields = ['tapete', 'farbe', 'sonstiges' ]

class AussenputzModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['projekt_name'].widget.attrs.update({'class': 'special'})
        self.fields['aussenputz'].widget.attrs.update(cols='80', rows='5')
        self.fields['sockel'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Aussenputz
        fields = ['aussenputz', 'sockel', 'sonstiges' ]

class FliesenlegerModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['projekt_name'].widget.attrs.update({'class': 'special'})
        self.fields['treppenhaus'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Fliesenleger
        fields = ['treppenhaus', 'sonstiges']

class BodenbelaegeModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['projekt_name'].widget.attrs.update({'class': 'special'})
        self.fields['treppenhaus'].widget.attrs.update(cols='80', rows='5')
        self.fields['tiefgarage'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Bodenbelaege
        fields = ['treppenhaus', 'tiefgarage', 'sonstiges' ]

class SchreinerModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['projekt_name'].widget.attrs.update({'class': 'special'})
        self.fields['haustuer'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Schreiner
        fields = ['haustuer', 'sonstiges']

class SchlosserModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['eingangstuer'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Schlosser
        fields = ['eingangstuer', 'sonstiges']

class SchliessanlageModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['schliessplan'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Schliessanlage
        fields = ['schliessplan', 'sonstiges']

class SicherheitstechnikModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['alarmanlage'].widget.attrs.update(cols='80', rows='5')
        self.fields['tuerschliesser'].widget.attrs.update(cols='80', rows='5')
        self.fields['sicherheitsschloesser'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Sicherheitstechnik
        fields = ['alarmanlage', 'tuerschliesser', 'sicherheitsschloesser', 'sonstiges']

class AussenanlagernModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['terrassenbelaege'].widget.attrs.update(cols='80', rows='5')
        self.fields['pflanzen'].widget.attrs.update(cols='80', rows='5')
        self.fields['pflaster'].widget.attrs.update(cols='80', rows='5')
        self.fields['grundflache'].widget.attrs.update(cols='80', rows='5')
        self.fields['wegeflachen'].widget.attrs.update(cols='80', rows='5')
        self.fields['mulleinhausung'].widget.attrs.update(cols='80', rows='5')
        self.fields['einfriedung'].widget.attrs.update(cols='80', rows='5')
        self.fields['dachaufbau_tiefgarage_grundflache'].widget.attrs.update(cols='80', rows='5')
        self.fields['dachaufbau_tiefgarage_park_wegeflache'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Aussenanlagern
        fields = ['terrassenbelaege', 'pflanzen', 'pflaster', 'grundflache', 'wegeflachen', 'mulleinhausung', 'einfriedung',
         'dachaufbau_tiefgarage_grundflache', 'dachaufbau_tiefgarage_park_wegeflache', 'sonstiges']

"""
########################################################################
########################  Wohnung Form ###################################
########################################################################
"""
class AddWohnungForm(forms.Form):
    """
    get choices options from models.choice field to generate custom 
    defalut text.
    """
    wohnung_nr = forms.CharField(label='Haus Nr.', max_length=10)
    clients_name = forms.CharField(label='Clients Name', max_length=50, required=False)
    clients_address = forms.CharField(label='Clients Address', max_length=50, required=False)
    clients_email = forms.CharField(label='Clients Email', max_length=50, required=False)
    clients_tel = forms.CharField(label='Clients Tel', max_length=50, required=False)


class WohnungFensterModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fensterbaenke'].widget.attrs.update(cols='80', rows='5')
        self.fields['rolllaeden'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Fenster
        fields = ['fensterbaenke', 'rolllaeden', 'sonstiges']

class WohnungElektroModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['elektro'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Elektro
        fields = ['elektro', 'sonstiges']

class WohnungRuambuchElektroModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bad'].widget.attrs.update(cols='80', rows='7')
        self.fields['kueche'].widget.attrs.update(cols='80', rows='7')
        self.fields['flur'].widget.attrs.update(cols='80', rows='7')
        self.fields['wohnzimmer'].widget.attrs.update(cols='80', rows='7')
        self.fields['gaeste_wc'].widget.attrs.update(cols='80', rows='7')
        self.fields['schlafzimmer'].widget.attrs.update(cols='80', rows='7')
        self.fields['kinderzimmer'].widget.attrs.update(cols='80', rows='7')
        self.fields['abstellraum'].widget.attrs.update(cols='80', rows='7')
        self.fields['schalterprogramm'].widget.attrs.update(cols='80', rows='7')
        self.fields['tv_anschluss'].widget.attrs.update(cols='80', rows='7')
        self.fields['telefon_anschluss'].widget.attrs.update(cols='80', rows='7')
        self.fields['internet_anschluss'].widget.attrs.update(cols='80', rows='7')
    class Meta:
        model = models.Raumbuch_elektro
        fields = ['bad', 'kueche', 'flur', 'wohnzimmer', 'gaeste_wc', 'schlafzimmer',
        'kinderzimmer','abstellraum','schalterprogramm','tv_anschluss','telefon_anschluss','internet_anschluss']

class WohnungSanitaerModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['aussenzapfstelle'].widget.attrs.update(cols='80', rows='5')
        self.fields['dusche'].widget.attrs.update(cols='80', rows='5')
        self.fields['badewanne'].widget.attrs.update(cols='80', rows='5')
        self.fields['waschbecken'].widget.attrs.update(cols='80', rows='5')
        self.fields['toilette'].widget.attrs.update(cols='80', rows='5')
        self.fields['waschmaschinenanschluss'].widget.attrs.update(cols='80', rows='5')
        self.fields['spuele'].widget.attrs.update(cols='80', rows='5')
        self.fields['spuelmaschinenanschluss'].widget.attrs.update(cols='80', rows='5')
        self.fields['fussbodenheizung'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Sanitaer
        fields = ['aussenzapfstelle', 'dusche', 'badewanne', 'waschbecken', 'toilette',
        'waschmaschinenanschluss', 'spuele', 'spuelmaschinenanschluss', 'fussbodenheizung', 'sonstiges' ]

class WohnungInnenputzModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['innenputz_bad'].widget.attrs.update(cols='80', rows='5')
        self.fields['innenputz_wohnraueme'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Innenputz
        fields = ['innenputz_bad', 'innenputz_wohnraueme', 'sonstiges' ]

class WohnungEstrichModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['daemmplatten'].widget.attrs.update(cols='80', rows='5')
        self.fields['estrich'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Estrich
        fields = ['daemmplatten', 'estrich', 'sonstiges' ]

class WohnungTrockenbauModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['wande'].widget.attrs.update(cols='80', rows='5')
        self.fields['decken'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Trockenbau
        fields = ['wande', 'decken', 'sonstiges' ]

class WohnungMalerModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tapete'].widget.attrs.update(cols='80', rows='5')
        self.fields['farbe'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Maler
        fields = ['tapete', 'farbe', 'sonstiges' ]

class WohnungFliesenlegerModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bad'].widget.attrs.update(cols='80', rows='5')
        self.fields['wohnzimmer'].widget.attrs.update(cols='80', rows='5')
        self.fields['abstellraum'].widget.attrs.update(cols='80', rows='5')
        self.fields['esszimmer'].widget.attrs.update(cols='80', rows='5')
        self.fields['keller'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Fliesenleger
        fields = ['bad', 'wohnzimmer', 'abstellraum','esszimmer', 'keller', 'sonstiges']

class WohnungBodenbelaegeModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bad'].widget.attrs.update(cols='80', rows='5')
        self.fields['kueche'].widget.attrs.update(cols='80', rows='5')
        self.fields['flur'].widget.attrs.update(cols='80', rows='5')
        self.fields['wohnzimmer'].widget.attrs.update(cols='80', rows='5')
        self.fields['gaeste_wc'].widget.attrs.update(cols='80', rows='5')
        self.fields['schlafzimmer'].widget.attrs.update(cols='80', rows='5')
        self.fields['kinderzimmer'].widget.attrs.update(cols='80', rows='5')
        self.fields['abstellraum'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Bodenbelaege
        fields = ['bad', 'kueche', 'flur', 'wohnzimmer', 'gaeste_wc', 'schlafzimmer', 'kinderzimmer','abstellraum', 'sonstiges']

class WohnungSchreinerModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['wohnungstuer'].widget.attrs.update(cols='80', rows='5')
        self.fields['innentueren'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Schreiner
        fields = ['wohnungstuer', 'innentueren', 'sonstiges']

class WohnungSchlosserModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['wohnungstuer'].widget.attrs.update(cols='80', rows='5')
        self.fields['innentueren'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Schreiner
        fields = ['wohnungstuer', 'innentueren', 'sonstiges']

class WohnungSchliessanlageModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['schliessplan'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Schliessanlage
        fields = ['schliessplan', 'sonstiges']