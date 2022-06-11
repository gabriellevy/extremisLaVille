# ---------- quartier + ses boutons et ses fonctions associées



screen boutons_carte_saint_maur_des_fosses():
    imagebutton:
        xpos 638
        ypos 64
        auto "images/carte/bouton_saint_denis_%s.png"
        action Jump("saint_denis") alt "Saint Denis"
        focus_mask True
    imagebutton:
        xpos 1217
        ypos 308
        auto "images/carte/bouton_noisiel_%s.png"
        action Jump("noisiel") alt "Noisiel"
        focus_mask True

label saint_maur_des_fosses:
    # arrivée dans le quartier
    $ setattr(situation_, quartier.Quartier.C_QUARTIER, quartier.SaintMaurDesFosses.NOM)
    scene bg saint_maur_des_fosses with dissolve
    show screen valeurs_traits
    $ evtAleatoire = determinationEvtCourant(situation_)
    $ renpy.call(evtAleatoire) # call comme ça les return à la fin des evts déclenchés nous ramènent ici
    # ici le joueur doit avoir le choix de ce qu'il veut faire dans ce quartier (dont toujours le choix => continuer son chemin)
    menu:
        "Maintenant..."
        "Vous continuez votre route":
            jump exploration
    jump exploration
