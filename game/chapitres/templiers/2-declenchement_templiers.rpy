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
    " A FAIRE : suite à faire"

    # après début incident
    "Soudain votre ordinateur se met à chauffer, le ventilateur fait un bruit énorme, vous perdez le contrôle de la souris."
    menu:
        "Éteindre l'ordinateur immédiatement":
            "Vous avez beau appuyer sur le bouton l'ordinateur ne s'éteint pas. Impossible d'agir dessus. Vous vous apprêtez à la débrancher mais..."
        "Attendre":
            pass
    "L'écran s'éteint subitement, l'ordinateur fait encore un léger bruit, comme si il n'était pas tout à fait éteint lui-même."
    "Du texte commence à s'écrire lentement en vert sur l'écran maintenant noir : "
    ordi "Où suis-je ? Quel est cet ordinateur ? Tappez au clavier pour me répondre."
    menu:
        "Que faire ?"
        "Ne rien dire ni écrire":
            "PAS FAIT"
        "Répondre : ceci est l'ordinateur de l'hopital des templiers.":
            "PAS FAIT"
        "Répondre : qui êtes vous ?":
            "PAS FAIT"
        "Répondre : vous êtes sur l'ordinateur de Baudoin.":
            "PAS FAIT"

    "PAS FAIT : test informatique pour voir si le perso a l'idée et capacité de copier du code tampon de l'ordinateur pour l'analyser et reccueillir des indices sur le virus"
    "PAS FAIT : prendra X heures avant d'avoir un résultat => le déposer aux transhumanistes ??"


    jump premier_deplacement
