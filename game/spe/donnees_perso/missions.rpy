init python:
    # --------------------------------------------------- missions ------------------------------
    def DemarrerMission(situation_, idMission):
        missionObjTemplate = missions_.lMissions_[idMission]
        situation_.SetCarac(idMission, missionObjTemplate)

    def GetDicoMissionsActives(situation_):
        """
        renvoi la liste des missions du perso sous forme d'un dico avec comme clé l'id de la mission et comme valeur son contenu
        les traits à "" ou 0 ne sont pas renvoyés
        """
        missionsPerso = {}

        for missionK in missions_.lMissions_.keys():
            valMission = self.GetValCarac(missionK)
            if valMission != None and valMission != "" and valMission != 0:
                missionObj = missions_[missionK]
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
