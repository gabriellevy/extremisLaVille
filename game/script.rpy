# toutes les datas d'état du jeu (sauvegardées etc)
default situation_ = SituationSpe("situation_")

# --------------------------------------------
# ------------------ Persos ------------------
# --------------------------------------------
define narrator = Character(color="#fafad8", what_italic=True)
define std = Character('Perso standard...', color="#B22222") # personnage standard remplacé selon les situations. (son nom est mis à jour)

# Musiques
# define audio.roi_mort = "musique/akingisdead.ogg"

init -10 python:
    from abs import selecteur
    import random

    selecteur_ = selecteur.Selecteur()
    def determinationEvtCourant(situation):
        global selecteur_
        return selecteur_.determinationEvtCourant(situation)

init -1 python:
    from abs import selecteur
    import random

    # événements aléatoires de quartier
    AjouterEvtsGenevilliers()
    AjouterEvtsSaintGermainEnLaye()
    AjouterEvtsSaintDenis()
    AjouterEvtsLaDefense()
    AjouterEvtsNoisiel()
    AjouterEvtsSaintMaurDesFosses()

label init_secondary_data:
    python:
        from spe import missions

        traits_ = trait.CollectionTraits()
        situation_.collectionTraits = traits_
        blessures_ = pbsante.CollectionBlessures()
        situation_.collectionBlessures = blessures_
        maladies_ = pbsante.CollectionMaladies()
        situation_.collectionMaladies = maladies_
        quartiers_ = quartier.CollectionQuartiers()
        situation_.collectionQuartiers = quartiers_
        metiers_ = metier.CollectionMetiers()
        situation_.collectionMetiers = metiers_
        missions_ = missions.Missions()
        situation_.collectionMissions = missions_
        objets_ = [objet_spe.EpeeTemplier()]
        situation_.collectionObjets_ = objets_
        debug_ = True
        situation_.debug_ = debug_
    jump naissance

# Le jeu commence ici
label start:
    scene bg priere
    # play music musique_menu
    # queue music [ epique_principale, conquetes ] # pseudo liste de lecture temporaire
    jump init_secondary_data

label mort:
    menu:
        "Fin de vie."
        "ok":
            pass
    return

label labelGoTo_pasFait:
    "Ce sélecteur d'énévement n'a pas de label go to on dirait"

label pas_evt_trouve:
    " ERREUR : pas d'événement trouvé à ce cycle"

label probaAbsoluesSup100:
    "Le total des probas absolues dépasse 100%% !"

label defaite:
    "défaite : PAS FAIT:"
    return
