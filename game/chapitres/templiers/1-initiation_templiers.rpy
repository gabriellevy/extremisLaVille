# musiques
define audio.principale_temple = "musique/templiers/principale.mp3"
define audio.rejoindre_temple = "musique/templiers/rejoindre_doux_spirituel.mp3"
define audio.tedonimum = "musique/templiers/tedonimum.mp3"
define audio.saladinbesiegejerusalem = "musique/templiers/saladinbesiegejerusalem.mp3"
define audio.guyderosesquandary = "musique/templiers/guyderosesquandary.mp3"

 # persos
define baudoin = Character('Baudoin', color="#195ac2") # héros templier

image lambert_img = "coteries/templiers/lambert.png"
define lambert = Character('Lambert', color="#82260d")

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
    "Mais avant l'initiation personnalisez un peu votre personnage."

    menu:
        "Quelle est votre plus grande qualité ?"
        "Je suis rusé":
            $ AjouterACarac(trait.Ruse.NOM, 3)
        "Je suis convainquant et plein de charme":
            $ AjouterACarac(trait.Persuasion.NOM,3)
        "Je suis très habile":
            $ AjouterACarac(trait.Habilete.NOM,3)
        "Je suis coriace comme un noyer":
            $ AjouterACarac(trait.Constitution.NOM,3)
        "Je suis fort comme Hercule":
            $ AjouterACarac(trait.Force.NOM,3)
        "J'ai l'oeil perçant comme un aigle":
            $ AjouterACarac(trait.Observation.NOM,3)
        "Je suis très intelligent":
            $ AjouterACarac(trait.Intelligence.NOM,3)

    menu:
        "Quelle est votre plus grand défaut ?"
        "Un tempérament ultraviolent":
            $ AjouterACarac(trait.Ruse.NOM, 5)
        "Je suis maladroit" if situation_.GetValCaracInt(trait.Habilete.NOM) <= 0:
            $ RetirerACarac(trait.Habilete.NOM, 2)
        "Je suis facilement malade":
            $ RetirerACarac(trait.Constitution.NOM, 2)
        "Un peu obsédé sexuel, en tout cas trop pour un templier":
            $ AjouterACarac(trait.Sexualite.NOM, 5)
        "La cupidité":
            $ AjouterACarac(trait.Cupidite.NOM, 5)
        "La bêtise":
            $ RetirerACarac(trait.Intelligence.NOM, 3)

    show lambert_img at right
    with moveinright
    lambert "Bienvenue jeune apprenti Baudoin. Je m'appelle Lambert, grand ordonateur du temple. Je suis chargé de vous accueillir dans la grande commanderie de la Ville. Vous venez de loin m'a t'on dit ?"
    baudoin "Je viens de la commanderie du Danube. C'est là que j'ai été envoyé pour tester mon endurance, ma volonté et ma dévotion envers l'ordre et envers notre seigneur Jésus Christ."
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
        "Je suis formé en architecture et ai été mis à contribution pour rénover le château de la commanderie.":
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
            $ AjouterACarac(trait.Erudition.NOM, 1)
        "J'aimerais travailler dans la rue à maintenir l'ordre.":
            lambert "Très bonne idée. Vous ferez connaissance avec le métier et avec la Ville."
            lambert "L'ordre du temple a en effet une grande importance dans la police de la ville et je devrais pouvoir arranger cela facilement."
            $ AjouterACarac(metier.Policier.NOM, 1)
        "J'aimerais protéger la commanderie et mes camarades.":
            lambert "Très bonne idée. Vous ferez connaissance avec le métier et avec la Ville."
            lambert "Les templiers sont toujours bienvenus dans la sécurité parttout sur Extremis. Car notre éthique et nos compétences martiales sont largement reconnues."
            $ AjouterACarac(metier.Vigile.NOM, 1)
            $ AjouterACarac(metier.GardeDuCorps.NOM, 1)
        "Nous avions très peu d'ordinateurs sur le Danube mais ils me fascinaient. Pourrais-je apprendre à m'en servir ?":
            lambert "Un intérêt peu orthodoxe pour un templier. Mais la technologie est un mal nécessaire dans la Ville.  Il est sain que certain d'entre nous la maîtrisent. J'arrangerai cela."
            $ AjouterACarac(metier.Informaticien.NOM, 1)

    hide lambert_img
    with moveoutright
    show screen valeurs_traits
    "A FAIRE ici : un peu de remplissage, présentation de l'Ordre etc..."
    jump templiersPostule

