
 # persos
define ordi = Character('Ordinateur', color="#097a1c") # == Arca Tamaris


label declenchement_templiers:
    scene bg priere
    with dissolve
    show screen valeurs_traits
    "déclenchement de l'histoire en tant que templier PAS FAIT => "

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




    jump premier_deplacement
