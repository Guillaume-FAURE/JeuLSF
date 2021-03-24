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
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.45
        yalign 0.39
        action [Hide ("Perdu1ToPerdu2"), Jump ("Perdu2")]
screen DOY:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.45
        yalign 0.39
        action [Hide ("Perdu1ToPerdu2"), Jump ("Perdu2")]
screen PIF:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.45
        yalign 0.39
        action [Hide ("Perdu1ToPerdu2"), Jump ("Perdu2")]
screen JUNQ:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.45
        yalign 0.39
        action [Hide ("Perdu1ToPerdu2"), Jump ("Perdu2")]
screen GREX:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
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

screen oliveau:
    imagebutton:
        idle "Oliveau.png"
        xalign 0.5
        yalign 0.2
        action[Hide("oliveau"), Show("oliveauStatic"), Jump("Oliveau")]
screen oliveauStatic:
    imagebutton:
        idle "Oliveau.png"
        xalign 0.5
        yalign 0.2

screen bird:
    imagebutton:
        idle "Oliveau.png"
        xalign 0.5
        yalign 0.2
        action[Hide("bird"), Show("birdStatic"), Jump("Bird")]
screen birdStatic:
    imagebutton:
        idle "Oliveau.png"
        xalign 0.5
        yalign 0.2

image rubis:
    "rubis.png"
image oui:
    "oui.png"

#####Background
image BlackScreen:
    "black.png"
image Perdu1:
    "Perdu1.jpg" 
image Perdu2:
    "Perdu2.jpg" 
image Perdu3:
    "Perdu3.jpg"
image Perdu4:
    "Perdu4.jpg"
image ArriveForetFees:
    "images/ArriveForetFees.jpg"
image Gouffre:
    "images/Gouffre.jpg"
image ArbreABonbons:
    "images/ArbreABonbons.jpg"
image FondDuGouffre:
    "images/FondDuGouffre.jpg"
image Bibliotheque:
    "images/Bibliotheque.png"
image Labyrinthe:
    "images/Labyrinthe.png"
image ClairiereDOliveau:
    "images/ClairiereDOliveau.png"
image Lac:
    "images/Lac.png"
image Cuisine:
    "images/Cuisine.png"
image NidDeLOiseau:
    "images/NidDeLOiseau.png"
image Cuisine:
    "images/Cuisine.png"
image PorteDuRoyaumeDesFees:
    "images/PorteDuRoyaumeDesFees.png"
image LieuDuVol:
    "images/LieuDuVol.png"
image Cuisine:
    "images/PseudoLabyrinthe.png"
image FalaiseAvecLierre:
    "images/FalaiseAvecLierre.png"
image PiegeDeLAlchimiste:
    "images/PiegeDeLAlchimiste.png"


######Links

###Links Perdu
screen Perdu1ToPerdu2:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.45
        yalign 0.39
        action [Hide ("Perdu1ToPerdu2"), Jump ("Perdu2")]
screen Perdu2ToPerdu3:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.87
        yalign 0.08
        action [Hide ("Perdu2ToPerdu3"), Jump ("Perdu3")]
screen Perdu3ToPerdu4:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.37
        yalign 0.26
        action [Hide ("Perdu3ToPerdu4"), Jump ("Perdu4")]
screen Perdu4ToArriveForetFees:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.6
        yalign 0.35
        action [Hide ("Perdu4ToArriveForetFees"), Jump ("ArriveForetFees")]

###Links ArriveForetFees
screen ArriveForetFeesLink:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.04
        yalign 0.4
        action [Hide("ArriveForetFeesLink"), Jump ("Gouffre")]
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
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
screen GouffreToArbreABonbons:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.04
        yalign 0.4
        action [Hide ("GouffreToArriveForetFees"), Hide ("GouffreToFondDuGouffre"), Hide ("GouffreToArbreABonbons"), Jump ("ArbreABonbons")]
screen GouffreToArriveForetFees:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.96
        yalign 0.6
        action [Hide ("GouffreToArbreABonbons"), Hide ("GouffreToFondDuGouffre"), Hide ("GouffreToArriveForetFees"), Jump ("ArriveForetFees")]
screen GouffreToFondDuGouffre:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("GouffreToArbreABonbons"), Hide ("GouffreToArriveForetFees"), Hide ("GouffreToFondDuGouffre"), Jump ("FondDuGouffre")]

###Links FondDuGouffre
screen FondDuGouffreToGouffre:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.8
        yalign 0.8
        action [Hide ("FondDuGouffreToGouffre"),Hide ("FondDuGouffreToBibliotheque"),Hide ("FondDuGouffreToLabyrinthe"), Jump ("Gouffre")]    
screen FondDuGouffreToBibliotheque:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.04
        yalign 0.4
        action [Hide ("FondDuGouffreToGouffre"),Hide ("FondDuGouffreToBibliotheque"),Hide ("FondDuGouffreToLabyrinthe"), Jump ("Bibliotheque")]
screen FondDuGouffreToLabyrinthe:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.3
        yalign 0.1
        action [Hide ("FondDuGouffreToGouffre"),Hide ("FondDuGouffreToBibliotheque"),Hide ("FondDuGouffreToLabyrinthe"), Jump ("Labyrinthe")]

###Link Bibliotheque
screen BibliothequeToFondDuGouffre:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("BibliothequeToFondDuGouffre"), Jump ("FondDuGouffre")]