label templiersPostule:
    "Le temps de votre dernier test est venu."
    "Vous avez demandé à rejoindre l'Ordre du Temple. C'est une des coteries les plus sélectives. Préparez vous à subir une série d'épreuves qui détermineront si vous êtes dignes de l'Ordre."
    scene bg catacombes
    $ religionActuelle = situation_.GetValCarac(religion.Religion.C_RELIGION)
    if religionActuelle != religion.Christianisme.NOM:
        "Malheureusement seul un chrétien à la foi pure et désintéressée peut entrer dans l'Ordre. Quelles que soient vos protestations les ordonnateurs sentent la faiblesse de votre foi et vous refusent."
        jump defaite
    show lambert_img at right
    with moveinright
    "Vous vous trouvez dans un noir tunnel. Vous et chacun des deux ordonnateurs avez une torche en main. Mais elles peinent à éclairer à quelques mètres alors que le tunnel semble très long vu la résonnance de vos voix."
    lambert "Nous sommes dans les souterrains de la basilique de Saint Denis, les catacombes du Temple."
    lambert "Nous avons jugé votre demande sincère ; maintenant vous allez devoir prouver votre pureté, votre courage et votre détermination."
    lambert "Votre tâche est simple : suivez le tunnel, ne vous en écartez sous aucun prétexte et vous serez digne de devenir un des nôtres."
    lambert "Que Dieu soit avec vous."
    hide lambert_img
    with moveoutright
    "Vous suivez le tunnel et réalisez qu'il est infiniment plus long que vous ne le pensiez."
    "Vous dépassez plusieurs croisements mais n'en empruntez aucun."
    "Vous perdez très vite la notion du temps. L'humidité vous gèle, vous vous mettez déjà à avoir faim. Des vapeurs étranges montent depuis les grilles sous vos pieds."
    "Plusieurs fois vous titubez et vous écorchez sur une pierre tant le chemin est plein de trous et votre lumière de plus en plus faible."
    "Vous croyez entendre une musique."
    "Vous voyez de la lumière au loin."
    "Ce n'était pas un rêve. Une salle luxueuse se trouve à votre droite au bout d'un court tunnel. De bonnez odeurs de nourriture en viennent ainsi que des rires."
    $ test = testDeCarac.TestDeCarac(trait.Ascetisme.NOM, 3, situation_)
    menu:
        "Si vous vous penchez pour voir un peu.":
            jump TempliersPostule_t1_phase2
        "Si vous continuez. [test.affichage_]":
            jump TempliersPostule_t1

    label TempliersPostule_t1:
    $ reussi = test.TesterDifficulte(situation_)
    if reussi:
        jump TempliersPostule_t2
    else:
        "La curiosité est trop forte, vous vous penchez pour  jeter juste un petit coup d'oeil."
        jump TempliersPostule_t1_phase2

    label TempliersPostule_t1_phase2:
        scene bg banquet
        "Vous apercevez nettement une grande tablée entourée de convives vêtues étrangement et s'amusant beaucoup."
        "La pièce est très sombre comme votre tunnel mais ça ajoute encore à l'ambiance et les convives semblent profiter avec plaisir des coins sombres."
        "Une d'entre elles vous apperçoit. D'abord surprise elle prend vite une attitude accueillante et vous fait signe de la rejoindre."
    menu:
        "Si vous acceptez l'invitation.":
            jump TempliersPostule_t1_rate
        "Si vous continuez. [test.affichage_]":
            jump TempliersPostule_t1_phase3

    label TempliersPostule_t1_phase3:
    $ reussi = test.TesterDifficulte(situation_)
    if reussi:
        jump TempliersPostule_t2
    else:
        "Vous êtes comme hypnotisé par la musique, les odeurs, et le charmant souvenir de la belle inconnue et vous marchez dans la grande salle."
        jump TempliersPostule_t1_rate

    label TempliersPostule_t1_rate:
        "Échouer si rapidement à des instructions si simples. L'Ordre est très déçu, vous aurez peut-être une autre chance un jour..."
        "PAS FAIT : développer cette rencontre pourrait être marrant !"

        # PAS FAIT : gérer que même avec un échec on s'en sort un peu autrement :
        jump TempliersPostule_t3 # tmp ?
        jump defaite

    label TempliersPostule_t2:
        scene bg catacombes
        "Votre reprenez votre longue marche pendant Dieu seul sait combien de longues très longues minutes ou heures."
        "Bientôt un large gouffre se trouve devant vous. Aucune issue à droite, aucune issue à gauche. De toute façon vous devez suivre le tunnel jusqu'au bout."
        "Vous pouvez en voir la suite de l'autre côté du trou mais il s'agit d'un saut de plus de 4 mètres à accomplir ! Vous ne voyez pas le fond du trou mais vu la faible portée de votre torche ça ne veut pas dire pour autant qu'il est profond."
        menu:
            "Si vous préférez retourner en arrière.":
                jump TempliersPostule_t2_rate
            "Si vous prenez votre élan pour tenter de sauter de l'autre côté.":
                jump TempliersPostule_t2_saute
            "Si vous marchez droit dans le vide.":
                jump TempliersPostule_t2_marche

    label TempliersPostule_t2_saute:
        $ testForce = testDeCarac.TestDeCarac(trait.Force.NOM, 6, situation_)
        $ reussi = testForce.TesterDifficulte(situation_)
        if reussi:
            "C'est à peine croyable mais vous parvenez à bondir de l'autre côté du gouffre sans même vous blesser à l'arrivée."
            jump TempliersPostule_t3
        else:
            "Vous prenez courageusement votre élan mais au moment de sauter c'est la catastrophe, vous doutez, perdez pied et tombez dans le gouffre."
            jump TempliersPostule_t2_tombe

    label TempliersPostule_t2_marche:
        $ testMiracle = testDeCarac.TestDeCarac(religion.Religion.C_MIRACLE, 2, situation_)
        $ reussi = testMiracle.TesterDifficulte(situation_)
        if reussi:
            "C'est un miracle ! Vos pieds restent suspendus en l'air et vous parvenez de l'autre côté du gouffre en marchant doucement sans ressentir aucune peur."
            jump TempliersPostule_t3
        else:
            "Vous avez beau vous concentrer, il n'y a pas de miracle. Votre pied lancé en avant ne rencontre que le vide et vous vous écrasez piteusement au fond du gouffre."
            jump TempliersPostule_t2_tombe


    label TempliersPostule_t2_tombe:
        $ blessure = blessures_.InfligerBlessureAleatoire(situation_, 1, 8)
        $ texteBlessure = blessure.GetDescriptionRecu()
        "Il n'est heureusement pas très profond mais tomber sur des caillous pointus dans le noir est une dure expérience. [texteBlessure]"
        jump TempliersPostule_t2_rate

    label TempliersPostule_t2_rate:
        "Quel triste manque de foi. Vous n'avez pas le coeur d'un templier voilà tout. Vous trouverez votre propre voie un jour."

        # PAS FAIT : gérer que même avec un échec on s'en sort un peu autrement :
        jump TempliersPostule_t3 # tmp ?
        jump defaite

    label TempliersPostule_t3:
        "PAS FAIT : seulement deux tests pour l'instant, un de plus ça serait bien !"

    label TempliersPostule_reussi:
        "Vous marchez encore presque une heure dans l'obscurité quandenfin vous appercevez des rayons de lumière du jour."
        "Le tunnel finit en un escalier de métal qui remonte en plein quinzième arrondissement."
        show lambert_img at right
        with moveinright
        lambert "Bravo mon fils tu as prouvé ta valeur morale et physique. Tu es digne de nous rejoindre dès aujourd'hui"
        jump TempliersRejoindre

    jump declenchement

