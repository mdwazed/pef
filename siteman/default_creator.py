"""
    create haus, wohnung and other components with default settings,
    ready to save in db.
"""
from . import models



def create_default_haus_components(default_choices):
    """
    Create default haus components with user selected options.
    attach those components to the passed haus
    return the haus to the view to save 
    """
    print("------creating default haus--------")
    haus = default_choices['haus']
    try:
        create_default_architekt_plan(default_choices)
    except Exception as e:
        print('Error in creating default Architekt.' + str(e))
    try:
        create_default_erdbau(default_choices)
    except Exception as e:
        print('Error in creating default Erdbau.' + str(e))
    try:
        create_default_rohbau(default_choices)
    except Exception as e:
        print('Error in creating default Rohbau.' + str(e))
    try:
        create_default_dach(default_choices)
    except Exception as e:
        print('Error in creating default Dach.' + str(e))
    try:
        create_default_fenster(default_choices)
    except Exception as e:
        print('Error in creating default Fenster.' + str(e))
    try:
        create_default_elektro(default_choices)
    except Exception as e:
        print('Error in creating default Elektro.' + str(e))
    try:
        create_default_hls(default_choices)
    except Exception as e:
        print('Error in creating default HLS.' + str(e))
    try:
        create_default_innenputz(default_choices)
    except Exception as e:
        print('Error in creating default Innenputz.' + str(e))
    try:
        create_default_estrich(default_choices)
    except Exception as e:
        print('Error in creating default Estrich.' + str(e))
    try:
        create_default_trockenbau(default_choices)
    except Exception as e:
        print('Error in creating default Trockenbau.' + str(e))
    try:
        create_default_aussenputz(default_choices)
    except Exception as e:
        print('Error in creating default Aussenputz.' + str(e))
    try:
        create_default_bodenbelaege(default_choices)
    except Exception as e:
        print('Error in creating default Bodelbelage.' + str(e))
    try:
        create_default_turen(default_choices)
    except Exception as e:
        print('Error in creating default Turen.' + str(e))
    try:
        create_default_schlosser(default_choices)
    except Exception as e:
        print('Error in creating default Schlosser.' + str(e))
    try:
        create_default_schliessanlage(default_choices)
    except Exception as e:
        print('Error in creating default Schliessanlage.' + str(e))
    try:
        create_default_sicherheitstechnik(default_choices)
    except Exception as e:
        print('Error in creating default Sicherheitstechnik.' + str(e))
    try:
        create_default_aussenanlagern(default_choices)
    except Exception as e:
        print('Error in creating default Sicherheitstechnik.' + str(e))

    return haus 

def create_default_wohnung_components(default_choices):
    print('-------- creating default wohnung---------')
    wohnung = default_choices['wohnung']
    try:
        create_default_fenster(default_choices)
    except Exception as e:
        print('creation of default fenster for wohnung failed' + str(e))
    try:
        create_default_raumbuch_elektro(default_choices)
    except Exception as e:
        print('creation of default Raumbuch_elektro for wohnung failed' + str(e))
    try:
        create_default_sanitaer(default_choices)
    except Exception as e:
        print('creation of default sanitar for wohnung failed' + str(e))
    try:
        create_default_innenputz(default_choices)
    except Exception as e:
        print('creation of default innenputz for wohnung failed' + str(e))
    try:
        create_default_estrich(default_choices)
    except Exception as e:
        print('creation of default estrich for wohnung failed' + str(e))
    try:
        create_default_trockenbau(default_choices)
    except Exception as e:
        print('creation of default trockenbau for wohnung failed' + str(e))
    try:
        create_default_maler(default_choices)
    except Exception as e:
        print('creation of default maler for wohnung failed' + str(e))
    try:
        create_default_bodenbelaege(default_choices)
    except Exception as e:
        print('creation of default Bodenbelaege for wohnung failed' + str(e))
    try:
        create_default_turen(default_choices)
    except Exception as e:
        print('creation of default turen for wohnung failed' + str(e))
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
    print('creating default erdbau')
    haus = default_choices['haus']
    erdbau = "Aushub, Boeschung, etc."
    erdbau_instance = models.Erdbau(haus=haus, erdbau=erdbau)
    try:
        erdbau_instance.save()
    except Exception as e:
        print('default erdbau creation failed' + str(e))


