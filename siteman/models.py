from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Projekt(models.Model):
    """
    the projekt itself. may contian one or more haus/building.
    """
    projekt_name = models.CharField(max_length=200)
    projekt_addresse =  models.CharField(max_length=200, null=True, blank=True)
    projekt_stadt = models.CharField(max_length=50, null=True, blank=True)
    projekt_nutzungstyp = models.CharField(max_length=50, null=True, blank=True)
    projekt_anfangsdatum = models.DateField(null=True, blank=True)
    projekt_enddatum = models.DateField(null=True, blank=True)
    projekt_energetischer_standard = models.CharField(max_length=20, null=True, blank=True)
    projekt_beschreibung = models.TextField(null=True, blank=True)
    projekt_status = models.BooleanField(default=True) # true-> running projekt
    
    def __str__(self):
        return self.projekt_name


class Haus(models.Model):
    """
    Each building in the project. one project may have one or more of them.
    made up of many small components.  
    """
    projekt = models.ForeignKey(Projekt, on_delete=models.CASCADE)
    haus_nr = models.CharField(max_length=10)
    display_nr = models.CharField(max_length=10, null=True, blank=True)
    tiefgaragenbeschichtung = models.TextField(null=True, blank=True)
    trennwandsysteme = models.TextField(null=True, blank=True)
    klimatisierung = models.TextField(null=True, blank=True)
    aufzug = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.projekt) + ' - haus-' + self.haus_nr
    

class Wohnung(models.Model):
    wohnung_nr = models.CharField(max_length=20)
    haus = models.ForeignKey(Haus, on_delete=models.CASCADE)
    clients_name = models.CharField(max_length=100, null=True, blank=True)
    clients_address = models.CharField(max_length=150, null=True, blank=True)
    clients_email = models.CharField(max_length=50, null=True, blank=True)
    clients_tel = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.haus.projekt) + ' - haus-' + str(self.haus) + ' - wohnung' + self.wohnung_nr
    

class Verantwortung(models.Model):
    """
    table for responsibilty.
    an abstruct model.
    all work class will inherite to get the commom fields 
    """
    choices = (
        ('ns', 'Not yet started'),
        ('ru', 'Running'),
        ('co', 'Completed')
        )
    anfangsdatum = models.DateField(null=True, blank=True)
    enddatum = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=2, choices=choices, default='ns')
    class Meta:
        abstract = True


class ChoiceFields(models.Model):
    """
    all choice should come from this table
    """
    option_types = (
        ('sl', '--select--'),
        ('gw', 'gewerk'),
        ('st', 'status'),
        ('gr', 'grundung'),
        ('aw_eg_og_dg', 'aussenwande_eg_og_dg'),
        ('dach', 'dach'),
        ('fenster_beschattung', 'fenster_beschattung'),
        )
    option = models.CharField(max_length=5, unique=True, default='sl')
    display = models.CharField(max_length=50, default='--select--')
    option_type = models.CharField(max_length=50, choices= option_types)
    
    def __str__(self):
        return self.option +'-->'+ self.display +'--for--' + self.get_option_type_display()

    class Meta:
        ordering = ['option_type']

class Architekt_plan(models.Model):
    """
    all plan which will be uploaded to the system as pdf file.
    default saving location is media_root/plan_pdf
    ensure implimentation of cascade deletion of the file once the data on the database has been deleted
    for haus and wohnung
    """
    haus = models.OneToOneField(Haus, on_delete=models.CASCADE, null=True, blank=True)
    abstandsflaechenplan = models.FileField(null=True, upload_to='plan_pdf/', blank=True)
    ansichten_plan = models.FileField(null=True, upload_to='plan_pdf', blank=True)
    freiflaechenplan = models.FileField(null=True, upload_to='plan_pdf', blank=True)
    statik_plan = models.FileField(null=True, upload_to='plan_pdf', blank=True)
    brandschutzkonzept = models.FileField(null=True, upload_to='plan_pdf', blank=True)
    energieausweis = models.FileField(null=True, upload_to='plan_pdf', blank=True)
    sonstiges = models.TextField(null=True, blank=True)

class Erdbau(Verantwortung):
    """
    ground work 
    """
    haus = models.OneToOneField('Haus', on_delete=models.CASCADE, null=True, blank=True)
    erdbau = models.TextField(null=True, blank=True)
    fundamentplan = models.FileField(null=True, upload_to='plan_pdf', blank=True)
    sonstiges = models.TextField(null=True, blank=True)

    def __str__(self):
        return ("Erdbau" + str(self.haus))

