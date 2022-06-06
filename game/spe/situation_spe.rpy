init python:
    from abs.religions import religion
    from spe.humanite import pnj_spe
    from abs.humanite import metier
    from abs.humanite import pnj
    from abs.humanite import trait
    from abs import mission
    from spe import missions
    import random

    class SituationSpe(Situation):

        # Set the store.{prefix}.character_id value
        # STORE_PREFIX = "character_stats"

        # Boolean toggle for validation - defaults both True
        # VALIDATE_VALUES = False
        # COERCE_VALUES = False

        STAT_DEFAULTS = {
            temps.Date.DATE: 0 # nb de jours au démarrage du jeu depuis an (ou jour ou autre) 0
        }

        def __init__(self, id, **kwargs):
            Situation.__init__(self, id, **kwargs)
            self.collectionMissions = missions.Missions()

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

        # --------------------------------------------------- missions ------------------------------
        def DemarrerMission(self, idMission):
            if getattr(self, "collectionMissions") == "":
                setattr(self, "collectionMissions", missions.Missions())

            missionObjTemplate = self.collectionMissions.lMissions_[idMission]
            self.SetCarac(idMission, missionObjTemplate)

        def GetDicoMissionsActives(self):
            """
            renvoi la liste des missions du perso sous forme d'un dico avec comme clé l'id de la mission et comme valeur son contenu
            les traits à "" ou 0 ne sont pas renvoyés
            """
            missionsPerso = {}
            if getattr(self, "collectionMissions") == "":
                setattr(self, "collectionMissions", missions.Missions())

            for missionK in self.collectionMissions.lMissions_.keys():
                valMission = self.GetValCarac(missionK)
                if valMission != None and valMission != "" and valMission != 0:
                    missionObj = self.collectionMissions[missionK]
                    missionsPerso[missionObj.m_Id] = valMission
            return missionsPerso

        def DescriptionMissionsActives(self):
            """
            Description des missions
            """
            str = u"Pas de mission..."
            missionsDico = self.GetDicoMissionsActives()
            str = u"Pas de mission... {}".format(len(missionsDico))
            for missionK in missionsDico.keys():
                missionObj = missionsDico[missionK]
                if missionObj != None and missionObj != "":
                    str = u"{}\n".format(missionObj)
            return str

        # DATES ET TEMPS QUI PASSE-----------------------------------------------------------------------------------------------------------
        # le temps est en minute => 0 étant le premier jour, et donc 60 * 24 est le début du deuxième

        def AffichageDate(self):
            dateStr = u"Jour {}".format(self.GetNumeroDuJour())
            return dateStr

        def GetNumeroDuJour(self):
            nbMinutes = self.GetValCaracInt( temps.Date.DATE)
            return nbMinutes / (60 * 24) + 1

        def AvanceDeXMinutes(self, nbMinutesPassees):
            nouvelleDateEnMinutes = self.GetValCaracInt( temps.Date.DATE) + nbMinutesPassees
            setattr(self, temps.Date.DATE, nouvelleDateEnMinutes)

            # application des jours passés aux missions :
            missionsActives = self.GetDicoMissionsActives()
            for missionActiveK in missionsActives:
                missionActiveObj = missionsActives[missionActiveK]
                missionActiveObj.AvanceDeXMinutes(nbMinutesPassees)
