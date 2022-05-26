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
    lambert "À quel métier vous êtes vous formé durant ce séjour ?"
    menu:
        "Je travaillais dans les champs, je m'occupais des troupeaux.":
            $ setattr(situation_, metier.Metier.C_METIER, metier.Paysan.NOM)
            $ AjouterACarac(metier.Paysan.NOM, 3)
            $ AjouterACarac(trait.Constitution.NOM, 1)
            lambert "Un métier noble et précieux pour la communauté. Et qui endurcit le corps. Je vous félicite."
        "Le prêtre de la commanderie m'a fait l'honneur de me nommer vicaire.":
            $ setattr(situation_, metier.Metier.C_METIER, metier.Pretre.NOM)
            $ AjouterACarac( metier.Pretre.NOM, 3)
            $ AjouterACarac(religion.Religion.C_MIRACLE, 1)
            lambert "Un grand honneur en effet. Votre foi et votre dévotion doivent être à toute épreuve."
        "J'étais un chevalier éclaireur, je patrouillais le long des frontières.":
            $ setattr(situation_, metier.Metier.C_METIER, metier.Chevalier.NOM)
            $ AjouterACarac( metier.Chevalier.NOM, 3)
            $ AjouterACarac( metier.Paysan.NOM, 1)
            $ AjouterACarac( metier.Guerrier.NOM, 1)
            lambert "Vous avez du affronter bien des dangers. Ici votre vie devrait être plus calme."
        "Je suis formé en architecture et ait été mis à contribution pour rénover le château de la commanderie.":
            $ setattr(situation_, metier.Metier.C_METIER, metier.Architecte.NOM)
            $ AjouterACarac(metier.Architecte.NOM, 3)
            lambert "Remarquable à votre âge. Les fortifications sont inutiles ici mais les architectes sont toujours précieux."
        "Je travaillais dans la comptabilité. Cette commanderie conserve et transfère les richesses de nombreux voyageurs.":
            $ setattr(situation_, metier.Metier.C_METIER, metier.Banquier.NOM)
            $ AjouterACarac(metier.Banquier.NOM, 3)
            lambert "Une compétence indispensable pour l'ordre. Mais qui a du soumettre votre serment de pauvreté à une dure tentation."
        "J'étais employé à l'hopital.":
            $ setattr(situation_, metier.Metier.C_METIER, metier.Medecin.NOM)
            $ AjouterACarac(metier.Medecin.NOM, 3)
            lambert "Alors vous allez être mis vite à contribution. Notre hopital est le plus grande la Ville et en grand manque de personnel."
        "Je traquais les monstres dans les forêts alentour.":
            $ setattr(situation_, metier.Metier.C_METIER, metier.TueurDeMonstres.NOM)
            $ AjouterACarac(metier.TueurDeMonstres.NOM, 3)
            $ AjouterACarac(metier.Aventurier.NOM, 3)
            $ AjouterACarac(trait.Observation.NOM, 1)
            lambert "Vous avez décidément été formé à la dure ! Nous avons peu de monstres ici mais ils se cachent bien, vos talents de traqueur seront surement utiles."
        "J'étais ermite dans la forêt.":
            $ AjouterACarac(metier.Aventurier.NOM, 1)
            $ AjouterACarac(trait.Ascetisme.NOM, 2)
            $ AjouterACarac(trait.Spiritualite.NOM, 1)
            $ AjouterACarac(religion.Religion.C_MIRACLE, 1)
            lambert "Ho vous êtes un mystique ? Je vous envie, nous aurons beaucoup de choses à nous dire je pense."
        "J'étais ouvrier.":
            $ setattr(situation_, metier.Metier.C_METIER, metier.Ouvrier.NOM)
            $ AjouterACarac(metier.Ouvrier.NOM, 3)
            $ AjouterACarac(trait.Constitution.NOM, 1)
            lambert "Un métier noble et précieux pour la communauté. Et qui endurcit le corps. Je vous félicite."

    lambert "Dans un premier temps, pour que vous vous intégriez à la commanderie et à la vie citadine, vous allez suivre une formation plus en accord avec notre activité."

    menu:
        "Où pensez vous que vous serez le plus dans votre élément ?"
        "J'aimerais avoir l'honneur de travailler un peu dans la grande bibliothèque.":
            lambert "Vous n'aurez pas accès à toutes les ailes mais pour le reste cela doit pouvoir se faire."
            $ AjouterACarac(metier.Bibliothecaire.NOM, 1)
        "J'aimerais travailler dans la rue à maintenir l'ordre.":
            lambert "Très bonne idée. Vous ferez connaissance avec le métier et avec la Ville."
            lambert "L'ordre du temple a en effet une grande importance dans la police de la ville et je devrais pouvoir arranger cela facilement."
            $ AjouterACarac(metier.Policier.NOM, 1)
        "J'aimerais protéger la commanderie et mes camarades.":
            lambert "Très bonne idée. Vous ferez connaissance avec le métier et avec la Ville."
            lambert "Les templiers sont toujours bienvenus dans la sécurité parttout sur Extremis. Car notre éthique et nos compétences martiales sont largement reconnues."
            $ AjouterACarac(metier.Vigile.NOM, 1)
            $ AjouterACarac(metier.GardeDuCorps.NOM, 1)

    show screen valeurs_traits
    jump declenchement