class Rohbau(Verantwortung):
    """
    common rohbau related task
    """
    haus = models.OneToOneField(Haus, on_delete=models.CASCADE, null=True, blank=True)
    # bodenplatte = models.TextField(null=True, blank=True)
    grundung = models.TextField(null=True, blank=True)
    geschossdecken= models.TextField(null=True, blank=True)
    aussenwande_kellergeschoss = models.TextField(null=True, blank=True)
    aussenwande_eg_og_dg = models.TextField(null=True, blank=True)
    wohnungstrenwande = models.TextField(null=True, blank=True)
    tragendeinnenwande = models.TextField(null=True, blank=True)
    nichttragendeinnenwande = models.TextField(null=True, blank=True)
    horizontale_abdichtung = models.TextField(null=True, blank=True)
    vertikale_abdictung = models.TextField(null=True, blank=True)
    tiefgaragenrampe = models.TextField(null=True, blank=True)    
    treppen = models.TextField(null=True, blank=True)
    balkon = models.TextField(null=True, blank=True)
    sonstiges = models.TextField(null=True, blank=True)

class Dach(Verantwortung):
    """
    roof of the house
    """
    haus = models.OneToOneField(Haus, on_delete=models.CASCADE, null=True, blank=True)
    hauptdach = models.TextField(null= True, blank=True)
    dachterrassen = models.TextField(null= True, blank=True)
    spenglerarbeiten = models.TextField(null= True, blank=True)
    sonstiges = models.TextField(null=True, blank=True)


class Fenster(Verantwortung):
    """
    each column represents a particular type of window. 
    may become foreign key of a haus or wohnung

    """
    haus = models.OneToOneField(Haus, on_delete=models.CASCADE, null=True, blank=True)
    wohnung = models.OneToOneField(Wohnung, on_delete=models.CASCADE, null=True, blank=True)
    # for haus
    beschattung = models.TextField(null=True, blank=True)
    kellergeschoss = models.TextField(null=True, blank=True)
    erdgeschoss = models.TextField(null=True, blank=True)
    regelgeschoss = models.TextField(null=True, blank=True)
    dachgeschoss = models.TextField(null=True, blank=True)
    treppenhaus = models.TextField(null=True, blank=True)
    tiefgarage = models.TextField(null=True, blank=True)
    keller = models.TextField(null=True, blank=True)

    # for wohnung
    schwellen = models.TextField(null=True, blank=True)
    sichtschutz = models.TextField(null=True, blank=True)
    # common to both
    fensterbaenke = models.TextField(null=True, blank=True)
    sonstiges = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.haus is not None:
            return str(self.haus)
        else:
            return str(self.wohnung)

class Elektro(Verantwortung):
    """
    Electic connectin description of haus 
    will be ForeignKey of haus 
    """
    haus = models.OneToOneField(Haus, on_delete=models.CASCADE, null=True, blank=True)
    wohnung = models.OneToOneField(Wohnung, on_delete=models.CASCADE, null=True, blank=True)
    # haus
    elektro = models.TextField(null=True, blank=True)
    treppenhaus = models.TextField(null=True, blank=True)
    keller = models.TextField(null=True, blank=True)
    private_abstellraum = models.TextField(null=True, blank=True)
    tiefgarage = models.TextField(null=True, blank=True)
    medientechnik = models.TextField(null=True, blank=True)
    freiflachen = models.TextField(null=True, blank=True)
    # wohnung    
    allgemein = models.TextField(null=True, blank=True)  
    # common fro both
    sonstiges = models.TextField(null=True, blank=True)

class Sanitaer(Verantwortung):
    """
    sanitary requirements. related to wohnung only
    """
    haus = models.OneToOneField(Haus, on_delete=models.CASCADE, null=True, blank=True)
    wohnung = models.OneToOneField(Wohnung, on_delete=models.CASCADE, null=True, blank=True)
    # haus level

    # wohnung level
    aussenzapfstelle = models.TextField(null=True, blank=True)# 
    dusche = models.TextField(null=True, blank=True)
    badewanne = models.TextField(null=True, blank=True)
    waschtisch_im_bad = models.TextField(null=True, blank=True)
    toilette = models.TextField(null=True, blank=True)
    heizkorper = models.TextField(null=True, blank=True)
    waschtisch_im_duschbad_wc = models.TextField(null=True, blank=True)
    waschmaschinenanschluss = models.TextField(null=True, blank=True)
    spuelmaschinenanschluss = models.TextField(null=True, blank=True)
    # waschbecken = models.TextField(null=True, blank=True)
    # toilette = models.TextField(null=True, blank=True)
    
    # spuele = models.TextField(null=True, blank=True)
    
    # common to both
    # fussbodenheizung = models.TextField(null=True, blank=True)
    sonstiges = models.TextField(null=True, blank=True)


