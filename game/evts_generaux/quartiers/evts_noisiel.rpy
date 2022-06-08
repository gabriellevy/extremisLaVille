# événements aléatoires dans ce quartier

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

    def AjouterEvtsNoisiel():
        global selecteur_
        conditionDansQuartier = condition.Condition( quartier.Quartier.C_QUARTIER, quartier.Noisiel.NOM, condition.Condition.EGAL)

        evtNoisiel1 = decU.DecU(0.1, "evtNoisiel1", 0)
        evtNoisiel1.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtNoisiel1)

        evtNoisiel2 = decU.DecU(0.1, "evtNoisiel2", 0)
        evtNoisiel2.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtNoisiel2)

        # Toujours garder un événement vide répétable au cas où tous les autres sont arrivés (vu qu'ils sont non répétables)
        evtNoisielVide = declencheur.Declencheur(0.1, "evtNoisielVide")
        evtNoisielVide.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtNoisielVide)

label evtNoisiel1:
    "PAS FAIT : evtNoisiel1"
    return

label evtNoisiel2:
    "PAS FAIT : evtNoisiel2"
    return

label evtNoisielVide:
    # à laisser vide (évt de remplissage en cas de manque d'évt réels)
    "Vous pénétrez dans Noisiel, quartier d'Achéron."
    return
