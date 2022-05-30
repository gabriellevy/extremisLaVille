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

    def AjouterEvtsSaintGermainEnLaye():
        global selecteur_
        conditionDansQuartier = condition.Condition( quartier.Quartier.C_QUARTIER, quartier.SaintGermainEnLaye.NOM, condition.Condition.EGAL)

        evtSaintGermainEnLaye1 = declencheur.Declencheur(0.1, "evtSaintGermainEnLaye1")
        evtSaintGermainEnLaye1.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtSaintGermainEnLaye1)

        evtSaintGermainEnLaye2 = declencheur.Declencheur(0.1, "evtSaintGermainEnLaye2")
        evtSaintGermainEnLaye2.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtSaintGermainEnLaye2)

        evtSaintGermainEnLaye3 = declencheur.Declencheur(0.1, "evtSaintGermainEnLaye3")
        evtSaintGermainEnLaye3.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtSaintGermainEnLaye3)

label evtSaintGermainEnLaye1:
    "PAS FAIT : evtSaintGermainEnLaye1"
    return

label evtSaintGermainEnLaye2:
    "PAS FAIT : evtSaintGermainEnLaye2"
    return

label evtSaintGermainEnLaye3:
    "PAS FAIT : evtSaintGermainEnLaye3"
    return
