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

    def AjouterEvtsSaintMaurDesFosses():
        global selecteur_
        conditionDansQuartier = condition.Condition( quartier.Quartier.C_QUARTIER, quartier.SaintMaurDesFosses.NOM, condition.Condition.EGAL)

        evtSaintMaurDesFosses1 = decU.DecU(0.1, "evtSaintMaurDesFosses1", 0)
        evtSaintMaurDesFosses1.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtSaintMaurDesFosses1)

        evtSaintMaurDesFosses2 = decU.DecU(0.1, "evtSaintMaurDesFosses2", 0)
        evtSaintMaurDesFosses2.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtSaintMaurDesFosses2)

        # Toujours garder un événement vide répétable au cas où tous les autres sont arrivés (vu qu'ils sont non répétables)
        evtSaintMaurDesFossesVide = declencheur.Declencheur(0.1, "evtSaintMaurDesFossesVide")
        evtSaintMaurDesFossesVide.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtSaintMaurDesFossesVide)

label evtSaintMaurDesFosses1:
    "PAS FAIT : evtSaintMaurDesFosses1"
    return

label evtSaintMaurDesFosses2:
    "PAS FAIT : evtSaintMaurDesFosses2"
    return

label evtSaintMaurDesFossesVide:
    # à laisser vide (évt de remplissage en cas de manque d'évt réels)
    "Vous pénétrez dans Saint Maur des fossés, quartier des cathares."
    return
