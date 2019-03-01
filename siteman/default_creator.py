"""
    create haus, wohnung and other components with default settings,
    ready to save in db.
"""
from . import models

def create_default_haus(default_choices):
    print(default_choices['haus_nr'])
    haus = models.Haus()
    haus.haus_nr = default_choices['haus_nr']   
    haus.display_nr = default_choices['display_nr']
    haus.projekt_id = default_choices['projekt_id'] 
    
    erdbau = create_default_erdbau(default_choices)
    haus.erdbau = erdbau
    rohbau = create_default_rohbau(default_choices)
    haus.rohbau = rohbau
    dach = create_default_dach(default_choices)
    haus.dach = dach
    fenster = create_default_fenster(default_choices)
    haus.fenster = fenster
    elektro = create_default_elektro(default_choices)
    haus.elektro = elektro
    sanitaer = create_default_sanitaer(default_choices)
    haus.sanitaer = sanitaer
    innenputz = create_default_innenputz(default_choices)
    haus.innenputz = innenputz
    estrich = create_default_estrich(default_choices)
    haus.estrich = estrich
    trockenbau = create_default_trockenbau(default_choices)
    haus.trockenbau = trockenbau
    maler = create_default_maler(default_choices)
    haus.maler = maler
    aussenputz = create_default_aussenputz(default_choices)
    haus.aussenputz = aussenputz
    fliesenleger = create_default_fliesenleger(default_choices)
    haus.fliesenleger = fliesenleger
    bodenbelaege = create_default_bodenbelaege(default_choices)
    haus.bodenbelaege = bodenbelaege
    schreiner = create_default_schreiner(default_choices)
    haus.schreiner = schreiner
    schlosser = create_default_schlosser(default_choices)
    haus.schlosser = schlosser
    schliessanlage = create_default_schliessanlage(default_choices)
    haus.schliessanlage = schliessanlage
    ## does not return an instance rather return text
    tiefgaragenbeschichtung = create_default_tiefgaragenbeschichtung(default_choices)
    haus.tiefgaragenbeschichtung = tiefgaragenbeschichtung
    ## does not return an instance rather return text
    trennwandsysteme = create_default_trennwandsysteme(default_choices)
    haus.trennwandsysteme = trennwandsysteme
    ## does not return an instance rather return text
    klimatisierung = create_default_klimatisierung(default_choices)
    haus.klimatisierung = klimatisierung
    sicherheitstechnik = create_default_sicherheitstechnik(default_choices)
    haus.sicherheitstechnik = sicherheitstechnik
    aufzug = create_default_aufzug(default_choices)
    haus.aufzug = aufzug
    aussenanlagern = create_default_aussenanlagern(default_choices)
    haus.aussenanlagern = aussenanlagern



    models.Haus()
    return haus 

def create_default_wohnung(default_choices):
    pass

def create_default_erdbau(default_choices):
    erdbau = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    erdbau_instance = models.Erdbau(erdbau=erdbau)
    try:
        erdbau_instance.save()
    except:
        pass
    return erdbau_instance


def create_default_rohbau(default_choices):
    bodenplatte = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    geschossdecken = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    aussenwaende = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    tiefgaragenrampe = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    tragendewaende = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    innenwaende = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    nichttragendewaende = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    dach = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    treppen = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    balkon = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    rohbau = models.Rohbau(bodenplatte=bodenplatte, geschossdecken=geschossdecken, aussenwaende=aussenwaende, tiefgaragenrampe=tiefgaragenrampe, tragendewaende=tragendewaende, innenwaende=innenwaende, nichttragendewaende=nichttragendewaende, dach=dach, treppen=treppen, balkon=balkon)
    try:
        rohbau.save()
    except:
        pass
    return rohbau



def create_default_fenster(default_choices):
    kellergeschoss = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    erdgeschoss = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    regelgeschoss = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    dachgeschoss = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    treppenhaus = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    tiefgarage = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi adipisci cupiditate illo unde. Neque obcaecati quam, corrupti error nobis harum dolore accusantium minima quos voluptates mollitia vel commodi, dignissimos officia."
    fenster = models.Fenster(kellergeschoss=kellergeschoss, erdgeschoss=erdgeschoss, regelgeschoss=regelgeschoss, dachgeschoss=dachgeschoss, treppenhaus=treppenhaus, tiefgarage=tiefgarage)
    try:
        fenster.save()
    except:
        pass
    return fenster

def create_default_dach(default_choices):
    dach = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    dach_instance = models.Dach(dach=dach)
    try:
        dach_instance.save()
    except:
        pass
    return dach_instance

def create_default_elektro(default_choices):
    elektro = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit officia in eaque sapiente exercitationem ipsum asperiores, laudantium perspiciatis necessitatibus voluptas culpa praesentium optio facilis obcaecati, adipisci rerum! Vero, saepe vitae!"
    elektro_instance = models.Elektro(elektro=elektro)
    try:
        elektro_instance.save()
    except:
        pass
    return elektro_instance

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
        pass
    return sanitaer

