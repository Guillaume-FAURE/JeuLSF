###Menu
screen menuShow:
    imagebutton:
        idle "SacIdle.png"
        hover "SacHover.png"
        at sizeButton
        xalign 0.98
        yalign 0.02
        action [Show("menu"), Hide ("menuShow")]
        
screen menu:
    imagebutton:
        idle "menuBackground.png"
        at sizeMenuBackground
        xalign 0.99
        yalign 0.01
    imagebutton:
        idle "SacHover.png"
        hover "SacIdle.png"
        at sizeButton
        xalign 0.98
        yalign 0.02
        action [Hide("menu") , Show ("menuShow")]
    imagebutton:
        idle "iconeMap.png"
        at sizeButton
        xalign 0.98
        yalign 0.15
        action If ((mapshow == 0), true = [SetVariable("mapshow", mapshow + 1), Show ("minimap")], false =[Hide ("minimap"), SetVariable("mapshow", 0)])
    imagebutton:
        idle "achievementShow.png"
        at sizeButton
        xalign 0.98
        yalign 0.85
        action If ((achievementshow == 0), true = [SetVariable("achievementshow", achievementshow + 1), Show ("achievements")], false =[Hide ("achievements"), SetVariable("achievementshow", 0)])
    imagebutton:
        idle "inventaireShow.png"
        at sizeButton
        xalign 0.98
        yalign 0.30
        action If ((inventaireshow == 0), true = [SetVariable("inventaireshow", inventaireshow + 1), Show ("inventaire")], false =[Hide ("inventaire"), SetVariable("inventaireshow", 0)])

screen minimap:
    $ s = -1
    imagebutton:
        idle "carte.png"
        at sizeMapBackground
        xpos 0
        ypos 0
    for i in minimap:
        frame:
            xpos i.x*10
            ypos i.y*10
            imagebutton:
                idle i.image
                at sizeRoom
                action If ((PossibiliteKAME==1), true=[Hide ("minimap"),Jump (i.label)], false=[Show(KAMEPasPossible)])
        frame:
            xpos i.x*10-65
            ypos i.y*10+75
            text i.name
screen achievements:
    $ x=0
    $ y=0
    imagebutton:
        idle "Background/black.png"
        at sizeMapBackground
        xpos 0
        ypos 0
    for i in achievements:
        imagebutton:   
            xpos x
            ypos y
            idle i.image
            at sizeAchievement
        if x<=590:
            $ x+=300
        else:
            $ x=0
            $ y+=200
screen inventaire:
    $ x=0
    $ y=0
    imagebutton:
        idle "Background/black.png"
        at sizeMapBackground
        xpos 0
        ypos 0
    for i in inventaire:
        imagebutton:   
            xpos x
            ypos y
            idle i.image
            at sizeObjet
        if x<=590:
            $ x+=200
        else:
            $ x=0
            $ y+=300

###Sorts
screen KAMEPasPossible:
    frame:
        xalign 0.5
        yalign 0.5
        text "{size=48}{color=#fd0a0a}Impossible de voler si on n'est pas en extérieur!{/color}{/size}"
    imagebutton:
        xalign 0.97
        yalign 0.45
        idle "fermeridle.png"
        hover "fermerhover.png"
        at sizeFermer
        action (Hide("KAMEPasPossible"))
screen DOYPasPossible:
    frame:
        xalign 0.5
        yalign 0.5
        text "{size=48}{color=#fd0a0a}Faire pousser des plantes ne servirait à rien ici!{/color}{/size}"
    imagebutton:
        xalign 0.96
        yalign 0.45
        idle "fermeridle.png"
        hover "fermerhover.png"
        at sizeFermer
        action (Hide("DOYPasPossible"))
screen PIFPasPossible:
    frame:
        xalign 0.5
        yalign 0.5
        text "{size=48}{color=#fd0a0a}Il n'y a rien à casser ici!{/color}{/size}"
    imagebutton:
        xalign 0.73
        yalign 0.45
        idle "fermeridle.png"
        hover "fermerhover.png"
        at sizeFermer
        action (Hide("PIFPasPossible"))
screen JUNQPasPossible:
    frame:
        xalign 0.5
        yalign 0.5
        text "{size=48}{color=#fd0a0a}Il n'y a pas d'eau!{/color}{/size}"
    imagebutton:
        xalign 0.68
        yalign 0.45
        idle "fermeridle.png"
        hover "fermerhover.png"
        at sizeFermer
        action (Hide("JUNQPasPossible"))
screen GREXPasPossible:
    frame:
        xalign 0.5
        yalign 0.5
        text "{size=48}{color=#fd0a0a}Creuser ne servirait à rien ici!{/color}{/size}"
    imagebutton:
        xalign 0.79
        yalign 0.45
        idle "fermeridle.png"
        hover "fermerhover.png"
        at sizeFermer
        action (Hide("GREXPasPossible"))

screen KAME:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.45
        yalign 0.39
        action [Hide ("Perdu1ToPerdu2"), Jump ("Perdu2")]
screen DOY:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.45
        yalign 0.39
        action [Hide ("Perdu1ToPerdu2"), Jump ("Perdu2")]
screen PIF:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.45
        yalign 0.39
        action [Hide ("Perdu1ToPerdu2"), Jump ("Perdu2")]
screen JUNQ:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.45
        yalign 0.39
        action [Hide ("Perdu1ToPerdu2"), Jump ("Perdu2")]
screen GREX:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.45
        yalign 0.39
        action [Hide ("Perdu1ToPerdu2"), Jump ("Perdu2")]

'''
screen gentillesse:
    frame:
        xalign 0.03
        yalign 0.97
        text "Gentillesse:"
    hbox:
        xalign 0.155
        yalign 0.967
        spacing 1
        for i in range (gentillesse):
            add "white.png" size(30,30)
'''

###Achievements
image achEnfantIgnorant:
    "Achievements/Secret_EnfantIgnorant.png"
image achCompter:
    "Achievements/Histoire_Compter.png"
image achMagie:
    "Achievements/Histoire_Magie.png"
image achAlphabet:
    "Achievements/Histoire_Alphabet.png"
image achNiveau1:
    "Achievements/Histoire_Niveau1.png"
image achGrosseBosse:
    "Achievements/Secret_GrosseBosse.png"
image achTueurdOiseau:
    "Achievements/Secret_TueurdOiseau.png"
image achGREX:
    "Achievements/Sort_GREX.png"
image achJUNQ:
    "Achievements/Sort_JUNQ.png"
image achKAME:
    "Achievements/Sort_KAME.png"
image achPIF:
    "Achievements/Sort_PIF.png"
image achSOY:
    "Achievements/Sort_SOY.png"
image achV:
    "Achievements/Lettre_V.png"
image achD:
    "Achievements/Lettre_D.png"
image achS:
    "Achievements/Lettre_S.png"
image achB:
    "Achievements/Lettre_B.png"
image achF:
    "Achievements/Lettre_F.png"
image achG:
    "Achievements/Lettre_G.png"
image achJ:
    "Achievements/Lettre_J.png"
image achK:
    "Achievements/Lettre_K.png"
image achMN:
    "Achievements/Lettre_MN.png"
image achP:
    "Achievements/Lettre_P.png"
image achBILBIOTHEQUE:
    "Achievements/Lettre_BIBLIOTHEQUE.png"
image achX:
    "Achievements/Lettre_X.png"
image achOLIVEAU:
    "Achievements/Lettre_OLIVEAU.png"
image achCHWYZ:
    "Achievements/Lettre_CHWYZ.png"
image achMagie:
    "Achievements/Histoire_Magie.png"

#Objet
image seau:
    "seau.png"
image seauPlein:
    "seauPlein.png"
image sifflet:
    "sifflet.png"
image LettreDeRemerciement:
    "LettreDeRemerciement.png"
image Sucette:
    "sucette.png"
image BouleCristal:
    "Boule_fantome.png"
