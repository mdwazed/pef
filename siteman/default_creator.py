"""
    create haus, wohnung and other components with default settings,
    ready to save in db.
"""
from . import models

"""
    Create default haus components with user selected options.
    attach those components to the passed haus
    return the haus to the view to save 
"""

def create_default_haus_components(default_choices):
    print("------creating default haus--------")
    haus = default_choices['haus']
    # grundung = default_choices['grundung']
    # print(default_choices['fenster_beschattung'])    

    create_default_architekt_plan(default_choices)
    create_default_erdbau(default_choices)
    create_default_rohbau(default_choices)
    create_default_dach(default_choices)
    create_default_fenster(default_choices)
    create_default_elektro(default_choices)
    create_default_sanitaer(default_choices)
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
    print("------default haus creation complete--------")
    return haus 

def create_default_wohnung_components(default_choices):
    
    wohnung = default_choices['wohnung']
    create_default_fenster(default_choices)
    create_default_elektro(default_choices)
    create_default_sanitaer(default_choices)
    create_default_raumbuch_elektro(default_choices)
    create_default_innenputz(default_choices)
    create_default_estrich(default_choices)
    create_default_trockenbau(default_choices)
    create_default_maler(default_choices)
    create_default_fliesenleger(default_choices)
    create_default_bodenbelaege(default_choices)
    create_default_schreiner(default_choices)
    create_default_schlosser(default_choices)
    create_default_schliessanlage(default_choices)
    return wohnung

def create_default_architekt_plan(default_choices):
    haus = default_choices['haus']
    sonstiges = " all plan will be added later."
    architekt_instance = models.Architekt_plan(haus=haus, sonstiges=sonstiges)
    try:
        architekt_instance.save()
    except Exception as e:
        print('default Architekt_plan creation failed' + str(e))

def create_default_erdbau(default_choices):
    haus = default_choices['haus']
    erdbau = "Aushub, Boeschung, etc."
    erdbau_instance = models.Erdbau(haus=haus, erdbau=erdbau)
    try:
        erdbau_instance.save()
    except:
        print('default erdbau creation failed')


def create_default_rohbau(default_choices):
    haus = default_choices['haus']
    if default_choices['grundung'] == 'sf':
        grundung = "streifenfundamente"
    elif default_choices['grundung'] == 'sb':
        grundung = "Stahlbeton"
    elif default_choices['grundung'] == 'sb_sf':
        grundung = "Stahlbeton mit streifenfundamente"
    geschossdecken = "Stahlbeton. In der Tiefgarage Boden mit OS8-Beschichtung und aufgehende Bauteile mit OS4-Beschichtung."
    aussenwande_kellergeschoss = "aussenwande kellergeschoss."
    if default_choices['aussenwande_eg_og_dg'] == 'su':
        aussenwande_eg_og_dg = "Aussenwande eg, og, dg von stahlbeton und unipor."
    elif default_choices['aussenwande_eg_og_dg'] == 'sk':
        aussenwande_eg_og_dg = "Aussenwande eg, og, dg von stahlbeton und kalksandstein."
    
    tragendeinnenwande = "Stahlbeton und Kalksandstein."
    nichttragendeinnenwande = "10 cm Mauerwerk aus massiven Gipswandbauplatten. Installationswände werden ausgeführt als mit Gipskarton 2-fach beplankte Metallständerwand, Wandstärke 15-35cm."
    tiefgaragenrampe = "Stahlbeton mit OS11-Beschichtung, einschl. Sockel."
    if default_choices['dach'] == 'zd':
        dach = "Zeigeldach"
    elif default_choices['dach'] == 'fds':
        dach = "Flachdach aus stahlbeton"
    treppen = "Treppenläufe aus Stahlbeton mit Schallenkoppelung."
    balkon = "Stahlbetonfertigteil, integriete rinne mit ablauf"
    rohbau = models.Rohbau(haus=haus, grundung=grundung, geschossdecken=geschossdecken,
            aussenwande_kellergeschoss=aussenwande_kellergeschoss, aussenwande_eg_og_dg=aussenwande_eg_og_dg,
            tragendeinnenwande=tragendeinnenwande, nichttragendeinnenwande=nichttragendeinnenwande,
            tiefgaragenrampe=tiefgaragenrampe,  dach=dach, treppen=treppen, balkon=balkon)
    try:
        rohbau.save()
    except:
        print('default rohbau creation failed')


