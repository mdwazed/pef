"""
All froms of app siteman resides here
"""
# from django import forms
from django import forms
from django.contrib.admin import widgets 


from siteman.models import Projekt



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
        model = Projekt
        fields = ['projekt_name', 'projekt_addresse', 'projekt_stadt', 'projekt_nutzungstyp', 'projekt_anfangsdatum', 'projekt_enddatum', 'projekt_energetischer_standard', 'projekt_beschreibung',]
        widgets = {
            # 'projekt_beschreibung': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
            'projekt_anfangsdatum' : forms.SelectDateWidget(empty_label="-"),
            'projekt_enddatum' : forms.SelectDateWidget(empty_label="-"),
        }


class AddHausForm(forms.Form):
    haus_nr = forms.CharField(label='Haus Nr.', max_length=10)
    display_nr = forms.CharField(label='display Nr.', max_length=10)