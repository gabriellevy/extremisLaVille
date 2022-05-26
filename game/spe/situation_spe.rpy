init python:
    from abs.religions import religion
    # from chapitres.classes import perso
    from spe.humanite import pnj_spe
    from abs.humanite import metier
    from abs.humanite import pnj
    from abs.humanite import trait
    import random

    class SituationSpe(Situation):

        # Set the store.{prefix}.character_id value
        # STORE_PREFIX = "character_stats"

        # Boolean toggle for validation - defaults both True
        # VALIDATE_VALUES = False
        # COERCE_VALUES = False

        STAT_DEFAULTS = {
            'gender' : 'f',
            'age' : 22,
            'location' : 'school',
            'affection' : 1,
            'obedience' : 0.01,
        }

        # ------------------------------------------------AFFICHAGE---------------------------------------
        # def AffichageGloire(self):
        #     val = self.GetValCarac(perso.Perso.C_GLOIRE)
        #     if self.debug_:
        #         return u"Gloire : {}".format(val)
        #     return u""

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