label TempliersRejoindre:
    scene bg univ_templiers
    show lambert_img at right
    with moveinright
    play music rejoindre_temple noloop
    lambert "Lisez le serment de l'Ordre."
    "Exauce, nous t'en prions, Seigneur, nos prières, de sorte que tu daignes bénir ton serviteur qui ce jour avec ton assentiment a ceint le glaive,"
    "qu'il soit le défenseur contre la cruauté de païens et de tous les méchants, et le protecteur des églises, des veuves, des orphelins, de tous tes serviteurs,"
    "et qu'avec ton aide il soit la terreur et l'épouvante de tous ceux qui rejettent la sainte foi."
    $ coterieTempliers = templiers.Templiers()
    $ coterieTempliers.RejoindreCoterie(situation_)
    $ prenom = situation_[identite.Identite.C_PRENOM]
    $ nom = situation_[identite.Identite.C_NOM]
    lambert "Dorénavant vous vous appellerez [prenom] [nom]."
    lambert "Lisez maintenant les voeux."
    "Moi [prenom], je fais profession et je jure chasteté, renoncement à la propriété et obéissance à Dieu, à la bienheureuse Marie et à toi, frère Aldebert, maître de l'Ordre du Temple et à tes successeurs, selon la règle et les institutions de l'ordre du Temple,"
    "et je jure que j'obéirai, à toi et à tes successeurs, jusqu'à la mort."
    $ situation_.SetValCarac(religion.Religion.C_VOEU_CHASTETE, "1")
    $ situation_.SetValCarac(religion.Religion.C_VOEU_PAUVRETE, "1")
    $ situation_.SetValCarac(templiers.Templiers.C_RICHESSE, templiers.Templiers.RICHESSE_TEMPLE)
    $ situation_.SetValCarac(trait.Richesse.NOM, templiers.Templiers.RICHESSE_TEMPLE)
    lambert "Voici votre robe blanche marquée du symbole de l'ordre."
    lambert "Voici votre épée rituelle de templier."
    $ situation_.AjouterObjet(objet_spe.EpeeTemplier.ID)
    lambert "Portez cette croix avec fierté et honneur, que tous les hommes qui vous croiseront continuent à y voir un symbole de pureté et de force comme ça a toujours été le cas depuis la fondation de notre Ordre il y a plus de deux mille ans."
    $ situation_.SetValCarac(quartier.Quartier.C_QUARTIER, coterieTempliers.quartier_)
    jump declenchement_templiers
