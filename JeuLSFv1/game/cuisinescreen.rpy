init python:
    config.screen_width=1280
    config.screen_height=800
    import time
    import pygame
    MOUSEBUTTONDOWN=pygame.MOUSEBUTTONDOWN
    dico_ingr = {"beurre":[100,100], "oeufs":[300,100], "lait":[500,100], "levure":[700,100], "farine":[100,300], "sucre":[300,300], "sirop_de_rose":[500,300], "sirop_d'arsenic":[700,300]}

image goutte_chaudron:
    "goutte_chaudron.png"
    xpos 1000 ypos 240
    pause 0.25
    "goutte_chaudron.png"
    xpos 1010 ypos 200
    pause 0.25
#    "goutte_chaudron.png"
#    xpos 1000 ypos 240
#    pause 0.25
#    "goutte_chaudron.png"
#    xpos 1010 ypos 200
#    pause 0.25
    "goutte_chaudron.png"
    xpos 10000 ypos 10000

transform goutte_chaudron_cuisson:
    xalign 0.5 yalign 1.02 xzoom 4.0 yzoom 2.0
    pause 0.25
    xalign 0.5 yalign 1.02 xzoom 4.5 yzoom 2.5
    pause 0.25
    repeat

screen ajout_ingr:
    add "goutte_chaudron"

init python:

    def ing_dragged(drags, drop):

        if not drop:
            return
        store.show_drag = False
        renpy.hide_screen("ajout_ingr")
        renpy.show_screen("ajout_ingr")
        if ((drags[0].drag_name == "sirop_de_rose") or (drags[0].drag_name == "sirop_d'arsenic")):
            drags[0].snap(10000,10000)
            if (drags[0].drag_name == "sirop_de_rose"):            
                globals()['choix_sirop'] = 1
            else:
                globals()['choix_sirop'] = 2
        else:
            drags[0].snap(dico_ingr[drags[0].drag_name][0],dico_ingr[drags[0].drag_name][1])
            if gat.check(drags[0].drag_name):
                gat.remove_ingredient(drags[0].drag_name)
            else:
                gat.echec_ingr()
        return


screen ingred:
    text "{size=+10}{b}{color=#ffd700} oeuf : [gat.n_oeufs], farine : [gat.n_farine] , levure : [gat.n_levure], beurre : [gat.n_beurre], lait: [gat.n_lait], sucre : [gat.n_sucre]{/color}{/b}{/size}" xalign 0.1 yalign 0.9
    draggroup:

        # ingrédients.
        drag:
            drag_name "beurre"
            child "Beurre.png"
            droppable False
            dragged ing_dragged
            xpos 100 ypos 100
        drag:
            drag_name "oeufs"
            child "Ingrédients_oeufs.png"
            droppable False
            dragged ing_dragged
            xpos 300 ypos 100
        drag:
            drag_name "lait"
            child "Ingrédients_lait.png"
            droppable False
            dragged ing_dragged
            xpos 500 ypos 100
        drag:
            drag_name "levure"
            child "Ingrédients_levure.png"
            droppable False
            dragged ing_dragged
            xpos 700 ypos 100
        drag:
            drag_name "farine"
            child "Ingrédients_farine.png"
            droppable False
            dragged ing_dragged
            xpos 100 ypos 300
        drag:
            drag_name "sucre"
            child "Ingrédients_sucre.png"
            droppable False
            dragged ing_dragged
            xpos 300 ypos 300
        drag:
            drag_name "sirop_de_rose"
            child "Ingrédients_sirop_rose.png"
            droppable choix_sirop
            dragged ing_dragged
            xpos 500 ypos 300
        drag:
            drag_name "sirop_d'arsenic"
            idle_child "Ingrédients_sirop_rose.png"
            hover_child "Ingrédients_sirop_arsenic.png"
            droppable choix_sirop
            dragged ing_dragged
            xpos 700 ypos 300
        # Le gateau ou on dépose les ingrédients.
        drag:
            drag_name "pate_a_gateau"
            child "chaudron_2.png"
            draggable False
            xpos 1000 ypos 300

    imagebutton:
        idle "bouton_cuisson.png"
        hover "bouton_cuisson_hover.png"
        xalign 0.92
        yalign 0.80
        action If ((gat.ingredients == []), true = [Hide("ingred",transition=dissolve), Jump("cuire_gateau")], false = [Hide("ingred",transition=dissolve), Jump("echec_jeu_four")])

    imagebutton:
        idle "gateau_bulle_idle.png"
        hover "gateau_bulle_hover.png"
        xalign 0.92
        yalign 0.1
        action Jump("ingredients_gateau")


screen cuisinefour:
    image "chaudron.png":
        xalign 0.10
        yalign 0.7
    imagebutton:
        idle "bouton_cuisson.png"
        hover "bouton_cuisson_hover.png"
        xalign 0.7
        yalign 0.5
        action [Hide("cuisinefour",transition=dissolve),Jump("cuisson")]

screen marmite_cuisson:
    image "chaudron.png" at center
    image "flamme.png" at goutte_chaudron_cuisson

screen show_vars:
    text "Raté: [misses], Flammes: [hits]!" xalign 0.5
    image "flamme.png":
        pos (1000, 50)

transform pos_flamme:
    xalign 0.0
    yalign 0.06

screen le_feu_cuisson:
    text "{b}Allumez le feu!!!{/b} Touchez au moins 10 flammes" at truecenter
