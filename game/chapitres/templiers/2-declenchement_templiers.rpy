
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
    lambert "Mais être templier c'est bien plus que d'être un bon chrétien obéissant. Notre réputation repose sur notre éthique, notre force de caractère, notre sens des responsabilités."
    menu:
        "Bien entendu, maître.":
            pass
        "Ne rien dire":
            pass
    lambert "C'est pourquoi pour t'éprouver et te former j'ai proposé de te charger de la sécurité dans un de nos hopitaux. Celui de Saint Christophe."
    lambert "Ces établissements sont modestes et n'ont pas pour but de faire des profits. Mais ils sont le symbole de notre mission sur terre au service des humbles, ce qui est bien plus important."
    "A FAIRE : petite intro de la première semaine de boulot (le problème arrive selement quelques jours après arrivée du héros => fait exprès par Lambert le traître)"

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