class Hls(Verantwortung):
    """
    Heitzung, luftung and sanitar. related to haus only
    """
    haus = models.OneToOneField(Haus, on_delete=models.CASCADE, null=True, blank=True)
    wohnung = models.OneToOneField(Wohnung, on_delete=models.CASCADE, null=True, blank=True)
    #  haus level
    energiegwinnung = models.TextField(null=True, blank=True)
    heizung = models.TextField(null=True, blank=True)
    be_und_entluftung = models.TextField(null=True, blank=True)
    verbauchserfassung = models.TextField(null=True, blank=True)
    klimatisierung = models.TextField(null=True, blank=True)
    kalt_und_warmwasser = models.TextField(null=True, blank=True)
    zirkulationsleitung = models.TextField(null=True, blank=True)
    entwasserung = models.TextField(null=True, blank=True)
    wasserenthartung = models.TextField(null=True, blank=True)
    # common to both
    sonstiges = models.TextField(null=True, blank=True)


class Innenputz(Verantwortung):
    """
    inner plaster
    may contian number of layers
    """
    haus = models.OneToOneField(Haus, on_delete=models.CASCADE, null=True, blank=True)
    wohnung = models.OneToOneField(Wohnung, on_delete=models.CASCADE, null=True, blank=True)
    # for haus
    innenputz_bad = models.TextField(null=True, blank=True)
    innenputz_wohnraueme = models.TextField(null=True, blank=True)
    innenputz_treppenhauswande = models.TextField(null=True, blank=True)
    innenputz_treppenhausdecken = models.TextField(null=True, blank=True)
    # wohnung
    edelputz_bad = models.TextField(null=True, blank=True)
    edelputz_wohnraume = models.TextField(null=True, blank=True)
    # common to both
    sonstiges = models.TextField(null=True, blank=True)

class Estrich(Verantwortung):
    """
    layer under the tiles
    """
    haus = models.OneToOneField(Haus, on_delete=models.CASCADE, null=True, blank=True)
    wohnung = models.OneToOneField(Wohnung, on_delete=models.CASCADE, null=True, blank=True)
    # for haus
    dammplatten = models.TextField(null=True, blank=True)
    wohnraume = models.TextField(null=True, blank=True)
    bader = models.TextField(null=True, blank=True)
    # wohnung
    fussbodenaufbau_wohnraume = models.TextField(null=True, blank=True)
    fussbodenaufbau_bad = models.TextField(null=True, blank=True)
    # common to both
    sonstiges = models.TextField(null=True, blank=True)

class Trockenbau(Verantwortung):
    """
    dry wall. additional layer of wall/floor/ceiling.
    will be foreign key of both haus and wohnung
    """
    haus = models.OneToOneField(Haus, on_delete=models.CASCADE, null=True, blank=True)
    wohnung = models.OneToOneField(Wohnung, on_delete=models.CASCADE, null=True, blank=True)
    # for haus
    installationsschachte = models.TextField(null=True, blank=True)
    # for wohnung
    
    # common to both
    wande = models.TextField(null=True, blank=True)
    decken = models.TextField(null=True, blank=True)
    vorsatzschalen = models.TextField(null=True, blank=True)
    sonstiges = models.TextField(null=True, blank=True)

class Maler(Verantwortung):
    """
    painting related description
    painting can be plain paint, wall paper, inside/outside
    """
    haus = models.OneToOneField(Haus, on_delete=models.CASCADE, null=True, blank=True)
    wohnung = models.OneToOneField(Wohnung, on_delete=models.CASCADE, null=True, blank=True)
    #for wohnung
    tapete = models.TextField(null=True, blank=True)
    farbe = models.TextField(null=True, blank=True)
    sonstiges = models.TextField(null=True, blank=True)

class Aussenputz(Verantwortung):
    """
    Outer plaster. applicable to haus only
    """
    haus = models.OneToOneField(Haus, on_delete=models.CASCADE, null=True, blank=True)
    unterputz = models.TextField(null=True, blank=True)
    edelputz = models.TextField(null=True, blank=True)
    sockel = models.TextField(null=True, blank=True)
    sonstiges = models.TextField(null=True, blank=True)

