#Python:
init python:
    config.screen_width=1280
    config.screen_height=720
    import time
    import pygame
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
        def __init__(self, name, video):
            self.name = name
            self.video = video

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
        def __init__(self, name, image):
            self.name = name
            self.image = image

#Initialisation Achievements
    Histoire_Alphabet= Achievements("Alphabet","Achievements/Histoire_Alphabet.png")
    Histoire_Compter= Achievements("Compter","Achievements/Histoire_Compter.png")
    Histoire_Magie= Achievements("Magie","Achievements/Histoire_Magie.png")
    Histoire_Niveau1= Achievements("Niveau1","Achievements/Histoire_Niveau1.png")
    Lettre_BIBLIOTHEQUE= Achievements("BIBLIOTHEQUE","Achievements/Lettre_BIBLIOTHEQUE.png")
    Lettre_CHWYZ= Achievements("CHWYZ","Achievements/Lettre_CHWYZ.png")
    Lettre_OLIVEAU= Achievements("Oliveau","Achievements/Lettre_Oliveau.png")
    Lettre_V = Achievements("V","Achievements/Lettre_V.png")
    Lettre_D = Achievements("D","Achievements/Lettre_D.png")  
    Lettre_S = Achievements("S","Achievements/Lettre_S.png")
    Lettre_B = Achievements("B","Achievements/Lettre_B.png")
    Lettre_F = Achievements("F","Achievements/Lettre_F.png")
    Lettre_G = Achievements("G","Achievements/Lettre_G.png")
    Lettre_J = Achievements("J","Achievements/Lettre_J.png")
    Lettre_K = Achievements("K","Achievements/Lettre_K.png")
    Lettre_MN = Achievements("MN","Achievements/Lettre_MN.png")
    Lettre_P = Achievements("P","Achievements/Lettre_P.png")
    Lettre_X = Achievements("X","Achievements/Lettre_X.png")
    Secret_EnfantIgnorant= Achievements("EnfantIgnorant","Achievements/Secret_EnfantIgnorant.png")
    Secret_GrosseBosse= Achievements("GrosseBosse","Achievements/Secret_GrosseBosse.png")
    Secret_TueurdOiseau= Achievements("TueurdOiseau","Achievements/Secret_TueurdOiseau.png")
    Sort_GREX= Achievements("GREX","Achievements/Sort_GREX.png")
    Sort_JUNQ= Achievements("JUNQ","Achievements/Sort_JUNQ.png")
    Sort_KAME= Achievements("KAME","Achievements/Sort_KAME.png")
    Sort_PIF= Achievements("PIF","Achievements/Sort_PIF.png")
    Sort_SOY= Achievements("SOY","Achievements/Sort_SOY.png")
#Initialisation Tableau
    dico = []
    avancement = ["null"]*50
    minimap = []
    inventaire = []
    magie = []
    achievements = []
#Initialisation Entier
    gentillesse = 0
    falaiseLierre = 0
    porteGouffre = 0
    achEnfantIgnorant = 0
    achV =0
    achD=0
    achS=0
    achB=0
    achF=0
    achG=0
    achJ=0
    achK=0
    achMN=0
    achP=0
    achBIBLIOTHEQUE=0
    achX=0
    achievementshow=0
    achOLIVEAU=0
    achCHWYZ=0
    achAlphabet=0
    achCompter=0
    achMagie=1
    achNiveau1=0
    achGrosseBosse=0
    achTueurdOiseau=0
    achGREX=0
    achJUNQ=0
    achKAME=0
    achPIF=0
    achSOY=0
    mapshow=0
    inventaireshow = 0
    PossibiliteKAME =0
    PossibiliteDOY =0
    PossibilitePIF=0
    PossibiliteJUNQ=0
    PossibiliteGREX=0
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
    Un = Mot("1", "oliveau_1_LSF.webm")
    Deux = Mot("2", "oliveau_2_LSF.webm")
    Trois = Mot("3", "oliveau_3_LSF.webm")
    Quatre = Mot("4", "oliveau_4_LSF.webm")
    Cinq = Mot("5", "oliveau_5_LSF.webm")
    Six = Mot("6", "oliveau_6_LSF.webm")
    Sept = Mot("7", "oliveau_7_LSF.webm")
    Huit = Mot("8", "oliveau_8_LSF.webm")
    Neuf = Mot("9", "oliveau_9_LSF.webm")
    Dix = Mot("10", "oliveau_10_LSF.webm")
    Onze = Mot("11", "oliveau_11_LSF.webm")
    Douze = Mot("12", "oliveau_12_LSF.webm")
    Treize = Mot("13", "oliveau_13_LSF.webm")
    Quatorze = Mot ("14", "oliveau_14_LSF.webm")
    Quinze = Mot("15", "oliveau_15_LSF.webm")
    Seize = Mot("16", "oliveau_16_LSF.webm")
    DixSept = Mot("17", "oliveau_17_LSF.webm")
    DixHuit = Mot ("18", "oliveau_18_LSF.webm")
    DixNeuf = Mot("19", "oliveau_19_LSF.webm")
    Vingt = Mot("20", "oliveau_20_LSF.webm")
