# phase de navigation sur la carte
label tmp_exploration:
    scene bg priere
    with dissolve
    show screen valeurs_traits
    "phase principale de l'histoire PAS FAIT => "
    jump final

init -40 python:
    import random

label exploration:
    scene carte_la_ville idle
    # temps qui passe (ici ?)
    $ situation_.AvanceDeXMinutes(random.randint(15,30))
    $ quartierStr = getattr(situation_, quartier.Quartier.C_QUARTIER)
    if quartierStr == quartier.SaintGermainEnLaye.NOM:
        call screen boutons_carte_saint_germain_en_laye
    if quartierStr == quartier.SaintDenis.NOM:
        call screen boutons_carte_saint_denis
    if quartierStr == quartier.Genevilliers.NOM:
        call screen boutons_carte_genevilliers
    if quartierStr == quartier.LaDefense.NOM:
        call screen boutons_carte_la_defense
