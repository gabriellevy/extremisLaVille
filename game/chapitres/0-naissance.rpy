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
        nbJoursDateNaissance = situation[temps.Date.DATE] - 365*ageActuel
        situation[temps.Date.DATE_NAISSANCE] = nbJoursDateNaissance

    # def genererParents(situation):
        # pere = pnj_spe.GenererPNJSpe(True, situation, 43 * 12 *30 + 24)
        # pere.prenom_ = "Jacques"
        # pere.nom_ = "d'Arc"
        # pere.portraitStr_ = "images/portraits/childeric.jpg"
        # situation.SetValCarac(pnj.Pnj.C_PERE, pere)

        # mere = pnj_spe.GenererPNJSpe(False, situation, 36 * 12 *30 + 297)
        # mere.prenom_ = "Isabelle"
        # mere.nom_ = "Romée"
        # mere.portraitStr_ = "images/portraits/basine.jpg"
        # situation.SetValCarac(pnj.Pnj.C_MERE, mere)

    def genererPersoTemplier(situation, tousLesTraits):
        # traits de base
        situation[trait.Richesse.NOM] = trait.Trait.SEUIL_A_PAS
        situation[trait.Sexualite.NOM] = trait.Trait.SEUIL_A_PAS
        situation[trait.Cupidite.NOM] = trait.Trait.SEUIL_A_PAS
        situation[trait.Honorabilite.NOM] = trait.Trait.SEUIL_A
        situation[trait.Courage.NOM] = trait.Trait.SEUIL_A

        # caracs secondaire selon choix au lancement
        situation[trait.Ruse.NOM] = trait.Trait.SEUIL_A
        situation[trait.Charme.NOM] = trait.Trait.SEUIL_A
        situation[trait.Habilete.NOM] = trait.Trait.SEUIL_A
        situation[trait.Beaute.NOM] = trait.Trait.SEUIL_A
        situation[trait.Constitution.NOM] = trait.Trait.SEUIL_A
        situation[trait.Observation.NOM] = trait.Trait.SEUIL_A
        situation[trait.Force.NOM] = trait.Trait.SEUIL_A
        situation[trait.Intelligence.NOM] = trait.Trait.SEUIL_A
        situation[trait.Ascetisme.NOM] = trait.Trait.SEUIL_A
        situation[trait.Altruisme.NOM] = trait.Trait.SEUIL_A

        # métier et/ou compétences secondaires à choisir à la création
        situation[metier.Metier.C_METIER] = metier.Paysan.NOM
        situation[metier.Paysan.NOM] = 5
        situation[metier.Bibliothecaire.NOM] = 5
        situation[metier.Pretre.NOM] = 5
        situation[metier.Ouvrier.NOM] = 5
        situation[metier.Medecin.NOM] = 5
        situation[metier.TueurDeMonstres.NOM] = 5
        situation[metier.Architecte.NOM] = 5
        situation[metier.Guerrier.NOM] = 5
        situation[metier.Vigile.NOM] = 5
        situation[metier.Policier.NOM] = 5
        situation[metier.Banquier.NOM] = 5
        situation[metier.GardeDuCorps.NOM] = 5
        situation[metier.Aventurier.NOM] = 5

        # défaut selon choix au lancement
        situation[trait.Violence.NOM] = trait.Trait.SEUIL_A
        situation[trait.Charme.NOM] = trait.Trait.SEUIL_A_PAS
        situation[trait.Observation.NOM] = trait.Trait.SEUIL_A_PAS
        situation[trait.Habilete.NOM] = trait.Trait.SEUIL_A_PAS
        situation[trait.Beaute.NOM] = trait.Trait.SEUIL_A_PAS
        situation[trait.Constitution.NOM] = trait.Trait.SEUIL_A_PAS
        situation[trait.Force.NOM] = trait.Trait.SEUIL_A_PAS
        situation[trait.Sexualite.NOM] = trait.Trait.SEUIL_A
        situation[trait.Cupidite.NOM] = trait.Trait.SEUIL_A
        situation[trait.Opportunisme.NOM] = trait.Trait.SEUIL_A
        situation[trait.Intelligence.NOM] = trait.Trait.SEUIL_A_PAS
        situation[trait.Courage.NOM] = trait.Trait.SEUIL_A_PAS

        # compétences professionnelles
        # situation[metier.Politique.NOM] = trait.Trait.SEUIL_A

        # caracs spécifiques
        # situation.SetValCarac(perso.Perso.C_GLOIRE, 0)

        # famille

        # quartierDeDepart = situation.collectionQuartiers.getQuartierAleatoire(True)
        # situation.SetCarac(quartier.Quartier.C_QUARTIER, quartierDeDepart.nom_)
        situation[identite.Identite.C_NOM] = "Baudoin"

        # situation[jeanne.Jeanne.CARTE_ACTUELLE] = "bg carte481"
        return

label naissance:
    scene bg rue_haussmann
    with dissolve
    $ genererDateNaissance(situation_, 17)
    menu:
        "Choisissez votre coterie. Cela affectera non seulement votre personnage de départ mais aussi l'histoire principale."
        "Les templiers, une coterie d'honorables guerriers chrétiens ayant fait voeu de pauvreté et de chasteté":
            $ situation_.SetValCarac(coterie.Coterie.C_COTERIE, templiers.Templiers.ID)
        "Ben il n'y a rien d'autre ! ":
            $ situation_.SetValCarac(coterie.Coterie.C_COTERIE, "")

    if situation_.GetValCarac(coterie.Coterie.C_COTERIE) == templiers.Templiers.ID:
        $ genererPersoTemplier(situation_, traits_)

    # $ genererParents(situation_)
    jump initiation
