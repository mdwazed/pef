from django.db import models

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
    architekt_plan = models.OneToOneField('Architekt_plan', on_delete=models.CASCADE, null=True, blank=True)
    erdbau = models.OneToOneField('Erdbau', on_delete=models.CASCADE, null=True, blank=True)
    rohbau = models.OneToOneField('Rohbau', on_delete=models.CASCADE, null=True, blank=True)
    dach = models.OneToOneField('Dach', on_delete=models.CASCADE, null=True, blank=True)
    fenster = models.OneToOneField('Fenster', on_delete=models.CASCADE, null=True, blank=True)
    elektro = models.OneToOneField('Elektro', on_delete=models.CASCADE, null=True, blank=True)
    sanitaer = models.OneToOneField('Sanitaer', on_delete=models.CASCADE, null=True, blank=True)
    innenputz = models.OneToOneField('Innenputz', on_delete=models.CASCADE, null=True, blank=True)
    estrich = models.OneToOneField('Estrich', on_delete=models.CASCADE, null=True, blank=True)
    trockenbau = models.OneToOneField('Trockenbau', on_delete=models.CASCADE, null=True, blank=True)
    maler = models.OneToOneField('Maler', on_delete=models.CASCADE, null=True, blank=True)
    aussenputz = models.OneToOneField('Aussenputz', on_delete=models.CASCADE, null=True, blank=True)
    fliesenleger = models.OneToOneField('Fliesenleger', on_delete=models.CASCADE, null=True, blank=True)
    bodenbelaege = models.OneToOneField('Bodenbelaege', on_delete=models.CASCADE, null=True, blank=True)
    schreiner = models.OneToOneField('Schreiner', on_delete=models.CASCADE, null=True, blank=True)
    schlosser = models.OneToOneField('Schlosser', on_delete=models.CASCADE, null=True, blank=True)
    schliessanlage = models.OneToOneField('Schliessanlage', on_delete=models.CASCADE, null=True, blank=True)
    tiefgaragenbeschichtung = models.TextField(null=True, blank=True)
    trennwandsysteme = models.TextField(null=True, blank=True)
    klimatisierung = models.TextField(null=True, blank=True)
    sicherheitstechnik = models.OneToOneField('Sicherheitstechnik', on_delete=models.CASCADE, null=True, blank=True)    
    aufzug = models.OneToOneField('aufzug', on_delete=models.CASCADE, null=True, blank=True)
    aussenanlagern = models.OneToOneField('Aussenanlagern', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.projekt) + ' - haus-' + self.haus_nr
    

class Wohnung(models.Model):
    wohnung_nr = models.CharField(max_length=20)
    haus = models.ForeignKey(Haus, on_delete=models.CASCADE)
    fenster = models.OneToOneField('Fenster', on_delete=models.CASCADE, null=True, blank=True)
    elektro = models.OneToOneField('Elektro', on_delete=models.CASCADE, null=True, blank=True)
    sanitaer = models.OneToOneField('Sanitaer', on_delete=models.CASCADE, null=True, blank=True)
    estrich = models.OneToOneField('Estrich', on_delete=models.CASCADE, null=True, blank=True)
    trockenbau = models.OneToOneField('Trockenbau', on_delete=models.CASCADE, null=True, blank=True)
    maler = models.OneToOneField('Maler', on_delete=models.CASCADE, null=True, blank=True)
    fliesenleger = models.OneToOneField('Fliesenleger', on_delete=models.CASCADE, null=True, blank=True)    
    bodenbelaege = models.OneToOneField('Bodenbelaege', on_delete=models.CASCADE, null=True, blank=True)
    schreiner = models.OneToOneField('Schreiner', on_delete=models.CASCADE, null=True, blank=True)
    schlosser = models.OneToOneField('Schlosser', on_delete=models.CASCADE, null=True, blank=True)
    schliessanlage = models.OneToOneField('Schliessanlage', on_delete=models.CASCADE, null=True, blank=True)
    sicherheitstechnik = models.OneToOneField('Sicherheitstechnik', on_delete=models.CASCADE, null=True, blank=True)    
    raumbuch_elektro = models.OneToOneField('Raumbuch_elektro', on_delete=models.CASCADE, null=True, blank=True)

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

class Choice(models.Model):
    """
    all choice should come from this table
    """
    option_types = (
        ('', '-----select-----'),
        ('gw', 'Gewerk'),
        ('st', 'Status'),
        )
    option = models.CharField(max_length=50)
    option_type = models.CharField(max_length=50, choices= option_types)


