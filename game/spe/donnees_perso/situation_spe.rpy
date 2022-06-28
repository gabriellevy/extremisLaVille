init python:
    from abs.religions import religion
    from spe.humanite import pnj_spe
    from abs.humanite import metier
    from abs.humanite import pnj
    from abs.humanite import trait
    from chapitres.templiers import carac
    import random

    class SituationSpe(Situation):

        # Set the store.{prefix}.character_id value
        STORE_PREFIX = "stats_spe"

        # Boolean toggle for validation - defaults both True
        VALIDATE_VALUES = False
        COERCE_VALUES = False

        STAT_DEFAULTS = {
            temps.Date.DATE: 0 # nb de jours au démarrage du jeu depuis an (ou jour ou autre) 0
        }

        # def __init__(self, id, **kwargs):
        #     Situation.__init__(self, id, **kwargs)


        def AffichageIndices(self):
            strIndices = u"Indices : "
            if self.GetValCarac(carac.Carac.C_IND_INFORMATIQ) == 1:
                strIndices = u"{}\n{}".format(strIndices, carac.Carac.C_IND_INFORMATIQ)
            if self.GetValCarac(carac.Carac.C_IND_HAINE_TEMPLIERS) == 1:
                strIndices = u"{}\n{}".format(strIndices, carac.Carac.C_IND_HAINE_TEMPLIERS)
            return strIndices

        # -------------------------------------------------- temps -------------------------------------------------

        # DATES ET TEMPS QUI PASSE-----------------------------------------------------------------------------------------------------------
        # le temps est en minute => 0 étant le premier jour, et donc 60 * 24 est le début du deuxième

        # def AffichageDate(self):
        #     dateStr = u"Jour {}".format(self.GetNumeroDuJour())
        #     return dateStr

        # def GetNumeroDuJour(self):
        #     nbMinutes = self.GetValCaracInt( temps.Date.DATE)
        #     return nbMinutes / (60 * 24) + 1

        # def AvanceDeXMinutes(self, nbMinutesPassees):
        #     nouvelleDateEnMinutes = self.GetValCaracInt( temps.Date.DATE) + nbMinutesPassees
        #     setattr(self, temps.Date.DATE, nouvelleDateEnMinutes)

            # application des jours passés aux missions :
            # missionsActives = self.GetDicoMissionsActives()
            # for missionActiveK in missionsActives:
            #     missionActiveObj = missionsActives[missionActiveK]
            #     missionActiveObj.AvanceDeXMinutes(nbMinutesPassees)