def create_default_dach(default_choices):
    haus = default_choices['haus']
    dach = "Wohngebäude: Flachdach Stahlbeton, mit Dampfsperre, Gefälledämmung und Dachabdichtung aus Bitumenbahnen, 2-lagig, und extensiver Begrünung."
    dach_instance = models.Dach(haus=haus, dach=dach)
    try:
        dach_instance.save()
    except:
        print('default dach creation failed')



def create_default_fenster(default_choices):
    if 'haus' in default_choices:
        haus = default_choices['haus']  
        algemeine_information = "algemeine information"
        # beschattung = "beschatung"
        if default_choices['fenster_beschattung']=='nbk':
            beschattung = "neubaukasten"
        elif default_choices['fenster_beschattung']=='aufsr':
            beschattung = "aufsatzrollladenkasten"
        elif default_choices['fenster_beschattung']=='rse':
            beschattung = "rafstorelement"
        kellergeschoss = "Kunststoff-Fenster mit Leibungsrahmen."
        erdgeschoss = "Kunststoff-Fenster, innen weiß, außen grau foliert, mit 3-fach-Verglasung, Dreh- bzw. Drehkippflügel mit Eingriffbedienung, teilweise Festverglasung, im EG abschließbare Griffe und Einbruchwiderstand RC 2 N.."
        regelgeschoss = "Kunststoff-Fenster, innen weiß, außen grau foliert, mit 3-fach-Verglasung, Dreh- bzw. Drehkippflügel mit Eingriffbedienung, teilweise Festverglasung, im EG abschließbare Griffe und Einbruchwiderstand RC 2 N."
        dachgeschoss = "Kunststoff-Fenster, innen weiß, außen grau foliert, mit 3-fach-Verglasung, Dreh- bzw. Drehkippflügel mit Eingriffbedienung, teilweise Festverglasung, im EG abschließbare Griffe und Einbruchwiderstand RC 2 N."
        treppenhaus = "Eingangselement aus farbigen Metallprofilen mit Isolierverglasung, je Treppenhaus ein Oberlicht als Dachausstieg mit RWA-Funktion, incl. Schlagtaster im EG und im obersten Geschoß, und ein feststehendes, lichtbandartiges Oberlicht oberhalb der Treppenanlage. "
        tiefgarage = "Kunststoff-Fenster mit Leibungsrahmen."
        fenster = models.Fenster(haus=haus, kellergeschoss=kellergeschoss, algemeine_information=algemeine_information, beschattung=beschattung, erdgeschoss=erdgeschoss, regelgeschoss=regelgeschoss, dachgeschoss=dachgeschoss, treppenhaus=treppenhaus, tiefgarage=tiefgarage)
        try:
            fenster.save()
        except:
            print('default fenster creation failed for haus')


    if 'wohnung' in default_choices:
        wohnung = default_choices['wohnung']
        fensterbaenke = "wohnung fenster banke"
        rolllaeden = "wohnung rollen laden"
        fenster = models.Fenster(wohnung=wohnung, fensterbaenke=fensterbaenke, rolllaeden=rolllaeden)
        try:
            fenster.save()
            print("default fenster for wohnung created ")
        except:
            print('default fenster creation failed for wohnung')


def create_default_elektro(default_choices):
    if 'haus' in default_choices:
        haus = default_choices['haus']
        elektro = "Unterputzinstallation in den Wohnungen, im Treppenhaus und in der Schleuse zur Tiefgarage. Aufputzinstallation im Untergeschoß, mit Ausnahme der vorstehend genannten Bereiche, und in der Tiefgarage."
        sonstiges = "haus sonstiges"
        elektro_instance = models.Elektro(haus=haus, elektro=elektro, sonstiges=sonstiges)
        try:
            elektro_instance.save()
        except:
            print('default elektro creation failed')
    if 'wohnung' in default_choices:
        wohnung = default_choices['wohnung']
        elektro = "Unterputzinstallation in den Wohnungen, im Treppenhaus und in der Schleuse zur Tiefgarage. Aufputzinstallation im Untergeschoß, mit Ausnahme der vorstehend genannten Bereiche, und in der Tiefgarage."
        sonstiges = "wohnung sonstiges"
        elektro_instance = models.Elektro(wohnung=wohnung, elektro=elektro, sonstiges=sonstiges)
        try:
            elektro_instance.save()
            print("default elektro for wohnung created ")
        except:
            print('default elektro creation failed for wohnung')