class Architekt_plan(models.Model):
    """
    all plan which will be uploaded to the system as pdf file.
    default saving location is media_root/plan_pdf
    ensure implimentation of cascade deletion of the file once the data on the database has been deleted
    for haus and wohnung
    """
    abstandsflaechenplan = models.FileField(null=True, upload_to='plan_pdf/', blank=True)
    ansichten_plan = models.FileField(null=True, upload_to='plan_pdf', blank=True)
    freiflaechenplan = models.FileField(null=True, upload_to='plan_pdf', blank=True)
    statik_plan = models.FileField(null=True, upload_to='plan_pdf', blank=True)
    brandschutzkonzept = models.FileField(null=True, upload_to='plan_pdf', blank=True)
    energieausweis = models.FileField(null=True, upload_to='plan_pdf', blank=True)

class Rohbau(Verantwortung):
    """
    common rohbau related task
    """
    bodenplatte = models.TextField(null=True, blank=True)
    geschossdecken= models.TextField(null=True, blank=True)
    aussenwaende = models.TextField(null=True, blank=True)
    tiefgaragenrampe = models.TextField(null=True, blank=True)
    tragendewaende = models.TextField(null=True, blank=True)
    innenwaende = models.TextField(null=True, blank=True)
    nichttragendewaende = models.TextField(null=True, blank=True)
    dach = models.TextField(null=True, blank=True)
    treppen = models.TextField(null=True, blank=True)
    balkon = models.TextField(null=True, blank=True)


class Fenster(Verantwortung):
    """
    each column represents a particular type of window. 
    may become foreign key of a haus or wohnung

    """
    # for haus
    kellergeschoss = models.TextField(null=True, blank=True)
    erdgeschoss = models.TextField(null=True, blank=True)
    regelgeschoss = models.TextField(null=True, blank=True)
    dachgeschoss = models.TextField(null=True, blank=True)
    treppenhaus = models.TextField(null=True, blank=True)
    tiefgarage = models.TextField(null=True, blank=True)

    # for wohnung
    fensterbaenke = models.TextField(null=True, blank=True)
    rolllaeden = models.TextField(null=True, blank=True)

class Fensterbanke(Verantwortung):
    """
    window base.
    for stair case and wohnung
    wohnung part may vary wohnung to wohnung
    """
    treppenhaus = models.TextField(null=True, blank=True)
    wohnung = models.TextField(null=True, blank=True)


class Trockenbau(Verantwortung):
    """
    dry wall. additional layer of wall/floor/ceiling.
    will be foreign key of both haus and wohnung
    """
    # for haus and wohnung
    waende = models.TextField(null=True, blank=True)
    decken = models.TextField(null=True, blank=True)

class Elektro(Verantwortung):
    """
    Electic connectin description of haus 
    will be ForeignKey of haus 
    """
    elektro = models.TextField(null=True, blank=True)


class Raumbuch_elektro(Verantwortung):
    """
    electric fitting per room
    ForeignKey of wohnung
    """
    bad = models.TextField(null=True, blank=True)
    kueche = models.TextField(null=True, blank=True)
    flur = models.TextField(null=True, blank=True)
    wohnzimmer = models.TextField(null=True, blank=True)
    gaeste_wc = models.TextField(null=True, blank=True)
    schlafzimmer = models.TextField(null=True, blank=True)
    kinderzimmer = models.TextField(null=True, blank=True)
    abstellraum = models.TextField(null=True, blank=True)
    schalterprogramm = models.TextField(null=True, blank=True)
    tv_anschluss = models.TextField(null=True, blank=True)
    telefon_anschluss = models.TextField(null=True, blank=True)
    internet_anschluss = models.TextField(null=True, blank=True)

class Sanitaer(Verantwortung):
    """
    sanitary requirements
    """
    aussenanschluss = models.TextField(null=True, blank=True)
    dusche = models.TextField(null=True, blank=True)
    badewanne = models.TextField(null=True, blank=True)
    waschbecken = models.TextField(null=True, blank=True)
    toilette = models.TextField(null=True, blank=True)
    waschmaschinenanschluss = models.TextField(null=True, blank=True)
    spuele = models.TextField(null=True, blank=True)
    spuelmaschinenanschluss = models.TextField(null=True, blank=True)
    fussbodenheizung = models.TextField(null=True, blank=True)

