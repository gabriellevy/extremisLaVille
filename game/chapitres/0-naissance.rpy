# fichier où sont générés les phrases d'ambiance à afficher quand il ne se passe rien durant un mois particulier

init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import testDeCarac
    from abs import condition
    from abs.humanite import trait
    from spe.humanite import pnj_spe
    from abs.univers import temps
    from abs.univers.geographie import quartier
    from abs.humanite import identite
    from chapitres.classes import perso
    from abs.religions import religion
    from abs.humanite import pnj
    from spe.univers import coterie
    from spe.univers.coteries import templiers
    from spe.univers.coteries import elfes
    from spe.univers.coteries import orks
    from spe.univers.coteries import transhumanistes
    from spe.univers.coteries import zaporogues
    from spe.univers.coteries import conquistadors

    def genererDateNaissance(situation, ageActuel=15):
        date = getattr(situation, temps.Date.DATE)
        nbJoursDateNaissance = date - 365*ageActuel
        setattr(situation, temps.Date.DATE_NAISSANCE, nbJoursDateNaissance)

    def genererPersoTemplier(situation, tousLesTraits):
        setattr(situation_, religion.Religion.C_RELIGION, religion.Christianisme.NOM)
        # traits de base
        setattr(situation_, trait.Richesse.NOM, trait.Trait.SEUIL_A_PAS)
        setattr(situation_, trait.Honorabilite.NOM, trait.Trait.SEUIL_A)

        # compétences indispensables pour un templier
        setattr(situation, metier.Guerrier.NOM, 1)

        situation[identite.Identite.C_NOM] = "Baudoin"

        # situation[jeanne.Jeanne.CARTE_ACTUELLE] = "bg carte481"
        return

label naissance:
    scene bg rue_haussmann
    with dissolve
    $ genererDateNaissance(Situation(situation_), 17)
    $ setattr(situation_, coterie.Coterie.C_COTERIE, "")
    menu:
        "Choisissez votre coterie. Cela affectera non seulement votre personnage de départ mais aussi l'histoire principale."
        "Les templiers, une coterie d'honorables guerriers chrétiens ayant fait voeu de pauvreté et de chasteté":
            $ setattr(situation_, coterie.Coterie.C_COTERIE, templiers.Templiers.ID)
            $ genererPersoTemplier(situation_, traits_)
            jump initiation_templiers
