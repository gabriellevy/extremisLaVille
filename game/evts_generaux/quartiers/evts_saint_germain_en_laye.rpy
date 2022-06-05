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

    def AjouterEvtsSaintGermainEnLaye():
        global selecteur_
        conditionDansQuartier = condition.Condition( quartier.Quartier.C_QUARTIER, quartier.SaintGermainEnLaye.NOM, condition.Condition.EGAL)

        evtSaintGermainEnLaye1 = decU.DecU(0.1, "evtSaintGermainEnLaye1")
        evtSaintGermainEnLaye1.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtSaintGermainEnLaye1)

        evtSaintGermainEnLaye2 = decU.DecU(0.1, "evtSaintGermainEnLaye2")
        evtSaintGermainEnLaye2.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtSaintGermainEnLaye2)

        # Toujours garder un événement vide répétable au cas où tous les autres sont arrivés (vu qu'ils sont non répétables)
        evtSaintGermainEnLayeVide = declencheur.Declencheur(0.1, "evtSaintGermainEnLayeVide")
        evtSaintGermainEnLayeVide.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtSaintGermainEnLayeVide)

label evtSaintGermainEnLaye1:
    "PAS FAIT : evtSaintGermainEnLaye1"
    return

label evtSaintGermainEnLaye2:
    "PAS FAIT : evtSaintGermainEnLaye2"
    return

label evtSaintGermainEnLayeVide:
    # à laisser vide (évt de remplissage en cas de manque d'évt réels)
    "Vous pénétrez dans Saint Germain en Laye, quartier des elfes."
    return