def create_default_rohbau(default_choices):
    print('creating default rohbau')
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
    wohnungstrenwande = "Stahlbeton und Kalksandstein."
    tragendeinnenwande = "Stahlbeton und Kalksandstein."
    nichttragendeinnenwande = "10 cm Mauerwerk aus massiven Gipswandbauplatten. Installationswände werden ausgeführt als mit Gipskarton 2-fach beplankte Metallständerwand, Wandstärke 15-35cm."
    horizontale_abdichtung = "Bitumenbahnen in der Lagerfuge der Mauerwerkswände im Kellergeschoss und Erdgeschoss. Auf der Tiefgaragendecke Abdichtung mit Bitumbahnen, 2-lagig, für gefällelose Ausführung, obere Lage wurzelfest."    
    vertikale_abdictung = "Abdichtung der erdberührten Außenwände Kellergeschoss und Tiefgarage als wasserundurchlässige Konstruktion. Abdichtung des Sockelbereichs im EG mit Bitumenbahn gegen zeitweise aufstauendes Sickerwasser."
    tiefgaragenrampe = "Stahlbeton mit Oberflächenschutzsystem."
    treppen = "Treppenläufe aus Stahlbeton mit Schallenkoppelung."
    balkon = "Gefälleestrich auf Stahlbetonfertigteil, thermisch getrennt oder gedämmt. Integrierte Rinne mit Ablauf"
    rohbau = models.Rohbau(haus=haus, grundung=grundung, geschossdecken=geschossdecken,
            aussenwande_kellergeschoss=aussenwande_kellergeschoss, aussenwande_eg_og_dg=aussenwande_eg_og_dg,
            wohnungstrenwande=wohnungstrenwande, tragendeinnenwande=tragendeinnenwande, 
            nichttragendeinnenwande=nichttragendeinnenwande, horizontale_abdichtung=horizontale_abdichtung,
            vertikale_abdictung=vertikale_abdictung, tiefgaragenrampe=tiefgaragenrampe, treppen=treppen, balkon=balkon)
    try:
        rohbau.save()
    except Exception as e:
        print('default rohbau save failed' + str(e))


def create_default_dach(default_choices):
    print('creating default dach')
    haus = default_choices['haus']
    hauptdach = "Wohngebäude: Flachdach Stahlbeton, mit Dampfsperre, Gefälledämmung und Dachabdichtung aus Bitumenbahnen, 2-lagig, und extensiver Begrünung."
    dachterrassen = "dachterrassen."
    spenglerarbeiten = "spenglerarbeiten."
    dach_instance = models.Dach(haus=haus, hauptdach=hauptdach, dachterrassen=dachterrassen, spenglerarbeiten=spenglerarbeiten)
    try:
        dach_instance.save()
    except Exception as e:
        print('default dach saving failed' + str(e))



def create_default_fenster(default_choices):
    if 'haus' in default_choices:
        haus = default_choices['haus']  
        # beschattung = "beschatung"
        if default_choices['fenster_beschattung']=='nbk':
            beschattung = "Aufsatzrollladenkästen an allen Wohnungsfenstern, außer im Treppenhaus."
        elif default_choices['fenster_beschattung']=='aufsr':
            beschattung = "Aufsatzrollladenkästen an allen Wohnungsfenstern, außer im Treppenhaus."
        elif default_choices['fenster_beschattung']=='rse':
            beschattung = "Aufsatzrollladenkästen an allen Wohnungsfenstern, außer im Treppenhaus."
        kellergeschoss = "Kunststoff-Fenster mit Leibungsrahmen."
        erdgeschoss = "Kunststoff-Fenster, innen weiß, außen grau foliert, mit 3-fach-Verglasung, Dreh- bzw. Drehkippflügel mit Eingriffbedienung, teilweise Festverglasung, im EG abschließbare Griffe und Einbruchwiderstand RC 2 N.."
        regelgeschoss = "Kunststoff-Fenster, innen weiß, außen grau foliert, mit 3-fach-Verglasung, Dreh- bzw. Drehkippflügel mit Eingriffbedienung, teilweise Festverglasung, im EG abschließbare Griffe und Einbruchwiderstand RC 2 N."
        dachgeschoss = "Kunststoff-Fenster, innen weiß, außen grau foliert, mit 3-fach-Verglasung, Dreh- bzw. Drehkippflügel mit Eingriffbedienung, teilweise Festverglasung, im EG abschließbare Griffe und Einbruchwiderstand RC 2 N."
        treppenhaus = "Eingangselement aus farbigen Metallprofilen mit Isolierverglasung, je Treppenhaus ein Oberlicht als Dachausstieg mit RWA-Funktion, incl. Schlagtaster im EG und im obersten Geschoß, und ein feststehendes, lichtbandartiges Oberlicht oberhalb der Treppenanlage. "
        tiefgarage = "Kunststoff-Fenster mit Leibungsrahmen."
        fenster = models.Fenster(haus=haus, beschattung=beschattung, kellergeschoss=kellergeschoss, erdgeschoss=erdgeschoss, regelgeschoss=regelgeschoss, dachgeschoss=dachgeschoss, treppenhaus=treppenhaus, tiefgarage=tiefgarage)
        try:
            fenster.save()
        except Exception as e:
            print('default fenster creation failed for haus' + str(e))
    if 'wohnung' in default_choices:
        wohnung = default_choices['wohnung']
        schwellen = "Zum Balkon Standard Austrittsschwelle 2cm "
        sichtschutz = "In Bädern Satinato"
        fensterbaenke = "Naturstein Padang dunkel (G 654), geschliffen"
        fenster = models.Fenster(wohnung=wohnung, schwellen=schwellen, sichtschutz=sichtschutz, fensterbaenke=fensterbaenke,)
        try:
            fenster.save()
        except:
            print('default fenster save failed for wohnung')


