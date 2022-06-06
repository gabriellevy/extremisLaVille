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

    def AjouterEvtsGenevilliers():
        global selecteur_
        conditionDansQuartier = condition.Condition( quartier.Quartier.C_QUARTIER, quartier.Genevilliers.NOM, condition.Condition.EGAL)

        evtGenevilliers1 = decU.DecU(0.1, "evtGenevilliers1", 0)
        evtGenevilliers1.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtGenevilliers1)

        evtGenevilliers2 = decU.DecU(0.1, "evtGenevilliers2", 0)
        evtGenevilliers2.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtGenevilliers2)

        # Toujours garder un événement vide répétable au cas où tous les autres sont arrivés (vu qu'ils sont non répétables)
        evtGenevilliersVide = declencheur.Declencheur(0.1, "evtGenevilliersVide")
        evtGenevilliersVide.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtGenevilliersVide)

label evtGenevilliers1:
    "PAS FAIT : evtGenevilliers1"
    return

label evtGenevilliers2:
    "PAS FAIT : evtGenevilliers2"
    return

label evtGenevilliersVide:
    # à laisser vide (évt de remplissage en cas de manque d'évt réels)
    "Vous pénétrez dans Genevilliers, quartier des orks."
    return
