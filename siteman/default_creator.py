"""
    create haus, wohnung and other components with default settings,
    ready to save in db.
"""
from . import models

def create_default_haus_components(default_choices):
    haus = default_choices['haus']
    print(haus.haus_nr)    

    create_default_architekt_plan(default_choices)
    create_default_erdbau(default_choices)
    create_default_rohbau(default_choices)
    create_default_dach(default_choices)
    create_default_fenster(default_choices)
    create_default_elektro(default_choices)
    create_default_innenputz(default_choices)
    create_default_estrich(default_choices)
    create_default_trockenbau(default_choices)
    create_default_maler(default_choices)
    create_default_aussenputz(default_choices)
    create_default_fliesenleger(default_choices)
    create_default_bodenbelaege(default_choices)
    create_default_schreiner(default_choices)
    create_default_schlosser(default_choices)
    create_default_schliessanlage(default_choices)
    tiefgaragenbeschichtung = create_default_tiefgaragenbeschichtung(default_choices)
    trennwandsysteme = create_default_trennwandsysteme(default_choices)
    klimatisierung = create_default_klimatisierung(default_choices)
    create_default_sicherheitstechnik(default_choices)
    aufzug = create_default_aufzug(default_choices)
    create_default_aussenanlagern(default_choices)

    haus.tiefgaragenbeschichtung = tiefgaragenbeschichtung
    haus.trennwandsysteme = trennwandsysteme
    haus.klimatisierung = klimatisierung
    haus.aufzug = aufzug
    return haus 

def create_default_wohnung(default_choices):
    pass

def create_default_architekt_plan(default_choices):
    haus = default_choices['haus']
    remarks = " all plan will be added later."
    architekt_instance = models.Architekt_plan(haus=haus, remarks=remarks)
    try:
        architekt_instance.save()
    except:
        print('default Architekt_plan creation failed')

def create_default_erdbau(default_choices):
    haus = default_choices['haus']
    erdbau = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    erdbau_instance = models.Erdbau(haus=haus, erdbau=erdbau)
    try:
        erdbau_instance.save()
    except:
        print('default erdbau creation failed')


def create_default_rohbau(default_choices):
    haus = default_choices['haus']
    bodenplatte = "Tragende Bodenplatte aus Stahlbeton. Weiße Wanne."
    geschossdecken = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    aussenwaende = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    tiefgaragenrampe = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    tragendewaende = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    innenwaende = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    nichttragendewaende = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    dach = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    treppen = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    balkon = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    rohbau = models.Rohbau(haus=haus, bodenplatte=bodenplatte, geschossdecken=geschossdecken, aussenwaende=aussenwaende, tiefgaragenrampe=tiefgaragenrampe, tragendewaende=tragendewaende, innenwaende=innenwaende, nichttragendewaende=nichttragendewaende, dach=dach, treppen=treppen, balkon=balkon)
    try:
        rohbau.save()
    except:
        print('default rohbau creation failed')


def create_default_dach(default_choices):
    haus = default_choices['haus']
    dach = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    dach_instance = models.Dach(haus=haus, dach=dach)
    try:
        dach_instance.save()
    except:
        print('default erdbau creation failed')



def create_default_fenster(default_choices):
    haus = default_choices['haus']
    kellergeschoss = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    erdgeschoss = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    regelgeschoss = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    dachgeschoss = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    treppenhaus = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    tiefgarage = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    fenster = models.Fenster(haus=haus, kellergeschoss=kellergeschoss, erdgeschoss=erdgeschoss, regelgeschoss=regelgeschoss, dachgeschoss=dachgeschoss, treppenhaus=treppenhaus, tiefgarage=tiefgarage)
    try:
        fenster.save()
    except:
        print('default erdbau creation failed')

def create_default_elektro(default_choices):
    haus = default_choices['haus']
    elektro = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit officia in eaque sapiente exercitationem ipsum asperiores, laudantium perspiciatis necessitatibus voluptas culpa praesentium optio facilis obcaecati, adipisci rerum! Vero, saepe vitae!"
    elektro_instance = models.Elektro(haus=haus, elektro=elektro)
    try:
        elektro_instance.save()
    except:
        print('default erdbau creation failed')