image FioleM:
    "JeuFiole_FioleM.png"
image FioleN:
    "JeuFiole_FioleN.png"
image sacFiole:
    "sac_fiole_alphabet.png"
image indication:
    "indicationBibliotheque.png"
image LinkHoverNE:
    "LinkHoverNE.png"

#####Background
image BlackScreen:
    "images/Background/Black.png"
image Perdu1:
    "images/Background/Perdu1.png" 
image Perdu2:
    "images/Background/Perdu2.png" 
image Perdu3:
    "images/Background/Perdu3.png"
image Perdu4:
    "images/Background/Perdu4.png"
image LieuDeDepart:
    "Background/LieuDeDepart.jpg"
image ArriveForetFees:
    "images/Background/ArriveForetFees.png"
image Gouffre:
    "images/Background/Gouffre.jpg"
image ArbreABonbons:
    "images/Background/ArbreABonbons.jpg"
image FondDuGouffre:
    "images/Background/FondDuGouffre.jpg"
image Bibliotheque:
    "images/Background/bibliotheque.jpg"
image Labyrinthe:
    "images/Background/Labyrinthe.png"
image ClairiereDOliveau:
    "images/Background/ClairiereDOliveau.png"
image Lac:
    "images/Background/Lac.jpg"
image FondDuLac:
    "images/Background/FondDuLac.png"
image Cuisine:
    "images/Background/Cuisine.png"
image NidDeLOiseau:
    "images/Background/NidDeLOiseau.png"
image PorteDuRoyaumeDesFees:
    "images/Background/PorteDuRoyaumeDesFees.png"
image LieuDuVol:
    "images/Background/LieuDuVol.png"
image Cuisine:
    "images/Background/PseudoLabyrinthe.png"
image Falaise:
    "images/Background/Falaise.png"
image FalaiseLierre:
    "images/Background/FalaiseLierre.png"
image DessusDeLaFalaise:
    "images/Background/DessusDeLaFalaise.jpg"
image PlanDeTravail:
    "images/Background/PlanDeTravail.png"
image CulDeSac:
    "Background/CulDeSac.png"
image CabaneDuVoleur:
    "Background/CabaneDuVoleur.png"


######Links

###Links Perdu
screen Perdu1ToPerdu2:
    imagebutton:
        idle "LinkIdleN.png"
        hover "LinkHoverN.png"
        at sizeButton
        xalign 0.45
        yalign 0.44
        action [Hide ("Perdu1ToPerdu2"), Jump ("Perdu2")]
screen Perdu2ToPerdu3:
    imagebutton:
        idle "LinkIdleNE.png"
        hover "LinkHoverNE.png"
        at sizeButton
        xalign 0.87
        yalign 0.14
        action [Hide ("Perdu2ToPerdu3"), Jump ("Perdu3")]
screen Perdu3ToPerdu4:
    imagebutton:
        idle "LinkIdleNO.png"
        hover "LinkHoverNO.png"
        at sizeButton
        xalign 0.38
        yalign 0.29
        action [Hide ("Perdu3ToPerdu4"), Jump ("Perdu4")]
screen Perdu4ToArriveForetFees:
    imagebutton:
        idle "LinkIdleNE.png"
        hover "LinkHoverNE.png"
        at sizeButton
        xalign 0.62
        yalign 0.39
        action [Hide ("Perdu4ToArriveForetFees"), Jump ("ArriveForetFees")]

###Links ArriveForetFees
screen ArriveForetFeesLink:
    imagebutton:
        idle "LinkIdleO.png"
        hover "LinkHoverO.png"
        at sizeButton
        xalign 0.04
        yalign 0.45
        action [Hide("ArriveForetFeesLink"), Jump ("Gouffre")]
    imagebutton:
        idle "LinkIdleN.png"
        hover "LinkHoverN.png"
        at sizeButton
        xalign 0.5
        yalign 0.3
        action [Hide ("ArriveForetFeesLink"), Jump ("ClairiereDOliveau")]
    if achMagie>=1:
        imagebutton:
            idle "iconeMagie.png"
            at sizeButton
            xalign 0.01
            yalign 0.01
        for i in magie:
            if i.name=="KAME":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.08
                    yalign 0.01
                    action [If ((PossibiliteKAME==0), true[Show("KAMEPasPossible")]),
                    If ((PossibiliteKAME==2), true[SetVariable("PossibiliteKAME",1), Jump("ArbreABonbons")]),
                    If ((PossibiliteKAME==1), true=[SetVariable("PossibiliteKAME",1),Jump("DansLesAirs")])]
            elif i.name=="DOY":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.16
                    yalign 0.01
                    action If ((PossibiliteDOY==1), true=[SetVariable("PossibiliteDOY",0),SetVariable("falaiseLierre",1),Jump("Falaise")], false=[Show("DOYPasPossible")])
            elif i.name=="PIF":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.24
                    yalign 0.01
                    action If ((PossibilitePIF==1), true=[SetVariable("PossibilitePIF",0),SetVariable("porteGouffre",1),Jump("FondDuGouffre")], false=[Show("PIFPasPossible")])
            elif i.name=="JUNQ":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.32
                    yalign 0.01
                    action If ((PossibiliteJUNQ==1), true=[SetVariable("PossibiliteJUNQ",0),Jump("FondDuLac")], false=[Show("JUNQPasPossible")])
            elif i.name=="GREX":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.40
                    yalign 0.01
                    action If ((PossibiliteGREX==1), true=[SetVariable("PossibiliteGREX",0),Jump("Labyrinthe")], false=[Show("GREXPasPossible")])
        
    

###Links Gouffre
screen GouffreLink:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.96
        yalign 0.6
        action [Hide ("GouffreLink"), Jump ("ArriveForetFees")]
    imagebutton:
        idle "LinkIdleS.png"
        hover "LinkHoverS.png"
        at sizeButton
        xalign 0.46
        yalign 0.4
        action [Hide ("GouffreLink"), Jump ("FondDuGouffre")]
    if achMagie>=1:
        imagebutton:
            idle "iconeMagie.png"
            at sizeButton
            xalign 0.01
            yalign 0.01
        for i in magie:
            if i.name=="KAME":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.08
                    yalign 0.01
                    action [If ((PossibiliteKAME==0), true[Show("KAMEPasPossible")]),
                    If ((PossibiliteKAME==2), true[SetVariable("PossibiliteKAME",1), Jump("ArbreABonbons")]),
                    If ((PossibiliteKAME==1), true=[SetVariable("PossibiliteKAME",1),Jump("DansLesAirs")])]
            elif i.name=="DOY":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.16
                    yalign 0.01
                    action If ((PossibiliteDOY==1), true=[SetVariable("PossibiliteDOY",0),SetVariable("falaiseLierre",1),Jump("Falaise")], false=[Show("DOYPasPossible")])
            elif i.name=="PIF":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.24
                    yalign 0.01
                    action If ((PossibilitePIF==1), true=[SetVariable("PossibilitePIF",0),SetVariable("porteGouffre",1),Jump("FondDuGouffre")], false=[Show("PIFPasPossible")])
            elif i.name=="JUNQ":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.32
                    yalign 0.01
                    action If ((PossibiliteJUNQ==1), true=[SetVariable("PossibiliteJUNQ",0),Jump("FondDuLac")], false=[Show("JUNQPasPossible")])
            elif i.name=="GREX":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.40
                    yalign 0.01
                    action If ((PossibiliteGREX==1), true=[SetVariable("PossibiliteGREX",0),Jump("Labyrinthe")], false=[Show("GREXPasPossible")])

