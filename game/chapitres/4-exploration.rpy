# phase de navigation sur la carte
label tmp_exploration:
    scene bg priere
    with dissolve
    show screen valeurs_traits
    "phase principale de l'histoire PAS FAIT => "
    jump final

screen boutons_carte_saint_germain_en_laye():
    imagebutton:
        xpos 638
        ypos 64
        auto "images/carte/bouton_saint_denis_%s.png"
        action Jump("saint_denis") alt "Saint Denis"
        focus_mask True

screen boutons_carte_genevilliers():
    imagebutton:
        xpos 638
        ypos 64
        auto "images/carte/bouton_saint_denis_%s.png"
        action Jump("saint_denis") alt "Saint Denis"
        focus_mask True

screen boutons_carte_saint_denis():
    imagebutton:
        xpos 460
        ypos 64
        auto "images/carte/bouton_genevilliers_%s.png"
        action Jump("genevilliers") alt "Genevilliers"
        focus_mask True

label exploration:
    "stop tmp --2"
    scene carte_la_ville idle
    $ quartierStr = getattr(situation_, quartier.Quartier.C_QUARTIER)
    if quartierStr == quartier.SaintGermainEnLaye.NOM:
        call screen boutons_carte_saint_germain_en_laye
    if quartierStr == quartier.SaintDenis.NOM:
        call screen boutons_carte_saint_denis
    if quartierStr == quartier.Genevilliers.NOM:
        call screen boutons_carte_genevilliers

label saint_germain_en_laye:
    $ setattr(situation_, quartier.Quartier.C_QUARTIER, quartier.SaintGermainEnLaye.NOM)
    scene bg saint_germain_en_laye
    "Bienvenue chez les elfes."
    jump exploration

label saint_denis:
    $ setattr(situation_, quartier.Quartier.C_QUARTIER, quartier.SaintDenis.NOM)
    scene bg saint_denis
    "Bienvenue chez les templiers."
    jump exploration

label genevilliers:
    $ setattr(situation_, quartier.Quartier.C_QUARTIER, quartier.Genevilliers.NOM)
    scene bg genevilliers
    "Bienvenue chez les orks."
    jump exploration
