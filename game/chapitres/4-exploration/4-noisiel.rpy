# ---------- quartier + ses boutons et ses fonctions associées



screen boutons_carte_noisiel():
    imagebutton:
        xpos 638
        ypos 64
        auto "images/carte/bouton_saint_denis_%s.png"
        action Jump("saint_denis") alt "Saint Denis"
        focus_mask True
    imagebutton:
        xpos 914
        ypos 448
        auto "images/carte/bouton_saint_maur_des_fosses_%s.png"
        action Jump("saint_maur_des_fosses") alt "Saint Maur des fossés"
        focus_mask True
    imagebutton:
        xpos 1217
        ypos 308
        idle "images/carte/bouton_noisiel_localisation.png"
        focus_mask True

label noisiel:
    # arrivée dans le quartier
    $ setattr(situation_, quartier.Quartier.C_QUARTIER, quartier.Noisiel.NOM)
    scene bg noisiel with dissolve
    show screen valeurs_traits
    $ evtAleatoire = determinationEvtCourant(situation_)
    $ renpy.call(evtAleatoire) # call comme ça les return à la fin des evts déclenchés nous ramènent ici
    # ici le joueur doit avoir le choix de ce qu'il veut faire dans ce quartier (dont toujours le choix => continuer son chemin)
    menu:
        "Maintenant..."
        "Vous continuez votre route":
            jump exploration
    jump exploration
