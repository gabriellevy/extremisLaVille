# événements aléatoires dans ce quartiers

init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.univers import temps
    from abs.univers.geographie import quartier

    def AjouterEvtsLaDefense():
        global selecteur_
        conditionDansQuartier = condition.Condition( quartier.Quartier.C_QUARTIER, quartier.LaDefense.NOM, condition.Condition.EGAL)

        evtLaDefense1 = declencheur.Declencheur(0.1, "evtLaDefense1")
        evtLaDefense1.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtLaDefense1)

        evtLaDefense2 = declencheur.Declencheur(0.1, "evtLaDefense2")
        evtLaDefense2.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtLaDefense2)

        evtLaDefense3 = declencheur.Declencheur(0.1, "evtLaDefense3")
        evtLaDefense3.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtLaDefense3)

label evtLaDefense1:
    "PAS FAIT : evtLaDefense1"
    return

label evtLaDefense2:
    "PAS FAIT : evtLaDefense2"
    return

label evtLaDefense3:
    "PAS FAIT : evtLaDefense3"
    return