#Initialisation inventaire
    Seau = Objet("Seau", "seau.png")
    Sifflet = Objet("Sifflet", "sifflet.png")
    LettreDeRemerciement = Objet("LettreDeRemerciement", "LettreDeRemerciement.png")
    Sucette = Objet("Sucette", "sucette.png")
    BouleDeCristal = Objet("Boule de cristal", "Boule_fantome.png")
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
        mot1=["JeuBiblio_BoulesCristal1.png","JeuBiblio_mot_AOC.png","AOC","Lettre_A_LSF.webm","Lettre_O_LSF.webm","Lettre_C_LSF.webm"]
        mot2=["JeuBiblio_BoulesCristal2.png","JeuBiblio_mot_CFP.png","CFP","Lettre_C_LSF.webm","Lettre_F_LSF.webm","Lettre_P_LSF.webm"]
        mot3=["JeuBiblio_BoulesCristal3.png","JeuBiblio_mot_DZS.png","DZS","Lettre_D_LSF.webm","Lettre_Z_LSF.webm","Lettre_S_LSF.webm"]
        mot4=["JeuBiblio_BoulesCristal4.png","JeuBiblio_mot_ELM.png","ELM","Lettre_E_LSF.webm","Lettre_L_LSF.webm","Lettre_M_LSF.webm"]
        mot5=["JeuBiblio_BoulesCristal5.png","JeuBiblio_mot_EPO.png","EPO","Lettre_E_LSF.webm","Lettre_P_LSF.webm","Lettre_O_LSF.webm"]
        mot6=["JeuBiblio_BoulesCristal6.png","JeuBiblio_mot_EVA.png","EVA","Lettre_E_LSF.webm","Lettre_V_LSF.webm","Lettre_A_LSF.webm"]
        mot7=["JeuBiblio_BoulesCristal6.png","JeuBiblio_mot_FOM.png","FOM","Lettre_F_LSF.webm","Lettre_O_LSF.webm","Lettre_M_LSF.webm"]
        mot8=["JeuBiblio_BoulesCristal7.png","JeuBiblio_mot_FSP.png","FSP","Lettre_F_LSF.webm","Lettre_S_LSF.webm","Lettre_P_LSF.webm"]
        mot9=["JeuBiblio_BoulesCristal8.png","JeuBiblio_mot_ICP.png","ICP","Lettre_I_LSF.webm","Lettre_C_LSF.webm","Lettre_P_LSF.webm"]
        mot10=["JeuBiblio_BoulesCristal9.png","JeuBiblio_mot_IZA.png","IZA","Lettre_I_LSF.webm","Lettre_Z_LSF.webm","Lettre_A_LSF.webm"]
        mot11=["JeuBiblio_BoulesCristal10.png","JeuBiblio_mot_LWV.png","LWV","Lettre_L_LSF.webm","Lettre_W_LSF.webm","Lettre_V_LSF.webm"]
        mot12=["JeuBiblio_BoulesCristal11.png","JeuBiblio_mot_MAV.png","MAV","Lettre_M_LSF.webm","Lettre_A_LSF.webm","Lettre_V_LSF.webm"]
        mot13=["JeuBiblio_BoulesCristal12.png","JeuBiblio_mot_OHA.png","OHA","Lettre_O_LSF.webm","Lettre_H_LSF.webm","Lettre_A_LSF.webm"]
        mot14=["JeuBiblio_BoulesCristal13.png","JeuBiblio_mot_OPB.png","OPB","Lettre_O_LSF.webm","Lettre_P_LSF.webm","Lettre_B_LSF.webm"]
        mot15=["JeuBiblio_BoulesCristal14.png","JeuBiblio_mot_PKO.png","PKO","Lettre_P_LSF.webm","Lettre_K_LSF.webm","Lettre_O_LSF.webm"]
        mot16=["JeuBiblio_BoulesCristal15.png","JeuBiblio_mot_PZK.png","PZK","Lettre_P_LSF.webm","Lettre_Z_LSF.webm","Lettre_K_LSF.webm"]
        mot17=["JeuBiblio_BoulesCristal16.png","JeuBiblio_mot_SNK.png","SNK","Lettre_S_LSF.webm","Lettre_N_LSF.webm","Lettre_K_LSF.webm"]
        mot18=["JeuBiblio_BoulesCristal17.png","JeuBiblio_mot_SUB.png","SUB","Lettre_S_LSF.webm","Lettre_U_LSF.webm","Lettre_B_LSF.webm"]
        mot19=["JeuBiblio_BoulesCristal18.png","JeuBiblio_mot_VYE.png","VYE","Lettre_V_LSF.webm","Lettre_Y_LSF.webm","Lettre_E_LSF.webm"]
        mot20=["JeuBiblio_BoulesCristal19.png","JeuBiblio_mot_WPC.png","WPC","Lettre_W_LSF.webm","Lettre_P_LSF.webm","Lettre_C_LSF.webm"]
        mot21=["JeuBiblio_BoulesCristal20.png","JeuBiblio_mot_ZFZ.png","ZFZ","Lettre_Z_LSF.webm","Lettre_F_LSF.webm","Lettre_Z_LSF.webm"]
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
        video = ["Lettre_V_LSF.webm","Lettre_H_LSF.webm","Lettre_D_LSF.webm","Lettre_L_LSF.webm","Lettre_Y_LSF.webm","Lettre_S_LSF.webm",
        "Lettre_C_LSF.webm","Lettre_A_LSF.webm","Lettre_W_LSF.webm","Lettre_E_LSF.webm","Lettre_I_LSF.webm","Lettre_O_LSF.webm",
        "Lettre_Z_LSF.webm","Lettre_U_LSF.webm"]
        coeur = 3
        return (tab,ordre,video,coeur)

    def jeuFiole_majtab(tableau,order,video):
        for i in range (16):
                if tableau[i][1] == order[0]:
                    tableau[i][1]=""
        order = order [1:]
        video = video [1:]
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