###Links ArbreABonbons
screen ArbreABonbonsLink:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.8
        yalign 0.8
        action [Hide ("ArbreABonbonsLink"), Jump ("Gouffre")]
    if achMagie>=1:
        imagebutton:
            idle "iconeMagie.png"
            at sizeButton
            xalign 0.01
            yalign 0.01
        for i in magie:
            if i.name=="KAME":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.08
                    yalign 0.01
                    action [If ((PossibiliteKAME==0), true[Show("KAMEPasPossible")]),
                    If ((PossibiliteKAME==2), true[SetVariable("PossibiliteKAME",1), Jump("ArbreABonbons")]),
                    If ((PossibiliteKAME==1), true=[SetVariable("PossibiliteKAME",1),Jump("DansLesAirs")])]
            elif i.name=="DOY":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.16
                    yalign 0.01
                    action If ((PossibiliteDOY==1), true=[SetVariable("PossibiliteDOY",0),SetVariable("falaiseLierre",1),Jump("Falaise")], false=[Show("DOYPasPossible")])
            elif i.name=="PIF":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.24
                    yalign 0.01
                    action If ((PossibilitePIF==1), true=[SetVariable("PossibilitePIF",0),SetVariable("porteGouffre",1),Jump("FondDuGouffre")], false=[Show("PIFPasPossible")])
            elif i.name=="JUNQ":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.32
                    yalign 0.01
                    action If ((PossibiliteJUNQ==1), true=[SetVariable("PossibiliteJUNQ",0),Jump("FondDuLac")], false=[Show("JUNQPasPossible")])
            elif i.name=="GREX":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.40
                    yalign 0.01
                    action If ((PossibiliteGREX==1), true=[SetVariable("PossibiliteGREX",0),Jump("Labyrinthe")], false=[Show("GREXPasPossible")])

    imagebutton:
        idle "enfant.png"
        xalign 0.5
        yalign 0.2
        action [Hide (ArbreABonbonsLink), Jump(enfant)]


###Links FondDuGouffre
screen FondDuGouffreLink:
    imagebutton:
        idle "LinkIdleN.png"
        hover "LinkHoverN.png"
        at sizeButton
        xalign 0.57
        yalign 0.55
        action [SetVariable("PossibiliteGREX",0),Hide ("FondDuGouffreLink"), Jump ("Gouffre")]
    if porteGouffre==1: 
        imagebutton:
            idle "Porte_bibliotheque.png"
            at sizePorte
            xalign 0.2
            yalign 0.6
            action [SetVariable("PossibiliteGREX",0),Hide ("FondDuGouffreLink"), Jump ("Bibliotheque")]
    if achMagie>=1:
        imagebutton:
            idle "iconeMagie.png"
            at sizeButton
            xalign 0.01
            yalign 0.01
        for i in magie:
            if i.name=="KAME":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.08
                    yalign 0.01
                    action [If ((PossibiliteKAME==0), true[Show("KAMEPasPossible")]),
                    If ((PossibiliteKAME==2), true[SetVariable("PossibiliteKAME",1), Jump("ArbreABonbons")]),
                    If ((PossibiliteKAME==1), true=[SetVariable("PossibiliteKAME",1),Jump("DansLesAirs")])]
            elif i.name=="DOY":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.16
                    yalign 0.01
                    action If ((PossibiliteDOY==1), true=[SetVariable("PossibiliteDOY",0),SetVariable("falaiseLierre",1),Jump("Falaise")], false=[Show("DOYPasPossible")])
            elif i.name=="PIF":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.24
                    yalign 0.01
                    action If ((PossibilitePIF==1), true=[SetVariable("PossibilitePIF",0),SetVariable("porteGouffre",1),Jump("FondDuGouffre")], false=[Show("PIFPasPossible")])
            elif i.name=="JUNQ":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.32
                    yalign 0.01
                    action If ((PossibiliteJUNQ==1), true=[SetVariable("PossibiliteJUNQ",0),Jump("FondDuLac")], false=[Show("JUNQPasPossible")])
            elif i.name=="GREX":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.40
                    yalign 0.01
                    action If ((PossibiliteGREX==1), true=[SetVariable("PossibiliteGREX",0),Jump("Labyrinthe")], false=[Show("GREXPasPossible")])
###Link Bibliotheque
screen BibliothequeLink:
    imagebutton:
        idle "LinkIdleS.png"
        hover "LinkHoverS.png"
        at sizeButton
        xalign 0.7
        yalign 0.97
        action [Hide ("BibliothequeLink"),(SetVariable("PossibiliteKAME",1)),Jump("FondDuGouffre")]
    if achMagie>=1:
        imagebutton:
            idle "iconeMagie.png"
            at sizeButton
            xalign 0.01
            yalign 0.01
        for i in magie:
            if i.name=="KAME":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.08
                    yalign 0.01
                    action [If ((PossibiliteKAME==0), true[Show("KAMEPasPossible")]),
                    If ((PossibiliteKAME==2), true[SetVariable("PossibiliteKAME",1), Jump("ArbreABonbons")]),
                    If ((PossibiliteKAME==1), true=[SetVariable("PossibiliteKAME",1),Jump("DansLesAirs")])]
            elif i.name=="DOY":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.16
                    yalign 0.01
                    action If ((PossibiliteDOY==1), true=[SetVariable("PossibiliteDOY",0),SetVariable("falaiseLierre",1),Jump("Falaise")], false=[Show("DOYPasPossible")])
            elif i.name=="PIF":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.24
                    yalign 0.01
                    action If ((PossibilitePIF==1), true=[SetVariable("PossibilitePIF",0),SetVariable("porteGouffre",1),Jump("FondDuGouffre")], false=[Show("PIFPasPossible")])
            elif i.name=="JUNQ":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.32
                    yalign 0.01
                    action If ((PossibiliteJUNQ==1), true=[SetVariable("PossibiliteJUNQ",0),Jump("FondDuLac")], false=[Show("JUNQPasPossible")])
            elif i.name=="GREX":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.40
                    yalign 0.01
                    action If ((PossibiliteGREX==1), true=[SetVariable("PossibiliteGREX",0),Jump("Labyrinthe")], false=[Show("GREXPasPossible")])

###Link Labyrinthe
screen LabyrintheLink:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [SetVariable("PossibiliteKAME",1),Hide ("LabyrintheLink"), Jump ("FondDuGouffre")]
    if achMagie>=1:
        imagebutton:
            idle "iconeMagie.png"
            at sizeButton
            xalign 0.01
            yalign 0.01
        for i in magie:
            if i.name=="KAME":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.08
                    yalign 0.01
                    action [If ((PossibiliteKAME==0), true[Show("KAMEPasPossible")]),
                    If ((PossibiliteKAME==2), true[SetVariable("PossibiliteKAME",1), Jump("ArbreABonbons")]),
                    If ((PossibiliteKAME==1), true=[SetVariable("PossibiliteKAME",1),Jump("DansLesAirs")])]
            elif i.name=="DOY":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.16
                    yalign 0.01
                    action If ((PossibiliteDOY==1), true=[SetVariable("PossibiliteDOY",0),SetVariable("falaiseLierre",1),Jump("Falaise")], false=[Show("DOYPasPossible")])
            elif i.name=="PIF":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.24
                    yalign 0.01
                    action If ((PossibilitePIF==1), true=[SetVariable("PossibilitePIF",0),SetVariable("porteGouffre",1),Jump("FondDuGouffre")], false=[Show("PIFPasPossible")])
            elif i.name=="JUNQ":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.32
                    yalign 0.01
                    action If ((PossibiliteJUNQ==1), true=[SetVariable("PossibiliteJUNQ",0),Jump("FondDuLac")], false=[Show("JUNQPasPossible")])
            elif i.name=="GREX":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.40
                    yalign 0.01
                    action If ((PossibiliteGREX==1), true=[SetVariable("PossibiliteGREX",0),Jump("Labyrinthe")], false=[Show("GREXPasPossible")])

