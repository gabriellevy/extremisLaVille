# ---------- quartier + ses boutons et ses fonctions associées

screen boutons_carte_genevilliers():
    imagebutton:
        xpos 638
        ypos 64
        auto "images/carte/bouton_saint_denis_%s.png"
        action Jump("saint_denis") alt "Saint Denis"
        focus_mask True
    imagebutton:
        xpos 281
        ypos 153
        auto "images/carte/bouton_la_defense_%s.png"
        action Jump("la_defense") alt "La Défense"
        focus_mask True
    imagebutton:
        xpos 460
        ypos 64
        idle "images/carte/bouton_genevilliers_localisation.png"
        focus_mask True

label genevilliers:
    # arrivée dans le quartier
    $ setattr(situation_, quartier.Quartier.C_QUARTIER, quartier.Genevilliers.NOM)
    scene bg genevilliers with dissolve
    show screen valeurs_traits
    $ evtAleatoire = determinationEvtCourant(situation_)
    $ renpy.call(evtAleatoire) # call comme ça les return à la fin des evts déclenchés nous ramènent ici
    # ici le joueur doit avoir le choix de ce qu'il veut faire dans ce quartier (dont toujours le choix => continuer son chemin)
    menu:
        "Maintenant..."
        "Vous continuez votre route":
            jump exploration
    jump exploration
