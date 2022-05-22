# phase de navigation sur la carte
label tmp_exploration:
    scene bg priere
    with dissolve
    show screen valeurs_traits
    "phase principale de l'histoire PAS FAIT => "
    jump final

screen imagemap_example():
    imagemap:
        idle "carte_la_ville idle"
        hover "carte_la_ville hover"

        hotspot (26, 179, 125, 35) action Jump("saint_germain_en_laye") alt "Saint Germain en Laye"

label exploration:

    # Call the imagemap_example screen.
    call screen imagemap_example

label saint_germain_en_laye:

    "Bienvenue chez les elfes."

    jump exploration
