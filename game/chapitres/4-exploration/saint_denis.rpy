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
    scene bg saint_denis
    "Bienvenue chez les templiers."
    jump exploration