class Bodenbelaege(Verantwortung):
    """
    floor cover for the haus and apartments
    """
    # common for the building
    treppenhaus = models.TextField(null=True, blank=True)
    tiefgarage = models.TextField(null=True, blank=True)
    

    # individual apartment 
    bad = models.TextField(null=True, blank=True)
    kueche = models.TextField(null=True, blank=True)
    flur = models.TextField(null=True, blank=True)
    wohnzimmer = models.TextField(null=True, blank=True)
    gaeste_wc = models.TextField(null=True, blank=True)
    schlafzimmer = models.TextField(null=True, blank=True)
    kinderzimmer = models.TextField(null=True, blank=True)
    abstellraum = models.TextField(null=True, blank=True)

class Fliesenleger(Verantwortung):
    """
    tiles for the haus and wohnung
    """
    # for the haus
    treppenhaus = models.TextField(null=True, blank=True)
    # for the individual wohnung
    bad = models.TextField(null=True, blank=True)
    wohnzimmer = models.TextField(null=True, blank=True)
    abstellraum = models.TextField(null=True, blank=True)
    esszimmer = models.TextField(null=True, blank=True)
    keller = models.TextField(null=True, blank=True)

class Sicherheitstechnik(Verantwortung):
    """
    sycurity system for haus and wohnung
    """
    alarmanlage = models.TextField(null=True, blank=True)
    tuerschliesser = models.TextField(null=True, blank=True)
    sicherheitsschloesser = models.TextField(null=True, blank=True)
    schliesssystem = models.TextField(null=True, blank=True)

class Schlosser(Verantwortung):
    """
    lock standard for the haus and wohnung
    """
    eingangstuer = models.TextField(null=True, blank=True)
    wohnungtuer = models.TextField(null=True, blank=True)
    innentueren = models.TextField(null=True, blank=True)

class Schreiner(Verantwortung):
    """
    wood related work for haus and wohnung
    """
    haustuer = models.TextField(null=True, blank=True)
    wohnungstuer = models.TextField(null=True, blank=True)
    innentueren = models.TextField(null=True, blank=True)

class Schliessanlage(Verantwortung):
    """
    door handle for haus and wohnung
    """
    schliessplan = models.TextField(null=True, blank=True)
    innenbaenke = models.TextField(null=True, blank=True)


class Aussenputz(Verantwortung):
    """
    puter plaster
    """
    aussenputz = models.TextField(null=True, blank=True)
    sockel = models.TextField(null=True, blank=True)

class Aussenanlagern(Verantwortung):
    """
    outside facilities of the haus
    """
    terrassenbelaege = models.TextField(null=True, blank=True)
    pflanzen = models.TextField(null=True, blank=True)
    pflaster = models.TextField(null=True, blank=True)
    grundflache = models.TextField(null=True, blank=True)
    wegeflachen = models.TextField(null=True, blank=True)
    mulleinhausung = models.TextField(null=True, blank=True)
    einfriedung = models.TextField(null=True, blank=True)
    dachaufbau_tiefgarage_grundflache = models.TextField(null=True, blank=True)
    dacchaufbau_tiefgarage_park_wegefkache = models.TextField(null=True, blank=True)





class Choice_options(Verantwortung):
    """
    universal table for all choices of the system.
    choice_type field determines which are the data will be visible for a particular choice.  
    """
    choice_option = models.CharField(max_length=100, blank=True)
    choice_type = models.CharField(max_length=100, blank=True)



class aufzug(Verantwortung):
    """
    description of lift
    """
    aufzug = models.TextField(null=True, blank=True)

class Dach(Verantwortung):
    """
    roof of the house
    """
    dach = models.TextField(null= True, blank=True)

class Maler(Verantwortung):
    """
    painting related description
    painting can be plain paint, wall paper, inside/outside
    """
    tapete = models.TextField(null=True, blank=True)
    farbe = models.TextField(null=True, blank=True)


class Innenputz(Verantwortung):
    """
    inner plaster
    may contian number of layers
    """
    innenputz_bad = models.TextField(null=True, blank=True)
    innenputz_wohnraueme = models.TextField(null=True, blank=True)

class Erdbau(Verantwortung):
    """
    ground work 
    """
    erdbau = models.TextField(null=True, blank=True)
    fundamentplan = models.FileField(null=True, upload_to='plan_pdf', blank=True)

class Estrich(Verantwortung):
    """
    layer under the tiles
    """
    daemmplatten = models.TextField(null=True, blank=True)
    estrich = models.TextField(null=True, blank=True)

class Klimatisierung(Verantwortung):
    """
    air conditioning
    """
    klimatisierung = models.TextField(null=True, blank=True)

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