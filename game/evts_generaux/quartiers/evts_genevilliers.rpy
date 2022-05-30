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

    def AjouterEvtsGenevilliers():
        global selecteur_
        conditionDansQuartier = condition.Condition( quartier.Quartier.C_QUARTIER, quartier.Genevilliers.NOM, condition.Condition.EGAL)

        evtGenevilliers1 = declencheur.Declencheur(0.1, "evtGenevilliers1")
        evtGenevilliers1.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtGenevilliers1)

        evtGenevilliers2 = declencheur.Declencheur(0.1, "evtGenevilliers2")
        evtGenevilliers2.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtGenevilliers2)

        evtGenevilliers3 = declencheur.Declencheur(0.1, "evtGenevilliers3")
        evtGenevilliers3.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtGenevilliers3)

label evtGenevilliers1:
    "PAS FAIT : evtGenevilliers1"
    return

label evtGenevilliers2:
    "PAS FAIT : evtGenevilliers2"
    return

label evtGenevilliers3:
    "PAS FAIT : evtGenevilliers3"
    return
