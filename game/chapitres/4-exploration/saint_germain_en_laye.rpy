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
    scene bg saint_germain_en_laye
    "Bienvenue chez les elfes."
    jump exploration
