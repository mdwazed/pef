"""
all classes and their common functionalities resides in this module
"""
from django.core.exceptions import ObjectDoesNotExist

from . import models

class Haus_fl:
    """
    haus class for front layer. this class is different from the .model.Haus class.
    all haus object instantiate from this class for further modification.
    
    """
    
    def __init__(self, pk):
        """
        construct a haus object collecting all data from all tables in db based on 
        provided pk of haus .
        """
        try:
            haus = models.Haus.objects.get(pk=pk)
        except ObjectDoesNotExist:
            print("haus not found in db")    
        self.haus_nr = haus.haus_nr
        self.display_nr = haus.display_nr
        
        try:
            self.architekt_plan = models.Architekt_plan.objects.get(haus=haus)
        except ObjectDoesNotExist:
            print("architekt components not found in db")
            self.architekt_plan = None
        try:
            self.erd_bau = models.Erdbau.objects.get(haus=haus)
        except ObjectDoesNotExist:
            print("erdbau components not found in db")
        try:
            self.rohbau = models.Rohbau.objects.get(haus=haus)
        except ObjectDoesNotExist:
            print("rohbau not found in db")
        try:
            self.dach = models.Dach.objects.get(haus=haus)
        except ObjectDoesNotExist:
            print("dach not found in db")
        try:
            self.fenster = models.Fenster.objects.get(haus=haus)
        except ObjectDoesNotExist:
            print("fenster not found in db")
        try:
            self.elektro = models.Elektro.objects.get(haus=haus)
        except ObjectDoesNotExist:
            print("fenster not found in db")
        try:
            self.innenputz = models.Innenputz.objects.get(haus=haus)
        except ObjectDoesNotExist:
            print("innenputz not found in db")
        try:
            self.estrich = models.Estrich.objects.get(haus=haus)
        except ObjectDoesNotExist:
            print("estrich not found in db")
        try:
            self.trockenbau = models.Trockenbau.objects.get(haus=haus)
        except ObjectDoesNotExist:
            print("trokenbau not found in db")
        try:
            self.aussenputz = models.Aussenputz.objects.get(haus=haus)
        except ObjectDoesNotExist:
            print("aussenputz not found in db")
        try:
            self.fliesenleger = models.Fliesenleger.objects.get(haus=haus)
        except ObjectDoesNotExist:
            print("fliesenleger not found in db")
        try:
            self.bodenbelaege = models.Bodenbelaege.objects.get(haus=haus)
        except ObjectDoesNotExist:
            print("bodenbelaege not found in db")
        try:
            self.schlosser = models.Schlosser.objects.get(haus=haus)
        except ObjectDoesNotExist:
            print("schlosser not found in db")
        try:
            self.schliessanlage = models.Schliessanlage.objects.get(haus=haus)
        except ObjectDoesNotExist:
            print("schliessanlage not found in db")
        try:
            self.sicherheitstechnik = models.Sicherheitstechnik.objects.get(haus=haus)
        except ObjectDoesNotExist:
            print("sicherheitstechnik not found in db")
            # self.aussenanlagern = models.Aussenanlagern.objects.get(haus=haus)
        try:
            self.tiefgaragenbeschichtung = haus.tiefgaragenbeschichtung
        except ObjectDoesNotExist:
            print("tiefgaragenbeschichtung components not found in db")

    def update(self):
        pass

    def __str__(self):
        return "Haus: " + str(self.haus_nr) + " Display nr: " + str(self.display_nr)




