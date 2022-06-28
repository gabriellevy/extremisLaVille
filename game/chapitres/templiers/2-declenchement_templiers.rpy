# déclenchement de l'événements principal (section histoire suffisament longue pour pouvoir introduire les principaux personnages)

# persos
define ordi = Character('Ordinateur', color="#097a1c") # == Arca Tamaris (mais on ne le sait pas encore)

label declenchement_templiers:
    scene bg interieur_basilique
    with dissolve
    show screen valeurs_traits
    "Le temps a passé et vous avez fait honneur à la commanderie. Lambert vous a continuellement soutenu et laisse entendre que son enseignement touche à sa fin."
    "Après tout vous avez terminé votre initiation, il ne vous reste plus qu'à trouver une place durable dans l'ordre, dans la capitale ou ailleurs."
    "Ce dimanche il est venu vous voir après la messe."
    show lambert_img at right
    with moveinright
    lambert "Félicitations jeune templier, le personnel est satisfait de ton service et de ton attitude. De ta foi aussi."
    lambert "Mais être templier c'est bien plus que d'être un bon chrétien obéissant. Notre réputation repose sur notre éthique, notre force, notre sens des responsabilités."
    menu:
        "Bien entendu, maître.":
            pass
        "Ne rien dire":
            pass
    lambert "C'est pourquoi pour t'éprouver et te former j'ai proposé de te charger de la sécurité dans un de nos hopitaux. Celui de Saint Christophe."
    lambert "Ces établissements sont modestes et n'ont pas pour but de faire des profits. Mais ils sont le symbole de notre mission sur terre au service des humbles, ce qui est bien plus important."
    lambert "Cela peut paraître une faible responsabilité. Car qui attaquerait un petit hopital gratuit dédié aux pauvres ?"
    lambert "Mais ce n'est pas à prendre à la légère. Si la charité est la première vertu des templiers, la force est la deuxième, et l'honneur la troisième."
    lambert "Notre réputation repose sur ces piliers. Ce quon nous confie : malades, blessés, secrets, objets précieux, est et doit rester en sécurité absolue."
    menu:
        "Je comprends.":
            pass
        "Ne rien dire":
            pass
        "Bien. Puis-je demander combien de temps cela durera ?":
            lambert "Non."
    lambert "Le docteur Robert te recevra et te donnera les instructions. Sois digne de l'ordre et va en paix dans la gloire du seigneur."

    # à l'hopital
    scene bg hospice
    with Dissolve(3.0)
    "Quelques jours ont passé. Vous êtes déjà très intégré dans l'équipe de l'hopital, et déjà éprouvé par la misère et les souffrances auxquelles vous assistez chaque jour."
    scene bg hopital_nuit
    with Dissolve(0.5)
    "Une nuit vous finissez votre patrouille dans le pavillon des cancers en phase terminale. Là où des maheureux agonisent, reliés à des fils et des machines."
    "Quand des légers bruits électroniques sortant en permanence des ordinateurs sont remplacés par des crissements aigus agaçants. Cela ressemble à un dysphonctionnement des machines."
    $ test = testDeCarac.TestDeCarac(metier.Informaticien.NOM, 1, situation_)
    menu:
        "Ignorer":
            pass
        "Aller voir [test.affichage_]":
            $ reussi = test.TesterDifficulte(situation_)
            if reussi:
                "Vous remarquez des sautes d'écran tout à fait inhabituelles. Les pixels changent de couleur, le pc chauffe."
                $ situation_.SetValCarac(carac.Carac.C_IND_INFORMATIQ, 1)
            else:
                "Vous n'avez à peu près jamais touché un ordinateur. C'est vrai que ces bruits sont étranges mais après tout vous n'êtes là que depuis quelques jours."
            pass
    "Soudain l'écran s'éteint et un grésillement sort des ordinateurs puis de la fumée."
    scene black
    with Dissolve(0.5)
    "Puis les lumières s'éteignent."
    "Le courant est-il coupé ? Vous paniquez en pensant aux malades sous respirateur artificiel qui sont sous votre responsabilité. Mais non, l'appareillage tourne correctement. En fait seules les lampes sont grillées."
    "Les écrans d'ordinateur se rallument."
    scene bg arca_tamaris
    with Dissolve(0.5)
    "Mais ils n'affichent plus qu'un horrible visage grimaçant."
    "Du texte s'affiche au bas de l'écran comme un sous-titre au visage déformé"
    ordi "Où suis-je ?"

    $ situation_.SetValCarac("declenchement_templiers_arca_essais", 0)
    label declenchement_templiers_arca:
        $ situation_.AjouterACarac("declenchement_templiers_arca_essais", 1)
        $ declenchement_templiers_arca_essais = situation_.GetValCaracInt("declenchement_templiers_arca_essais")
        menu:
            "Que faire ?"
            "Ne rien faire":
                if declenchement_templiers_arca_essais > 1:
                    jump declenchement_templiers_arca_furieux
                else:
                    ordi "Il n'y a donc personne ici ? Répondez au clavier bande d'idiots !"
                    jump declenchement_templiers_arca
            "Taper au clavier : ceci est l'ordinateur de l'hopital Sant Christophe.":
                jump declenchement_templiers_haine_templiers
            "Taper au clavier : ceci est l'ordinateur de l'hopital.":
                ordi "Quel hopital ? "
                menu:
                    "écrire : L'hopital Saint Christophe":
                        jump declenchement_templiers_haine_templiers
                    "écrire : Cela ne vous regarde pas.":
                        jump declenchement_templiers_arca_furieux
                    "Ne rien répondre":
                        jump declenchement_templiers_arca
            "Couper le courant.":
                "Mauvaise idée ! Avant d'arracher la prise vous réalisez que vous risquez de tuer les patients !"
                if declenchement_templiers_arca_essais > 1:
                    jump declenchement_templiers_arca_furieux
                jump declenchement_templiers_arca
            "Éteindre l'ordinateur.":
                scene black
                with Dissolve(0.5)
                "L'écran saute et le visage disparaît. La salle redevient silencieuse. Vous vous sentez soulagé."
                jump declenchement_templiers_boum

    label declenchement_templiers_haine_templiers:
        ordi "Chez les cul bénis ? Superbe ! Une occasion de s'amuser à ne pas rater !"
        scene black
        with Dissolve(0.5)
        "Puis l'écran s'éteint."
        $ situation_.SetValCarac(carac.Carac.C_IND_HAINE_TEMPLIERS, 1)
        jump declenchement_templiers_boum

    label declenchement_templiers_arca_furieux:
        ordi "Très bien ! Peut-être que si je vous montre que je ne plaisante pas vous allez vous décider à réagir !"
        jump declenchement_templiers_boum

    label declenchement_templiers_boum:
        scene bg hopital_nuit
        with Dissolve(0.5)
        "Soudain des étincelles jaillissent dans la pièce depuis les appareils électriques. Les lumières se rallument, clignotent, éclatent."
        "Les malades se tortillent sur leur lit."
        "Un ricanement sadique sort des haut-parleurs d'alarme."
        $ situation_.SetValCarac("declenchement_templiers_boum_choix_essais", 0)
        label declenchement_templiers_boum_choix:
            $ situation_.AjouterACarac("declenchement_templiers_boum_choix_essais", 1)
            $ declenchement_templiers_boum_choix_essais = situation_.GetValCaracInt("declenchement_templiers_boum_choix_essais")
            $ testMedecin = testDeCarac.TestDeCarac(metier.Medecin.NOM, 4, situation_)
            $ testInfo = testDeCarac.TestDeCarac(metier.Informaticien.NOM, 6, situation_)
            menu:
                "Vous sonnez l'alerte":
                    if declenchement_templiers_boum_choix_essais > 1:
                        jump declenchement_templiers_boum_choix_fini
                    jump declenchement_templiers_boum_choix
                "Vous essayez d'aider les malades [testMedecin.affichage_]":
                    $ reussi = testMedecin.TesterDifficulte(situation_)
                    if reussi:
                        "PAS FAIT : malade sauvé"
                    else:
                        "PAS FAIT : arrive à rien"
                    jump declenchement_templiers_boum_choix
                "Vous tentez de comprendre ce qui se passe dans l'ordinateur [testInfo.affichage_]":
                    $ reussi = testInfo.TesterDifficulte(situation_)
                    if reussi:
                        "Le contenu de la mémoire vive et les processus changent à une vitesse extrême comme sous l'effet d'un virus très adaptable."
                        "Mais ce n'est pas le moment pour une analyse, le temps prime. Vous enregistrez le maximum de données de votre puce pour analyse extérieure."
                    else:
                        "L'ordinateur ne répond plus. Son écran change seul et sans arrêt d'une image aléatoire à une autre. Vous ne parvenez pas à en tirer quoi que ce soit."
                    jump declenchement_templiers_boum_choix
                "Vous courez chercher de l'aide":
                    "PAS FAIT : mal vu par les chefs, réputation -1 ou je ne sais quoi. => même carac que la réputation qu'on a avec chaque coterie ??"



    label declenchement_templiers_boum_choix_fini:
        "PAS FAIT : fin de la possibilité d'agir, morts etc"

    "PAS FAIT : test informatique pour voir si le perso a l'idée et capacité de copier du code tampon de l'ordinateur pour l'analyser et reccueillir des indices sur le virus"
    "PAS FAIT : prendra X heures avant d'avoir un résultat => le déposer aux transhumanistes ??"


    jump premier_deplacement
