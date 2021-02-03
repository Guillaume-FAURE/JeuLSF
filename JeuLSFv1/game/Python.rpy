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

#Classe Objet pour les objets qui sont dans l'inventaire
    class Objet:
        def __init__(self, name, image):
            self.name = name
            self.image = image
#Classe Magie pour les sorts appris
    class Magie:
        def __init__(self, name, image):
            self.name = name
            self.image = image

#Initialisation Tableau
    dico = []
    avancement = ["null"]*50
    minimap = []
    inventaire = []
    magie = []
    gentillesse = 0
    achievement = []
#Initialisation Variables de la minimap
    ArriveForetFees = Room("Arrive foret fees","ArriveForetFees","Salle2.png", 55, 55)
    TransitionKabeGouffre = Room("Transition Kabe gouffre","TransitionKabeGouffre","Salle2.png", 30, 52)
    ArbreABonbons = Room("Arbre a bonbons","ArbreABonbons","Salle2.png", 5, 50)
    PassageObstrue = Room("Passage obstrue","PassageObstrue","Salle2.png", 32, 37)
    Bibliotheque = Room("Bibliotheque","Bibliotheque","Salle2.png", 6, 35)
    Labyrinthe = Room("Labyrinthe","Labyrinthe","Salle2.png", 12, 20)
    ClairiereDOliveau = Room("Clairiere d Oliveau","ClairiereDOliveau","Salle2.png", 55, 40)
    Lac = Room("Lac","Lac","Salle2.png", 80, 38)
    Cuisine = Room("Cuisine","Cuisine","Salle2.png", 83, 52)
    NidDeLOiseau = Room("Nid de l oiseau","NidDeLOiseau","Salle2.png", 105, 35)
    PorteDuRoyaumeDesFees = Room("Porte du royaume des fees","PorteDuRoyaumeDesFees","Salle2.png", 107, 2)
    LieuDuVol = Room("Lieu du vol","LieuDuVol","Salle2.png", 57, 18)
    PseudoLabyrinthe = Room("Pseudo labyrinthe","PseudoLabyrinthe","Salle2.png", 73, 3)
    FalaiseAvecLierre = Room("Falaise avec lierre","FalaiseAvecLierre","Salle2.png", 33, 13)
    PiegeDeLAlchimiste = Room("Piege de l'alchimiste","PiegeDeLAlchimiste","Salle2.png", 14, 2)
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
    Zero = Mot("0")
    Un = Mot("1")
    Deux = Mot("2")
    Trois = Mot("3")
    Quatre = Mot("4")
    Cinq = Mot("5")
    Six = Mot("6")
    Sept = Mot("7")
    Huit = Mot("8")
    Neuf = Mot("9")
#Initialisation inventaire
    Sifflet = Objet("Sifflet", "Salle2.png")
    Sucette = Objet("Sucette", "Salle2.png")
    BouleDeCristal = Objet("Boule de cristal", "Salle2.png")
#Initialisation magie
    DOY = Magie("DOY", "Salle2.png")
    KAME = Magie("KAME", "Salle2.png")
    PIF = Magie("PIF", "Salle2.png")
    JUNQ = Magie("JUNQ", "Salle2.png")