###Link Lac
screen LacLink:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.1
        yalign 0.5
        action [SetVariable("PossibiliteJUNQ",0),Hide ("LacLink"), Jump ("ClairiereDOliveau")]
    if IleAcces==1:
        imagebutton:
            idle "LinkIdleNE.png"
            hover "LinkHoverNE.png"
            at sizeButton
            xalign 0.1
            yalign 0.9
            action [SetVariable("PossibiliteJUNQ",0),Hide ("LacLink"), Jump ("NidDeLOiseau")]
    if achMagie>=1:
        imagebutton:
            idle "iconeMagie.png"
            at sizeButton
            xalign 0.01
            yalign 0.01
        for i in magie:
            if i.name=="KAME":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.08
                    yalign 0.01
                    action [If ((PossibiliteKAME==0), true[Show("KAMEPasPossible")]),
                    If ((PossibiliteKAME==2), true[SetVariable("PossibiliteKAME",1), Jump("ArbreABonbons")]),
                    If ((PossibiliteKAME==1), true=[SetVariable("PossibiliteKAME",1),Jump("DansLesAirs")])]
            elif i.name=="DOY":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.16
                    yalign 0.01
                    action If ((PossibiliteDOY==1), true=[SetVariable("PossibiliteDOY",0),SetVariable("falaiseLierre",1),Jump("Falaise")], false=[Show("DOYPasPossible")])
            elif i.name=="PIF":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.24
                    yalign 0.01
                    action If ((PossibilitePIF==1), true=[SetVariable("PossibilitePIF",0),SetVariable("porteGouffre",1),Jump("FondDuGouffre")], false=[Show("PIFPasPossible")])
            elif i.name=="JUNQ":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.32
                    yalign 0.01
                    action If ((PossibiliteJUNQ==1), true=[SetVariable("PossibiliteJUNQ",0),Jump("FondDuLac")], false=[Show("JUNQPasPossible")])
            elif i.name=="GREX":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.40
                    yalign 0.01
                    action If ((PossibiliteGREX==1), true=[SetVariable("PossibiliteGREX",0),Jump("Labyrinthe")], false=[Show("GREXPasPossible")])

#Oliveau Intro
screen OliveauIntroLink:
    imagebutton:
        idle "Oliveau.png"
        xalign 0.5
        yalign 0.2
        action [Hide("OliveauIntroLink"), Show("oliveauStatic"), Jump("OliveauIntro")]

###Link Clairiere d'Oliveau
screen ClairiereDOliveauLink:
    imagebutton:
        idle "Oliveau.png"
        xalign 0.5
        yalign 0.2
        action [Hide ("ClairiereDOliveauLink"), Show("oliveauStatic"), Jump("Oliveau")]
    imagebutton:
        idle "LinkIdleSO.png"
        hover "LinkHoverSO.png"
        at sizeButton
        xalign 0.2
        yalign 0.95
        action [Hide ("ClairiereDOliveauLink"), Hide("oliveauStatic"), Jump ("ArriveForetFees")]
    if VoleurAcces==1:
        imagebutton:
            idle "LinkIdleNO.png"
            hover "LinkHoverNO.png"
            at sizeButton
            xalign 0.25
            yalign 0.48
            action [Hide ("ClairiereDOliveauLink"),Hide("oliveauStatic"), Jump ("LieuDuVol")]
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.97
        yalign 0.8
        action [Hide ("ClairiereDOliveauLink"),Hide("oliveauStatic"), Jump ("Lac")]
    if PorteRoyaumeAcces==1:
        imagebutton:
            idle "LinkIdleNE.png"
            hover "LinkHoverNE.png"
            at sizeButton
            xalign 0.95
            yalign 0.5
            action [Hide ("ClairiereDOliveauLink"),Hide("oliveauStatic"), Jump ("PorteDuRoyaumeDesFees")]
    if achMagie>=1:
        imagebutton:
            idle "iconeMagie.png"
            at sizeButton
            xalign 0.01
            yalign 0.01
        for i in magie:
            if i.name=="KAME":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.08
                    yalign 0.01
                    action [If ((PossibiliteKAME==0), true[Show("KAMEPasPossible")]),
                    If ((PossibiliteKAME==2), true[SetVariable("PossibiliteKAME",1), Jump("ArbreABonbons")]),
                    If ((PossibiliteKAME==1), true=[SetVariable("PossibiliteKAME",1),Jump("DansLesAirs")])]
            elif i.name=="DOY":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.16
                    yalign 0.01
                    action If ((PossibiliteDOY==1), true=[SetVariable("PossibiliteDOY",0),SetVariable("falaiseLierre",1),Jump("Falaise")], false=[Show("DOYPasPossible")])
            elif i.name=="PIF":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.24
                    yalign 0.01
                    action If ((PossibilitePIF==1), true=[SetVariable("PossibilitePIF",0),SetVariable("porteGouffre",1),Jump("FondDuGouffre")], false=[Show("PIFPasPossible")])
            elif i.name=="JUNQ":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.32
                    yalign 0.01
                    action If ((PossibiliteJUNQ==1), true=[SetVariable("PossibiliteJUNQ",0),Jump("FondDuLac")], false=[Show("JUNQPasPossible")])
            elif i.name=="GREX":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.40
                    yalign 0.01
                    action If ((PossibiliteGREX==1), true=[SetVariable("PossibiliteGREX",0),Jump("Labyrinthe")], false=[Show("GREXPasPossible")])

screen oliveauStatic:
    imagebutton:
        idle "Oliveau.png"
        xalign 0.5
        yalign 0.2

###Link Nid De L'Oiseau
screen NidDeLOiseauLink:
    imagebutton:
        idle "oiseau.png"
        xalign 0.5
        yalign 0.2
        action[Hide("NidDeLOiseauLink"), Show("birdStatic"), Jump("Bird")]
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.9
        yalign 0.1
        action [Hide ("NidDeLOiseauLink"),Hide("birdStatic"), Jump ("Lac")]
    if achMagie>=1:
        imagebutton:
            idle "iconeMagie.png"
            at sizeButton
            xalign 0.01
            yalign 0.01
        for i in magie:
            if i.name=="KAME":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.08
                    yalign 0.01
                    action [If ((PossibiliteKAME==0), true[Show("KAMEPasPossible")]),
                    If ((PossibiliteKAME==2), true[SetVariable("PossibiliteKAME",1), Jump("ArbreABonbons")]),
                    If ((PossibiliteKAME==1), true=[SetVariable("PossibiliteKAME",1),Jump("DansLesAirs")])]
            elif i.name=="DOY":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.16
                    yalign 0.01
                    action If ((PossibiliteDOY==1), true=[SetVariable("PossibiliteDOY",0),SetVariable("falaiseLierre",1),Jump("Falaise")], false=[Show("DOYPasPossible")])
            elif i.name=="PIF":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.24
                    yalign 0.01
                    action If ((PossibilitePIF==1), true=[SetVariable("PossibilitePIF",0),SetVariable("porteGouffre",1),Jump("FondDuGouffre")], false=[Show("PIFPasPossible")])
            elif i.name=="JUNQ":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.32
                    yalign 0.01
                    action If ((PossibiliteJUNQ==1), true=[SetVariable("PossibiliteJUNQ",0),Jump("FondDuLac")], false=[Show("JUNQPasPossible")])
            elif i.name=="GREX":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.40
                    yalign 0.01
                    action If ((PossibiliteGREX==1), true=[SetVariable("PossibiliteGREX",0),Jump("Labyrinthe")], false=[Show("GREXPasPossible")])

screen birdStatic:
    imagebutton:
        idle "oiseau.png"
        xalign 0.5
        yalign 0.2