def create_default_elektro(default_choices):
    if 'haus' in default_choices:
        haus = default_choices['haus']
        elektro = "Unterputzinstallation in den Wohnungen, im Treppenhaus und in der Schleuse zur Tiefgarage. Aufputzinstallation im Untergeschoß, mit Ausnahme der vorstehend genannten Bereiche, und in der Tiefgarage."
        treppenhaus= "LED Wand- und/oder Deckenleuchten, mit integriertem Bewegungsmelder. Beleuchtete Fluchtpiktogramme im Untergeschoß. Die Klingeltaster für die Wohnungen befinden sich jeweils neben der Wohnungseingangstüre. Die innen liegenden Treppenhäuser werden mit einer Sicherheitsbeleuchtung mittels Einzelbatterieleuchten in Bereitschaftsschaltung ausgestattet."
        keller= "Langfeldleuchten ohne Vorschaltgerät mit Bewegungsmelder"
        private_abstellraum = "1 Ausschaltung mit darunter liegender Steckdose\n1 Schiffsarmatur"
        tiefgarage= "Eine abschließbare Steckdose mit individueller Verbrauchserfassung je Stellplatz"
        medientechnik = "Vom Übergabepunkt im Kellergeschoß wird zu jeder Wohnung ein Telefonkabel (IYSTY) sowie ein Multimedia-Datenkabel (S/FT) Kategorie 7A, im geschlossenen Rohrsystem M25, bis zur wohnungseigenen, 4-reihigen, mit Montageplatte, Patch-Panel und Schuko-Steckdose bestückter Kommunikationsverteilung verlegt. Von hier sternförmige Unterputzanbindung mittels Datenkabel (S/FT) Kategorie 7A zu den 2-fach RJ45-Anschlußdosen samt Auflegearbeiten gemäß Raumbuch Elektro. Vom Übergabepunkt im Kellergeschoß wird bis zur Kommunikationsverteilung in jeder Wohnung ein Antennenkoaxialkabel >100dB, Class A, im geschlossenen Rohrsystem M25, verlegt. Von hier sternförmige Unterputzanbindung mittels Antennenkoaxialkabel >100dB, Class A, bis zu den Anschlussdosen gemäß Raumbuch Elektro. Alle Anschlussdosen in der Wohnung sowie die Anschlussleiste in der Wohnungsverteilung werden betriebsfertig montiert und angeschlossen zur Verfügung gestellt. Ausnahme sind die Antennenanschlussdosen, die vom jeweiligen Versorger geliefert, montiert und angeschlossen werden. Abdeckrahmen und Zentralplatte für die Antennenanschlussdosen sind jedoch Bestandteil der Leistung des Verkäufers. Die Freischaltung und das Auflegen der Multimedia-Datenkabel und der Antennenleitung im Kellergeschoß und an der wohnungseigenen Kommunikationsverteilung muss beim jeweiligen Versorger beantragt werden und ist nicht Bestandteil der Leistung des Verkäufers."
        freiflachen = "Pollerleuchten als Orientierungsleuchte für Gehwege und Plätze, mit Fassung geeignet für LED-Leuchtmittel, Schaltung über Dämmerungsschalter. Ausleuchtung der öffentliche Durchwegung vor Haus 1 und Haus 2 mit Mastleuchten, Schaltung über Dämmerungsschalter."
        elektro_instance = models.Elektro(haus=haus, elektro=elektro, treppenhaus=treppenhaus, keller=keller, private_abstellraum=private_abstellraum,
        tiefgarage=tiefgarage, medientechnik=medientechnik, freiflachen=freiflachen,)
        try:
            elektro_instance.save()
        except Exception as e:
            print('default elektro saving failed' + str(e))
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
        raumbuch_elektro_instance = models.Raumbuch_elektro(wohnung=wohnung, bad=bad, kueche=kueche, flur=flur, wohnzimmer=wohnzimmer, 
            gaeste_wc=gaeste_wc, schlafzimmer=schlafzimmer, kinderzimmer=kinderzimmer, abstellraum=abstellraum, schalterprogramm=schalterprogramm,)
        try:
            raumbuch_elektro_instance.save()
        except Exception as e:
            print("raumbuch_elektro_instance save failed" + str(e))

