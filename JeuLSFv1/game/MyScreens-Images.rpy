screen menuShow:
    imagebutton:
        idle "LinkHover.png"
        hover "LinkIdle.png"
        at sizeButton
        xalign 0.98
        yalign 0.02
        action [Show("menuHide") ,Show ("minimapShow"),Show ("gentillesse"), Hide ("menuShow")]
screen menuHide:
    imagebutton:
        idle "LinkHover.png"
        hover "LinkIdle.png"
        at sizeButton
        xalign 0.98
        yalign 0.02
        action [Hide("menuHide") ,Hide ("minimapShow"),Hide ("gentillesse"), Show ("menuShow")]

screen minimapShow:
    imagebutton:
        idle "minimapShow.png"
        at sizeButton
        xalign 0.98
        yalign 0.12
        action [Show("Whitescreen") ,Show ("minimap"),Show("minimapHide"),Hide ("minimapShow")]
screen minimapHide:
    imagebutton:
        idle "minimapHide.png"
        at sizeButton
        xalign 0.98
        yalign 0.12
        action [Show ("minimapShow"),Hide ("minimap"),Hide ("Whitescreen"),Hide ("minimapHide")]
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
            xpos i.x*10-14
            ypos i.y*10+75
            text i.name

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
screen ArriveForetFeesToGouffre:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.04
        yalign 0.4
        action [Hide ("ArriveForetFeesToGouffre"), Hide ("ArriveForetFeesToClairiereDOliveau"), Jump ("Gouffre")]
screen ArriveForetFeesToClairiereDOliveau:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("ArriveForetFeesToGouffre"), Hide ("ArriveForetFeesToClairiereDOliveau"), Jump ("ClairiereDOliveau")]

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
screen LinkLac:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("LinkLac"), Jump ("Lac")]

screen LinkNidDeLOiseau:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("LinkNidDeLOiseau"), Jump ("NidDeLOiseau")]

screen LinkPorteDuRoyaumeDesFees:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("LinkPorteDuRoyaumeDesFees"), Jump ("PorteDuRoyaumeDesFees")]

screen LinkLieuDuVol:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("LinkLieuDuVol"), Jump ("LieuDuVol")]

screen LinkPseudoLabyrinthe:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("LinkPseudoLabyrinthe"), Jump ("PseudoLabyrinthe")]

screen LinkFalaiseAvecLierre:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("LinkFalaiseAvecLierre"), Jump ("FalaiseAvecLierre")]

screen LinkPiegeDeLAlchimiste:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("LinkPiegeDeLAlchimiste"), Jump ("PiegeDeLAlchimiste")]