#Labyrinthe python
    dico_lab_vid ={"1":"fantome_1.webm","2":"fantome_2.webm","3":"fantome_3.webm","4":"fantome_4.webm","5":"fantome_5.webm","6":"fantome_6.webm",
    "7":"fantome_7.webm","8":"fantome_8.webm","9":"fantome_9.webm","A":"fantome_A.webm","B":"fantome_B.webm",
    "C":"fantome_C.webm","D":"fantome_D.webm","E":"fantome_E.webm","F":"fantome_F.webm","G":"fantome_G.webm","H":"fantome_H.webm","I":"fantome_I.webm",
    "J":"fantome_J.webm","K":"fantome_K.webm","L":"fantome_L.webm","M":"fantome_M.webm","N":"fantome_N.webm","O":"fantome_O.webm","P":"fantome_P.webm",
    "Q":"fantome_Q.webm","R":"fantome_R.webm","S":"fantome_S.webm","T":"fantome_T.webm","U":"fantome_U.webm","V":"fantome_V.webm",
    "W":"fantome_W.webm","X":"fantome_X.webm","Y":"fantome_Y.webm","Z":"fantome_Z.webm"}
    Choix_laby = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N",
    "O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    def random_code_lab():
        a_lab= renpy.random.randint(0,len(Choix_laby)-1)
        b_lab= renpy.random.randint(0,len(Choix_laby)-1)
        c_lab= renpy.random.randint(0,len(Choix_laby)-1)
        d_lab= renpy.random.randint(0,len(Choix_laby)-1)
        return (a_lab,b_lab,c_lab,d_lab)

    class Code_laby():
        def __init__(self):
            self.a_laby = 0
            self.b_laby = 0
            self.c_laby = 0
            self.d_laby = 0
            self.sum_code = ""

        def nouv_code(self):
            (a_l, b_l,c_l, d_l) = random_code_lab()
            self.a_laby = a_l
            self.b_laby = b_l
            self.c_laby = c_l
            self.d_laby = d_l
            self.sum_code = Choix_laby[self.a_laby] + Choix_laby[self.b_laby] + Choix_laby[self.c_laby] + Choix_laby[self.d_laby]

        def verif(code):
            return (self.sum_code == code)

    class Bon_chem():
        def __init__(self):
            self.n_laby = 0
            self.a_laby = 0
            self.b_laby = 0
            self.c_laby = 0

        def nouv_code(self,n):
            if n == 2:
                self.n_laby = renpy.random.randint(1,2)
                self.a_laby = renpy.random.randint(0,len(Choix_laby)-1)
                self.b_laby = renpy.random.randint(0,len(Choix_laby)-1)
            else:
                self.n_laby = renpy.random.randint(1,3)
                self.a_laby = renpy.random.randint(0,len(Choix_laby)-1)
                self.b_laby = renpy.random.randint(0,len(Choix_laby)-1)
                self.c_laby = renpy.random.randint(0,len(Choix_laby)-1)

    dico_panneau ={"1":"panneau_1.png","2":"panneau_2.png","3":"panneau_3.png","4":"panneau_4.png",
    "5":"panneau_5.png","6":"panneau_6.png","7":"panneau_7.png","8":"panneau_8.png",
    "9":"panneau_9.png","A":"panneau_A.png","B":"panneau_B.png", "C":"panneau_C.png",
    "D":"panneau_D.png","E":"panneau_E.png","F":"panneau_F.png","G":"panneau_G.png",
    "H":"panneau_H.png","I":"panneau_I.png","J":"panneau_J.png","K":"panneau_K.png",
    "L":"panneau_L.png","M":"panneau_M.png","N":"panneau_N.png","O":"panneau_O.png",
    "P":"panneau_P.png","Q":"panneau_Q.png","R":"panneau_R.png","S":"panneau_S.png",
    "T":"panneau_T.png","U":"panneau_U.png","V":"panneau_V.png","W":"panneau_W.png",
    "X":"panneau_X.png","Y":"panneau_Y.png","Z":"panneau_Z.png"}
    Choix_laby = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N",
    "O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#Cuisine
    MOUSEBUTTONDOWN=pygame.MOUSEBUTTONDOWN
    dico_ingr = {"beurre":[100,100], "oeufs":[300,100], "lait":[500,100], "levure":[700,100], "farine":[100,300], "sucre":[300,300], "sirop_de_rose":[500,300], "sirop_d'arsenic":[700,300]}

    def ing_dragged(drags, drop):

        if not drop:
            return
        store.show_drag = False
        renpy.hide_screen("ajout_ingr")
        renpy.show_screen("ajout_ingr")
        if ((drags[0].drag_name == "sirop_de_rose") or (drags[0].drag_name == "sirop_d'arsenic")):
            drags[0].snap(10000,10000)
            if (drags[0].drag_name == "sirop_de_rose"):            
                globals()['choix_sirop'] = 1
            else:
                globals()['choix_sirop'] = 2
        else:
            drags[0].snap(dico_ingr[drags[0].drag_name][0],dico_ingr[drags[0].drag_name][1])
            if gat.check(drags[0].drag_name):
                gat.remove_ingredient(drags[0].drag_name)
            else:
                gat.echec_ingr()
        return

    class Four(object):
        def __init__(self, sprite, speed, delay, ypos=0):
            self.sprite = sprite
            self.speed = speed
            self.delay = delay
            self.show = manager.create(sprite)
            self.show.x = 0
            self.show.y = ypos
            self.moving = False

        def update(self):
            if store.t + self.delay < time.time():
                self.moving = True
                self.x = self.x + self.speed
            else:
                pass

        @property
        def x(self):
            return self.show.x
        @x.setter
        def x(self, value):
            self.show.x = value

        @property
        def y(self):
            return self.show.y
        @y.setter
        def y(self, value):
            self.show.y = value

    def sprites_update(st):
        for sprite in sprites[:]:
            sprite.update()
            if sprite.x > config.screen_width:
                sprite.show.destroy()
                sprites.remove(sprite)
                store.misses += 1
                renpy.restart_interaction()
            if store.misses > 5:
                renpy.hide_screen("show_vars")
                renpy.hide_screen("le_feu_cuisson")
                renpy.hide_screen("marmite_cuisson")
                renpy.hide("_")
                renpy.hide("barre_flamme")
                renpy.jump("echec_jeu_four")
        return 0.05

    def sprites_event(ev, x, y, st):
        if ev.type == MOUSEBUTTONDOWN:
            if ev.button == 1:
                hit = False
                for sprite in sprites[:]:
                    if sprite.moving:
                        if int(sprite.x) in store.targets:
                            store.hits += 1
                            hit = True
                            sprite.show.destroy()
                            sprites.remove(sprite)
                            break
                if not hit:
                    store.misses += 1
                if store.misses > 5:
                    renpy.hide_screen("show_vars")
                    renpy.hide_screen("le_feu_cuisson")
                    renpy.hide_screen("marmite_cuisson")
                    renpy.hide("_")
                    renpy.hide("barre_flamme")
                    renpy.jump("echec_jeu_four")
                if store.hits > 10:
                    renpy.hide_screen("show_vars")
                    renpy.hide_screen("le_feu_cuisson")
                    renpy.hide_screen("marmite_cuisson")
                    renpy.hide("_")
                    renpy.hide("barre_flamme")
                    renpy.jump("fin_minijeu_cuisine")
                renpy.restart_interaction()


    #renvoie un tuple avec en 1. nombre de chaque ingrédients du gateau 2.
    def creer_list_ingr():
        l=[]
        n_oeufs = renpy.random.randint(2, 4)
        n_farine = renpy.random.randint(1, 9)
        n_levure = renpy.random.randint(1, 9)
        n_beurre = renpy.random.randint(1, 9)
        n_lait = renpy.random.randint(1, 9)
        n_sucre = renpy.random.randint(2, 4)
        #n_oeufs = renpy.random.randint(1, 1)
        #n_farine = renpy.random.randint(1, 1)
        #n_levure = renpy.random.randint(1, 1)
        #n_beurre = renpy.random.randint(1, 1)
        #n_lait = renpy.random.randint(1, 1)
        #n_sucre = renpy.random.randint(1, 1)
        n= [n_oeufs*5, n_farine, n_levure, n_beurre, n_lait, n_sucre*5]
        for i in range (n_oeufs):
            l.append("oeufs")
        for i in range (n_farine):
            l.append("farine")
        for i in range (n_levure):
            l.append("levure")
        for i in range(n_beurre):
            l.append("beurre")
        for i in range(n_lait):
            l.append("lait")
        for i in range(n_sucre):
            l.append("sucre")
        return (n,l)

