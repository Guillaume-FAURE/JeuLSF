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

    label Salle1:
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
    scene ISalle1

    label Salle2:
    scene ISalle2

    "pause"

    return