def create_default_hls(default_choices):
    if 'haus' in default_choices:
        haus = default_choices['haus']
        energiegwinnung = "„Zum Zweck der Wärmeversorgung der Eigentumswohnanlage errichtet ein gewerblicher Wärmelieferant eine zentrale Wärmeversorgungsanlage auf eigene Rechnung, die in seinem Eigentum steht und nicht Bestandteil des gemeinschaftlichen Eigentums wird. Hierzu wird mit dem Wärmelieferanten ein Wärmelieferungsvertrag über eine Vertragslaufzeit von 15 Jahren abgeschlossen, dem der Miteigentümer (Käufer) für den Umfang seiner Miteigentumsanteile vorbehaltlos zustimmt. Die Wohnungseigentümergemeinschaft als solches tritt in den bestehenden Wärmelieferungsvertrag gemäß § 10 Abs. 8 WEG ein.“ Leistung des Wärmelieferanten: Zentrale Wärmeerzeugungsanlage mit Pelletskessel, Gas-Brennwertkessel, 3 Stück Blockheizkraftwerk mit erforderlicher Wärmeleistung, mit Pufferspeichern, Pelletlagerraum, automatische Pelletbeschickung, Schornsteinanlage, Ausdehnungsgefäße, automatische Wassernachspeisung, Regelanlage, Heizkreispumpen und Armaturen, Fernüberwachung mit GLT, gebäudeweise außentemperaturabhängige Regelung, gebäudeweiser Warmwasserbehälter (WWB) mit Hygiene-Kombispeicher, Anschluss des WWB an das Heizungssystem mit Ladepumpe, Regelung, und Wärmemengenzähler, geregelter Heizkreis mit Mischer, Regelgerät, Heizkreispumpe und Armaturen. Verlegung der Verteilleitungen Heizung vom Heizraum in die jeweiligen Häuser mit gedämmten Doppelmantelrohren und Datenkabel. Verlegung der Gasleitungen ab HAR in den Heizraum, einschließlich Anschlüsse der Wärmeerzeuger. Anschluss der Sekundärkreise an die installierten Absperrarmaturen der geregelten Heizkreise je Gebäude."
        heizung = "Fußbodenheizung in allen Wohnräumen, nicht im Abstellraum. Die Flurbereiche ohne Heizlast werden mit einem separat regelbaren Heizkreis versehen."
        be_und_entluftung = "In innen liegenden Bädern, Duschbädern und Abstellräumen Luftabsaugung über dezentrale Abluftanlage (Einrohrlüftung) über Dach, Luftnachströmung über Außenluftdurchlaß (ALD) auf Rollladenkasten. Lüftung zum Feuchteschutz und reduzierte Lüftung unter Einbindung der Einrohrlüfter."
        verbauchserfassung = "Kalt - und Warmwasserzähler mit Funkablesung auf Mietbasis. Wohnungsweise Wärmemengenzähler mit Funkablesung auf Mietbasis."
        klimatisierung = "klimatisierung"
        kalt_und_warmwasser = "Verteil- und Steigeleitungen aus Edelstahlrohr, Objektanbindeleitungen aus Kunststoff-Aluminium-Verbundrohr."
        zirkulationsleitung = "An allen Warmwasserauslässen vorhanden"
        entwasserung = "Leitungen aus Kunststoff, Fallstränge aus schallgedämmtem Kunststoffrohr."
        wasserenthartung = "wasserenthartung"
        hls = models.Hls(haus=haus, energiegwinnung=energiegwinnung, heizung=heizung, be_und_entluftung=be_und_entluftung,
            verbauchserfassung=verbauchserfassung, klimatisierung=klimatisierung, kalt_und_warmwasser=kalt_und_warmwasser, zirkulationsleitung=zirkulationsleitung,
            entwasserung=entwasserung, wasserenthartung=wasserenthartung)
        try:
            hls.save()
        except Exception as e:
            print('default hls creation failed for haus' + str(e))

