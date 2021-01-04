#Python:
init python:
#Class Room pour les salles de la minimap
    class Room:
        def __init__(self, name, label, image, x, y):
            self.name = name
            self.label = label
            self.image = image
            self.x = x
            self.y = y
#Classe Mot pour les mots appris qui sont dans le dictionnaire
    class Mot:
        def __init__(self, name):
            self.name = name

#Initialisation Tableau
    dico = []
    avancement = [50]
    minimap = []
#Initialisation Variables de la minimap
    ArriveForetFees = Room("Arrive foret fees","ArriveForetFees","Salle2.png", 50, 60)
    TransitionKabeGouffre = Room("Transition Kabe gouffre","TransitionKabeGouffre","Salle2.png", 1, 2)
    ArbreABonbons = Room("Arbre a bonbons","ArbreABonbons","Salle2.png", 1, 3)
    PassageObstrue = Room("Passage obstrue","PassageObstrue","Salle2.png", 1, 4)
    Bibliotheque = Room("Bibliotheque","Bibliotheque","Salle2.png", 1, 5)
    Labyrinthe = Room("Labyrinthe","Labyrinthe","Salle2.png", 1, 6)
    ClairiereDOliveau = Room("Clairiere d Oliveau","ClairiereDOliveau","Salle2.png", 2, 1)
    Lac = Room("Lac","Lac","Salle2.png", 3, 1)
    Cuisine = Room("Cuisine","Cuisine","Salle2.png", 4, 1)
    NidDeLOiseau = Room("Nid de l oiseau","NidDeLOiseau","Salle2.png", 5, 1)
    PorteDuRoyaumeDesFees = Room("Porte du royaume des fees","PorteDuRoyaumeDesFees","Salle2.png", 6, 1)
    LieuDuVol = Room("Lieu du vol","LieuDuVol","Salle2.png", 7, 1)
    PseudoLabyrinthe = Room("Pseudo labyrinthe","PseudoLabyrinthe","Salle2.png", 8, 1)
    FalaiseAvecLierre = Room("Falaise avec lierre","FalaiseAvecLierre","Salle2.png", 3, 3)
    PiegeDeLAlchimiste = Room("Piege de l'alchimiste","PiegeDeLAlchimiste","Salle2.png", 20, 10)
#Initialisation Variables du dictionnaire
    A = Mot("A")
    B = Mot("B")
    C = Mot("C")
    D = Mot("D")
    E = Mot("E")
    F = Mot("F")
    G = Mot("G")
    H = Mot("H")
    I = Mot("I")
    J = Mot("J")
    K = Mot("K")
    L = Mot("L")
    M = Mot("M")
    N = Mot("N")
    O = Mot("O")
    P = Mot("P")
    Q = Mot("Q")
    R = Mot("R")
    S = Mot("S")
    T = Mot("T")
    U = Mot("U")
    V = Mot("V")
    W = Mot("W")
    X = Mot("X")
    Y = Mot("Y")
    Z = Mot("Z")