def create_default_raumbuch_elektro(default_choices):
    if 'wohnung' in default_choices:
        wohnung = default_choices['wohnung']
        bad = "Serienschaltung für Decken- und Wandauslass\n 2 Steckdosen\n 1 Waschmaschinenanschluss, extra Stromkreis\n 1 Trockneranschluss, extra Stromkreis\n 1 Steckdose für Badheizkörper\n 1 Raumthermostat Fußbodenheizung"
        kueche = "Ausschaltung für Deckenauslass\n 3 Doppelsteckdosen\n1 Steckdose Spülmaschine, extra Stromkreis\n1 Steckdose für Umluftdunstabzug\n1 Herdanschluss 400 V/16A\n2 Steckdosen\n1 Raumthermostat Fußbodenheizung"
        flur = "Kreuz-/Wechselschaltung für Deckenauslass\n1 Freisprechstelle/Türsprechanlage\n1 Steckdose\n1 Deckenauslass\n1 Rauchmelder, batteriebetrieben\n1 Raumthermostat Fußbodenheizung"
        wohnzimmer = "Aus-/Wechselschaltung für Deckenauslass\nSerienschaltung für Deckenauslass\n3 Doppelsteckdosen\n1 Antennenanschlußdose (TV)\n1 Datenanschlußdose RJ45 (2-fach)\n3 Steckdosen\n1 Rauchmelder, batteriebetrieben\n1 Raumthermostat Fußbodenheizung"
        gaeste_wc ="Kreuz-/Wechselschaltung für Deckenauslass\n1 Freisprechstelle/Türsprechanlage\n1 Steckdose\n1 Deckenauslass\n1 Rauchmelder, batteriebetrieben"
        schlafzimmer = "Wechselschaltung für Deckenauslass\n1 Ausschalter an der Tür\n1 Ausschalter am Bett\n2 Doppelsteckdosen\n2 Steckdosen"
        kinderzimmer = "Wechselschaltung für Deckenauslass\n1 Ausschalter an der Tür\n1 Ausschalter am Bett\n2 Doppelsteckdosen\n2 Steckdosen"
        abstellraum = "Ausschaltung für Deckenauslass\n1 Steckdose"
        schalterprogramm = "Kreuz-/Wechselschaltung für Deckenauslass\n1 Freisprechstelle/Türsprechanlage\n1 Steckdose\n1 Deckenauslass\n1 Rauchmelder, batteriebetrieben"
        tv_anschluss = "Kreuz-/Wechselschaltung für Deckenauslass\n1 Freisprechstelle/Türsprechanlage\n1 Steckdose\n1 Deckenauslass\n1 Rauchmelder, batteriebetrieben"
        telefon_anschluss = "Kreuz-/Wechselschaltung für Deckenauslass\n1 Freisprechstelle/Türsprechanlage\n1 Steckdose\n1 Deckenauslass\n1 Rauchmelder, batteriebetrieben"
        internet_anschluss = "Kreuz-/Wechselschaltung für Deckenauslass\n1 Freisprechstelle/Türsprechanlage\n1 Steckdose\n1 Deckenauslass\n1 Rauchmelder, batteriebetrieben"
        raumbuch_elektro_instance = models.Raumbuch_elektro(wohnung=wohnung, bad=bad, kueche=kueche, flur=flur, wohnzimmer=wohnzimmer, gaeste_wc=gaeste_wc, schlafzimmer=schlafzimmer, kinderzimmer=kinderzimmer, abstellraum=abstellraum, schalterprogramm=schalterprogramm, tv_anschluss=tv_anschluss, telefon_anschluss=telefon_anschluss, internet_anschluss=internet_anschluss,)
        try:
            raumbuch_elektro_instance.save()
            print("raumbuch_elektro_instance saved for wohnugn")
        except:
            print("raumbuch_elektro_instance creation failed")