def create_default_sanitaer(default_choices):
    if 'wohnung' in default_choices:
        wohnung = default_choices['wohnung']
        aussenzapfstelle = "Eine frostsichere, selbstentleerende Armatur mit Schlauchverschraubung je Dachterrasse, 2 Stück an einer Gebäudeaußenwand im Bereich der gemeinschaftlichen Freiflächen und 1 Stück je EG-Wohnung mit Terrasse."
        dusche = "Duschbereich mit Board und Bodeneinlauf, oder mit flacher Stahlblech-Duschwanne mit ca. 2,5cm Aufkantung im gedämmten Wannenträger. Alle Duschen ohne Duschabtrennung. Aufputz-Einhand-Brausebatterie Fabrikat F. Grohe, Typ Lineare, und Brausegarnitur bestehend aus Brausestange, Handbrause und 1,50 m kunststoffummanteltem Metallschlauch."
        badewanne = "Weiße Stahlblech-Einbauwanne, Fabrikat Kaldewei 1,70 x 0,75 m, gedämmter Wannenträger, verchromte Aufputz-Einhand-Wannenbatterie, Fabrikat F. Grohe, Typ Lineare, und Brausegarnitur bestehend aus Handbrause mit kunststoffummanteltem Metallschlauch, Excenterverschluss."
        waschtisch_im_bad = "Weißer Keramik-Einzelwaschtisch, Fabrikat Keramag Renova Nr. 1, eckig, Größe ca. 65 x 45 cm, mit verchromter Einhand-Hebelmischbatterie, Fabrikat F. Grohe, Typ Lineare, Zugstangenablaufgarnitur."
        toilette = "Weißes, wandhängendes Keramik-Tiefspülklosett, Fabrikat Keramag Renova 1, Einbauspülkasten Geberit oder gleichwertig mit weißer Betätigungsplatte und Spartaste, schwerer Kunststoff-WC Sitz mit Deckel und Metallscharnieren."
        heizkorper = "Handtuchheizkörper im Bad mit horizontalen Rundrohren und Betrieb über elektrische Heizpatrone. Im Treppenhaus ein zentraler Heizkörper im Untergeschoß."
        waschtisch_im_duschbad_wc = "Weißer Keramik-Einzelwaschtisch, Fabrikat Keramag Renova Nr. 1, eckig, Größe ca. 55 x 44 cm, mit verchromter Einhand -Hebelmischbatterie, Fabrikat F. Grohe, Typ Lineare, Zugstangenablaufgarnitur."
        waschmaschinenanschluss = "Gerätegeruchsverschluss mit integrierter Wasserversorgung, verchromt."
        spuelmaschinenanschluss = "Kombinationseckventil Kaltwasser, Eckventil Warmwasser und Abwasseranschluss am Installationsschacht."
        sanitaer = models.Sanitaer(wohnung=wohnung, aussenzapfstelle=aussenzapfstelle, dusche=dusche, badewanne=badewanne, waschtisch_im_bad=waschtisch_im_bad,
         toilette=toilette, heizkorper=heizkorper, waschtisch_im_duschbad_wc=waschtisch_im_duschbad_wc,
         waschmaschinenanschluss=waschmaschinenanschluss, spuelmaschinenanschluss=spuelmaschinenanschluss)
        try:
            sanitaer.save()
            print("default sanitar for wohnung created ")
        except Exception as e:
            print('default sanitar save failed for haus' + str(e))



def create_default_innenputz(default_choices):
    if 'haus' in default_choices:        
        haus = default_choices['haus']
        innenputz_bad = " for haus  Im Bereich der Dusche und Badewanne raumhoch gefliest, im Bereich der 1,20 m hohen Vorwandinstallation auf Höhe der Vorwand gefliest, incl. der oberen Ablagefläche. Übrige Flächen ohne Fliesen gemäß 6.2.1."
        innenputz_wohnraueme = " for haus Raufasertapete mit weißem Dispersionsanstrich. "
        innenputz_treppenhauswande = "Verputzt"
        innenputz_treppenhausdecken = "Spachtelung/Dünnputz, alternativ verputzt"
        innenputz = models.Innenputz(haus=haus, innenputz_bad=innenputz_bad, innenputz_wohnraueme=innenputz_wohnraueme,
            innenputz_treppenhauswande=innenputz_treppenhauswande, innenputz_treppenhausdecken=innenputz_treppenhausdecken)
        try:
            innenputz.save()
        except Exception as e:
            print('default innenputz creation failed for haus' + str(e))
    if 'wohnung' in default_choices:
        wohnung = default_choices['wohnung']
        innenputz_bad = "n.a."
        innenputz_wohnraueme = "n.a. "
        innenputz = models.Innenputz(wohnung=wohnung, innenputz_bad=innenputz_bad, innenputz_wohnraueme=innenputz_wohnraueme)
        try:
            innenputz.save()
        except:
            print('default innenputz creation failed for wohnung')