###Link Labyrinthe
screen LabyrintheToFondDuGouffre:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("LabyrintheToFondDuGouffre"), Jump ("FondDuGouffre")]

###Link Lac
screen LacToClairiereDOliveau:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.1
        yalign 0.5
        action [Hide ("LacToCuisine"),Hide ("LacToNidDeLOiseau"),Hide ("LacToClairiereDOliveau"), Jump ("ClairiereDOliveau")]
screen LacToCuisine:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.2
        yalign 0.8
        action [Hide ("LacToClairiereDOliveau"),Hide ("LacToNidDeLOiseau"),Hide ("LacToCuisine"), Jump ("Cuisine")]
screen LacToNidDeLOiseau:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.9
        yalign 0.5
        action [Hide ("LacToClairiereDOliveau"),Hide ("LacToCuisine"),Hide ("LacToNidDeLOiseau"), Jump ("NidDeLOiseau")]

###Link Clairiere d'Oliveau
screen ClairiereDOliveauToArriveForetFees:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.2
        yalign 0.95
        action [Hide ("ClairiereDOliveauToPorteDuRoyaumeDesFees"),Hide ("ClairiereDOliveauToLieuDuVol"),Hide ("ClairiereDOliveauToLac"),Hide("oliveau"), Hide("oliveauStatic"),Hide ("ClairiereDOliveauToArriveForetFees"), Jump ("ArriveForetFees")]
screen ClairiereDOliveauToLieuDuVol:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.45
        yalign 0.05
        action [Hide ("ClairiereDOliveauToPorteDuRoyaumeDesFees"),Hide ("ClairiereDOliveauToLac"),Hide ("ClairiereDOliveauToArriveForetFees"),Hide("oliveau"), Hide("oliveauStatic"),Hide ("ClairiereDOliveauToLieuDuVol"), Jump ("LieuDuVol")]
screen ClairiereDOliveauToLac:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.97
        yalign 0.5
        action [Hide ("ClairiereDOliveauToPorteDuRoyaumeDesFees"),Hide ("ClairiereDOliveauToLieuDuVol"),Hide ("ClairiereDOliveauToArriveForetFees"),Hide("oliveau"), Hide("oliveauStatic"),Hide ("ClairiereDOliveauToLac"), Jump ("Lac")]
screen ClairiereDOliveauToPorteDuRoyaumeDesFees:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.9
        yalign 0.1
        action [Hide ("ClairiereDOliveauToLieuDuVol"),Hide ("ClairiereDOliveauToLac"),Hide("oliveau"), Hide("oliveauStatic"),Hide ("ClairiereDOliveauToArriveForetFees"),Hide ("ClairiereDOliveauToPorteDuRoyaumeDesFees"), Jump ("PorteDuRoyaumeDesFees")]

###Link Nid De L'Oiseau
screen NidDeLOiseauToLac:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.9
        yalign 0.1
        action [Hide ("NidDeLOiseauToLac"), Jump ("PorteDuRoyaumeDesFees")]

###Link Porte du royaume des fées
screen LinkPorteDuRoyaumeDesFees:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("LinkPorteDuRoyaumeDesFees"), Jump ("PorteDuRoyaumeDesFees")]

###Link Lieu du vol
screen LieuDuVolToClairiereDOliveau:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.3
        yalign 0.8
        action [Hide ("LieuDuVolToFalaiseAvecLierre"),Hide ("LieuDuVolToPseudoLabyrinthe"),Hide ("LieuDuVolToClairiereDOliveau"), Jump ("ClairiereDOliveau")]
screen LieuDuVolToPseudoLabyrinthe:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.7
        yalign 0.1
        action [Hide ("LieuDuVolToFalaiseAvecLierre"),Hide ("LieuDuVolToClairiereDOliveau"),Hide ("LieuDuVolToPseudoLabyrinthe"), Jump ("PseudoLabyrinthe")]
screen LieuDuVolToFalaiseAvecLierre:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.2
        yalign 0.5
        action [Hide ("LieuDuVolToClairiereDOliveau"),Hide ("LieuDuVolToPseudoLabyrinthe"),Hide ("LieuDuVolToFalaiseAvecLierre"), Jump ("FalaiseAvecLierre")]
        
###Link PseudoLabyrinthe
screen PseudoLabyrintheToLieuDuVol:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.3
        yalign 0.8
        action [Hide ("PseudoLabyrintheToLieuDuVol"), Jump ("LieuDuVol")]

###Link Falaise avec lierre
screen FalaiseAvecLierreToPiegeDeLAlchimiste:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.1
        yalign 0.1
        action [Hide ("FalaiseAvecLierreToLieuDuVol"),Hide ("FalaiseAvecLierreToPiegeDeLAlchimiste"), Jump ("PiegeDeLAlchimiste")]
screen FalaiseAvecLierreToLieuDuVol:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.9
        yalign 0.8
        action [Hide ("FalaiseAvecLierreToPiegeDeLAlchimiste"),Hide ("FalaiseAvecLierreToLieuDuVol"), Jump ("LieuDuVol")]
    
###Link Piege de l'alchimiste
screen PiegeDeLAlchimisteToFalaiseAvecLierre:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.9
        yalign 0.8
        action [Hide ("PiegeDeLAlchimisteToFalaiseAvecLierre"), Jump ("FalaiseAvecLierre")]