###Link Porte du royaume des fées
screen LinkPorteDuRoyaumeDesFees:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("LinkPorteDuRoyaumeDesFees"), Jump ("PorteDuRoyaumeDesFees")]
    if achMagie>=1:
        imagebutton:
            idle "iconeMagie.png"
            at sizeButton
            xalign 0.01
            yalign 0.01
        for i in magie:
            if i.name=="KAME":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.08
                    yalign 0.01
                    action [If ((PossibiliteKAME==0), true[Show("KAMEPasPossible")]),
                    If ((PossibiliteKAME==2), true[SetVariable("PossibiliteKAME",1), Jump("ArbreABonbons")]),
                    If ((PossibiliteKAME==1), true=[SetVariable("PossibiliteKAME",1),Jump("DansLesAirs")])]
            elif i.name=="DOY":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.16
                    yalign 0.01
                    action If ((PossibiliteDOY==1), true=[SetVariable("PossibiliteDOY",0),SetVariable("falaiseLierre",1),Jump("Falaise")], false=[Show("DOYPasPossible")])
            elif i.name=="PIF":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.24
                    yalign 0.01
                    action If ((PossibilitePIF==1), true=[SetVariable("PossibilitePIF",0),SetVariable("porteGouffre",1),Jump("FondDuGouffre")], false=[Show("PIFPasPossible")])
            elif i.name=="JUNQ":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.32
                    yalign 0.01
                    action If ((PossibiliteJUNQ==1), true=[SetVariable("PossibiliteJUNQ",0),Jump("FondDuLac")], false=[Show("JUNQPasPossible")])
            elif i.name=="GREX":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.40
                    yalign 0.01
                    action If ((PossibiliteGREX==1), true=[SetVariable("PossibiliteGREX",0),Jump("Labyrinthe")], false=[Show("GREXPasPossible")])

###Link Lieu du vol
screen LieuDuVolLink:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.3
        yalign 0.8
        action [Hide ("LieuDuVolLink"), Jump ("ClairiereDOliveau")]
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.7
        yalign 0.1
        action [Hide ("LieuDuVolLink"), Jump ("PseudoLabyrinthe")]
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.2
        yalign 0.5
        action [Hide ("LieuDuVolLink"), Jump ("Falaise")]
    if achMagie>=1:
        imagebutton:
            idle "iconeMagie.png"
            at sizeButton
            xalign 0.01
            yalign 0.01
        for i in magie:
            if i.name=="KAME":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.08
                    yalign 0.01
                    action [If ((PossibiliteKAME==0), true[Show("KAMEPasPossible")]),
                    If ((PossibiliteKAME==2), true[SetVariable("PossibiliteKAME",1), Jump("ArbreABonbons")]),
                    If ((PossibiliteKAME==1), true=[SetVariable("PossibiliteKAME",1),Jump("DansLesAirs")])]
            elif i.name=="DOY":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.16
                    yalign 0.01
                    action If ((PossibiliteDOY==1), true=[SetVariable("PossibiliteDOY",0),SetVariable("falaiseLierre",1),Jump("Falaise")], false=[Show("DOYPasPossible")])
            elif i.name=="PIF":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.24
                    yalign 0.01
                    action If ((PossibilitePIF==1), true=[SetVariable("PossibilitePIF",0),SetVariable("porteGouffre",1),Jump("FondDuGouffre")], false=[Show("PIFPasPossible")])
            elif i.name=="JUNQ":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.32
                    yalign 0.01
                    action If ((PossibiliteJUNQ==1), true=[SetVariable("PossibiliteJUNQ",0),Jump("FondDuLac")], false=[Show("JUNQPasPossible")])
            elif i.name=="GREX":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.40
                    yalign 0.01
                    action If ((PossibiliteGREX==1), true=[SetVariable("PossibiliteGREX",0),Jump("Labyrinthe")], false=[Show("GREXPasPossible")])
     
###Link PseudoLabyrinthe
screen PseudoLabyrintheLink:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.3
        yalign 0.8
        action [Hide ("PseudoLabyrintheLink"), Jump ("LieuDuVol")]
    if achMagie>=1:
        imagebutton:
            idle "iconeMagie.png"
            at sizeButton
            xalign 0.01
            yalign 0.01
        for i in magie:
            if i.name=="KAME":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.08
                    yalign 0.01
                    action [If ((PossibiliteKAME==0), true[Show("KAMEPasPossible")]),
                    If ((PossibiliteKAME==2), true[SetVariable("PossibiliteKAME",1), Jump("ArbreABonbons")]),
                    If ((PossibiliteKAME==1), true=[SetVariable("PossibiliteKAME",1),Jump("DansLesAirs")])]
            elif i.name=="DOY":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.16
                    yalign 0.01
                    action If ((PossibiliteDOY==1), true=[SetVariable("PossibiliteDOY",0),SetVariable("falaiseLierre",1),Jump("Falaise")], false=[Show("DOYPasPossible")])
            elif i.name=="PIF":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.24
                    yalign 0.01
                    action If ((PossibilitePIF==1), true=[SetVariable("PossibilitePIF",0),SetVariable("porteGouffre",1),Jump("FondDuGouffre")], false=[Show("PIFPasPossible")])
            elif i.name=="JUNQ":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.32
                    yalign 0.01
                    action If ((PossibiliteJUNQ==1), true=[SetVariable("PossibiliteJUNQ",0),Jump("FondDuLac")], false=[Show("JUNQPasPossible")])
            elif i.name=="GREX":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.40
                    yalign 0.01
                    action If ((PossibiliteGREX==1), true=[SetVariable("PossibiliteGREX",0),Jump("Labyrinthe")], false=[Show("GREXPasPossible")])
###Link Cuisine
screen CuisineLink:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.1
        yalign 0.1
        action [Hide ("CuisineLink"), Jump ("FondDuLac")]
    if achMagie>=1:
        imagebutton:
            idle "iconeMagie.png"
            at sizeButton
            xalign 0.01
            yalign 0.01
        for i in magie:
            if i.name=="KAME":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.08
                    yalign 0.01
                    action [If ((PossibiliteKAME==0), true[Show("KAMEPasPossible")]),
                    If ((PossibiliteKAME==2), true[SetVariable("PossibiliteKAME",1), Jump("ArbreABonbons")]),
                    If ((PossibiliteKAME==1), true=[SetVariable("PossibiliteKAME",1),Jump("DansLesAirs")])]
            elif i.name=="DOY":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.16
                    yalign 0.01
                    action If ((PossibiliteDOY==1), true=[SetVariable("PossibiliteDOY",0),SetVariable("falaiseLierre",1),Jump("Falaise")], false=[Show("DOYPasPossible")])
            elif i.name=="PIF":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.24
                    yalign 0.01
                    action If ((PossibilitePIF==1), true=[SetVariable("PossibilitePIF",0),SetVariable("porteGouffre",1),Jump("FondDuGouffre")], false=[Show("PIFPasPossible")])
            elif i.name=="JUNQ":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.32
                    yalign 0.01
                    action If ((PossibiliteJUNQ==1), true=[SetVariable("PossibiliteJUNQ",0),Jump("FondDuLac")], false=[Show("JUNQPasPossible")])
            elif i.name=="GREX":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.40
                    yalign 0.01
                    action If ((PossibiliteGREX==1), true=[SetVariable("PossibiliteGREX",0),Jump("Labyrinthe")], false=[Show("GREXPasPossible")])

###Link FondDuLac
screen FondDuLacLink:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.1
        yalign 0.1
        action [SetVariable("PossibiliteKAME",1),Hide ("FondDuLacLink"), Jump ("Lac")]
    imagebutton:
        idle "porte_cuisine.png"
        at sizeButton
        xalign 0.1
        yalign 0.1
        action [Hide ("FondDuLacLink"), Jump ("Cuisine")]
    if achMagie>=1:
        imagebutton:
            idle "iconeMagie.png"
            at sizeButton
            xalign 0.01
            yalign 0.01
        for i in magie:
            if i.name=="KAME":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.08
                    yalign 0.01
                    action [If ((PossibiliteKAME==0), true[Show("KAMEPasPossible")]),
                    If ((PossibiliteKAME==2), true[SetVariable("PossibiliteKAME",1), Jump("ArbreABonbons")]),
                    If ((PossibiliteKAME==1), true=[SetVariable("PossibiliteKAME",1),Jump("DansLesAirs")])]
            elif i.name=="DOY":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.16
                    yalign 0.01
                    action If ((PossibiliteDOY==1), true=[SetVariable("PossibiliteDOY",0),SetVariable("falaiseLierre",1),Jump("Falaise")], false=[Show("DOYPasPossible")])
            elif i.name=="PIF":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.24
                    yalign 0.01
                    action If ((PossibilitePIF==1), true=[SetVariable("PossibilitePIF",0),SetVariable("porteGouffre",1),Jump("FondDuGouffre")], false=[Show("PIFPasPossible")])
            elif i.name=="JUNQ":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.32
                    yalign 0.01
                    action If ((PossibiliteJUNQ==1), true=[SetVariable("PossibiliteJUNQ",0),Jump("FondDuLac")], false=[Show("JUNQPasPossible")])
            elif i.name=="GREX":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.40
                    yalign 0.01
                    action If ((PossibiliteGREX==1), true=[SetVariable("PossibiliteGREX",0),Jump("Labyrinthe")], false=[Show("GREXPasPossible")])