def create_default_estrich(default_choices):
    if 'haus' in default_choices:
        haus = default_choices['haus']
        dammplatten = "Schwimmender Heizestrich auf Trittschall- und Wärmedämmplatten in den Wohnungen. Schwimmender Estrich im Treppenhaus, auch im Untergeschoß."
        wohnraume = "Schwimmender Heizestrich auf Trittschall- und Wärmedämmplatten in den Wohnungen. Schwimmender Estrich im Treppenhaus, auch im Untergeschoß."
        bader = "bader"
        estrich_instance = models.Estrich(haus=haus, dammplatten=dammplatten, wohnraume=wohnraume, bader=bader)
        try:
            estrich_instance.save()
        except Exception as e :
            print('default estrich  creation failed for haus' + str(e))

    if 'wohnung' in default_choices:
        wohnung = default_choices['wohnung']
        fussbodenaufbau_wohnraume = "8mm."
        fussbodenaufbau_bad = "15mm"
        estrich_instance = models.Estrich(wohnung=wohnung, fussbodenaufbau_wohnraume=fussbodenaufbau_wohnraume, fussbodenaufbau_bad=fussbodenaufbau_bad)
        try:
            estrich_instance.save()
        except:
            print('default estrich  save failed for wohnung')


def create_default_trockenbau(default_choices):
    if 'haus' in default_choices:
        haus = default_choices['haus']
        wande = "Tapezierfähig verputzt bzw. gespachtelt Qualitätsstufe Q2."
        decken = "Tapezierfähig verputzt bzw. gespachtelt Qualitätsstufe Q2."
        vorsatzschalen = "Mit Gipskarton 2-fach beplankte Metallständerwand."
        installationsschachte = "Mit Gipskarton 2-fach beplankte Metallständerwand."
        trockenbau_instance = models.Trockenbau(haus=haus, wande=wande, decken=decken, vorsatzschalen=vorsatzschalen,
            installationsschachte=installationsschachte)
        try:
            trockenbau_instance.save()
        except Exception as e:
            print('default trockenbau save failed for haus.' + str(e))
    if 'wohnung' in default_choices:
        wohnung = default_choices['wohnung']
        wande = "Tapezierfähig verputzt bzw. gespachtelt Qualitätsstufe Q3."
        decken = "Tapezierfähig verputzt bzw. gespachtelt Qualitätsstufe Q2."
        vorsatzschalen = "Mit Gipskarton 2-fach beplankte Metallständerwand"
        trockenbau_instance = models.Trockenbau(wohnung=wohnung, wande=wande, decken=decken, vorsatzschalen=vorsatzschalen)
        try:
            trockenbau_instance.save()
        except:
            print('default trocken save failed for wohung')

def create_default_maler(default_choices):

    if 'wohnung' in default_choices:
        wohnung = default_choices['wohnung']
        tapete = "Raufasertapete "
        farbe = "weißer Dispersionsanstrich."
        maler_instance = models.Maler(wohnung=wohnung, tapete=tapete, farbe=farbe)
        try:
            maler_instance.save()
        except:
            print('default maler save failed for wohnung')

def create_default_aussenputz(default_choices):
    haus = default_choices['haus']
    unterputz = "Außenputz mit 3 mm Körnung auf Wärmedämmung"
    edelputz = "edelputz"
    sockel = "Gefilzter Sockelputz auf Wärmedämmung."
    aussenputz_instance = models.Aussenputz(haus=haus, unterputz=unterputz, edelputz=edelputz, sockel=sockel)
    try:
        aussenputz_instance.save()
    except Exception as e:
        print('default erdbau creation failed' + str(e))


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
        keller = "Grauer Schutzanstrich, ölfest, mit umlaufend grau gestrichenem Sockel, h=30 cm."
        technikraum = "Grauer Schutzanstrich, ölfest, mit umlaufend grau gestrichenem Sockel, h=30 cm."
        
        bodenbelaege_instance = models.Bodenbelaege(haus=haus, treppenhaus=treppenhaus, tiefgarage=tiefgarage,
            keller=keller, technikraum=technikraum)
        try:
            bodenbelaege_instance.save()
        except Exception as e:
            print('Default Bodenbelage save failed for haus' + str(e))
    if 'wohnung' in default_choices:
        wohnung = default_choices['wohnung']
        bad = "Fliesen, orthogonal verlegt. Bereiche ohne Wandfliesen mit Fliesensockel"
        kueche = "Fliesen, orthogonal verlegt. Bereiche ohne Wandfliesen mit Fliesensockel"
        flur = "Mosaikparkett Eiche rustikal, 8 mm, ölgewachst"
        wohnzimmer = "Mosaikparkett Eiche rustikal, 8 mm, ölgewachst"
        gaeste_wc = "Fliesen, orthogonal verlegt. Bereiche ohne Wandfliesen mit Fliesensockel"
        schlafzimmer = "Mosaikparkett Eiche rustikal, 8 mm, ölgewachst"
        kinderzimmer = "Mosaikparkett Eiche rustikal, 8 mm, ölgewachst"
        abstellraum = "Fliesen, orthogonal verlegt. Bereiche ohne Wandfliesen mit Fliesensockel"
        bodenbelaege_instance = models.Bodenbelaege(wohnung=wohnung, bad=bad, kueche=kueche, flur=flur, wohnzimmer=wohnzimmer, gaeste_wc=gaeste_wc,
         schlafzimmer=schlafzimmer, kinderzimmer=kinderzimmer, abstellraum=abstellraum)
        try:
            bodenbelaege_instance.save()
        except:
            print('default Bodenbelaege save failed for wohnung')

