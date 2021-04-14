###Menu
screen menuShow:
    imagebutton:
        idle "SacIdle.png"
        hover "SacHover.png"
        at sizeButton
        xalign 0.98
        yalign 0.02
        action [Show("menuBackground"), Show("menuHide") ,Show ("minimapShow"), Hide ("menuShow")]
        
screen menuHide:
    imagebutton:
        idle "SacHover.png"
        hover "SacIdle.png"
        at sizeButton
        xalign 0.98
        yalign 0.02
        action [Hide("menuHide") ,Hide ("minimapShow"),Hide("menuBackground"), Show ("menuShow")]

screen menuBackground:
    imagebutton:
        idle "menuBackground.png"
        at sizeMenuBackground
        xalign 0.99
        yalign 0.01
    

screen minimapShow:
    imagebutton:
        idle "iconeMap.png"
        at sizeButton
        xalign 0.98
        yalign 0.15
        action [Show("mapBackground") ,Show ("minimap"),Show("minimapHide"), Hide ("minimapShow")]
screen minimapHide:
    imagebutton:
        idle "iconeMap.png"
        at sizeButton
        xalign 0.98
        yalign 0.15
        action [Show ("minimapShow"),Hide ("minimap"),Hide ("mapBackground"),Hide ("minimapHide")]

screen mapBackground:
    imagebutton:
        idle "map.png"
        at sizeMapBackground
        xpos 0
        ypos 0

screen Blackscreen:
    imagebutton:
        idle "black.png"
screen Whitescreen:
    imagebutton:
        idle "white.png"
        at zoom4
        xpos 0
        ypos 0
screen minimap:
    $ s = -1
    for i in minimap:
        frame:
            xpos i.x*10
            ypos i.y*10
            imagebutton:
                idle i.image
                at sizeRoom
                action [Hide ("minimap"),Hide ("Blackscreen"),Hide ("minimapHide"),Show ("minimapShow"), Jump (i.label)]
        frame:
            xpos i.x*10-65
            ypos i.y*10+75
            text i.name

###Sorts

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
image achOliveau:
    "Achievements/achOliveau.png"
image achEnfantIgnorant:
    "Achievements/achEnfantIgnorant.png"

#####Background
image BlackScreen:
    "images/Background/Black.png"
image Perdu1:
    "images/Background/Perdu1.jpg" 
image Perdu2:
    "images/Background/Perdu2.jpg" 
image Perdu3:
    "images/Background/Perdu3.jpg"
image Perdu4:
    "images/Background/Perdu4.jpg"
image ArriveForetFees:
    "images/Background/ArriveForetFees.jpg"
image Gouffre:
    "images/Background/Gouffre.jpg"
image ArbreABonbons:
    "images/Background/ArbreABonbons.jpg"
image FondDuGouffre:
    "images/Background/FondDuGouffre.jpg"
image Bibliotheque:
    "images/Background/Bibliotheque.png"
image Labyrinthe:
    "images/Background/Labyrinthe.png"
image ClairiereDOliveau:
    "images/Background/ClairiereDOliveau.jpg"
image Lac:
    "images/Background/Lac.jpg"
image SurLac:
    "images/Background/SurLac.png"
image FondDuLac:
    "images/Background/FondDuLac.png"
image Cuisine:
    "images/Background/Cuisine.png"
image NidDeLOiseau:
    "images/Background/NidDeLOiseau.jpg"
image Cuisine:
    "images/Background/Cuisine.png"
image PorteDuRoyaumeDesFees:
    "images/Background/PorteDuRoyaumeDesFees.png"
image LieuDuVol:
    "images/Background/LieuDuVol.png"
image Cuisine:
    "images/Background/PseudoLabyrinthe.png"
image Falaise:
    "images/Background/Falaise.jpg"
image FalaiseLierre:
    "images/Background/FalaiseLierre.png"
image DessusDeLaFalaise:
    "images/Background/DessusDeLaFalaise.jpg"