###Link Falaise
screen FalaiseLink:
    if falaiseLierre==1:
        imagebutton:
            idle "LinkIdleE.png"
            hover "LinkHoverE.png"
            at sizeButton
            xalign 0.1
            yalign 0.1
            action [Hide ("FalaiseLink"), Jump ("DessusDeLaFalaise")]
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.3
        yalign 0.4
        action [Hide ("FalaiseLink"), Jump ("LieuDeVol")]
    if achMagie>=1:
        imagebutton:
            idle "iconeMagie.png"
            at sizeButton
            xalign 0.01
            yalign 0.01
        for i in magie:
            if i.name=="KAME":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.08
                    yalign 0.01
                    action [If ((PossibiliteKAME==0), true[Show("KAMEPasPossible")]),
                    If ((PossibiliteKAME==2), true[SetVariable("PossibiliteKAME",1), Jump("ArbreABonbons")]),
                    If ((PossibiliteKAME==1), true=[SetVariable("PossibiliteKAME",1),Jump("DansLesAirs")])]
            elif i.name=="DOY":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.16
                    yalign 0.01
                    action If ((PossibiliteDOY==1), true=[SetVariable("PossibiliteDOY",0),SetVariable("falaiseLierre",1),Jump("Falaise")], false=[Show("DOYPasPossible")])
            elif i.name=="PIF":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.24
                    yalign 0.01
                    action If ((PossibilitePIF==1), true=[SetVariable("PossibilitePIF",0),SetVariable("porteGouffre",1),Jump("FondDuGouffre")], false=[Show("PIFPasPossible")])
            elif i.name=="JUNQ":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.32
                    yalign 0.01
                    action If ((PossibiliteJUNQ==1), true=[SetVariable("PossibiliteJUNQ",0),Jump("FondDuLac")], false=[Show("JUNQPasPossible")])
            elif i.name=="GREX":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.40
                    yalign 0.01
                    action If ((PossibiliteGREX==1), true=[SetVariable("PossibiliteGREX",0),Jump("Labyrinthe")], false=[Show("GREXPasPossible")])

###DessusDeLaFalaiseLink
screen DessusDeLaFalaiseLink:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.1
        yalign 0.1
        action [Hide ("DessusDeLaFalaiseLink"), Jump ("Falaise")]
    if achMagie>=1:
        imagebutton:
            idle "iconeMagie.png"
            at sizeButton
            xalign 0.01
            yalign 0.01
        for i in magie:
            if i.name=="KAME":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.08
                    yalign 0.01
                    action [If ((PossibiliteKAME==0), true[Show("KAMEPasPossible")]),
                    If ((PossibiliteKAME==2), true[SetVariable("PossibiliteKAME",1), Jump("ArbreABonbons")]),
                    If ((PossibiliteKAME==1), true=[SetVariable("PossibiliteKAME",1),Jump("DansLesAirs")])]
            elif i.name=="DOY":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.16
                    yalign 0.01
                    action If ((PossibiliteDOY==1), true=[SetVariable("PossibiliteDOY",0),SetVariable("falaiseLierre",1),Jump("Falaise")], false=[Show("DOYPasPossible")])
            elif i.name=="PIF":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.24
                    yalign 0.01
                    action If ((PossibilitePIF==1), true=[SetVariable("PossibilitePIF",0),SetVariable("porteGouffre",1),Jump("FondDuGouffre")], false=[Show("PIFPasPossible")])
            elif i.name=="JUNQ":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.32
                    yalign 0.01
                    action If ((PossibiliteJUNQ==1), true=[SetVariable("PossibiliteJUNQ",0),Jump("FondDuLac")], false=[Show("JUNQPasPossible")])
            elif i.name=="GREX":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.40
                    yalign 0.01
                    action If ((PossibiliteGREX==1), true=[SetVariable("PossibiliteGREX",0),Jump("Labyrinthe")], false=[Show("GREXPasPossible")])
    imagebutton:
        idle "alchimiste.png"
        xalign 0.5
        yalign 0.2
        action[Hide(DessusDeLaFalaiseLink), Jump(alchimiste)]


###Link Piege de l'alchimiste
screen PiegeDeLAlchimisteLink:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.9
        yalign 0.8
        action [Hide ("PiegeDeLAlchimisteLink"), Jump ("FalaiseAvecLierre")]
    if achMagie>=1:
        imagebutton:
            idle "iconeMagie.png"
            at sizeButton
            xalign 0.01
            yalign 0.01
        for i in magie:
            if i.name=="KAME":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.08
                    yalign 0.01
                    action [If ((PossibiliteKAME==0), true[Show("KAMEPasPossible")]),
                    If ((PossibiliteKAME==2), true[SetVariable("PossibiliteKAME",1), Jump("ArbreABonbons")]),
                    If ((PossibiliteKAME==1), true=[SetVariable("PossibiliteKAME",1),Jump("DansLesAirs")])]
            elif i.name=="DOY":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.16
                    yalign 0.01
                    action If ((PossibiliteDOY==1), true=[SetVariable("PossibiliteDOY",0),SetVariable("falaiseLierre",1),Jump("Falaise")], false=[Show("DOYPasPossible")])
            elif i.name=="PIF":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.24
                    yalign 0.01
                    action If ((PossibilitePIF==1), true=[SetVariable("PossibilitePIF",0),SetVariable("porteGouffre",1),Jump("FondDuGouffre")], false=[Show("PIFPasPossible")])
            elif i.name=="JUNQ":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.32
                    yalign 0.01
                    action If ((PossibiliteJUNQ==1), true=[SetVariable("PossibiliteJUNQ",0),Jump("FondDuLac")], false=[Show("JUNQPasPossible")])
            elif i.name=="GREX":
                imagebutton:
                    idle i.image
                    at sizeButton
                    xalign 0.40
                    yalign 0.01
                    action If ((PossibiliteGREX==1), true=[SetVariable("PossibiliteGREX",0),Jump("Labyrinthe")], false=[Show("GREXPasPossible")])

# ----- DEBUT SCREEN JEU BIBLIOTHEQUE -----

