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

    def AjouterEvtsSaintDenis():
        global selecteur_
        conditionDansQuartier = condition.Condition( quartier.Quartier.C_QUARTIER, quartier.SaintDenis.NOM, condition.Condition.EGAL)

        evtMissionnaires = decU.DecU(0.1, "evtMissionnaires")
        evtMissionnaires.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtMissionnaires)

        evtSaintDenis2 = decU.DecU(0.1, "evtSaintDenis2")
        evtSaintDenis2.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtSaintDenis2)

        # Toujours garder un événement vide répétable au cas où tous les autres sont arrivés (vu qu'ils sont non répétables)
        evtSaintDenisVide = declencheur.Declencheur(0.01, "evtSaintDenisVide")
        evtSaintDenisVide.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtSaintDenisVide)

label evtMissionnaires:
    "PAS FAIT : evtMissionnaires"
    return

label evtSaintDenis2:
    "PAS FAIT : evtSaintDenis2"
    return

label evtSaintDenisVide:
    # à laisser vide (évt de remplissage en cas de manque d'évt réels)
    return
