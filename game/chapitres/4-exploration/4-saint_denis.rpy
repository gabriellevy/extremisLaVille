# ---------- quartier + ses boutons et ses fonctions associées



screen boutons_carte_saint_denis():
    imagebutton:
        xpos 460
        ypos 64
        auto "images/carte/bouton_genevilliers_%s.png"
        action Jump("genevilliers") alt "Genevilliers"
        focus_mask True

label saint_denis:
    $ setattr(situation_, quartier.Quartier.C_QUARTIER, quartier.SaintDenis.NOM)
    # $ situation_.TourSuivant() # gérer temps qui passe
    scene bg saint_denis
    $ evtAleatoire = determinationEvtCourant(situation_)
    $ renpy.call(evtAleatoire) # call comme ça les return à la fin des evts déclenchés nous ramènent ici
    # ici le joueur doit avoir le choix de ce qu'il veut faire dans ce quartier (dont toujours le choix => continuer son chemin)
    menu:
        "Maintenant..."
        "Vous continuez votre route":
            jump exploration
    jump exploration
