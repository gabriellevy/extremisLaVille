# phase de navigation sur la carte
label tmp_exploration:
    scene bg priere
    with dissolve
    show screen valeurs_traits
    "phase principale de l'histoire PAS FAIT => "
    jump final

screen boutons_carte():
    imagebutton:
        xpos 638
        ypos 64
        auto "images/carte/bouton_saint_denis_%s.png"
        action Jump("saint_denis") alt "Saint Denis"
        focus_mask True

        # hotspot (26, 179, 125, 35) action Jump("saint_germain_en_laye") alt "Saint Germain en Laye"

label exploration:
    "stop tmp"
    scene carte_la_ville idle
    call screen boutons_carte

label saint_germain_en_laye:
    "Bienvenue chez les elfes."
    jump exploration

label saint_denis:
    "Bienvenue chez les templiers."
    jump exploration

label genevilliers:
    "Bienvenue chez les orks."
    jump exploration
