 # persos
image arca_tamaris_img = "coteries/templiers/histoire/arca_tamaris.png"
define arca_tamaris = Character('Arca Tamaris', color="#660033")

label final_templiers:
    scene bg univ_templiers with dissolve
    show screen valeurs_traits
    show arca_tamaris_img at right
    with moveinright
    arca_tamaris "Salut mon bichon"
    jump fin_cycle