def create_default_sanitaer(default_choices):
    if 'haus' in default_choices:
        haus = default_choices['haus']    
        fussbodenheizung = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit officia in eaque sapiente exercitationem ipsum asperiores, laudantium perspiciatis necessitatibus voluptas culpa praesentium optio facilis obcaecati, adipisci rerum! Vero, saepe vitae!"
        heizung = "„Zum Zweck der Wärmeversorgung der Eigentumswohnanlage errichtet ein gewerblicher Wärmelieferant eine zentrale Wärmeversorgungsanlage auf eigene Rechnung, die in seinem Eigentum steht und nicht Bestandteil des gemeinschaftlichen Eigentums wird. Hierzu wird mit dem Wärmelieferanten ein Wärmelieferungsvertrag über eine Vertragslaufzeit von 15 Jahren abgeschlossen, dem der Miteigentümer (Käufer) für den Umfang seiner Miteigentumsanteile vorbehaltlos zustimmt. Die Wohnungseigentümergemeinschaft als solches tritt in den bestehenden Wärmelieferungsvertrag gemäß § 10 Abs. 8 WEG ein.“ Leistung des Wärmelieferanten: Zentrale Wärmeerzeugungsanlage mit Pelletskessel, Gas-Brennwertkessel, 3 Stück Blockheizkraftwerk mit erforderlicher Wärmeleistung, mit Pufferspeichern, Pelletlagerraum, automatische Pelletbeschickung, Schornsteinanlage, Ausdehnungsgefäße, automatische Wassernachspeisung, Regelanlage, Heizkreispumpen und Armaturen, Fernüberwachung mit GLT, gebäudeweise außentemperaturabhängige Regelung, gebäudeweiser Warmwasserbehälter (WWB) mit Hygiene-Kombispeicher, Anschluss des WWB an das Heizungssystem mit Ladepumpe, Regelung, und Wärmemengenzähler, geregelter Heizkreis mit Mischer, Regelgerät, Heizkreispumpe und Armaturen. Verlegung der Verteilleitungen Heizung vom Heizraum in die jeweiligen Häuser mit gedämmten Doppelmantelrohren und Datenkabel. Verlegung der Gasleitungen ab HAR in den Heizraum, einschließlich Anschlüsse der Wärmeerzeuger. Anschluss der Sekundärkreise an die installierten Absperrarmaturen der geregelten Heizkreise je Gebäude."
        entwasserung = "Leitungen aus Kunststoff, Fallstränge aus schallgedämmtem Kunststoffrohr."
        sonstiges= "haus sonstiges"
        sanitaer = models.Sanitaer(haus=haus, fussbodenheizung=fussbodenheizung, heizung=heizung, entwasserung=entwasserung, sonstiges=sonstiges)
        try:
            sanitaer.save()
        except:
            print('default sanitar creation failed for haus')
    if 'wohnung' in default_choices:
        wohnung = default_choices['wohnung']
        aussenzapfstelle = "aussenzapfstelle fur wohnung"
        dusche = "dusche fur wohnung"
        badewanne = "badewanne fur wohnung"
        waschbecken = "waschbecken fur wohnung"
        toilette = "toilette fur wohnung"
        waschmaschinenanschluss = "waschmaschinenanschluss fur wohnung"
        spuele = "spuele fur wohnung"
        spuelmaschinenanschluss = "spuelmaschinenanschluss fur wohnung"
        fussbodenheizung = "fussbodenheizung fur wohnung"
        sonstiges = "sonstiges fur wohnung"
        sanitaer = models.Sanitaer(wohnung=wohnung, aussenzapfstelle=aussenzapfstelle, dusche=dusche, badewanne=badewanne, waschbecken=waschbecken, toilette=toilette, waschmaschinenanschluss=waschmaschinenanschluss, spuele=spuele, spuelmaschinenanschluss=spuelmaschinenanschluss, fussbodenheizung=fussbodenheizung, sonstiges=sonstiges)
        try:
            sanitaer.save()
            print("default sanitar for wohnung created ")
        except:
            print('default sanitar creation failed for haus')



