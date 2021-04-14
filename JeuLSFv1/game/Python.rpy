#Python:
init python:
    import random
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

#Classe Achievements pour les achievements appris
    class Achievements:
        def __init__(self, name, image, bool):
            self.name = name
            self.image = image
            self.bool = 0

#Initialisation Tableau
    dico = []
    avancement = ["null"]*50
    minimap = []
    inventaire = []
    magie = []
    gentillesse = 0
    achievement = []
    falaiseLierre = 0
    nbOliveau = 0
#Initialisation Variables de la minimap
    ArriveForetFees = Room("Arrive foret fees","ArriveForetFees","ArriveForetFees.jpg", 55, 55)
    Gouffre = Room("Gouffre","Gouffre","Gouffre.jpg", 30, 52)
    ArbreABonbons = Room("Arbre a bonbons","ArbreABonbons","Salle2.png", 5, 50)
    FondDuGouffre = Room("FondDuGouffre","FondDuGouffre","FondDuGouffre.jpg", 32, 37)
    Bibliotheque = Room("Bibliotheque","Bibliotheque","Salle2.png", 6, 35)
    Labyrinthe = Room("Labyrinthe","Labyrinthe","Salle2.png", 12, 20)
    ClairiereDOliveau = Room("Clairiere d Oliveau","ClairiereDOliveau","Salle2.png", 55, 40)
    Lac = Room("Lac","Lac","Salle2.png", 80, 38)
    Cuisine = Room("Cuisine","Cuisine","Salle2.png", 83, 52)
    NidDeLOiseau = Room("Nid de l oiseau","NidDeLOiseau","Salle2.png", 105, 35)
    PorteDuRoyaumeDesFees = Room("Porte du royaume","PorteDuRoyaumeDesFees","Salle2.png", 107, 2)
    LieuDuVol = Room("Lieu du vol","LieuDuVol","Salle2.png", 57, 18)
    PseudoLabyrinthe = Room("Pseudo labyrinthe","PseudoLabyrinthe","Salle2.png", 73, 3)
    Falaise = Room("Falaise","Falaise","Salle2.png", 33, 13)
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
    DOY = Magie("DOY", "doy.png")
    KAME = Magie("KAME", "kame.png")
    PIF = Magie("PIF", "pif.png")
    JUNQ = Magie("JUNQ", "junq.png")
    GREX = Magie("GREX", "grex.png")
#Initialisation achievements
    

