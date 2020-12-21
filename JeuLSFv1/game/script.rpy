label start:
    $ minimap = []
    $ ArriveForetFees = Room("Arrive foret fees","Salle2.png", 540, 600)
    $ TransitionKabeGouffre = Room("Transition Kabe gouffre","Salle2.png", 400, 600)
    $ ArbreABonbons = Room("Arbre a bonbons","Salle2.png", 260, 600)
    $ PassageObstrue = Room("Passage obstrue","Salle2.png", 400, 500)
    $ Bibliotheque = Room("Bibliotheque","Salle2.png", 400, 230)
    $ Labyrinthe = Room("Labyrinthe","Salle2.png", 400, 230)
    $ ClairiereDOliveau = Room("Clairiere d Oliveau","Salle2.png", 400, 230)
    $ Lac = Room("Lac","Salle2.png", 400, 230)
    $ Cuisine = Room("Cuisine","Salle2.png", 400, 230)
    $ NidDeLOiseau = Room("Nid de l oiseau","Salle2.png", 400, 230)
    $ PorteDuRoyaumeDesFees = Room("Porte du royaume des fees","Salle2.png", 400, 230)
    $ LieuDuVol = Room("Lieu du vol","Salle2.png", 400, 230)
    $ PseudoLabyrinthe = Room("Pseudo labyrinthe","Salle2.png", 400, 230)
    $ FalaiseAvecLierre = Room("Falaise avec lierre","Salle2.png", 400, 230)
    $ PiegeDeLAlchimiste = Room("Piege de l'alchimiste","Salle2.png", 400, 230)
    show screen minimapShow

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

    m "après ce message ce sera la salle 2"
    label Salle2:
    scene ISalle2

    "pause"

    return