def create_default_innenputz(default_choices):
    if 'haus' in default_choices:        
        haus = default_choices['haus']
        innenputz_bad = " for haus  Im Bereich der Dusche und Badewanne raumhoch gefliest, im Bereich der 1,20 m hohen Vorwandinstallation auf Höhe der Vorwand gefliest, incl. der oberen Ablagefläche. Übrige Flächen ohne Fliesen gemäß 6.2.1."
        innenputz_wohnraueme = " for haus Raufasertapete mit weißem Dispersionsanstrich. "
        innenputz = models.Innenputz(haus=haus, innenputz_bad=innenputz_bad, innenputz_wohnraueme=innenputz_wohnraueme)
        try:
            innenputz.save()
        except:
            print('default innenputz creation failed for haus')
    if 'wohnung' in default_choices:
        wohnung = default_choices['wohnung']
        innenputz_bad = " for wohnuhng Im Bereich der Dusche und Badewanne raumhoch gefliest, im Bereich der 1,20 m hohen Vorwandinstallation auf Höhe der Vorwand gefliest, incl. der oberen Ablagefläche. Übrige Flächen ohne Fliesen gemäß 6.2.1."
        innenputz_wohnraueme = " for wohnung Raufasertapete mit weißem Dispersionsanstrich. "
        innenputz = models.Innenputz(wohnung=wohnung, innenputz_bad=innenputz_bad, innenputz_wohnraueme=innenputz_wohnraueme)
        try:
            innenputz.save()
        except:
            print('default innenputz creation failed for wohnung')

def create_default_estrich(default_choices):
    if 'haus' in default_choices:
        haus = default_choices['haus']
        daemmplatten = "Schwimmender Heizestrich auf Trittschall- und Wärmedämmplatten in den Wohnungen. Schwimmender Estrich im Treppenhaus, auch im Untergeschoß."
        estrich = "Schwimmender Heizestrich auf Trittschall- und Wärmedämmplatten in den Wohnungen. Schwimmender Estrich im Treppenhaus, auch im Untergeschoß."
        estrich_instance = models.Estrich(haus=haus, daemmplatten=daemmplatten, estrich=estrich)
        try:
            estrich_instance.save()
        except:
            print('default estrich  creation failed for haus')
    if 'wohnung' in default_choices:
        wohnung = default_choices['wohnung']
        daemmplatten = "Schwimmender Heizestrich auf Trittschall- und Wärmedämmplatten in den Wohnungen. Schwimmender Estrich im Treppenhaus, auch im Untergeschoß."
        estrich = "Schwimmender Heizestrich auf Trittschall- und Wärmedämmplatten in den Wohnungen. Schwimmender Estrich im Treppenhaus, auch im Untergeschoß."
        estrich_instance = models.Estrich(wohnung=wohnung, daemmplatten=daemmplatten, estrich=estrich)
        try:
            estrich_instance.save()
        except:
            print('default estrich  creation failed for wohnung')


def create_default_trockenbau(default_choices):
    if 'haus' in default_choices:
        haus = default_choices['haus']
        wande = "Tapezierfähig verputzt bzw. gespachtelt Qualitätsstufe Q2."
        decken = "Tapezierfähig verputzt bzw. gespachtelt Qualitätsstufe Q2."
        trockenbau_instance = models.Trockenbau(haus=haus, wande=wande, decken=decken)
        try:
            trockenbau_instance.save()
        except:
            print('default trocken creation failed for haus')
    if 'wohnung' in default_choices:
        wohnung = default_choices['wohnung']
        wande = "Tapezierfähig verputzt bzw. gespachtelt Qualitätsstufe Q2."
        decken = "Tapezierfähig verputzt bzw. gespachtelt Qualitätsstufe Q2."
        trockenbau_instance = models.Trockenbau(wohnung=wohnung, wande=wande, decken=decken)
        try:
            trockenbau_instance.save()
        except:
            print('default trocken creation failed for wohung')

def create_default_maler(default_choices):
    if 'haus' in default_choices:
        haus = default_choices['haus']
        tapete = "Raufasertapete "
        farbe = "weißer Dispersionsanstrich."
        maler_instance = models.Maler(haus=haus, tapete=tapete, farbe=farbe)
        try:
            maler_instance.save()
        except:
            print('default maler creation failed for haus')
    if 'wohnung' in default_choices:
        wohnung = default_choices['wohnung']
        tapete = "Raufasertapete "
        farbe = "weißer Dispersionsanstrich."
        maler_instance = models.Maler(wohnung=wohnung, tapete=tapete, farbe=farbe)
        try:
            maler_instance.save()
        except:
            print('default maler creation failed for wohnung')

