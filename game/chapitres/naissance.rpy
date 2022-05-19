# fichier où sont générés les phrases d'ambiance à afficher quand il ne se passe rien durant un mois particulier

init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import testDeCarac
    from abs import condition
    from abs.humanite import trait
    from spe.humanite import pnj_jeanne
    from abs.univers import temps
    # from geographie import quartier
    from abs.humanite import identite
    from chapitres.classes import jeanne
    from abs.religions import religion
    from abs.humanite import pnj

    def genererDateNaissance(situation, ageActuel=15):
        nbJoursDateNaissance = situation[temps.Date.DATE] - 365*ageActuel
        situation[temps.Date.DATE_NAISSANCE] = nbJoursDateNaissance

    def genererJeanne(situation, tousLesTraits):

        # situation[trait.Altruisme.NOM] = trait.Trait.SEUIL_A_PAS

        # situation[metier.Metier.C_METIER] = u"Prince de sang"

        # compétences professionnelles
        # situation[metier.Politique.NOM] = trait.Trait.SEUIL_A

        # caracs spécifiques
        situation.SetValCarac(jeanne.Jeanne.C_SAINTETE, 0)
        situation.SetValCarac(jeanne.Jeanne.C_POPULARITE_SOLDATS, 0)
        situation.SetValCarac(jeanne.Jeanne.C_CONFIANCE_ROI, 0)
        situation.SetValCarac(jeanne.Jeanne.C_POPULARITE_PEUPLE, 0)
        situation.SetValCarac(jeanne.Jeanne.C_GLOIRE, 0)

        # famille

        # quartierDeDepart = situation.collectionQuartiers.getQuartierAleatoire(True)
        # situation.SetCarac(quartier.Quartier.C_QUARTIER, quartierDeDepart.nom_)
        situation[identite.Identite.C_NOM] = "Jeanne"

        # situation[jeanne.Jeanne.CARTE_ACTUELLE] = "bg carte481"
        return

    def genererParents(situation):
        pere = pnj_jeanne.GenererPNJJeanne(True, situation, 43 * 12 *30 + 24)
        pere.prenom_ = "Jacques"
        pere.nom_ = "d'Arc"
        # pere.portraitStr_ = "images/portraits/childeric.jpg"
        situation.SetValCarac(pnj.Pnj.C_PERE, pere)

        mere = pnj_jeanne.GenererPNJJeanne(False, situation, 36 * 12 *30 + 297)
        mere.prenom_ = "Isabelle"
        mere.nom_ = "Romée"
        # mere.portraitStr_ = "images/portraits/basine.jpg"
        situation.SetValCarac(pnj.Pnj.C_MERE, mere)

label naissance:
    $ genererDateNaissance(situation_, 13)
    $ genererJeanne(situation_, traits_)
    $ genererParents(situation_)
    jump intro
