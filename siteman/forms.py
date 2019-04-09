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

"""
########################################################################
########################  Haus Form ###################################
########################################################################
"""


class PlanUploadForm(forms.ModelForm):
    """
    upload pdf plan for haus
    """
    # haus_qs = models.objects.filter(haus=haus)
    # haus = forms.ModelChoiceField(queryset=, widget=forms.HiddenInput())
    class Meta:
        model = models.Plan
        fields = ['name', 'components', 'plan',]


class AddHausForm(forms.Form):
    """
    get choices options from models.choice field to generate custom 
    defalut text.
    """
    haus_nr = forms.CharField(label='Haus Nr.', max_length=10)
    display_nr = forms.CharField(label='Display Nr.', max_length=10)
    grundung = forms.ChoiceField(label='Grundung')
    aussenwande_eg_og_dg = forms.ChoiceField(label='Aussenwande ab EG')
    dach = forms.ChoiceField(label='Dach')
    fenster_beschattung = forms.ChoiceField(label='Fenster Beschattung')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        qs_grundung = models.ChoiceFields.objects.filter(option_type='gr')
        choices_grundung = [(x.option, x.display) for x in qs_grundung]
        qs_aussenwande_ab_eg = models.ChoiceFields.objects.filter(option_type='aw_eg_og_dg')
        choices_aussenwande_ab_eg = [(x.option, x.display) for x in qs_aussenwande_ab_eg]
        qs_dach = models.ChoiceFields.objects.filter(option_type='dach')
        choices_dach = [(x.option, x.display) for x in qs_dach]
        qs_fenster_beschattung = models.ChoiceFields.objects.filter(option_type='fenster_beschattung')
        choices_fenster_beschattung = [(x.option, x.display) for x in qs_fenster_beschattung]
        # print(choices_grundung)

        self.fields['grundung'].choices = choices_grundung
        self.fields['aussenwande_eg_og_dg'].choices = choices_aussenwande_ab_eg
        self.fields['dach'].choices = choices_dach
        self.fields['fenster_beschattung'].choices = choices_fenster_beschattung



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
        self.fields['wohnungstrenwande'].widget.attrs.update(cols='80', rows='5')
        self.fields['tragendeinnenwande'].widget.attrs.update(cols='80', rows='5')
        self.fields['nichttragendeinnenwande'].widget.attrs.update(cols='80', rows='5')
        self.fields['horizontale_abdichtung'].widget.attrs.update(cols='80', rows='5')
        self.fields['vertikale_abdictung'].widget.attrs.update(cols='80', rows='5')
        self.fields['tiefgaragenrampe'].widget.attrs.update(cols='80', rows='5')
        self.fields['treppen'].widget.attrs.update(cols='80', rows='5')
        self.fields['balkon'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Rohbau
        fields = ['grundung', 'geschossdecken', 'aussenwande_kellergeschoss', 'aussenwande_eg_og_dg', 'wohnungstrenwande', 
        'tragendeinnenwande', 'nichttragendeinnenwande', 'horizontale_abdichtung', 'vertikale_abdictung', 'tiefgaragenrampe', 'treppen', 'balkon', 'sonstiges']

class DachModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['projekt_name'].widget.attrs.update({'class': 'special'})
        self.fields['hauptdach'].widget.attrs.update(cols='80', rows='5')
        self.fields['dachterrassen'].widget.attrs.update(cols='80', rows='5')
        self.fields['spenglerarbeiten'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Dach
        fields = ['hauptdach', 'dachterrassen', 'spenglerarbeiten','sonstiges']

class FensterModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['projekt_name'].widget.attrs.update({'class': 'special'})
        
        self.fields['kellergeschoss'].widget.attrs.update(cols='80', rows='5')
        self.fields['erdgeschoss'].widget.attrs.update(cols='80', rows='5')
        self.fields['regelgeschoss'].widget.attrs.update(cols='80', rows='5')
        self.fields['dachgeschoss'].widget.attrs.update(cols='80', rows='5')
        self.fields['treppenhaus'].widget.attrs.update(cols='80', rows='5')
        self.fields['tiefgarage'].widget.attrs.update(cols='80', rows='5')
        self.fields['beschattung'].widget.attrs.update(cols='80', rows='5')
        self.fields['fensterbaenke'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Fenster
        fields = [ 'kellergeschoss', 'erdgeschoss', 'regelgeschoss', 'dachgeschoss', 'treppenhaus',
                    'tiefgarage','beschattung', 'fensterbaenke', 'sonstiges']

class ElektroModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['projekt_name'].widget.attrs.update({'class': 'special'})
        self.fields['elektro'].widget.attrs.update(cols='80', rows='5')
        self.fields['treppenhaus'].widget.attrs.update(cols='80', rows='5')
        self.fields['keller'].widget.attrs.update(cols='80', rows='5')
        self.fields['private_abstellraum'].widget.attrs.update(cols='80', rows='5')
        self.fields['tiefgarage'].widget.attrs.update(cols='80', rows='5')
        self.fields['medientechnik'].widget.attrs.update(cols='80', rows='5')
        self.fields['freiflachen'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Elektro
        fields = ['elektro', 'treppenhaus', 'keller', 'private_abstellraum', 'tiefgarage', 'medientechnik', 'freiflachen', 'sonstiges']

class HlsModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['energiegwinnung'].widget.attrs.update(cols='80', rows='5')
        self.fields['heizung'].widget.attrs.update(cols='80', rows='5')
        self.fields['be_und_entluftung'].widget.attrs.update(cols='80', rows='5')
        self.fields['verbauchserfassung'].widget.attrs.update(cols='80', rows='5')
        self.fields['klimatisierung'].widget.attrs.update(cols='80', rows='5')
        self.fields['kalt_und_warmwasser'].widget.attrs.update(cols='80', rows='5')
        self.fields['zirkulationsleitung'].widget.attrs.update(cols='80', rows='5')
        self.fields['entwasserung'].widget.attrs.update(cols='80', rows='5')
        self.fields['wasserenthartung'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Hls
        fields = ['energiegwinnung', 'heizung', 'be_und_entluftung', 'verbauchserfassung', 'klimatisierung', 'kalt_und_warmwasser',
         'zirkulationsleitung', 'entwasserung', 'wasserenthartung', 'sonstiges']


# class SanitaerModelForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # self.fields['projekt_name'].widget.attrs.update({'class': 'special'})
#         self.fields['heizung'].widget.attrs.update(cols='80', rows='5')
#         self.fields['entwasserung'].widget.attrs.update(cols='80', rows='5')
#         self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
#     class Meta:
#         model = models.Sanitaer
#         fields = ['heizung', 'entwasserung', 'sonstiges' ]

class InnenputzModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['projekt_name'].widget.attrs.update({'class': 'special'})
        self.fields['innenputz_bad'].widget.attrs.update(cols='80', rows='5')
        self.fields['innenputz_wohnraueme'].widget.attrs.update(cols='80', rows='5')
        self.fields['innenputz_treppenhauswande'].widget.attrs.update(cols='80', rows='5')
        self.fields['innenputz_treppenhausdecken'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Innenputz
        fields = ['innenputz_bad', 'innenputz_wohnraueme', 'innenputz_treppenhauswande', 'innenputz_treppenhausdecken', 'sonstiges']

class EstrichModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['projekt_name'].widget.attrs.update({'class': 'special'})
        self.fields['dammplatten'].widget.attrs.update(cols='80', rows='5')
        self.fields['wohnraume'].widget.attrs.update(cols='80', rows='5')
        self.fields['bader'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Estrich
        fields = ['dammplatten', 'wohnraume', 'bader', 'sonstiges' ]

class TrockenbauModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['projekt_name'].widget.attrs.update({'class': 'special'})
        self.fields['installationsschachte'].widget.attrs.update(cols='80', rows='5')
        self.fields['wande'].widget.attrs.update(cols='80', rows='5')
        self.fields['decken'].widget.attrs.update(cols='80', rows='5')
        self.fields['vorsatzschalen'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Trockenbau
        fields = ['installationsschachte', 'wande', 'decken', 'vorsatzschalen', 'sonstiges' ]

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
        self.fields['unterputz'].widget.attrs.update(cols='80', rows='5')
        self.fields['edelputz'].widget.attrs.update(cols='80', rows='5')
        self.fields['sockel'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Aussenputz
        fields = ['unterputz', 'edelputz', 'sockel', 'sonstiges' ]

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
        self.fields['keller'].widget.attrs.update(cols='80', rows='5')
        self.fields['technikraum'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Bodenbelaege
        fields = ['treppenhaus', 'tiefgarage', 'keller', 'technikraum', 'sonstiges' ]

class turenModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['projekt_name'].widget.attrs.update({'class': 'special'})
        self.fields['haustuer'].widget.attrs.update(cols='80', rows='5')
        self.fields['brandschutzturen'].widget.attrs.update(cols='80', rows='5')
        self.fields['schleusenturen'].widget.attrs.update(cols='80', rows='5')
        self.fields['kellerflurturen'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Turen
        fields = ['haustuer', 'brandschutzturen', 'schleusenturen', 'kellerflurturen', 'sonstiges']


# class SchreinerModelForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # self.fields['projekt_name'].widget.attrs.update({'class': 'special'})
#         self.fields['haustuer'].widget.attrs.update(cols='80', rows='5')
#         self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
#     class Meta:
#         model = models.Schreiner
#         fields = ['haustuer', 'sonstiges']

class SchlosserModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['treppenglander'].widget.attrs.update(cols='80', rows='5')
        self.fields['balkongelander'].widget.attrs.update(cols='80', rows='5')
        self.fields['absturzsicherungen'].widget.attrs.update(cols='80', rows='5')
        self.fields['kellerabtrennungen'].widget.attrs.update(cols='80', rows='5')
        self.fields['rollgittertor'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Schlosser
        fields = ['treppenglander', 'balkongelander', 'absturzsicherungen', 'kellerabtrennungen', 'rollgittertor', 'sonstiges']

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
        self.fields['videouberwachung'].widget.attrs.update(cols='80', rows='5')
        self.fields['sicherheitsschloesser'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Sicherheitstechnik
        fields = ['alarmanlage', 'videouberwachung', 'sicherheitsschloesser', 'sonstiges']

class AussenanlagernModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['terrassenbelaege'].widget.attrs.update(cols='80', rows='5')
        self.fields['vegetationsflachen'].widget.attrs.update(cols='80', rows='5')
        self.fields['pflaster'].widget.attrs.update(cols='80', rows='5')
        self.fields['wegeflachen'].widget.attrs.update(cols='80', rows='5')
        self.fields['mulleinhausung'].widget.attrs.update(cols='80', rows='5')
        self.fields['einfriedung'].widget.attrs.update(cols='80', rows='5')
        self.fields['dachaufbau_tiefgarage_befestigt'].widget.attrs.update(cols='80', rows='5')
        self.fields['dachaufbau_tiefgarage_grun'].widget.attrs.update(cols='80', rows='5')
        self.fields['feuerwehraufstellflachen'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Aussenanlagern
        fields = ['terrassenbelaege', 'vegetationsflachen', 'pflaster', 'wegeflachen', 'mulleinhausung', 'einfriedung',
         'dachaufbau_tiefgarage_befestigt', 'dachaufbau_tiefgarage_grun', 'feuerwehraufstellflachen', 'sonstiges']

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

class WohnungPlanUploadForm(forms.ModelForm):
    """
    upload pdf plan for haus
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['components'].widget = forms.HiddenInput()
    class Meta:
        model = models.WohnungPlan
        fields = ['name', 'components', 'plan',]

class WohnungFensterModelForm(forms.ModelForm):
    """
    ACHTUNG: uploaded file objects for this fields refer to this objects by prefix-fieldname 
    as html name. Be very careful before changing the preifx and html name attributes of any field.
    """

    prefix = 'fenster'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['schwellen'].widget.attrs.update(cols='80', rows='5')
        self.fields['sichtschutz'].widget.attrs.update(cols='80', rows='5')
        self.fields['fensterbaenke'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
        
    class Meta:
        model = models.Fenster
     
        fields = ['schwellen', 'sichtschutz', 'fensterbaenke', 'sonstiges']


class WohnungElektroModelForm(forms.ModelForm):
    """
    ACHTUNG: uploaded file objects for this fields refer to this objects by prefix-fieldname 
    as html name. Be very careful before changing the preifx and html name attributes of any field.
    """

    prefix = 'elektro'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['elektro'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Elektro
        fields = ['elektro', 'sonstiges']

class WohnungRuambuchElektroModelForm(forms.ModelForm):
    """
    ACHTUNG: uploaded file objects for this fields refer to this objects by prefix-fieldname 
    as html name. Be very careful before changing the preifx and html name attributes of any field.
    """

    prefix = 'raumbuch_elektro'
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
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='7')
        
    class Meta:
        model = models.Raumbuch_elektro
        fields = ['bad', 'kueche', 'flur', 'wohnzimmer', 'gaeste_wc', 'schlafzimmer',
        'kinderzimmer','abstellraum','schalterprogramm', 'sonstiges']

class WohnungSanitaerModelForm(forms.ModelForm):
    """
    ACHTUNG: uploaded file objects for this fields refer to this objects by prefix-fieldname 
    as html name. Be very careful before changing the preifx and html name attributes of any field.
    """

    prefix = 'sanitaer'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['aussenzapfstelle'].widget.attrs.update(cols='80', rows='5')
        self.fields['dusche'].widget.attrs.update(cols='80', rows='5')
        self.fields['badewanne'].widget.attrs.update(cols='80', rows='5')
        self.fields['waschtisch_im_bad'].widget.attrs.update(cols='80', rows='5')
        self.fields['toilette'].widget.attrs.update(cols='80', rows='5')
        self.fields['heizkorper'].widget.attrs.update(cols='80', rows='5')
        self.fields['waschtisch_im_duschbad_wc'].widget.attrs.update(cols='80', rows='5')
        self.fields['waschmaschinenanschluss'].widget.attrs.update(cols='80', rows='5')
        self.fields['spuelmaschinenanschluss'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Sanitaer
        fields = ['aussenzapfstelle', 'dusche', 'badewanne', 'waschtisch_im_bad', 'toilette',
        'heizkorper', 'waschtisch_im_duschbad_wc', 'waschmaschinenanschluss', 'spuelmaschinenanschluss', 'sonstiges' ]

class WohnungInnenputzModelForm(forms.ModelForm):
    """
    ACHTUNG: uploaded file objects for this fields refer to this objects by prefix-fieldname 
    as html name. Be very careful before changing the preifx and html name attributes of any field.
    """

    prefix = 'innenputz'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['innenputz_bad'].widget.attrs.update(cols='80', rows='5')
        self.fields['innenputz_wohnraueme'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Innenputz
        fields = ['innenputz_bad', 'innenputz_wohnraueme', 'sonstiges' ]

class WohnungEstrichModelForm(forms.ModelForm):
    """
    ACHTUNG: uploaded file objects for this fields refer to this objects by prefix-fieldname 
    as html name. Be very careful before changing the preifx and html name attributes of any field.
    """

    prefix = 'estrich'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dammplatten'].widget.attrs.update(cols='80', rows='5')
        # self.fields['estrich'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Estrich
        fields = ['dammplatten', 'sonstiges' ]

class WohnungTrockenbauModelForm(forms.ModelForm):
    """
    ACHTUNG: uploaded file objects for this fields refer to this objects by prefix-fieldname 
    as html name. Be very careful before changing the preifx and html name attributes of any field.
    """

    prefix = 'trockenbau'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['wande'].widget.attrs.update(cols='80', rows='5')
        self.fields['decken'].widget.attrs.update(cols='80', rows='5')
        self.fields['vorsatzschalen'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Trockenbau
        fields = ['wande', 'decken', 'vorsatzschalen', 'sonstiges' ]

class WohnungMalerModelForm(forms.ModelForm):
    """
    ACHTUNG: uploaded file objects for this fields refer to this objects by prefix-fieldname 
    as html name. Be very careful before changing the preifx and html name attributes of any field.
    """

    prefix = 'maler'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tapete'].widget.attrs.update(cols='80', rows='5')
        self.fields['farbe'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Maler
        fields = ['tapete', 'farbe', 'sonstiges' ]

class WohnungFliesenlegerModelForm(forms.ModelForm):
    """
    ACHTUNG: uploaded file objects for this fields refer to this objects by prefix-fieldname 
    as html name. Be very careful before changing the preifx and html name attributes of any field.
    """

    prefix = 'fliesenleger'
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
    """
    ACHTUNG: uploaded file objects for this fields refer to this objects by prefix-fieldname 
    as html name. Be very careful before changing the preifx and html name attributes of any field.
    """

    prefix = 'bodenbelaege'
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

class WohnungTurenModelForm(forms.ModelForm):
    """
    ACHTUNG: uploaded file objects for this fields refer to this objects by prefix-fieldname 
    as html name. Be very careful before changing the preifx and html name attributes of any field.
    """

    prefix = 'turen'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['wohnungstur'].widget.attrs.update(cols='80', rows='5')
        self.fields['innenturen'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Turen
        fields = ['wohnungstur', 'innenturen', 'sonstiges']

class WohnungSchlosserModelForm(forms.ModelForm):
    """
    ACHTUNG: uploaded file objects for this fields refer to this objects by prefix-fieldname 
    as html name. Be very careful before changing the preifx and html name attributes of any field.
    """

    prefix = 'schlosser'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['wohnungstuer'].widget.attrs.update(cols='80', rows='5')
        # self.fields['innentueren'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Schlosser
        fields = ['sonstiges']

class WohnungSchliessanlageModelForm(forms.ModelForm):
    """
    ACHTUNG: uploaded file objects for this fields refer to this objects by prefix-fieldname 
    as html name. Be very careful before changing the preifx and html name attributes of any field.
    """

    prefix = 'schliessanlage'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['schliessplan'].widget.attrs.update(cols='80', rows='5')
        self.fields['sonstiges'].widget.attrs.update(cols='80', rows='5')
    class Meta:
        model = models.Schliessanlage
        fields = ['schliessplan', 'sonstiges']