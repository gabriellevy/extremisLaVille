# fichier où sont générés les phrases d'ambiance à afficher quand il ne se passe rien durant un mois particulier

init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.univers import temps
    # from religions import religion
    # from geographie import quartier

    def AjouterEvtsRien():
        global selecteur_, situation_
        selecteurDEvenementVide = declencheur.Declencheur(1.0, "selecteurDEvenementVide")
        selecteur_.ajouterDeclencheur(selecteurDEvenementVide)

    def LancerEvtVide(situation):
        sceneParDefaut = ""
        # régénère les événements compatibles avec la situation
        evtsVides_ = [
        # "evtRien1"
        ]
        scenesParDefaut = []
        musiquesAEnquiller = []

        # selon religion
        religionActuelle = situation_.GetValCarac(religion.Religion.C_RELIGION)
        if religionActuelle == religion.Christianisme.NOM:
            # evts
            evtsVides_.append("evtRien_saints")
            # images
            scenesParDefaut.append("bg crucifixion")
            # musiques
            musiquesAEnquiller.append("musique/journeytoabsolution.ogg")

        # saison
        saison = situation.GetDateDuJour().GetSaison()
        if saison == temps.Date.PRINTEMPS:
            evtsVides_.append("evtRien1_printemps")
            musiquesAEnquiller.append("musique/Sea Season.ogg")
        if saison == temps.Date.HIVER:
            musiquesAEnquiller.append("musique/Dark Season.ogg")
        if saison == temps.Date.ETE:
            musiquesAEnquiller.append("musique/Fire Season.ogg")
        if saison == temps.Date.AUTOMNE:
            evtsVides_.append("evtRien1_automne")
            evtsVides_.append("evtRien2_automne")
            evtsVides_.append("evtRien3_automne")

        # -----------------------------------------------------------------------------
        if len(evtsVides_) == 0:
            evtsVides_ = ["evtRien1", "evtRien2" ]

        if len(scenesParDefaut) == 0:
            sceneParDefaut = "bg cours_merovingienne"

        # ajoute une musique à la file au hasard :
        if len(musiquesAEnquiller) != 0:
            renpy.music.queue(random.choice(musiquesAEnquiller), clear_queue=False)

        # fond
        if sceneParDefaut != "":
            renpy.scene()
            renpy.show(random.choice(scenesParDefaut))
        # en lance un au hasard
        renpy.jump(random.choice(evtsVides_))

label evtRien1_automne:
    "C'est l'époque des semailles d'orge."
    jump fin_cycle

label evtRien2_automne:
    "C'est l'époque des semailles de froment."
    jump fin_cycle

label evtRien3_automne:
    "C'est l'époque des semailles de seigle."
    jump fin_cycle

label evtRien1_printemps:
    "C'est l'époque des semailles d'avoine."
    jump fin_cycle

label selecteurDEvenementVide:
    $ LancerEvtVide(situation_)
