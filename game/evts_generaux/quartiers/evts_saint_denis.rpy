# événements aléatoires dans ce quartier

 # persos
image missionnaire_img = "coteries/templiers/missionnaire.png"
define missionnaire = Character('Missionnaire', color="#a8fffb")

init -5 python:
    import random
    from abs import declencheur
    from spe import decU
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.univers import temps
    from abs.univers.geographie import quartier

    def AjouterEvtsSaintDenis():
        global selecteur_
        conditionDansQuartier = condition.Condition( quartier.Quartier.C_QUARTIER, quartier.SaintDenis.NOM, condition.Condition.EGAL)

        evtMissionnaires = decU.DecU(0.1, "evtMissionnaires", 0)
        evtMissionnaires.AjouterCondition(estPasChretien)
        evtMissionnaires.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtMissionnaires)

        evtSaintDenis2 = decU.DecU(0.1, "evtSaintDenis2", 0)
        evtSaintDenis2.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtSaintDenis2)

        # Toujours garder un événement vide répétable au cas où tous les autres sont arrivés (vu qu'ils sont non répétables)
        evtSaintDenisVide = declencheur.Declencheur(0.01, "evtSaintDenisVide")
        evtSaintDenisVide.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtSaintDenisVide)

label evtMissionnaires:
    "Un groupe de chrétiens missionnaires vous a remarqué."
    missionnaire "Bonjour mon frère, vous ne semblez pas connaître notre seigneur Jésus Christ qui a souffert pouvr vos péchés et veut votre plus grand bien."
    menu:
        "Laisez moi tranquille s'il vous plaît.":
            missionnaire "Allez en paix dans la lumière du seigneur."
            return
        "Non en effet de qui s'agit-t'il ?":
            missionnaire "PAS FAIT : arguments d'évangélistes..."
            missionnaire "Je comprends que votre temps est compté mon frère mais si vous le souhaitez je peux moi-même vous baptiser dans la basilique Saint Denis d'où vous ressortirez sur le champs en vrai chértien."
            missionnaire "Croyez moi cette foi et cette protection vous seront grandement utiles dans votre quête."
            $ situation_.AvanceDeXMinutes(5)
            menu:
                "Non merci":
                    missionnaire "Allez en paix dans la lumière du seigneur. Nous nous reverrons j'en suis sûr."
                    return
                "D'accord":
                    "PAS FAIT : baptème avec en inclus le temps qui passe (au moins deux heures)"
                    $ setattr(situation_, religion.Religion.C_RELIGION, religion.Christianisme.NOM)
                    $ situation_.AvanceDeXMinutes(137)
                    return

label evtSaintDenis2:
    "PAS FAIT : evtSaintDenis2"
    return

label evtSaintDenisVide:
    # à laisser vide (évt de remplissage en cas de manque d'évt réels)
    "Vous pénétrez dans Saint Denis, quartier de l'ordre des templiers."
    return