def create_default_aussenputz(default_choices):
    haus = default_choices['haus']
    aussenputz = "Außenputz mit 3 mm Körnung auf Wärmedämmung"
    sockel = "Gefilzter Sockelputz auf Wärmedämmung."
    aussenputz_instance = models.Aussenputz(haus=haus, aussenputz=aussenputz, sockel=sockel)
    try:
        aussenputz_instance.save()
    except:
        print('default erdbau creation failed')


def create_default_fliesenleger(default_choices):
    if 'haus' in default_choices:
        haus = default_choices['haus']
        treppenhaus = "Fliesen, Feinsteinzeug, etc."
        fliesenleger_instance = models.Fliesenleger(haus=haus, treppenhaus=treppenhaus,)
        try:
            fliesenleger_instance.save()
        except:
            print('default Fliesenleger creation failed for haus')
    if 'wohnung' in default_choices:
        wohnung = default_choices['wohnung']
        bad = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
        wohnzimmer = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
        abstellraum = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
        esszimmer = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
        keller = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
        fliesenleger_instance = models.Fliesenleger(wohnung=wohnung, bad=bad, wohnzimmer=wohnzimmer, abstellraum=abstellraum, esszimmer=esszimmer, keller=keller)
        try:
            fliesenleger_instance.save()
        except:
            print('default Fliesenleger creation failed for wohnung')

def create_default_bodenbelaege(default_choices):
    if 'haus' in default_choices:
        haus = default_choices['haus']
        treppenhaus = "Naturstein Padang dunkel (G 654), geschliffen, auf den Treppen mit 3 cm starken Trittstufen und 2 cm starken Setzstufen, kein Untertritt, umlaufender Sockel, Hauseingang mit eingelassenem Fußabstreifer, Einfassung mit Alu-Rahmen, Größe ca. 120 x 80 cm."
        tiefgarage = "Grauer Schutzanstrich, ölfest, mit umlaufend grau gestrichenem Sockel, h=30 cm."
        
        bodenbelaege_instance = models.Bodenbelaege(haus=haus, treppenhaus=treppenhaus, tiefgarage=tiefgarage,)
        try:
            bodenbelaege_instance.save()
        except:
            print('default Bodenbelaege creation failed for haus')
    if 'wohnung' in default_choices:
        wohnung = default_choices['wohnung']
        bad = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
        kueche = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
        flur = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
        wohnzimmer = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
        gaeste_wc = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
        schlafzimmer = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
        kinderzimmer = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
        abstellraum = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
        bodenbelaege_instance = models.Bodenbelaege(wohnung=wohnung, bad=bad, kueche=kueche, flur=flur, wohnzimmer=wohnzimmer, gaeste_wc=gaeste_wc, schlafzimmer=schlafzimmer, kinderzimmer=kinderzimmer, abstellraum=abstellraum)
        try:
            bodenbelaege_instance.save()
        except:
            print('default Bodenbelaege creation failed for wohnung')

def create_default_schreiner(default_choices):
    if 'haus' in default_choices:
        haus = default_choices['haus']
        haustuer = "Tuermodell, Schliessung, Farbe, Glas"
        schreiner_instance = models.Schreiner(haus=haus, haustuer=haustuer,)
        try:
            schreiner_instance.save()
        except:
            print('default schreiner creation failed for haus')
    if 'wohnung' in default_choices:
        wohnung = default_choices['wohnung']
        wohnungstuer = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
        innentueren = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."

        schreiner_instance = models.Schreiner(wohnung=wohnung, wohnungstuer=wohnungstuer, innentueren=innentueren)
        try:
            schreiner_instance.save()
        except:
            print('default schreiner creation failed for wohnung')
    