def create_default_turen(default_choices):
    if 'haus' in default_choices:
        haus = default_choices['haus']
        haustuer = "Tuermodell, Schliessung, Farbe, Glas"
        brandschutzturen = "brandschutzturen"
        schleusenturen = "schleusenturen"
        kellerflurturen = "kellerflurturen"
        turen_instance = models.Turen(haus=haus, haustuer=haustuer, brandschutzturen=brandschutzturen, schleusenturen=schleusenturen,
            kellerflurturen=kellerflurturen, )
        try:
            turen_instance.save()
        except:
            print('default turen creation failed for haus')
    if 'wohnung' in default_choices:
        wohnung = default_choices['wohnung']
        wohnungstur = "Weiße Vollspantüren, Fabr. Prüm oder gleichwertig, glatte Oberfläche, dreiseitiger Doppelfalz und Obentüreschließer mit Scherengestänge, Stahlzargen treppenhausseitig farbig lackiert, wohnungsseitig weiß lackiert, Schall-Ex-Element, Dichtungsprofile, Edelstahlbeschläge als Wechsel-Sicherheitsgarnitur mit Profilzylinder, Türspion."
        innenturen = "Weiße Röhrenspantüren, Fabr. Prüm oder gleichwertig, mit glatter Oberfläche, dreiseitig überfälzt, mit dreiseitiger Dichtung, Edelstahlbeschläge mit Rosetten, Buntbart-Schloss, Futter und Bekleidung weiß."
        turen_instance = models.Turen(wohnung=wohnung, wohnungstur=wohnungstur, innenturen=innenturen)
        try:
            turen_instance.save()
        except:
            print('default turen save failed for wohnung')
    

def create_default_schlosser(default_choices):
    if 'haus' in default_choices:
        haus = default_choices['haus']
        treppenglander = "Lackiertes Stahlgeländer, Handlauf in Holz auf Obergurt montiert, Füllung mit senkrechten Flachstahlstäben und Flachstahlober- und Untergurt."
        balkongelander = "Stahlgeländer als Absturzsicherung in verzinkter Ausführung, feinverputzt und pulverbeschichtet. Füllung mit senkrechten Flachstahlstäben, für Balkone zum Teil mit farbig beschichtetem Alu-Blech. Obergurt aus Rechteckhohlprofil, Untergurt bzw. Rahmen aus Flachstahl."
        absturzsicherungen = "Bodentiefe Fenster ab dem 1.OG mit absturzsichernder Festverglasung unterhalb des Fensterflügels."
        kellerabtrennungen = "Verzinkte, luftdurchlässige Stahllamellenprofile auf Metallunterkonstruktion bzw. Mauerwerk."
        rollgittertor = "Sektionaltor mit Funkfernbedienung"
        schlosser_instance = models.Schlosser(haus=haus, treppenglander=treppenglander, balkongelander=balkongelander, 
            absturzsicherungen=absturzsicherungen, kellerabtrennungen=kellerabtrennungen, rollgittertor=rollgittertor,)
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
    if 'haus' in default_choices:
        haus = default_choices['haus']
        alarmanlage = "alarmanlage"
        videouberwachung = "videouberwachung"
        sicherheitsschloesser = "sicherheitsschloesser"
        sicherheitstechnik_instance = models.Sicherheitstechnik(haus=haus, alarmanlage=alarmanlage, videouberwachung=videouberwachung,
         sicherheitsschloesser=sicherheitsschloesser,)
        try:
            sicherheitstechnik_instance.save()
        except:
            print('default Sicherheitstechnik saving failed')

