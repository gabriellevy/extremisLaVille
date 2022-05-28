# ---------- quartier + ses boutons et ses fonctions associées

screen boutons_carte_la_defense():
    imagebutton:
        xpos 460
        ypos 64
        auto "images/carte/bouton_genevilliers_%s.png"
        action Jump("genevilliers") alt "Genevilliers"
        focus_mask True

label la_defense:
    $ setattr(situation_, quartier.Quartier.C_QUARTIER, quartier.LaDefense.NOM)
    scene bg la_defense
    "Bienvenue chez les transhumanistes."
    jump exploration
