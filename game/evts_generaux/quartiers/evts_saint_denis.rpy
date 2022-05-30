# événements aléatoires dans ce quartier

init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.univers import temps
    from abs.univers.geographie import quartier

    def AjouterEvtsSaintDenis():
        global selecteur_
        conditionDansQuartier = condition.Condition( quartier.Quartier.C_QUARTIER, quartier.SaintDenis.NOM, condition.Condition.EGAL)

        evtSaintDenis1 = declencheur.Declencheur(0.1, "evtSaintDenis1")
        evtSaintDenis1.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtSaintDenis1)

        evtSaintDenis2 = declencheur.Declencheur(0.1, "evtSaintDenis2")
        evtSaintDenis2.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtSaintDenis2)

        evtSaintDenis3 = declencheur.Declencheur(0.1, "evtSaintDenis3")
        evtSaintDenis3.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtSaintDenis3)

label evtSaintDenis1:
    "PAS FAIT : evtSaintDenis1"
    return

label evtSaintDenis2:
    "PAS FAIT : evtSaintDenis2"
    return

label evtSaintDenis3:
    "PAS FAIT : evtSaintDenis3"
    return
