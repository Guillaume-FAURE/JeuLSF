screen minimapShow:
    imagebutton:
        idle "minimapShow.png"
        at sizeButton
        action [Show("Whitescreen") ,Show ("minimap"),Show("minimapHide"),Hide ("minimapShow")]

screen Blackscreen:
    imagebutton:
        idle "black.png"

screen Whitescreen:
    imagebutton:
        idle "white.png"
        at zoom4
        xpos 0
        ypos 0

screen minimapHide:
    imagebutton:
        idle "minimapHide.png"
        at sizeButton
        action [Show ("minimapShow"),Hide ("minimap"),Hide ("Whitescreen"),Hide ("minimapHide")]


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
image TransitionKabeGouffre:
    "iamges/TransitionKabeGouffre.jpg"
image ArbreABonbons:
    "images/ArbreABonbons.jpg"
image PassageObstrue:
    "images/PassageObstrue.jpg"
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
screen ArriveForetFeesToTransitionKabeGouffre:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.04
        yalign 0.4
        action [Hide ("ArriveForetFeesToTransitionKabeGouffre"), Hide ("ArriveForetFeesToClairiereDOliveau"), Jump ("TransitionKabeGouffre")]

screen ArriveForetFeesToClairiereDOliveau:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("ArriveForetFeesToTransitionKabeGouffre"), Hide ("ArriveForetFeesToClairiereDOliveau"), Jump ("ClairiereDOliveau")]
###Links TransitionKabeGouffre
screen TransitionKabeGouffreToArbreABonbons:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.04
        yalign 0.4
        action [Hide ("TransitionKabeGouffreToArriveForetFees"), Hide ("TransitionKabeGouffreToPassageObstrue"), Hide ("TransitionKabeGouffreToArbreABonbons"), Jump ("ArbreABonbons")]

screen TransitionKabeGouffreToArriveForetFees:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.96
        yalign 0.6
        action [Hide ("TransitionKabeGouffreToArbreABonbons"), Hide ("TransitionKabeGouffreToPassageObstrue"), Hide ("TransitionKabeGouffreToArriveForetFees"), Jump ("ArriveForetFees")]

screen TransitionKabeGouffreToPassageObstrue:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("TransitionKabeGouffreToArbreABonbons"), Hide ("TransitionKabeGouffreToArriveForetFees"), Hide ("TransitionKabeGouffreToPassageObstrue"), Jump ("PassageObstrue")]
###Links PassageObstrue
screen LinkPassageObstrue:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("LinkPassageObstrue"), Jump ("PassageObstrue")]

screen LinkBibliotheque:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("LinkBibliotheque"), Jump ("Bibliotheque")]

screen LinkLabyrinthe:
    imagebutton:
        idle "LinkIdle.png"
        hover "LinkHover.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("LinkLabyrinthe"), Jump ("Labyrinthe")]

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