#le gateau à préparer
    class Gateau:
        def __init__(self):
            (a,b) = creer_list_ingr()
            self.n_ingr = a
            self.ingredients = b
            self.n_oeufs = 0
            self.n_farine = 0
            self.n_levure = 0
            self.n_beurre = 0
            self.n_lait = 0
            self.n_sucre = 0

        def remove_ingredient(self, ing):
            (self.ingredients).remove(ing)
            if ing == "oeufs":
                self.n_oeufs += 5
            if ing == "farine":
                self.n_farine += 1
            if ing == "levure":
                self.n_levure += 1
            if ing == "beurre":
                self.n_beurre += 1
            if ing == "lait":
                self.n_lait += 1
            if ing == "sucre":
                self.n_sucre += 5
            renpy.restart_interaction()

        def echec_ingr(self):
            (self.ingredients).append("oups")

        def check(self, ing):
            return (ing in self.ingredients)

#Fonction arbre à bonbons
    bonbon1valeur = ""
    bonbon2valeur = ""
    bonbon3valeur = ""
    bonbon4valeur = ""
    bonbon5valeur = ""
    bonbon6valeur = ""

    def verif(a,b,c,d,e,f):
        if a=="1" and b=="1" and c=="1" and d=="1" and e=="1" and f=="1":
            return "jeuBonbonFin"
        else:
            return "jeuBonbon"

#Fonction Poursuite
    def dialog_beep(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/sfx-bip.wav", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()