def create_default_schlosser(default_choices):
    if 'haus' in default_choices:
        haus = default_choices['haus']
        eingangstuer = "Weiße Vollspantüren, Fabr. Prüm oder gleichwertig, glatte Oberfläche, dreiseitiger Doppelfalz und Obentüreschließer mit Scherengestänge, Stahlzargen treppenhausseitig farbig lackiert, wohnungsseitig weiß lackiert, Schall-Ex-Element, Dichtungsprofile, Edelstahlbeschläge als Wechsel-Sicherheitsgarnitur mit Profilzylinder, Türspion."
        schlosser_instance = models.Schlosser(haus=haus, eingangstuer=eingangstuer,)
        try:
            schlosser_instance.save()
        except:
            print('default schlosser creation failed for haus')
    if 'wohnung' in default_choices:
        wohnung = default_choices['wohnung']
        wohnungstuer = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."
        innentueren = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias voluptates minima libero deserunt, placeat assumenda unde sapiente doloremque corporis, voluptate quia quaerat ut officiis! Numquam dolorum animi, laboriosam deserunt velit."

        schlosser_instance = models.Schlosser(wohnung=wohnung, wohnungstuer=wohnungstuer, innentueren=innentueren)
        try:
            schlosser_instance.save()
        except:
            print('default schlosser creation failed for wohnung')

def create_default_schliessanlage(default_choices):
    if 'haus' in default_choices:
        haus = default_choices['haus']
        schliessplan = "Profilzylinder für Hauseingang, Wohnungseingang, Kellerflure, Fahrradräume, Kinderwagenräume, Zugänge zu der Tiefgarage sowie Hausanschluss- und Heizraum, Knauf-Zylinder für die Fluchttüren."
        sonstiges = "sonstiges"
        schliessanlage_instance = models.Schliessanlage(haus=haus, schliessplan=schliessplan, sonstiges=sonstiges)
        try:
            schliessanlage_instance.save()
        except:
            print('default Schliessanlage creation failed for haus')
    if 'wohnung' in default_choices:
        wohnung = default_choices['wohnung']
        schliessplan = "Profilzylinder für Hauseingang, Wohnungseingang, Kellerflure, Fahrradräume, Kinderwagenräume, Zugänge zu der Tiefgarage sowie Hausanschluss- und Heizraum, Knauf-Zylinder für die Fluchttüren."
        sonstiges = "sonstiges"
        schliessanlage_instance = models.Schliessanlage(wohnung=wohnung, schliessplan=schliessplan, sonstiges=sonstiges)
        try:
            schliessanlage_instance.save()
        except:
            print('default Schliessanlage creation failed for wohnung')





def create_default_sicherheitstechnik(default_choices):
    haus = default_choices['haus']
    alarmanlage = "verbundene Tueren,"
    tuerschliesser = "Sicherheitsstandard, Notfallschliessung"
    sicherheitsschloesser = "Schliessungen, Schluessel"
    sicherheitstechnik_instance = models.Sicherheitstechnik(haus=haus, alarmanlage=alarmanlage, tuerschliesser=tuerschliesser, sicherheitsschloesser=sicherheitsschloesser,)
    try:
        sicherheitstechnik_instance.save()
    except:
        print('default Sicherheitstechnik creation failed')

