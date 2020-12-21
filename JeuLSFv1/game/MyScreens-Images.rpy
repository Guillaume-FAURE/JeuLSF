screen minimapShow:
    imagebutton:
        idle "minimapShow.png"
        at sizeButton
        action [Show("Blackscreen") ,Show ("minimap"),Show("minimapHide"),Hide ("minimapShow")]

screen Blackscreen:
    imagebutton:
        idle "black.png"

screen minimapHide:
    imagebutton:
        idle "minimapHide.png"
        at sizeButton
        action [Show ("minimapShow"),Hide ("minimap"),Hide ("Blackscreen"),Hide ("minimapHide")]

screen minimap:
    $ s = -1
    for i in minimap:
        frame:
            xpos i.x*100
            ypos i.y*100
            imagebutton:
                idle i.image
                at sizeRoom
                action [Hide ("minimap"),Hide ("Blackscreen"),Hide ("minimapHide"),Show ("minimapShow"), Jump (i.name)]
        frame:
            xpos i.x+20
            ypos i.y+77
            text i.name




image ISalle1:
    "images/Salle1.png"

image ISalle2:
    "images/Salle2.png"

image BlackScreen:
    "black.png"
