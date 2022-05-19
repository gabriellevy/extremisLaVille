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
    # from geographie import quartier
    from abs.humanite import identite
    from chapitres.classes import perso
    from abs.religions import religion
    from abs.humanite import pnj

    # def genererDateNaissance(situation, ageActuel=15):
    #     nbJoursDateNaissance = situation[temps.Date.DATE] - 365*ageActuel
    #     situation[temps.Date.DATE_NAISSANCE] = nbJoursDateNaissance

    def genererPerso(situation, tousLesTraits):

        # situation[trait.Altruisme.NOM] = trait.Trait.SEUIL_A_PAS

        # situation[metier.Metier.C_METIER] = u"Prince de sang"

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

label naissance:
    # $ genererDateNaissance(situation_, 13)
    $ genererPerso(situation_, traits_)
    # $ genererParents(situation_)
    jump intro