def create_default_innenputz(default_choices):
    innenputz_bad = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit officia in eaque sapiente exercitationem ipsum asperiores, laudantium perspiciatis necessitatibus voluptas culpa praesentium optio facilis obcaecati, adipisci rerum! Vero, saepe vitae!"
    innenputz_wohnraueme = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit officia in eaque sapiente exercitationem ipsum asperiores, laudantium perspiciatis necessitatibus voluptas culpa praesentium optio facilis obcaecati, adipisci rerum! Vero, saepe vitae!"
    innenputz = models.Innenputz(innenputz_bad=innenputz_bad, innenputz_wohnraueme=innenputz_wohnraueme)
    try:
        innenputz.save()
    except:
        pass
    return innenputz

def create_default_estrich(default_choices):
    daemmplatten = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    estrich = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    estrich_instance = models.Estrich(daemmplatten=daemmplatten, estrich=estrich)
    try:
        estrich_instance.save()
    except:
        pass
    return estrich_instance

def create_default_trockenbau(default_choices):
    waende = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    decken = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    trockenbau_instance = models.Trockenbau(waende=waende, decken=decken)
    try:
        trockenbau_instance.save()
    except:
        pass
    return trockenbau_instance

def create_default_maler(default_choices):
    tapete = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    farbe = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    maler_instance = models.Maler(tapete=tapete, farbe=farbe)
    try:
        maler_instance.save()
    except:
        pass
    return maler_instance

def create_default_aussenputz(default_choices):
    aussenputz = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    sockel = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    aussenputz_instance = models.Aussenputz(aussenputz=aussenputz, sockel=sockel)
    try:
        aussenputz_instance.save()
    except:
        pass
    return aussenputz_instance


def create_default_fliesenleger(default_choices):
    treppenhaus = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    bad = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    wohnzimmer = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    abstellraum = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    esszimmer = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    keller = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    fliesenleger_instance = models.Fliesenleger(treppenhaus=treppenhaus, bad=bad, wohnzimmer=wohnzimmer, abstellraum=abstellraum, esszimmer=esszimmer, keller=keller)
    try:
        fliesenleger_instance.save()
    except:
        pass
    return fliesenleger_instance

def create_default_bodenbelaege(default_choices):
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
    bodenbelaege_instance = models.Bodenbelaege(treppenhaus=treppenhaus, tiefgarage=tiefgarage, bad=bad, kueche=kueche, flur=flur, wohnzimmer=wohnzimmer, gaeste_wc=gaeste_wc, schlafzimmer=schlafzimmer, kinderzimmer=kinderzimmer, abstellraum=abstellraum)
    try:
        bodenbelaege_instance.save()
    except:
        pass
    return bodenbelaege_instance

def create_default_schreiner(default_choices):
    haustuer = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    wohnungstuer = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    innentueren = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."

    schreiner_instance = models.Schreiner(haustuer=haustuer, wohnungstuer=wohnungstuer, innentueren=innentueren)
    try:
        schreiner_instance.save()
    except:
        pass
    return schreiner_instance
    

def create_default_schlosser(default_choices):
    eingangstuer = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    wohnungstuer = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    innentueren = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."

    schlosser_instance = models.Schlosser(eingangstuer=eingangstuer, wohnungstuer=wohnungstuer, innentueren=innentueren)
    try:
        schlosser_instance.save()
    except:
        pass
    return schlosser_instance

def create_default_schliessanlage(default_choices):
    schliessplan = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
 

    schliessanlage_instance = models.Schliessanlage(schliessplan=schliessplan)
    try:
        schliessanlage_instance.save()
    except:
        pass
    return schliessanlage_instance

def create_default_klimatisierung(default_choices):
    klimatisierung = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
 

    klimatisierung_instance = klimatisierung


def create_default_sicherheitstechnik(default_choices):
    alarmanlage = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    tuerschliesser = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    sicherheitsschloesser = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    schliesssystem = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
 

    sicherheitstechnik_instance = models.Sicherheitstechnik(alarmanlage=alarmanlage, tuerschliesser=tuerschliesser, sicherheitsschloesser=sicherheitsschloesser, schliesssystem=schliesssystem)
    try:
        sicherheitstechnik_instance.save()
    except:
        pass
    return sicherheitstechnik_instance

def create_default_aufzug(default_choices):
    aufzug = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    aufzug_instance = models.Aufzug(aufzug=aufzug)
    try:
        aufzug_instance.save()
    except:
        pass
    return aufzug_instance

def create_default_aussenanlagern(default_choices):
    terrassenbelaege = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    pflanzen = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    pflaster = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    grundflache = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    wegeflachen = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    mulleinhausung = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    einfriedung = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    dachaufbau_tiefgarage_grundflache = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    dachaufbau_tiefgarage_park_wegefkache = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
    aussenanlagern_instance = models.Aussenanlagern(terrassenbelaege=terrassenbelaege, pflanzen=pflanzen, pflaster=pflaster, grundflache=grundflache, wegeflachen=wegeflachen, mulleinhausung=mulleinhausung, einfriedung=einfriedung, dachaufbau_tiefgarage_grundflache=dachaufbau_tiefgarage_grundflache, dachaufbau_tiefgarage_park_wegefkache=dachaufbau_tiefgarage_park_wegefkache)
    try:
        aussenanlagern_instance.save()
    except:
        pass
    return aussenanlagern_instance

def create_default_tiefgaragenbeschichtung(default_choices):
    tiefgaragenbeschichtung = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."

    return tiefgaragenbeschichtung

def create_default_trennwandsysteme(default_choices):
    trennwandsysteme = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."

    return trennwandsysteme

