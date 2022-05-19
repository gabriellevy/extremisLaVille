import random
from abs.humanite import metier
from abs.humanite import portrait
from chapitres.classes import jeanne

class PortraitJeanne(portrait.Portrait):

    def DeterminerPortraitPersoPrincipal(self, situation, masculin):
        """
        retourne l'adresse du portrait à afficher pour le perso courant
        """
        ageAnnees = situation.AgeEnAnnees()
        traitsPerso = situation.GetDicoTraits()

        return self.DeterminerPortraits(situation, ageAnnees, "Jeanne", traitsPerso, masculin)

    def DeterminerPortraits(self, situation, ageAnnees, nom, valeursTraits, masculin):
        """
        retourne l'adresse du portrait à afficher pour le perso courant
        valeursTraits : dico contenant en clé le nom des traits possédés par le personnage et en valeur leur niveau
        """
        portraits = []
        portraitCourant = situation.GetValCarac(portrait.Portrait.C_PORTRAIT)

        # if nom == "Jeanne":
        #     portraits.append("images/portraits/clovis_15.jpg")
        # if nom == clovis.Clovis.C_NOM_BASINE:
        #     portraits.append("images/portraits/basine.jpg")
        # if nom == clovis.Clovis.C_NOM_CHILDERIC:
        #     portraits.append("images/portraits/childeric.jpg")

        if len(portraits) == 0:
            portraits = ["images/portraits/inconnu.jpg"]

        if portraits.count(portraitCourant) == 0:
            portraitCourant = random.choice(portraits)

        return portraitCourant