def create_default_aussenanlagern(default_choices):
    haus = default_choices['haus']
    terrassenbelaege = "Terrassen an Privatgärten: zu Gartenflächen eingefasst wie übrige Vegetationsflächen, in einer von drei Einfassungsseiten eine Treppe mit 5 Betonblockstufen, Breite ca. 50 cm, einseitig ein Handlauf, Bodenbelag-Aufbau wie Laufflächen, Bodenbelag aus Betonsteinplatten, ca. 40 x 40 cm, grau, Unterbau unter Terrassenplatten abgestimmt auf Dachaufbau."
    pflanzen = "Bepflanzung Gemeinschaftseigentum"
    pflaster = "Pflasterung Wege und Einfahrten, Terrassen"
    grundflache = "Einfassung zu Fahr- und Wegeflächen, Terrassen und Bahngrundstück in Ortbeton oder mit Fertigteil-Winkelelementen, Höhenbindung an Schattenfuge in den Lüftungselementen der Tiefgarage bzw. an Oberkante der Lüftungselemente im Bereich der Baumstandorte, Oberfläche Sichtbeton mindestens SB 2, bewehrt, Farbe betongrau, Fugen abgedichtet, Anschlüsse an Lüftungselemente abgedichtet."
    wegeflachen = "Für die angebotenen Produkte müssen Empfehlungen des Herstellers für die geforderte Belastung vorgelegt werden. Wege- und Platzflächen, Ökopflaster 20x10 cm, grau und anthrazit (Fahrflächen 10cm, Laufflächen 8cm Steinhöhe), Tragschicht unter Pflasterflächen abgestimmt auf Dachaufbau. Entwässerung vor Hauseingängen und bodentiefen Fenstern/Türen im EG mittels Kastenrinne und Anschluß an die Entwässerungsleitungen. Auf Schutzlage der Dachabdichtung Wasserleitprofile zur Ableitung des anfallenden Oberflächenwassers von Ostseite der Tiefgaragendecke zur Westseite, von Einlaufkasten zu Einlaufkasten, auf jedem 90° Knick einen Einlaufkasten setzen, in Drainageschicht integrieren. Stufenanlagen, Betonblockstufen grau, wie Betonsteinpflaster Wegeflächen. Seitliche Abstützung Rampe, wie Betonblockstufen."
    mulleinhausung = "Gebäudenahe Einhausungen: Müllschränke, Sichtbeton, betongrau, geräuscharme Stahltüren, abschließbar mit Halbzylinder, verzinkt, 1-3 Einstellmöglichkeiten, rückseitige und seitliche Anfüllung mit Pflanzsubstrat, Abdichtung dieser Seiten zum Schutz der Einhausung. Zentrale Müllsammlung: Stahlpfosten, Gittermatte verzinkt, Sichtschutzhöhe min. 2,0m, Pfette auf 2,4m, Sparren Hochkant-Rechteckrohr 30° geneigt auf Pfette montiert für reduzierte Einsehbarkeit aus den oberen Stockwerken, Aussparung für Lüftungsbauwerk der Tiefgarage, Tor Höhe wie Schichtschutz, min. 1,5 m lichte Weite."
    einfriedung = "In Richtung Bahn, an bewohntem EG, Gittermatte, Höhe 120 cm, verzinkt Poller in weiß-rot für Zufahrtsbeschränkung, herausnehmbar mit Dreikant Fahrradständer, Bügel aus T-Profil, ca. 70x35x6mm, Höhe 90cm , Flansch außen, verzinkt Zaun zwischen Haus 2 und Treppe zum Bahnhof, Gittermatte, zzgl. Verankerung u. Fundament"
    dachaufbau_tiefgarage_grundflache = "Bautenschutzmatte auf Dachabdichtung, Schutz- und Gleitlage, Drainageschicht aus Lava Körnung 2/16 oder vergleichbar, Dicke 10 cm, Filtervlies, Substrataufbau, auf gesamtem Tiefgaragendach. Auf der Ostseite, Fuge zwischen TG-Decke und aufgesetzter Mauer mit Profilblech, Steg eingearbeitet in Dachabdichtung, Flansch asymmetrisch auf Steg, verzinkt."
    dachaufbau_tiefgarage_park_wegeflache = "Bautenschutzmatte auf Dachabdichtung, Schutz- und Gleitlage, Drainageschicht aus Lava Körnung 2/16 oder vergleichbar, Dicke 10 cm, Filtervlies, Substrataufbau, auf gesamtem Tiefgaragendach. Auf der Ostseite, Fuge zwischen TG-Decke und aufgesetzter Mauer mit Profilblech, Steg eingearbeitet in Dachabdichtung, Flansch asymmetrisch auf Steg, verzinkt."
    aussenanlagern_instance = models.Aussenanlagern(haus=haus, terrassenbelaege=terrassenbelaege, pflanzen=pflanzen, pflaster=pflaster, grundflache=grundflache, wegeflachen=wegeflachen, mulleinhausung=mulleinhausung, einfriedung=einfriedung, dachaufbau_tiefgarage_grundflache=dachaufbau_tiefgarage_grundflache, dachaufbau_tiefgarage_park_wegeflache=dachaufbau_tiefgarage_park_wegeflache)
    try:
        aussenanlagern_instance.save()
    except:
        print('default aussenlagern creation failed')

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