from abs.religions import religion
from chapitres.classes import jeanne
from spe.humanite import portrait_jeanne
from abs.humanite import portrait
from spe.humanite import pnj_jeanne
from abs import situation
from abs.humanite import metier
from abs.humanite import pnj
from abs.humanite import trait
import random

class SituationJeanne(situation.Situation):

    def __init__(self):
        situation.Situation.__init__(self, 175000)

    # ------------------------------------------------AFFICHAGE---------------------------------------
    def AffichageGloire(self):
        val = self.GetValCarac(jeanne.Jeanne.C_GLOIRE)
        if self.debug_:
            return u"Gloire : {}".format(val)
        return u""

    def DeterminerPortrait(self):
        """
        récupérer une liste de portraits selon les caracs du perso et en choisir un aléatoirement
        celui est choisi est stocké dans une carac mais en cas de changement important (âge, métier, coterie...) on en recalcule un
        """
        portr = portrait_jeanne.PortraitJeanne()
        portraitStr = portr.DeterminerPortraitPersoPrincipal(self, True)
        self.SetCarac(portrait.Portrait.C_PORTRAIT, portraitStr)
        return self.GetValCarac(portrait.Portrait.C_PORTRAIT)

    # ------------------------------------------------- PNJ ---------------------------------------------------

    def AffichagePortraitPere(self):
        # père
        str = u""
        pere = self.GetValCarac(pnj.Pnj.C_PERE)
        if isinstance(pere, pnj_jeanne.PnjJeanne) :
            return pere.portraitStr_
        return ""

    def AffichagePortraitMere(self):
        # mère
        str = u""
        mere = self.GetValCarac(pnj.Pnj.C_MERE)
        if isinstance(mere, pnj_jeanne.PnjJeanne) :
            return mere.portraitStr_
        return ""

    def AffichagePere(self):
        # père
        str = u""
        pere = self.GetValCarac(pnj.Pnj.C_PERE)
        if isinstance(pere, pnj_jeanne.PnjJeanne) :
            str = u"{}".format(pere)
        return str

    def AffichageMere(self):
        # mère
        str = u""
        mere = self.GetValCarac(pnj.Pnj.C_MERE)
        if isinstance(mere, pnj_jeanne.PnjJeanne) :
            str = u"{}".format(mere)
        return str

    # -------------------------------------------------- temps -------------------------------------------------

    def TourSuivant(self):
        """
        Passage au "tour" suivant c'est à dire grosso modo 15 jours un peu randomisé
        """
        nbJoursPasses = 11 + random.randint(0, 8)
        self.AvanceDeXJours(nbJoursPasses)