screen jeubiblio:
    frame:
        add "Jeu_bgblanc.png" size (3000,3000) at jeuBiblio_custom_zoom
        add "JeuBiblio_bg.png" size (1920,1160) at jeuBiblio_custom_zoom
        for a in range (21):
            $i = a%7
            $j = a//7
            if tab[a][2]!=rep[0][2] or tab[a][2]!=rep[1][2] or tab[a][2]!=rep[2][2] or tab[a][2]==rep[0][2] and repV[0]==0 or tab[a][2]==rep[1][2] and repV[1]==0 or  tab[a][2]==rep[2][2] and repV[2]==0:
                $b="jeuBiblio_video"+str(a)
                imagebutton:
                    idle tab[a][0]  at jeuBiblio_custom_zoom
                    xpos 20 + 120*i
                    ypos 30 + 165*j
                    action [Jump (b)]
            imagebutton:
                if tab[a][2]==rep[0][2] and repV[0]==1 or  tab[a][2]==rep[1][2] and repV[1]==1 or  tab[a][2]==rep[2][2] and repV[2]==1:
                    idle "jeuBiblio_Validation2.png"  at jeuBiblio_custom_zoom2
                else:
                    idle "jeuBiblio_Validation.png" at jeuBiblio_custom_zoom2

                xpos 52 + 120*i
                ypos 145 + 165*j
                if tab[a][2]==rep[0][2]:
                    action [Jump ("jeuBiblio_valider1")]
                elif tab[a][2]==rep[1][2] :
                    action [Jump ("jeuBiblio_valider2")]
                elif tab[a][2]==rep[2][2]:
                    action [Jump ("jeuBiblio_valider3")]
                else :
                    action [Jump ("jeuBiblio_echec")]



            add (rep[0][1])  xpos 930 ypos 130
            add (rep[1][1])  xpos 930 ypos 250
            add (rep[2][1])  xpos 930 ypos 370

            for i in range (3):
                add "Jeu_CoeurVide.png" xpos 1120-100*i ypos 20

            for i in range (coeur):
                add "Jeu_CoeurPlein.png" xpos 1120-100*i ypos 20

# ----- FIN SCREEN JEU BIBLIOTHEQUE -----

# --- DEBUT SCREEN JEU FIOLE ---

screen lancementjeufiole:
    imagebutton:
        xpos 450
        ypos 50
        idle "JeuFiole_Chaudron.png" at jeuFiole_custom_zoom2
        action [Show("jeufiole"),Hide ("lancementjeufiole"),Jump ("jeuFiole_init")]

screen jeufiole:
    frame:
        add "Jeu_bgblanc.png" size (5000,5000)
        add "JeuFiole_Chaudron.png" size(200,200) at top
        for a in range (16):
            $j=a%8
            $i=a//8
            if tab[a][1] != "":
                imagebutton:
                    idle (tab[a][0])  at jeuFiole_custom_zoom
                    xpos 50 + 150*j
                    ypos 220 + 150*i
                    if tab[a][1] == ordre[0]:
                        action [Jump ("jeuFiole_valider")]
                    else:
                        action [Jump ("jeuFiole_echec")]
    for i in range (3):
        add "Jeu_CoeurVide.png" xpos 1150-100*i ypos 50
    for i in range (coeur):
        add "Jeu_CoeurPlein.png" xpos 1150-100*i ypos 50
# --- FIN SCREEN JEU FIOLE ---

#bibliotheque
screen carrefour_deux:
    imagebutton:        #aller a gauche
        idle "fleche_laby_g.png"
        hover "fleche_laby_hover_g.png"
        xalign 0.2 yalign 0.27
        action [Hide("carrefour_deux",transition=dissolve), If((chem_laby.n_laby == 1), true = [Jump("transition_lab")], false = [Jump("echec_lab")])]
    imagebutton:        #aller a droite
        idle "fleche_laby.png"
        hover "fleche_laby_hover.png"
        xalign 0.7 yalign 0.3
        action [Hide("carrefour_deux",transition=dissolve), If((chem_laby.n_laby == 2), true = [Jump("transition_lab")], false = [Jump("echec_lab")])]

    add dico_panneau[Choix_laby[chem_laby.a_laby]] xalign 0.2 yalign 0.8              # Panneau à gauche
    add dico_panneau[Choix_laby[chem_laby.b_laby]] xalign 0.75 yalign 0.8              # Panneau à droite

    imagebutton:                        # Fantome LSF
        idle "Boule_fantome.png"
        hover "Boule_fantome_hover.png"
        xalign 0.9 yalign 0.9
        action [Jump("video_fantome_deux")]

    imagebutton:                        # Taupe
        idle "taupe_01.png"
        hovered [Show("taupe_sort")]
        unhovered [Hide("taupe_sort")]
        xalign 0.5 yalign 1.0
        action [Hide("taupe_sort"),Hide("carrefour_deux",transition=dissolve), Jump("labyrinthe_minijeu")]


screen carrefour_trois:
    imagebutton:        #aller a gauche
        idle "fleche_laby_g.png"
        hover "fleche_laby_hover_g.png"
        xalign 0.2 yalign 0.3
        action [Hide("carrefour_deux",transition=dissolve), If((chem_laby.n_laby == 1), true = [Jump("transition_lab")], false = [Jump("echec_lab")])]
    imagebutton:        #aller au milieu
        idle "fleche_laby_m.png"
        hover "fleche_laby_hover_m.png"
        xalign 0.5 yalign 0.1
        action [Hide("carrefour_deux",transition=dissolve), If((chem_laby.n_laby == 2), true = [Jump("transition_lab")], false = [Jump("echec_lab")])]
    imagebutton:        #aller a droite
        idle "fleche_laby.png"
        hover "fleche_laby_hover.png"
        xalign 0.8 yalign 0.3
        action [Hide("carrefour_deux",transition=dissolve), If((chem_laby.n_laby == 3), true = [Jump("transition_lab")], false = [Jump("echec_lab")])]

    add dico_panneau[Choix_laby[chem_laby.a_laby]] xalign 0.2 yalign 0.8              # Panneau à gauche
    add dico_panneau[Choix_laby[chem_laby.b_laby]] xalign 0.5 yalign 0.7              # Panneau au milieu
    add dico_panneau[Choix_laby[chem_laby.c_laby]] xalign 0.8 yalign 0.8              # Panneau à droite

    imagebutton:                        # Fantome LSF
        idle "Boule_fantome.png"
        hover "Boule_fantome_hover.png"
        xalign 0.9 yalign 0.9
        action [Jump("video_fantome_trois")]

    imagebutton:                        # Taupe
        idle "taupe_01.png"
        hovered [Show("taupe_sort")]
        unhovered [Hide("taupe_sort")]
        xalign 0.5 yalign 1.0
        action [Hide("taupe_sort"),Hide("carrefour_trois",transition=dissolve), Jump("labyrinthe_minijeu")]

screen porte_gallerie:
    imagebutton:                    #passer la porte
        idle "fleche_laby_m.png"
        hover "fleche_laby_hover_m.png"
        xalign 0.4 yalign 0.5
        action [Jump("entrer_code_laby")]

    imagebutton:                        # Fantome LSF
        idle "Boule_fantome.png"
        hover "Boule_fantome_hover.png"
        xalign 0.7 yalign 0.9
        action [Jump("video_fantome_porte")]

    imagebutton:                        # Taupe
        idle "taupe_01.png"
        hovered [Show("taupe_sort")]
        unhovered [Hide("taupe_sort")]
        xalign 0.5 yalign 1.0
        action [Hide("taupe_sort"),Hide("porte_gallerie",transition=dissolve), Jump("labyrinthe_minijeu")]

image taupe_sorti:
    "taupe_01.png"
    xalign 0.5 yalign 1.0
    pause 0.3
    "taupe_02.png"
    xalign 0.5 yalign 1.0
    pause 0.3
    "taupe_03.png"
    xalign 0.5 yalign 1.0
    pause 0.3
    "taupe_04.png"
    xalign 0.5 yalign 1.0
    pause 1.0

screen taupe_sort:

    add "taupe_sorti"
screen taupe_lab:

    imagebutton:                        # Taupe
        idle "taupe_01.png"
        hovered [Show("taupe_sort")]
        unhovered [Hide("taupe_sort")]
        xalign 0.5 yalign 1.0
        action [Hide("taupe_sort"),Hide("taupe_lab",transition=dissolve), Jump("labyrinthe_minijeu")]

