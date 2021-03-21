transform sizeRoom:
    size(108,72)
transform sizeButton:
    size(72,72)
transform sizeBackground:
    size(1280,720)
transform sizeMenuBackground:
    size(100, 650)
transform sizeMapBackground:
    size(1150,720)

transform position(x,y):
    xpos x
    ypos y
transform zoom4:
    zoom 4.0
define slowDissolve = Dissolve(1)

transform goRight:
    xalign 0.1
    yalign 0.4

transform test:
    xalign 0.5 yalign 0.5
    linear 0.5 yalign 0.0
    linear 0.5 yalign 0.5

transform Tinventaire:
    xalign 0.5 yalign 0.5
    zoom 0.0
    linear 0.5 zoom 1.0
    pause 1.5
    linear 0.75 yalign 0.05 xalign 0.95
    linear 0.5 zoom 0.0

transform Tachievement:
    xalign 0.5 yalign 0.5
    zoom 0.0
    linear 0.6 zoom 2.5
    linear 0.4 zoom 1.0
    pause 1.0
    parallel:
        linear 1.5 rotate 1800
    parallel:
        linear 1.5 yalign 0.05 xalign 0.95 zoom 0.0
    