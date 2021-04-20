transform sizeRoom:
    size(120,120)
transform sizeButton:
    size(72,72)
transform sizeBackground:
    size(1280,720)
transform sizeMenuBackground:
    size(100, 650)
transform sizeMapBackground:
    size(1150,720)
transform sizeAchievement:
    size(139,50)
transform sizeObjet:
    size(200,200)
transform sizeFermer:
    size(30,30)

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
    size(400,400)
    xalign 0.5 yalign 0.5
    zoom 0.0
    linear 0.5 zoom 1.0
    pause 1.5
    linear 0.75 yalign 0.05 xalign 0.95
    linear 0.5 zoom 0.0

transform Tachievement:
    size(288,100)
    xalign 0.5 yalign 0.5
    zoom 0.0
    linear 0.6 zoom 2.5
    linear 0.4 zoom 1.0
    pause 1.0
    parallel:
        linear 1.5 rotate 1800
    parallel:
        linear 1.5 yalign 0.05 xalign 0.95 zoom 0.0
    
transform jeuBiblio_custom_zoom:
    zoom 0.45

transform jeuBiblio_custom_zoom2:
    zoom 0.6

transform jeuFiole_custom_zoom:
    zoom 0.5

transform jeuFiole_custom_zoom2:
    zoom 0.2

transform goutte_chaudron_cuisson:
    xalign 0.5 yalign 1.02 xzoom 4.0 yzoom 2.0
    pause 0.25
    xalign 0.5 yalign 1.02 xzoom 4.5 yzoom 2.5
    pause 0.25
    repeat

transform pos_flamme:
    xalign 0.0
    yalign 0.06


transform custom_zoom:
    zoom 0.05

transform custom_zoom3:
    zoom 0.35

transform custom_zoom2:
    zoom 0.090

transform indication1:
    size(50,50)
    xalign 0.95 
    yalign 0.5
    zoom 0.0
    linear 1.0 zoom 1.0
    linear 1.0 zoom 0.0

transform Montrer:
    zoom 1
    pause 0.5
    linear 0.5 zoom 0

transform sizePorte:
    size(500,500)
transform sizeAlchimiste:
    zoom 0.5
transform sizeEnfant:
    zoom 0.35
transform sizeBibliothecaire:
    zoom 0.7

transform sizeOliveau:
    zoom 0.8