def create_default_aussenanlagern(default_choices):
    if 'haus' in default_choices:
        haus = default_choices['haus']
        terrassenbelaege = "Terrassen an Privatgärten: zu Gartenflächen eingefasst wie übrige Vegetationsflächen, in einer von drei Einfassungsseiten eine Treppe mit Betonblockstufen, Breite ca. 50 cm, einseitig ein Handlauf, Bodenbelag aus Betonsteinplatten, ca. 40 x 40 cm, grau."
        vegetationsflachen = "Verfüllung mit Baum- oder Pflanzsubstrat, Düngung, Fertigstellungspflege und 1 Jahr Entwicklungspflege der Allgemeinflächen. Allgemeine Grünflächen auf der Ostseite mit Sekuranten. Private Grünflächen: Raseneinsaat. Allgemeine Grünflächen: bepflanzt mit Staudenmischungen und Bäumen. Hecke, Ostseite: Hainbuche 50-70 cm Rankpflanzen für zentrale Müllsammlung."
        pflaster = "Pflasterung Wege und Einfahrten, Terrassen"
        wegeflachen = "Wege- und Platzflächen, Ökopflaster 20x10 cm, grau und anthrazit. Entwässerung vor Hauseingängen und bodentiefen Fenstern/Türen im EG mittels Kastenrinne. Auf Schutzlage der Dachabdichtung Wasserleitprofile zur Ableitung des anfallenden Oberflächenwassers. Stufenanlagen, Betonblockstufen grau, wie Betonsteinpflaster Wegeflächen. Seitliche Abstützung Rampe, wie Betonblockstufen."
        mulleinhausung = "Gebäudenahe Einhausungen: Müllschränke, Sichtbeton, betongrau, geräuscharme Stahltüren, abschließbar mit Halbzylinder, verzinkt, 1-3 Einstellmöglichkeiten, rückseitige und seitliche Anfüllung mit Pflanzsubstrat, Abdichtung dieser Seiten zum Schutz der Einhausung. Zentrale Müllsammlung: Stahlpfosten, Gittermatte verzinkt, Sichtschutzhöhe min. 2,0m, Pfette auf 2,4m, Sparren Hochkant-Rechteckrohr 30° geneigt auf Pfette montiert für reduzierte Einsehbarkeit aus den oberen Stockwerken, Aussparung für Lüftungsbauwerk der Tiefgarage, Tor Höhe wie Schichtschutz, min. 1,5 m lichte Weite."
        einfriedung = "In Richtung Bahn, an bewohntem EG, Gittermatte, Höhe 120 cm, verzinkt Poller in weiß-rot für Zufahrtsbeschränkung, herausnehmbar mit Dreikant Fahrradständer, Bügel aus T-Profil, ca. 70x35x6mm, Höhe 90cm , Flansch außen, verzinkt Zaun zwischen Haus 2 und Treppe zum Bahnhof, Gittermatte, zzgl. Verankerung u. Fundament"
        dachaufbau_tiefgarage_befestigt = "Bautenschutzmatte auf Dachabdichtung, Schutz- und Gleitlage, Drainageschicht aus Lava Körnung 2/16 oder vergleichbar, Dicke 10 cm, Filtervlies, Substrataufbau, auf gesamtem Tiefgaragendach. Auf der Ostseite, Fuge zwischen TG-Decke und aufgesetzter Mauer mit Profilblech, Steg eingearbeitet in Dachabdichtung, Flansch asymmetrisch auf Steg, verzinkt."
        dachaufbau_tiefgarage_grun = "Bautenschutzmatte auf Dachabdichtung, Schutz- und Gleitlage, Drainageschicht aus Lava Körnung 2/16 oder vergleichbar, Dicke 10 cm, Filtervlies, Substrataufbau, auf gesamtem Tiefgaragendach. Auf der Ostseite, Fuge zwischen TG-Decke und aufgesetzter Mauer mit Profilblech, Steg eingearbeitet in Dachabdichtung, Flansch asymmetrisch auf Steg, verzinkt."
        feuerwehraufstellflachen = "Kunststoff Rasenwaben, Substrat verfüllt, Raseneinsaat."
        aussenanlagern_instance = models.Aussenanlagern(haus=haus, terrassenbelaege=terrassenbelaege, vegetationsflachen=vegetationsflachen,
         pflaster=pflaster, wegeflachen=wegeflachen, mulleinhausung=mulleinhausung, einfriedung=einfriedung,
         dachaufbau_tiefgarage_befestigt=dachaufbau_tiefgarage_befestigt, dachaufbau_tiefgarage_grun=dachaufbau_tiefgarage_grun,
         feuerwehraufstellflachen=feuerwehraufstellflachen, )
        try:
            aussenanlagern_instance.save()
        except Exception as e:
            print('default aussenlagern creation failed' + str(e))

