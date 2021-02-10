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




image ISalle1:
    "images/Salle1.png"

image ISalle2:
    "images/Salle2.png"

image BlackScreen:
    "black.png"

screen ArriveForetFeesToTransitionKabeGouffre:
    imagebutton:
        idle "link.png"
        at sizeButton
        xalign 0.04
        yalign 0.4
        action [Hide ("ArriveForetFeesToTransitionKabeGouffre"), Hide ("ArriveForetFeesToClairiereDOliveau"), Jump ("TransitionKabeGouffre")]

screen ArriveForetFeesToClairiereDOliveau:
    imagebutton:
        idle "link.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("ArriveForetFeesToTransitionKabeGouffre"), Jump ("ClairiereDOliveau"), Hide ("ArriveForetFeesToClairiereDOliveau")]

screen TransitionKabeGouffreToArbreABonbons:
    imagebutton:
        idle "link.png"
        at sizeButton
        xalign 0.04
        yalign 0.4
        action [Hide ("TransitionKabeGouffreToArriveForetFees"), Hide ("TransitionKabeGouffreToPassageObstrue"), Jump ("ArbreABonbons"), Hide ("TransitionKabeGouffreToArbreABonbons")]

screen TransitionKabeGouffreToArriveForetFees:
    imagebutton:
        idle "link.png"
        at sizeButton
        xalign 0.96
        yalign 0.6
        action [Hide ("TransitionKabeGouffreToArbreABonbons"), Hide ("TransitionKabeGouffreToPassageObstrue"), Jump ("ArriveForetFees"), Hide ("TransitionKabeGouffreToArriveForetFees")]

screen TransitionKabeGouffreToPassageObstrue:
    imagebutton:
        idle "link.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("TransitionKabeGouffreToArbreABonbons"), Hide ("TransitionKabeGouffreToArriveForetFees"), Jump ("PassageObstrue"), Hide ("TransitionKabeGouffreToPassageObstrue")]

screen LinkPassageObstrue:
    imagebutton:
        idle "link.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("LinkPassageObstrue"), Jump ("PassageObstrue")]

screen LinkBibliotheque:
    imagebutton:
        idle "link.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("LinkBibliotheque"), Jump ("Bibliotheque")]

screen LinkLabyrinthe:
    imagebutton:
        idle "link.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("LinkLabyrinthe"), Jump ("Labyrinthe")]

screen LinkLac:
    imagebutton:
        idle "link.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("LinkLac"), Jump ("Lac")]

screen LinkNidDeLOiseau:
    imagebutton:
        idle "link.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("LinkNidDeLOiseau"), Jump ("NidDeLOiseau")]

screen LinkPorteDuRoyaumeDesFees:
    imagebutton:
        idle "link.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("LinkPorteDuRoyaumeDesFees"), Jump ("PorteDuRoyaumeDesFees")]

screen LinkLieuDuVol:
    imagebutton:
        idle "link.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("LinkLieuDuVol"), Jump ("LieuDuVol")]

screen LinkPseudoLabyrinthe:
    imagebutton:
        idle "link.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("LinkPseudoLabyrinthe"), Jump ("PseudoLabyrinthe")]

screen LinkFalaiseAvecLierre:
    imagebutton:
        idle "link.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("LinkFalaiseAvecLierre"), Jump ("FalaiseAvecLierre")]

screen LinkPiegeDeLAlchimiste:
    imagebutton:
        idle "link.png"
        at sizeButton
        xalign 0.5
        yalign 0.1
        action [Hide ("LinkPiegeDeLAlchimiste"), Jump ("PiegeDeLAlchimiste")]


