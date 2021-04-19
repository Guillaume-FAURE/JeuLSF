screen Button1:
    frame:
        xpos 0.5
        ypos 0.5
        text "test !":
            size 68

screen magie:
    imagebutton:
        xpos 0.5
        ypos 0.5
        idle "images/monika.webp"
        at custom_zoom
        action [Hide("magie"), Jump("advancedTransition")]
transform custom_zoom:
    zoom 0.2
transform dictionnary:
    size(60,60)

screen dictionnary:
    vbox:
        for i in dictionnary:
            frame:
                xpadding 20
                ypadding 20
                xmargin 2
                ymargin 2
                add i.image size(60,60)
