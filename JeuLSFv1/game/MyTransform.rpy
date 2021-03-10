transform sizeRoom:
    size(108,72)
transform sizeButton:
    size(72,72)
transform sizeBackground:
    size(1280,720)
transform position(x,y):
    xpos x
    ypos y
transform zoom4:
    zoom 4.0
define slowDissolve = Dissolve(1)

transform goRight:
    xalign 0.1
    yalign 0.4

transform inventaire:
    xalign 0.5 yalign 0.5
    zoom 0.0
    linear 0.5 zoom 1.0
    pause 2.0
    linear 0.75 yalign 0.05 xalign 0.95
    linear 0.5 zoom 0.0

transform achievement:
    xalign 0.5 yalign 0.5
    zoom 0.0
    linear 0.5 zoom 1.0
    block:
        linear 0.1 rotate 360.0
        repeat 5
    linear 0.75 yalign 0.5 xalign 0.95
    linear 0.5 zoom 0.0
    