def create_default_sanitaer(default_choices):
    aussenanschluss = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit officia in eaque sapiente exercitationem ipsum asperiores, laudantium perspiciatis necessitatibus voluptas culpa praesentium optio facilis obcaecati, adipisci rerum! Vero, saepe vitae!"
    dusche = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit officia in eaque sapiente exercitationem ipsum asperiores, laudantium perspiciatis necessitatibus voluptas culpa praesentium optio facilis obcaecati, adipisci rerum! Vero, saepe vitae!"
    badewanne = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit officia in eaque sapiente exercitationem ipsum asperiores, laudantium perspiciatis necessitatibus voluptas culpa praesentium optio facilis obcaecati, adipisci rerum! Vero, saepe vitae!"
    waschbecken = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit officia in eaque sapiente exercitationem ipsum asperiores, laudantium perspiciatis necessitatibus voluptas culpa praesentium optio facilis obcaecati, adipisci rerum! Vero, saepe vitae!"
    toilette = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit officia in eaque sapiente exercitationem ipsum asperiores, laudantium perspiciatis necessitatibus voluptas culpa praesentium optio facilis obcaecati, adipisci rerum! Vero, saepe vitae!"
    waschmaschinenanschluss = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit officia in eaque sapiente exercitationem ipsum asperiores, laudantium perspiciatis necessitatibus voluptas culpa praesentium optio facilis obcaecati, adipisci rerum! Vero, saepe vitae!"
    spuele = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit officia in eaque sapiente exercitationem ipsum asperiores, laudantium perspiciatis necessitatibus voluptas culpa praesentium optio facilis obcaecati, adipisci rerum! Vero, saepe vitae!"
    spuelmaschinenanschluss = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit officia in eaque sapiente exercitationem ipsum asperiores, laudantium perspiciatis necessitatibus voluptas culpa praesentium optio facilis obcaecati, adipisci rerum! Vero, saepe vitae!"
    fussbodenheizung = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit officia in eaque sapiente exercitationem ipsum asperiores, laudantium perspiciatis necessitatibus voluptas culpa praesentium optio facilis obcaecati, adipisci rerum! Vero, saepe vitae!"
    sanitaer = models.Sanitaer(aussenanschluss=aussenanschluss, dusche=dusche, badewanne=badewanne, waschbecken=waschbecken, toilette=toilette, waschmaschinenanschluss=waschmaschinenanschluss, spuele=spuele, spuelmaschinenanschluss=spuelmaschinenanschluss, fussbodenheizung=fussbodenheizung)
    try:
        sanitaer.save()
    except:
        print('default erdbau creation failed')

def create_default_innenputz(default_choices):
    haus = default_choices['haus']
    innenputz_bad = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit officia in eaque sapiente exercitationem ipsum asperiores, laudantium perspiciatis necessitatibus voluptas culpa praesentium optio facilis obcaecati, adipisci rerum! Vero, saepe vitae!"
    innenputz_wohnraueme = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit officia in eaque sapiente exercitationem ipsum asperiores, laudantium perspiciatis necessitatibus voluptas culpa praesentium optio facilis obcaecati, adipisci rerum! Vero, saepe vitae!"
    innenputz = models.Innenputz(haus=haus, innenputz_bad=innenputz_bad, innenputz_wohnraueme=innenputz_wohnraueme)
    try:
        innenputz.save()
    except:
        print('default erdbau creation failed')

def create_default_estrich(default_choices):
    haus = default_choices['haus']
    daemmplatten = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    estrich = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    estrich_instance = models.Estrich(haus=haus, daemmplatten=daemmplatten, estrich=estrich)
    try:
        estrich_instance.save()
    except:
        print('default erdbau creation failed')

def create_default_trockenbau(default_choices):
    haus = default_choices['haus']
    waende = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    decken = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    trockenbau_instance = models.Trockenbau(haus=haus, waende=waende, decken=decken)
    try:
        trockenbau_instance.save()
    except:
        print('default erdbau creation failed')

def create_default_maler(default_choices):
    haus = default_choices['haus']
    tapete = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    farbe = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    maler_instance = models.Maler(haus=haus, tapete=tapete, farbe=farbe)
    try:
        maler_instance.save()
    except:
        print('default erdbau creation failed')

def create_default_aussenputz(default_choices):
    haus = default_choices['haus']
    aussenputz = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    sockel = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    aussenputz_instance = models.Aussenputz(haus=haus, aussenputz=aussenputz, sockel=sockel)
    try:
        aussenputz_instance.save()
    except:
        print('default erdbau creation failed')


