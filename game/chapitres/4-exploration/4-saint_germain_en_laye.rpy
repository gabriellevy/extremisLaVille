# ---------- quartier + ses boutons et ses fonctions associées

screen boutons_carte_saint_germain_en_laye():
    imagebutton:
        xpos 281
        ypos 153
        auto "images/carte/bouton_la_defense_%s.png"
        action Jump("la_defense") alt "La Défense"
        focus_mask True

label saint_germain_en_laye:
    $ setattr(situation_, quartier.Quartier.C_QUARTIER, quartier.SaintGermainEnLaye.NOM)
    # $ situation_.TourSuivant() # gérer temps qui passe
    scene bg saint_germain_en_laye with dissolve
    $ evtAleatoire = determinationEvtCourant(situation_)
    $ renpy.call(evtAleatoire) # call comme ça les return à la fin des evts déclenchés nous ramènent ici
    # ici le joueur doit avoir le choix de ce qu'il veut faire dans ce quartier (dont toujours le choix => continuer son chemin)
    menu:
        "Maintenant..."
        "Vous continuez votre route":
            jump exploration
    jump exploration