image PlanDeTravail:
    "images/Background/PlanDeTravail.png"


######Links

###Links Perdu
screen Perdu1ToPerdu2:
    imagebutton:
        idle "LinkIdleN.png"
        hover "LinkHoverN.png"
        at sizeButton
        xalign 0.45
        yalign 0.39
        action [Hide ("Perdu1ToPerdu2"), Jump ("Perdu2")]
screen Perdu2ToPerdu3:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.87
        yalign 0.08
        action [Hide ("Perdu2ToPerdu3"), Jump ("Perdu3")]
screen Perdu3ToPerdu4:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.37
        yalign 0.26
        action [Hide ("Perdu3ToPerdu4"), Jump ("Perdu4")]
screen Perdu4ToArriveForetFees:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.6
        yalign 0.35
        action [Hide ("Perdu4ToArriveForetFees"), Jump ("ArriveForetFees")]

###Links ArriveForetFees
screen ArriveForetFeesLink:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.04
        yalign 0.4
        action [Hide("ArriveForetFeesLink"), Jump ("Gouffre")]
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("ArriveForetFeesLink"), Jump ("ClairiereDOliveau")]
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
                action[Jump("ClairiereDOliveau")]
        elif i.name=="DOY":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.16
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="PIF":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.24
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="JUNQ":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.32
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        
        
    

###Links Gouffre
screen GouffreLink:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.04
        yalign 0.4
        action [Hide ("GouffreLink"), Jump ("ArbreABonbons")]
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.96
        yalign 0.6
        action [Hide ("GouffreLink"), Jump ("ArriveForetFees")]
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("GouffreLink"), Jump ("FondDuGouffre")]
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
                action[Jump("ClairiereDOliveau")]
        elif i.name=="DOY":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.16
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="PIF":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.24
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="JUNQ":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.32
                yalign 0.01
                action[Jump("ClairiereDOliveau")]

###Links FondDuGouffre
screen FondDuGouffreLink:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.8
        yalign 0.8
        action [Hide ("FondDuGouffreLink"), Jump ("Gouffre")]    
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.04
        yalign 0.4
        action [Hide ("FondDuGouffreLink"), Jump ("Bibliotheque")]
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.3
        yalign 0.1
        action [Hide ("FondDuGouffreLink"), Jump ("Labyrinthe")]
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
                action[Jump("ClairiereDOliveau")]
        elif i.name=="DOY":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.16
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="PIF":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.24
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="JUNQ":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.32
                yalign 0.01
                action[Jump("ClairiereDOliveau")]

###Link Bibliotheque
screen BibliothequeLink:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("BibliothequeLink"), Jump ("FondDuGouffre")]
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
                action[Jump("ClairiereDOliveau")]
        elif i.name=="DOY":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.16
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="PIF":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.24
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="JUNQ":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.32
                yalign 0.01
                action[Jump("ClairiereDOliveau")]

###Link Labyrinthe
screen LabyrintheLink:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("LabyrintheLink"), Jump ("FondDuGouffre")]
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
                action[Jump("ClairiereDOliveau")]
        elif i.name=="DOY":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.16
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="PIF":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.24
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="JUNQ":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.32
                yalign 0.01
                action[Jump("ClairiereDOliveau")]

###Link Lac
screen LacLink:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.1
        yalign 0.5
        action [Hide ("LacLink"), Jump ("ClairiereDOliveau")]
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.2
        yalign 0.8
        action [Hide ("LacLink"), Jump ("Cuisine")]
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.9
        yalign 0.5
        action [Hide ("LacLink"), Jump ("NidDeLOiseau")]
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
                action[Jump("ClairiereDOliveau")]
        elif i.name=="DOY":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.16
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="PIF":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.24
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="JUNQ":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.32
                yalign 0.01
                action[Jump("ClairiereDOliveau")]