def create_default_fliesenleger(default_choices):
    haus = default_choices['haus']
    treppenhaus = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    bad = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    wohnzimmer = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    abstellraum = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    esszimmer = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    keller = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    fliesenleger_instance = models.Fliesenleger(haus=haus, treppenhaus=treppenhaus, bad=bad, wohnzimmer=wohnzimmer, abstellraum=abstellraum, esszimmer=esszimmer, keller=keller)
    try:
        fliesenleger_instance.save()
    except:
        print('default erdbau creation failed')

def create_default_bodenbelaege(default_choices):
    haus = default_choices['haus']
    treppenhaus = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    tiefgarage = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    bad = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    kueche = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    flur = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    wohnzimmer = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    gaeste_wc = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    schlafzimmer = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    kinderzimmer = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    abstellraum = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    bodenbelaege_instance = models.Bodenbelaege(haus=haus, treppenhaus=treppenhaus, tiefgarage=tiefgarage, bad=bad, kueche=kueche, flur=flur, wohnzimmer=wohnzimmer, gaeste_wc=gaeste_wc, schlafzimmer=schlafzimmer, kinderzimmer=kinderzimmer, abstellraum=abstellraum)
    try:
        bodenbelaege_instance.save()
    except:
        print('default erdbau creation failed')

def create_default_schreiner(default_choices):
    haus = default_choices['haus']
    haustuer = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    wohnungstuer = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    innentueren = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."

    schreiner_instance = models.Schreiner(haus=haus, haustuer=haustuer, wohnungstuer=wohnungstuer, innentueren=innentueren)
    try:
        schreiner_instance.save()
    except:
        print('default erdbau creation failed')
    

def create_default_schlosser(default_choices):
    haus = default_choices['haus']
    eingangstuer = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    wohnungstuer = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    innentueren = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."

    schlosser_instance = models.Schlosser(haus=haus, eingangstuer=eingangstuer, wohnungstuer=wohnungstuer, innentueren=innentueren)
    try:
        schlosser_instance.save()
    except:
        print('default erdbau creation failed')

def create_default_schliessanlage(default_choices):
    haus = default_choices['haus']
    schliessplan = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    schliessanlage_instance = models.Schliessanlage(haus=haus, schliessplan=schliessplan)
    try:
        schliessanlage_instance.save()
    except:
        print('default erdbau creation failed')




def create_default_sicherheitstechnik(default_choices):
    haus = default_choices['haus']
    alarmanlage = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    tuerschliesser = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    sicherheitsschloesser = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    schliesssystem = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    sicherheitstechnik_instance = models.Sicherheitstechnik(haus=haus, alarmanlage=alarmanlage, tuerschliesser=tuerschliesser, sicherheitsschloesser=sicherheitsschloesser, schliesssystem=schliesssystem)
    try:
        sicherheitstechnik_instance.save()
    except:
        print('default erdbau creation failed')

def create_default_aussenanlagern(default_choices):
    haus = default_choices['haus']
    terrassenbelaege = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    pflanzen = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    pflaster = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    grundflache = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    wegeflachen = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    mulleinhausung = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    einfriedung = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    dachaufbau_tiefgarage_grundflache = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    dachaufbau_tiefgarage_park_wegefkache = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    aussenanlagern_instance = models.Aussenanlagern(haus=haus, terrassenbelaege=terrassenbelaege, pflanzen=pflanzen, pflaster=pflaster, grundflache=grundflache, wegeflachen=wegeflachen, mulleinhausung=mulleinhausung, einfriedung=einfriedung, dachaufbau_tiefgarage_grundflache=dachaufbau_tiefgarage_grundflache, dachaufbau_tiefgarage_park_wegefkache=dachaufbau_tiefgarage_park_wegefkache)
    try:
        aussenanlagern_instance.save()
    except:
        print('default erdbau creation failed')

def create_default_aufzug(default_choices):
    aufzug = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    return aufzug

def create_default_tiefgaragenbeschichtung(default_choices):
    tiefgaragenbeschichtung = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    return tiefgaragenbeschichtung

def create_default_trennwandsysteme(default_choices):
    trennwandsysteme = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    return trennwandsysteme

def create_default_klimatisierung(default_choices):
    klimatisierung = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    return klimatisierung