# événements aléatoires dans ce quartiers

 # persos
image holo_rockeur_img = "quartiers/la_defense/holo_rockeur.png"
define holo_rockeur = Character('Holopub', color="#f2e122")

image holo_lyla_img = "quartiers/la_defense/holo_lyla.png"
define holo_lyla = Character('Holopub', color="#f2e122")

image holo_majordome_img = "quartiers/la_defense/holo_majordome.png"
define holo_majordome = Character('Holopub', color="#f2e122")

image holo_may_img = "quartiers/la_defense/holo_may.png"
define holo_may = Character('Holopub', color="#f2e122")

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

    def AjouterEvtsLaDefense():
        global selecteur_
        conditionDansQuartier = condition.Condition( quartier.Quartier.C_QUARTIER, quartier.LaDefense.NOM, condition.Condition.EGAL)

        evtholo_rockeur = decU.DecU(0.1, "evtholo_rockeur", 0)
        evtholo_rockeur.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtholo_rockeur)

        evtholo_lyla = decU.DecU(0.1, "evtholo_lyla", 0)
        evtholo_lyla.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtholo_lyla)

        evtholo_majordome = decU.DecU(0.1, "evtholo_majordome", 0)
        evtholo_majordome.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtholo_majordome)

        evtholo_may = decU.DecU(0.1, "evtholo_may", 0)
        evtholo_may.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtholo_may)

        evtLaDefenseVide = declencheur.Declencheur(0.01, "evtLaDefenseVide")
        evtLaDefenseVide.AjouterCondition(conditionDansQuartier)
        selecteur_.ajouterDeclencheur(evtLaDefenseVide)

label evtholo_rockeur:
    show holo_rockeur_img at left
    with moveinleft
    holo_rockeur "Un bon défoulement pas cher au coin de la rue : catch de rue cyber augmenté et bières ! Plus des chiens mutants et des robots géants !"
    hide holo_rockeur_img
    with moveoutleft
    return

label evtholo_lyla:
    show holo_lyla_img at left
    with moveinleft
    holo_rockeur "Venez visiter nos superbes appartements en plein coeur de la défense ! Jusqu'à 50 ans de crédit autorisés !"
    hide holo_lyla_img
    with moveoutleft
    return

label evtholo_majordome:
    show holo_majordome_img at left
    with moveinleft
    holo_majordome "Le meilleur hotel de toute la défense, venez passer la nuit de vos rêves au Petit Palace del Peine."
    hide holo_majordome_img
    with moveoutleft
    return

label evtholo_may:
    show holo_may_img at left
    with moveinleft
    holo_may "Venez goûter nos gâteaux faits maison au salon de thé de tante May."
    hide holo_may_img
    with moveoutleft
    return

label evtLaDefenseVide:
    # à laisser vide (évt de remplissage en cas de manque d'évt réels)
    "Vous pénétrez dans La Défense, quartier des transhumanistes."
    return
