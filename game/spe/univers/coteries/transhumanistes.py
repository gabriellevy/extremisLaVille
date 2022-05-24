from spe.univers import coterie
from abs.humanite import metier
from abs.humanite import trait
from abs.univers.geographie import quartier
import random

class Transhumanistes(coterie.Coterie):

    NOM = u"Transhumanistes"
    ID = u"transhumanistes"

    def __init__(self):
        self.nom_ = Transhumanistes.NOM
        self.id_ = Transhumanistes.ID
        self.quartier_ = quartier.LaDefense.NOM

    def getLabelUniversite(self):
        return "univTranshumanistes"

    def GetTraitsCompatibles(self):
        """
        si le perso a ces caracs il a plus de chances de vouloir rejoindre cette coterie
        """
        return [ \
            trait.Cupidite.NOM, \
            trait.Pragmatisme.NOM, \
            trait.Individualisme.NOM, \
            trait.Opportunisme.NOM, \
            trait.Ambition.NOM, \
            trait.Industrie.NOM, \
            # classe sociale élevée
            ]

    def GetMetiersCompatibles(self):
        """
        si le perso a des compétences dans ces métiers il a plus de chances de vouloir rejoindre cette coterie où ils sont souvent pratiqués
        """
        return [ \
            metier.Marchand.NOM, \
            metier.Informaticien.NOM, \
            metier.Cyberneticien.NOM, \
            metier.Geneticien.NOM, \
            metier.Commercial.NOM \
            ]

    def GetGentile(self, masculin):
        return "transhumaniste"

    def GetPoidsDemo(self):
        """
        à quel point cette coterie est nombreuse dans la population
        1.0 = normal
        0.1 = 10 fois moins que la moyenne
        """
        return 1.1

    def GetTraitsIncompatibles(self):
        """
        si le perso a ces caracs il a plus de chances de ne pas vouloir rejoindre cette coterie
        """
        return [ \
            trait.Spiritualite.NOM, \
            trait.Ascetisme.NOM, \
            trait.Nature.NOM, \
            trait.Artiste.NOM, \
            trait.Serenite.NOM, \
            metier.Pretre.NOM \
            # classe sociale basse
            ]

    def GenererPortraits(self, age, masculin, metObj, portraits, valeursTraits):
        """
        ajoute des portraits correspondants aux caracs en paramtre (et à la coterie courante)
        """
        if masculin:
            if age > 10:
                if age > 15:
                    if age > 20:
                        if age > 35: # > 35
                            portraits.append("images/coteries/transhumanistes/portraits/portrait35+.jpg")
                            portraits.append("images/coteries/transhumanistes/portraits/portrait35+_2.jpg")
                            portraits.append("images/coteries/transhumanistes/portraits/portrait35+_3.jpg")
                            if age > 40: # > 40
                                portraits.append("images/coteries/transhumanistes/portraits/portrait40+.jpg")
                                if age > 50: # > 50
                                    portraits.append("images/coteries/transhumanistes/portraits/portrait50+.jpg")
                                    if age > 60: # > 60
                                        portraits.append("images/coteries/transhumanistes/portraits/portrait60+.jpg")
                                        portraits.append("images/coteries/transhumanistes/portraits/portrait60+_2.jpg")
                                        if age > 60: # > 60
                                            portraits.append("images/coteries/transhumanistes/portraits/portrait70+.jpg")
                        if age > 30:
                            if age < 50: # 30 à 50
                                portraits.append("images/coteries/transhumanistes/portraits/portrait30-50.jpg")
                                portraits.append("images/coteries/transhumanistes/portraits/portrait30-50_2.jpg")
                                portraits.append("images/coteries/transhumanistes/portraits/portrait30-50_2.png")
                                portraits.append("images/coteries/transhumanistes/portraits/portrait30-50_3.jpg")
                        if age < 50: # 20 à 50
                            portraits.append("images/coteries/transhumanistes/portraits/portrait20-50.jpg")
                            portraits.append("images/coteries/transhumanistes/portraits/portrait20-50.png")
                            portraits.append("images/coteries/transhumanistes/portraits/portrait20-50_2.jpg")
                            portraits.append("images/coteries/transhumanistes/portraits/portrait20-50_3.jpg")
                            if age < 40: # 20 à 40
                                portraits.append("images/coteries/transhumanistes/portraits/portrait20-40.jpg")
                    if age < 40:
                        if age < 30: # 15 à 30
                            portraits.append("images/coteries/transhumanistes/portraits/portrait15-30.jpg")
                            portraits.append("images/coteries/transhumanistes/portraits/portrait15-30_2.jpg")
                            portraits.append("images/coteries/transhumanistes/portraits/portrait15-30_3.jpg")
                if age < 20: # 10 à 20
                    portraits.append("images/coteries/transhumanistes/portraits/portrait10-20.jpg")
        # else:
        #    if age > 20:
        #        if age < 40:

        return portraits
