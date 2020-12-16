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
            xpos i.x
            ypos i.y
            add i.image at sizeRoom


image Salle1:
    "images/Salle1.png"

image Salle2:
    "images/Salle2.png"

image BlackScreen:
    "black.png"