class Fliesenleger(Verantwortung):
    """
    tiles for the haus and wohnung
    """
    haus = models.OneToOneField(Haus, on_delete=models.CASCADE, null=True, blank=True)
    wohnung = models.OneToOneField(Wohnung, on_delete=models.CASCADE, null=True, blank=True)
    # for the haus
    treppenhaus = models.TextField(null=True, blank=True)
    # for the individual wohnung
    bad = models.TextField(null=True, blank=True)
    wohnzimmer = models.TextField(null=True, blank=True)
    abstellraum = models.TextField(null=True, blank=True)
    esszimmer = models.TextField(null=True, blank=True)
    keller = models.TextField(null=True, blank=True)
    sonstiges = models.TextField(null=True, blank=True)

class Bodenbelaege(Verantwortung):
    """
    floor cover for the haus and apartments
    """
    haus = models.OneToOneField(Haus, on_delete=models.CASCADE, null=True, blank=True)
    wohnung = models.OneToOneField(Wohnung, on_delete=models.CASCADE, null=True, blank=True)
    # for the building/ haus
    treppenhaus = models.TextField(null=True, blank=True)
    tiefgarage = models.TextField(null=True, blank=True)    
    keller = models.TextField(null=True, blank=True)    
    technikraum = models.TextField(null=True, blank=True)    

    # individual apartment/wohnung 
    bad = models.TextField(null=True, blank=True)
    kueche = models.TextField(null=True, blank=True)
    flur = models.TextField(null=True, blank=True)
    wohnzimmer = models.TextField(null=True, blank=True)
    gaeste_wc = models.TextField(null=True, blank=True)
    schlafzimmer = models.TextField(null=True, blank=True)
    kinderzimmer = models.TextField(null=True, blank=True)
    abstellraum = models.TextField(null=True, blank=True)
    # Common to both
    sonstiges = models.TextField(null=True, blank=True)

# class Schreiner(Verantwortung):
#     """
#     wood related work for haus and wohnung
#     addressed as turn somewhere
#     """
#     haus = models.OneToOneField(Haus, on_delete=models.CASCADE, null=True, blank=True)
#     wohnung = models.OneToOneField(Wohnung, on_delete=models.CASCADE, null=True, blank=True)
#     # haus level
#     haustuer = models.TextField(null=True, blank=True)
#     #  wohnung level
#     wohnungstuer = models.TextField(null=True, blank=True)
#     innentueren = models.TextField(null=True, blank=True)
#     sonstiges = models.TextField(null=True, blank=True)

class Turen(Verantwortung):
    """
    doors of haus and wohnung
    """
    haus = models.OneToOneField(Haus, on_delete=models.CASCADE, null=True, blank=True)
    wohnung = models.OneToOneField(Wohnung, on_delete=models.CASCADE, null=True, blank=True)
    # haus level
    haustuer = models.TextField(null=True, blank=True)
    brandschutzturen = models.TextField(null=True, blank=True)
    schleusenturen = models.TextField(null=True, blank=True)
    kellerflurturen = models.TextField(null=True, blank=True)
    #wohnung
    wohnungstur = models.TextField(null=True, blank=True)
    innenturen = models.TextField(null=True, blank=True)
    # common
    sonstiges = models.TextField(null=True, blank=True)
    



class Schlosser(Verantwortung):
    """
    lock standard for the haus and wohnung
    """
    haus = models.OneToOneField(Haus, on_delete=models.CASCADE, null=True, blank=True)
    wohnung = models.OneToOneField(Wohnung, on_delete=models.CASCADE, null=True, blank=True)
    # haus
    treppenglander = models.TextField(null=True, blank=True)
    balkongelander = models.TextField(null=True, blank=True)
    absturzsicherungen = models.TextField(null=True, blank=True)
    kellerabtrennungen = models.TextField(null=True, blank=True)
    rollgittertor = models.TextField(null=True, blank=True)
    # wohnung
    # wohnungstuer = models.TextField(null=True, blank=True)
    # innentueren = models.TextField(null=True, blank=True)
    # Common to both
    sonstiges = models.TextField(null=True, blank=True)

class Schliessanlage(Verantwortung):
    """
    door handle for haus and wohnung
    """
    haus = models.OneToOneField(Haus, on_delete=models.CASCADE, null=True, blank=True)
    wohnung = models.OneToOneField(Wohnung, on_delete=models.CASCADE, null=True, blank=True)
    # for haus
    schliessplan = models.TextField(null=True, blank=True)
    # innenbaenke = models.TextField(null=True, blank=True)
    # common to both
    sonstiges = models.TextField(null=True, blank=True)


