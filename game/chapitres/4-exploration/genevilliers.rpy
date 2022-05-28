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

label genevilliers:
    $ setattr(situation_, quartier.Quartier.C_QUARTIER, quartier.Genevilliers.NOM)
    scene bg genevilliers
    "Bienvenue chez les orks."
    jump exploration