#Bibliotheque
# ----- DEBUT PYTHON JEU BIBLIOTHEQUE -----

    def jeuBiblio_initVar():
        mot1=["JeuBiblio_BoulesCristal1.png","AEI_mot.png","AEI","AEI_film.mpeg"]
        mot2=["JeuBiblio_BoulesCristal2.png","AEI_mot.png","AEI","AEI_film.mpeg"]
        mot3=["JeuBiblio_BoulesCristal3.png","AEI_mot.png","AEI","AEI_film.mpeg"]
        mot4=["JeuBiblio_BoulesCristal4.png","AEI_mot.png","AEI","AEI_film.mpeg"]
        mot5=["JeuBiblio_BoulesCristal5.png","AEI_mot.png","AEI","AEI_film.mpeg"]
        mot6=["JeuBiblio_BoulesCristal6.png","AEI_mot.png","AEI","AEI_film.mpeg"]
        mot7=["JeuBiblio_BoulesCristal7.png","AEI_mot.png","AEI","AEI_film.mpeg"]
        mot8=["JeuBiblio_BoulesCristal8.png","AEI_mot.png","AEI","AEI_film.mpeg"]
        mot9=["JeuBiblio_BoulesCristal9.png","AEI_mot.png","AEI","AEI_film.mpeg"]
        mot10=["JeuBiblio_BoulesCristal10.png","AEI_mot.png","AEI","AEI_film.mpeg"]
        mot11=["JeuBiblio_BoulesCristal11.png","AEI_mot.png","AEI","AEI_film.mpeg"]
        mot12=["JeuBiblio_BoulesCristal12.png","AEI_mot.png","AEI","AEI_film.mpeg"]
        mot13=["JeuBiblio_BoulesCristal13.png","AEI_mot.png","AEI","AEI_film.mpeg"]
        mot14=["JeuBiblio_BoulesCristal14.png","AEI_mot.png","AEI","AEI_film.mpeg"]
        mot15=["JeuBiblio_BoulesCristal15.png","AEI_mot.png","AEI","AEI_film.mpeg"]
        mot16=["JeuBiblio_BoulesCristal16.png","AEI_mot.png","AEI","AEI_film.mpeg"]
        mot17=["JeuBiblio_BoulesCristal17.png","AEI_mot.png","AEI","AEI_film.mpeg"]
        mot18=["JeuBiblio_BoulesCristal18.png","AEI_mot.png","AEI","AEI_film.mpeg"]
        mot19=["JeuBiblio_BoulesCristal19.png","AEI_mot.png","AEI","AEI_film.mpeg"]
        mot20=["JeuBiblio_BoulesCristal20.png","AEI_mot.png","AEI","AEI_film.mpeg"]
        mot21=["JeuBiblio_BoulesCristal21.png","AEI_mot.png","AEI","AEI_film.mpeg"]
        tab = [mot1,mot2,mot3,mot4,mot5,mot6,mot7,mot8,mot9,mot10,mot11,mot12,mot13,mot14,mot15,mot16,mot17,mot18,mot19,mot20,mot21]
        rep=random.sample(tab,3)
        repV=[0,0,0]
        coeur = 3
        return rep,repV,tab,coeur

    def jeuBiblio_validation(repV):
        if repV[0]==1 and repV[1]==1 and repV[2]==1:
            res = "jeuBiblio_fingagner"
        else:
            res = "jeuBiblio_loop"
        return res

    def jeuBiblio_echec(coeur):
        if coeur <= 0:
            res = "jeuBiblio_finperdu"
        else:
            res = "jeuBiblio_loop"
        return res

# ----- FIN PYTHON JEU BIBLIOTHEQUE -----

# --- DEBUT PYTHON JEU FIOLE ---

    def jeuFiole_initVar():
        fiole1=["JeuFiole_FioleA.png","A"]
        fiole2=["JeuFiole_FioleC.png","C"]
        fiole3=["JeuFiole_FioleD.png","D"]
        fiole4=["JeuFiole_FioleE.png","E"]
        fiole5=["JeuFiole_FioleH.png","H"]
        fiole6=["JeuFiole_FioleI.png","I"]
        fiole7=["JeuFiole_FioleL.png","L"]
        fiole8=["JeuFiole_FioleM.png","M"]
        fiole9=["JeuFiole_FioleN.png","N"]
        fiole10=["JeuFiole_FioleO.png","O"]
        fiole11=["JeuFiole_FioleS.png","S"]
        fiole12=["JeuFiole_FioleU.png","U"]
        fiole13=["JeuFiole_FioleV.png","V"]
        fiole14=["JeuFiole_FioleW.png","W"]
        fiole15=["JeuFiole_FioleY.png","Y"]
        fiole16=["JeuFiole_FioleZ.png","Z"]
        tab = [fiole1,fiole2,fiole3,fiole4,fiole5,fiole6,fiole7,fiole8,fiole9,fiole10,fiole11,fiole12,fiole13,fiole14,fiole15,fiole16]
        ordre = ["V","H","D","L","Y","S","C","A","W","E","I","O","Z","U"]
        coeur = 3
        return (tab,ordre,coeur)

    def jeuFiole_majtab(tableau,order):
        for i in range (16):
                if tableau[i][1] == order[0]:
                    tableau[i][1]=""
        order = order [1:]
        if not order:
            order.append("fin")
        return (tableau,order)

    def jeuFiole_fin(order):
        if order[0]!="fin":
            res = "jeuFiole_loop"
        else:
            res = "jeuFiole_fingagner"
        return res

    def jeuFiole_nul(coeur):
        if coeur <= 0:
            res = "jeuFiole_finperdu"
        else:
            res = "jeuFiole_loop"
        return res

# --- FIN PYTHON JEU FIOLE ---