#Cuisine
screen ingred:
    text "{size=+10}{b}{color=#ffd700} oeuf : [gat.n_oeufs], farine : [gat.n_farine] , levure : [gat.n_levure], beurre : [gat.n_beurre], lait: [gat.n_lait], sucre : [gat.n_sucre]{/color}{/b}{/size}" xalign 0.1 yalign 0.9
    draggroup:

        # ingrédients.
        drag:
            drag_name "beurre"
            child "Beurre.png"
            droppable False
            dragged ing_dragged
            xpos 100 ypos 100
        drag:
            drag_name "oeufs"
            child "Ingrédients_oeufs.png"
            droppable False
            dragged ing_dragged
            xpos 300 ypos 100
        drag:
            drag_name "lait"
            child "Ingrédients_lait.png"
            droppable False
            dragged ing_dragged
            xpos 500 ypos 100
        drag:
            drag_name "levure"
            child "Ingrédients_levure.png"
            droppable False
            dragged ing_dragged
            xpos 700 ypos 100
        drag:
            drag_name "farine"
            child "Ingrédients_farine.png"
            droppable False
            dragged ing_dragged
            xpos 100 ypos 300
        drag:
            drag_name "sucre"
            child "Ingrédients_sucre.png"
            droppable False
            dragged ing_dragged
            xpos 300 ypos 300
        drag:
            drag_name "sirop_de_rose"
            child "Ingrédients_sirop_rose.png"
            droppable choix_sirop
            dragged ing_dragged
            xpos 500 ypos 300
        drag:
            drag_name "sirop_d'arsenic"
            idle_child "Ingrédients_sirop_rose.png"
            hover_child "Ingrédients_sirop_arsenic.png"
            droppable choix_sirop
            dragged ing_dragged
            xpos 700 ypos 300
        # Le gateau ou on dépose les ingrédients.
        drag:
            drag_name "pate_a_gateau"
            child "chaudron_2.png"
            draggable False
            xpos 1000 ypos 300

    imagebutton:
        idle "bouton_cuisson.png"
        hover "bouton_cuisson_hover.png"
        xalign 0.92
        yalign 0.80
        action If ((gat.ingredients == []), true = [Hide("ingred",transition=dissolve), Jump("cuire_gateau")], false = [Hide("ingred",transition=dissolve), Jump("echec_jeu_four")])

    imagebutton:
        idle "gateau_bulle_idle.png"
        hover "gateau_bulle_hover.png"
        xalign 0.92
        yalign 0.1
        action Jump("ingredients_gateau")


screen cuisinefour:
    image "chaudron.png":
        xalign 0.10
        yalign 0.7
    imagebutton:
        idle "bouton_cuisson.png"
        hover "bouton_cuisson_hover.png"
        xalign 0.7
        yalign 0.5
        action [Hide("cuisinefour",transition=dissolve),Jump("cuisson")]

screen marmite_cuisson:
    image "chaudron.png" at center
    image "flamme.png" at goutte_chaudron_cuisson

screen show_vars:
    text "Raté: [misses], Flammes: [hits]!" xalign 0.5
    image "flamme.png":
        pos (1000, 50)

screen le_feu_cuisson:
    text "{b}Allumez le feu!!!{/b} Touchez au moins 10 flammes" at truecenter

image goutte_chaudron:
    "goutte_chaudron.png"
    xpos 1000 ypos 240
    pause 0.25
    "goutte_chaudron.png"
    xpos 1010 ypos 200
    pause 0.25
#    "goutte_chaudron.png"
#    xpos 1000 ypos 240
#    pause 0.25
#    "goutte_chaudron.png"
#    xpos 1010 ypos 200
#    pause 0.25
    "goutte_chaudron.png"
    xpos 10000 ypos 10000

screen ajout_ingr:
    add "goutte_chaudron"

#Arbre A Bonbons
screen tempon:
    imagebutton:
        xpos 935
        ypos 380
        idle "bonbon.jpg"
        at custom_zoom

image bgArbreFeuillage = "ArbreFeuillage.png"

screen bonbonScreen:
    if bonbon1valeur != "1":
        imagebutton:
            xpos 910
            ypos 350
            idle "Dessin_bonbon_barrechocolatlait.png"
            at custom_zoom
            action [SetVariable("bonbon1valeur", "1")]

    if bonbon2valeur != "1":
        imagebutton:
            xpos 342
            ypos 288
            idle "Dessin_bonbon_barrechocolatnoire.png"
            at custom_zoom
            action [SetVariable("bonbon2valeur", "1")]

    if bonbon3valeur != "1":
        imagebutton:
            xpos 1060
            ypos 389
            idle "Dessin_bonbon_Carambarbleu.png"
            at custom_zoom
            action [SetVariable("bonbon3valeur", "1")]

    if bonbon4valeur != "1":
        imagebutton:
            xpos 20
            ypos 393
            idle "Dessin_bonbon_Carambarviolet.png"
            at custom_zoom
            action [SetVariable("bonbon4valeur", "1")]

    if bonbon5valeur != "1":
        imagebutton:
            xpos 1084
            ypos 30
            idle "Dessin_bonbon_dentrose.png"
            at custom_zoom
            action [SetVariable("bonbon5valeur", "1")]

    if bonbon6valeur != "1":
        imagebutton:
            xpos 80
            ypos 30
            idle "Dessin_bonbon_jellyjaune.png"
            at custom_zoom
            action [SetVariable("bonbon6valeur", "1")]

#Poursuite
screen papier:
    imagebutton:
        xpos 300
        ypos 100
        idle "boutDePapierFinal.png"
        at custom_zoom3


screen papierJeu:

    imagebutton:
        xpos 323
        ypos 570
        idle "bouton.png"
        at custom_zoom2
        action [Hide("bouton"), Jump("CulDeSac")]

    imagebutton:
        xpos 355
        ypos 570
        idle "bouton.png"
        at custom_zoom2
        action [Hide("bouton"), Jump("CulDeSac")]

    imagebutton:
        xpos 392
        ypos 570
        idle "bouton.png"
        at custom_zoom2
        action [Hide("bouton"), Jump("CulDeSac")]

    imagebutton:
        xpos 424
        ypos 570
        idle "bouton.png"
        at custom_zoom2
        action [Hide("bouton"), Jump("CulDeSac")]

    imagebutton:
        xpos 460
        ypos 570
        idle "bouton.png"
        at custom_zoom2
        action [Hide("bouton"), Jump("CulDeSac")]

    imagebutton:
        xpos 491
        ypos 570
        idle "bouton.png"
        at custom_zoom2
        action [Hide("bouton"), Jump("CulDeSac")]

    imagebutton:
        xpos 527
        ypos 570
        idle "bouton.png"
        at custom_zoom2
        action [Hide("bouton"), Jump("CulDeSac")]

    imagebutton:
        xpos 559
        ypos 570
        idle "bouton.png"
        at custom_zoom2
        action [Hide("bouton"), Jump("Arrivee")]

    imagebutton:
        xpos 597
        ypos 570
        idle "bouton.png"
        at custom_zoom2
        action [Hide("bouton"), Jump("CulDeSac")]

    imagebutton:
        xpos 627
        ypos 570
        idle "bouton.png"
        at custom_zoom2
        action [Hide("bouton"), Jump("CulDeSac")]

    imagebutton:
        xpos 668
        ypos 570
        idle "bouton.png"
        at custom_zoom2
        action [Hide("bouton"), Jump("CulDeSac")]

    imagebutton:
        xpos 700
        ypos 570
        idle "bouton.png"
        at custom_zoom2
        action [Hide("bouton"), Jump("CulDeSac")]

    imagebutton:
        xpos 737
        ypos 570
        idle "bouton.png"
        at custom_zoom2
        action [Hide("bouton"), Jump("CulDeSac")]

    imagebutton:
        xpos 769
        ypos 570
        idle "bouton.png"
        at custom_zoom2
        action [Hide("bouton"), Jump("CulDeSac")]

    imagebutton:
        xpos 806
        ypos 570
        idle "bouton.png"
        at custom_zoom2
        action [Hide("bouton"), Jump("CulDeSac")]

    imagebutton:
        xpos 838
        ypos 570
        idle "bouton.png"
        at custom_zoom2
        action [Hide("bouton"), Jump("CulDeSac")]