###Link Clairiere d'Oliveau
screen ClairiereDOliveauLink:
    imagebutton:
        idle "Oliveau.png"
        xalign 0.5
        yalign 0.2
        action [Hide ("ClairiereDOliveauLink"), Show("oliveauStatic"), Jump("Oliveau")]
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.2
        yalign 0.95
        action [Hide ("ClairiereDOliveauLink"), Jump ("ArriveForetFees")]
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.45
        yalign 0.05
        action [Hide ("ClairiereDOliveauLink"), Jump ("LieuDuVol")]
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.97
        yalign 0.5
        action [Hide ("ClairiereDOliveauLink"), Jump ("Lac")]
    if avancement[0] != "null" and avancement[0] != "Q2":
        imagebutton:
            idle "LinkIdleE.png"
            hover "LinkHoverE.png"
            at sizeButton
            xalign 0.9
            yalign 0.1
            action [Hide ("ClairiereDOliveauLink"), Jump ("PorteDuRoyaumeDesFees")]
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
                action[Jump("ClairiereDOliveau")]
        elif i.name=="DOY":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.16
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="PIF":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.24
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="JUNQ":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.32
                yalign 0.01
                action[Jump("ClairiereDOliveau")]

screen oliveauStatic:
    imagebutton:
        idle "Oliveau.png"
        xalign 0.5
        yalign 0.2

###Link Nid De L'Oiseau
screen NidDeLOiseauLink:
    imagebutton:
        idle "Oliveau.png"
        xalign 0.5
        yalign 0.2
        action[Hide("NidDeLOiseauLink"), Show("birdStatic"), Jump("Bird")]
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.9
        yalign 0.1
        action [Hide ("NidDeLOiseauLink"), Jump ("Lac")]
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
                action[Jump("ClairiereDOliveau")]
        elif i.name=="DOY":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.16
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="PIF":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.24
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="JUNQ":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.32
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
screen birdStatic:
    imagebutton:
        idle "Oliveau.png"
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
                action[Jump("ClairiereDOliveau")]
        elif i.name=="DOY":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.16
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="PIF":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.24
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="JUNQ":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.32
                yalign 0.01
                action[Jump("ClairiereDOliveau")]

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
        action [Hide ("LieuDuVolLink"), Jump ("FalaiseAvecLierre")]
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
                action[Jump("ClairiereDOliveau")]
        elif i.name=="DOY":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.16
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="PIF":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.24
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="JUNQ":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.32
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
     
###Link PseudoLabyrinthe
screen PseudoLabyrintheLink:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.3
        yalign 0.8
        action [Hide ("PseudoLabyrintheLink"), Jump ("LieuDuVol")]
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
                action[Jump("ClairiereDOliveau")]
        elif i.name=="DOY":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.16
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="PIF":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.24
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="JUNQ":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.32
                yalign 0.01
                action[Jump("ClairiereDOliveau")]

###Link Falaise avec lierre
screen FalaiseAvecLierreLink:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.1
        yalign 0.1
        action [Hide ("FalaiseAvecLierreLink"), Jump ("PiegeDeLAlchimiste")]
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.9
        yalign 0.8
        action [Hide ("FalaiseAvecLierreLink"), Jump ("LieuDeVol")]
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
                action[Jump("ClairiereDOliveau")]
        elif i.name=="DOY":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.16
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="PIF":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.24
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="JUNQ":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.32
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
  
###Link Piege de l'alchimiste
screen PiegeDeLAlchimisteLink:
    imagebutton:
        idle "LinkIdleE.png"
        hover "LinkHoverE.png"
        at sizeButton
        xalign 0.9
        yalign 0.8
        action [Hide ("PiegeDeLAlchimisteLink"), Jump ("FalaiseAvecLierre")]
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
                action[Jump("ClairiereDOliveau")]
        elif i.name=="DOY":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.16
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="PIF":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.24
                yalign 0.01
                action[Jump("ClairiereDOliveau")]
        elif i.name=="JUNQ":
            imagebutton:
                idle i.image
                at sizeButton
                xalign 0.32
                yalign 0.01
                action[Jump("ClairiereDOliveau")]

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
