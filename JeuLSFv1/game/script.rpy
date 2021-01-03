label start:
    $ minimap = []
    $ ArriveForetFees = Room("Arrive foret fees","Salle2.png", 50, 60)
    $ TransitionKabeGouffre = Room("Transition Kabe gouffre","Salle2.png", 1, 2)
    $ ArbreABonbons = Room("Arbre a bonbons","Salle2.png", 1, 3)
    $ PassageObstrue = Room("Passage obstrue","Salle2.png", 1, 4)
    $ Bibliotheque = Room("Bibliotheque","Salle2.png", 1, 5)
    $ Labyrinthe = Room("Labyrinthe","Salle2.png", 1, 6)
    $ ClairiereDOliveau = Room("Clairiere d Oliveau","Salle2.png", 2, 1)
    $ Lac = Room("Lac","Salle2.png", 3, 1)
    $ Cuisine = Room("Cuisine","Salle2.png", 4, 1)
    $ NidDeLOiseau = Room("Nid de l oiseau","Salle2.png", 5, 1)
    $ PorteDuRoyaumeDesFees = Room("Porte du royaume des fees","Salle2.png", 6, 1)
    $ LieuDuVol = Room("Lieu du vol","Salle2.png", 7, 1)
    $ PseudoLabyrinthe = Room("Pseudo labyrinthe","Salle2.png", 8, 1)
    $ FalaiseAvecLierre = Room("Falaise avec lierre","Salle2.png", 3, 3)
    $ PiegeDeLAlchimiste = Room("Piege de l'alchimiste","Salle2.png", 20, 10)
    show screen minimapShow

    label Didacticiel:
    scene ISalle1
    $ minimap.append(ArriveForetFees)
    $ minimap.append(TransitionKabeGouffre)
    $ minimap.append(ArbreABonbons)
    $ minimap.append(PassageObstrue)
    $ minimap.append(Bibliotheque)
    $ minimap.append(Labyrinthe)
    $ minimap.append(ClairiereDOliveau)
    $ minimap.append(Lac)
    $ minimap.append(Cuisine)
    $ minimap.append(NidDeLOiseau)
    $ minimap.append(PorteDuRoyaumeDesFees)
    $ minimap.append(LieuDuVol)
    $ minimap.append(PseudoLabyrinthe)
    $ minimap.append(FalaiseAvecLierre)
    $ minimap.append(PiegeDeLAlchimiste)
    label Blackscreen1:
    "Comme à votre habitude, vous vous baladez dans la forêt. Le soleil brille comme toujours, mais cette fois-ci, vous sentez une légère brise tout à fait différente..."

    label LieuDArrivee2:
    #inclure des imagemap pour aller dans le gouffre ou dans la foret avec oliveau comme daprès le script
    label ClairiereDOliveau3:
    #Possibilité d’aller à différents endroits en vain.
    #Imagemap Oliveau vers label OliveauParle
    label OliveauLSF:
    #Inclure video de Oliveau qui parle en LSF (EAU) (voir FaceRig)
    "Qu’a-t-il dit?"
    menu:
        "Eau":
            jump TransitionNiveau3
        "Choix2":
            jump OliveauLSFL
        "Choix3":
            jump OliveauLSFL
        "Choix4":
            jump OliveauLSFL
    
    label TransitionNiveau3:
    "Vous avez passé la première épreuve de compréhension de la langue des signes, le jeu va donc s’adapter à votre niveau."
    menu:
        "Continuer":
            jump Niveau3
        "Annuler":
            jump OliveauLSFL

    label OliveauLSFL:
    #Inclure video de Oliveau E-A-U
        "Qu’a-t-il dit?"
    menu:
        "Eau":
            jump TransitionNiveau2
        "Choix2":
            jump OliveauSeau
        "Choix3":
            jump OliveauSeau
        "Choix4":
            jump OliveauSeau

    label TransitionNiveau2:
    "Vous avez passé la première épreuve de compréhension de la langue des signes, le jeu va donc s’adapter à votre niveau."
    menu:
        "Continuer":
            jump Niveau2
        "Annuler":
            jump OliveauSeau
    
    label OliveauSeau:
    #Oliveau te tend un sceau et te montre le lac, tu vas chercher de l’eau et tu passes niveau 1.
    #Obtention seau dans inventaire
    "Vous allez chercher de l'eau pour l'arbre qui avait de toute évidence très soif"
    label Niveau1:
    o "Quel est ton nom?"
    python:
        nom = renpy.input("Quel est ton nom?")
        nom = nom.strip() or "Anonyme"
    o "Bienvenue dans cette forêt pas tout à fait ordinaire [nom], Je me fait appeler Oliveau"
    #Video Oliveau O-L-I-V-E-A-U LSF "O-L-I-V-E-A-U; O-L-I-V-E-A-U O L I V E A U"
    #Succes Oliveau debloque
    

    "pause"

    return
