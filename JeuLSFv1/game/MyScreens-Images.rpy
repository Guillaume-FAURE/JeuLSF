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
        idle "model map.png"
        xpos 108
        ypos 72

screen minimapHide:
    imagebutton:
        idle "minimapHide.png"
        at sizeButton
        action [Show ("minimapShow"),Hide ("minimap"),Hide ("Whitescreen"),Hide ("minimapHide")]

screen LinkArriveForetFees:
    imagebutton:
        idle "link.png"
        at sizeButton
        action [Hide ("doorRight"), Jump (i.right)]


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
            xalign i.x*10
            yalign i.y*10
            text i.name




image ISalle1:
    "images/Salle1.png"

image ISalle2:
    "images/Salle2.png"

image BlackScreen:
    "black.png"