class Sicherheitstechnik(Verantwortung):
    """
    sycurity system for haus and wohnung
    """
    haus = models.OneToOneField(Haus, on_delete=models.CASCADE, null=True, blank=True)
    wohnung = models.OneToOneField(Wohnung, on_delete=models.CASCADE, null=True, blank=True)
    # for haus
    alarmanlage = models.TextField(null=True, blank=True)
    videouberwachung = models.TextField(null=True, blank=True)
    sicherheitsschloesser = models.TextField(null=True, blank=True)
    # schliesssystem = models.FileField(null=True, upload_to='static/pdf', blank=True)
    # Common to both
    sonstiges = models.TextField(null=True, blank=True)


class Aussenanlagern(Verantwortung):
    """
    outside facilities of the haus. related to haus only
    """
    haus = models.OneToOneField(Haus, on_delete=models.CASCADE, null=True, blank=True)
    terrassenbelaege = models.TextField(null=True, blank=True)
    vegetationsflachen = models.TextField(null=True, blank=True)
    pflaster = models.TextField(null=True, blank=True)
    wegeflachen = models.TextField(null=True, blank=True)
    mulleinhausung = models.TextField(null=True, blank=True)
    einfriedung = models.TextField(null=True, blank=True)
    dachaufbau_tiefgarage_befestigt = models.TextField(null=True, blank=True)
    dachaufbau_tiefgarage_grun = models.TextField(null=True, blank=True)
    feuerwehraufstellflachen = models.TextField(null=True, blank=True)
    sonstiges = models.TextField(null=True, blank=True)


class Raumbuch_elektro(Verantwortung):
    """
    electric fitting per room
    ForeignKey of wohnung
    """
    wohnung = models.OneToOneField(Wohnung, on_delete=models.CASCADE, null=True, blank=True)
    bad = models.TextField(null=True, blank=True)
    kueche = models.TextField(null=True, blank=True)
    flur = models.TextField(null=True, blank=True)
    wohnzimmer = models.TextField(null=True, blank=True)
    gaeste_wc = models.TextField(null=True, blank=True)
    schlafzimmer = models.TextField(null=True, blank=True)
    kinderzimmer = models.TextField(null=True, blank=True)
    abstellraum = models.TextField(null=True, blank=True)
    schalterprogramm = models.TextField(null=True, blank=True)
    sonstiges = models.TextField(null=True, blank=True)


############ possible duplicate ########################
# class Choice_options(Verantwortung):
#     """
#     universal table for all choices of the system.
#     choice_type field determines which are the data will be visible for a particular choice.  
#     """
#     choice_option = models.CharField(max_length=100, blank=True)
#     choice_type = models.CharField(max_length=100, blank=True)



class Handwerker(models.Model):
    """
    working partner i.e. painter, plumber, electritian
    """
    unternehmen = models.CharField(max_length=200)
    anschrift = models.CharField(max_length=200, null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.unternehmen

class Plan(models.Model):
    """
    all pdf files related to haus goes here. 
    catagorised as per components like erdbau, roh bau etc.
    """
    component_tuple = (
            ('ar', 'Architeckt'),
            ('gp', 'Gesamtplanung'),
            ('eb', 'Erdbau'),
            ('rb', 'Rohbau'),
            ('fen', 'Fenster'),
            ('elek', 'Elektro'),
            ('sani', 'Sanitar'),
            ('flie', 'Fliesenleger'),
            ('boden', 'Bodenbelaege'),
            ('turen', 'Turen'),
            ('sanl', 'Schliessanlage'),
            ('aanl', 'Aussenanlage'),
        )
    haus = models.ForeignKey(Haus, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    components = models.CharField(max_length=50, choices=component_tuple)
    plan = models.FileField(null=True, upload_to='haus/plan_pdf/', blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg'])])

    def __str__(self):
        return self.name

class WohnungPlan(models.Model):
    """
    all pdf and images files related to wohnung goes here. 
    catagorised as per components and subcomponents like flisenlage_bad, raumbuch_elektro_kuche.
    """
    component_tuple = (
            ('ar', 'Architeckt'),
            ('eb', 'Erdbau'),
            ('rb', 'Rohbau'),
            ('fen', 'Fenster'),
            ('elek', 'Elektro'),
            ('sani', 'Sanitar'),
            ('flie', 'Fliesenleger'),
            ('boden', 'Bodenbelaege'),
            ('turen', 'Turen'),
            ('sanl', 'Schliessanlage'),
            ('aanl', 'Aussenanlage'),
            ('w_fb', 'wohnung Fensterbanke'),
        )
    wohnung = models.ForeignKey(Wohnung, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    components = models.CharField(max_length=50,)
    plan = models.FileField(null=True, upload_to='wohnung/plan_pdf/', blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg'])])

    def __str__(self):
        return self.name