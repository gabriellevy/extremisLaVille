# musiques
define audio.principale_temple = "musique/templiers/principale.mp3"
 # persos
define baudoin = Character('Baudoin', color="#87faf4") # héros templier

image lambert_img = "coteries/templiers/lambert.png"
define lambert = Character('Lambert', color="#e30909")

label initiation_templiers:
    scene bg univ_templiers
    with dissolve
    # intro :
    play music principale_temple noloop
    "Le temple est basé sur la foi inébranlable en Dieu et sur l'honneur guerrier de l'aristocratie franque."
    "Les templiers sont avant tout des guerriers saints avec un code de l'honneur très strict. "
    "Ce code de l'honneur méprise la cupidité et l'ostentation mais l'enrichissement n'est pas interdit, surtout lorsqu'il est utilisé pour financer les nombreux hopitaux de l'ordre. "
    "Ainsi les templiers sont aussi mercenaires tant que la cause est jugée honorable par l'ordre. "
    "L'université du temple est une somptueuse abbaye de pierre. "
    "Le confort y est médiocre comme y pousse la doctrine du temple mais la camaraderie et la foi inébranlable des occupants réchauffent le coeur de tous les apprentis."

    show lambert_img at right
    with moveinright
    lambert "Bienvenue jeune apprenti. Je suis chargé de vous accueillir dans la grande commanderie de la Ville. Vous venez de loin m'a t'on dit ?"
    baudoin "De la commanderie du Danube. C'est là que j'ai été envoyé pour tester mon endurance, ma volonté et ma dévotion envers l'ordre et envers notre seigneur Jésus Christ."
    baudoin "J'y suis resté un an et je viens seulement d'arriver. C'est la première fois que j'entre dans la capitale."
    lambert "Une destination rude. Vous devez donc déjà vous être endurci et intégré à l'ordre. Mais vous n'êtes cependant pas encore un templier."
    menu:
        "À quel métier vous êtes vous formé durant ce séjour ?"
        "Je travaillais dans les champs, je m'occupais des troupeaux.":
            $ setattr(situation_, metier.Metier.C_METIER, metier.Paysan.NOM)
            $ setattr(situation_, metier.Paysan.NOM, 3)
            $ AjouterACarac(trait.Constitution.NOM, 1)
            "Un métier noble et précieux pour la communauté. Et qui endurcit le corps. Je vous félicite."
        "Le prêtre de la commanderie m'a fait l'honneur de me nommer vicaire.":
            $ setattr(situation_, metier.Metier.C_METIER, metier.Pretre.NOM)
            $ setattr(situation_, metier.Pretre.NOM, 3)
            $ AjouterACarac(religion.Religion.C_MIRACLE, 1)
            "Un grand honneur en effet. Votre foi et votre dévotion doivent être à toute épreuve."


    show screen valeurs_traits
    jump declenchement
