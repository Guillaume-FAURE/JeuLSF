init python:
    dico_panneau ={"1":"panneau_1.png","2":"panneau_2.png","3":"panneau_3.png","4":"panneau_4.png",
    "5":"panneau_5.png","6":"panneau_6.png","7":"panneau_7.png","8":"panneau_8.png",
    "9":"panneau_9.png","A":"panneau_A.png","B":"panneau_B.png", "C":"panneau_C.png",
    "D":"panneau_D.png","E":"panneau_E.png","F":"panneau_F.png","G":"panneau_G.png",
    "H":"panneau_H.png","I":"panneau_I.png","J":"panneau_J.png","K":"panneau_K.png",
    "L":"panneau_L.png","M":"panneau_M.png","N":"panneau_N.png","O":"panneau_O.png",
    "P":"panneau_P.png","Q":"panneau_Q.png","R":"panneau_R.png","S":"panneau_S.png",
    "T":"panneau_T.png","U":"panneau_U.png","V":"panneau_V.png","W":"panneau_W.png",
    "X":"panneau_X.png","Y":"panneau_Y.png","Z":"panneau_Z.png"}
    Choix_laby = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N",
    "O","P","Q","R","S","T","U","V","W","X","Y","Z"]

screen carrefour_deux:
    imagebutton:        #aller a gauche
        idle "fleche_laby_g.png"
        hover "fleche_laby_hover_g.png"
        xalign 0.2 yalign 0.27
        action [Hide("carrefour_deux",transition=dissolve), If((chem_laby.n_laby == 1), true = [Jump("transition_lab")], false = [Jump("echec_lab")])]
    imagebutton:        #aller a droite
        idle "fleche_laby.png"
        hover "fleche_laby_hover.png"
        xalign 0.7 yalign 0.3
        action [Hide("carrefour_deux",transition=dissolve), If((chem_laby.n_laby == 2), true = [Jump("transition_lab")], false = [Jump("echec_lab")])]

    add dico_panneau[Choix_laby[chem_laby.a_laby]] xalign 0.2 yalign 0.8              # Panneau à gauche
    add dico_panneau[Choix_laby[chem_laby.b_laby]] xalign 0.75 yalign 0.8              # Panneau à droite

    imagebutton:                        # Fantome LSF
        idle "Boule_fantome.png"
        hover "Boule_fantome_hover.png"
        xalign 0.9 yalign 0.9
        action [Jump("video_fantome_deux")]

    imagebutton:                        # Taupe
        idle "taupe_01.png"
        hovered [Show("taupe_sort")]
        unhovered [Hide("taupe_sort")]
        xalign 0.5 yalign 1.0
        action [Hide("taupe_sort"),Hide("carrefour_deux",transition=dissolve), Jump("labyrinthe_minijeu")]


screen carrefour_trois:
    imagebutton:        #aller a gauche
        idle "fleche_laby_g.png"
        hover "fleche_laby_hover_g.png"
        xalign 0.2 yalign 0.3
        action [Hide("carrefour_deux",transition=dissolve), If((chem_laby.n_laby == 1), true = [Jump("transition_lab")], false = [Jump("echec_lab")])]
    imagebutton:        #aller au milieu
        idle "fleche_laby_m.png"
        hover "fleche_laby_hover_m.png"
        xalign 0.5 yalign 0.1
        action [Hide("carrefour_deux",transition=dissolve), If((chem_laby.n_laby == 2), true = [Jump("transition_lab")], false = [Jump("echec_lab")])]
    imagebutton:        #aller a droite
        idle "fleche_laby.png"
        hover "fleche_laby_hover.png"
        xalign 0.8 yalign 0.3
        action [Hide("carrefour_deux",transition=dissolve), If((chem_laby.n_laby == 3), true = [Jump("transition_lab")], false = [Jump("echec_lab")])]

    add dico_panneau[Choix_laby[chem_laby.a_laby]] xalign 0.2 yalign 0.8              # Panneau à gauche
    add dico_panneau[Choix_laby[chem_laby.b_laby]] xalign 0.5 yalign 0.7              # Panneau au milieu
    add dico_panneau[Choix_laby[chem_laby.c_laby]] xalign 0.8 yalign 0.8              # Panneau à droite

    imagebutton:                        # Fantome LSF
        idle "Boule_fantome.png"
        hover "Boule_fantome_hover.png"
        xalign 0.9 yalign 0.9
        action [Jump("video_fantome_trois")]

    imagebutton:                        # Taupe
        idle "taupe_01.png"
        hovered [Show("taupe_sort")]
        unhovered [Hide("taupe_sort")]
        xalign 0.5 yalign 1.0
        action [Hide("taupe_sort"),Hide("carrefour_trois",transition=dissolve), Jump("labyrinthe_minijeu")]

screen porte_gallerie:
    imagebutton:                    #passer la porte
        idle "fleche_laby_m.png"
        hover "fleche_laby_hover_m.png"
        xalign 0.4 yalign 0.5
        action [Jump("entrer_code_laby")]

    imagebutton:                        # Fantome LSF
        idle "Boule_fantome.png"
        hover "Boule_fantome_hover.png"
        xalign 0.7 yalign 0.9
        action [Jump("video_fantome_porte")]

    imagebutton:                        # Taupe
        idle "taupe_01.png"
        hovered [Show("taupe_sort")]
        unhovered [Hide("taupe_sort")]
        xalign 0.5 yalign 1.0
        action [Hide("taupe_sort"),Hide("porte_gallerie",transition=dissolve), Jump("labyrinthe_minijeu")]

image taupe_sorti:
    "taupe_01.png"
    xalign 0.5 yalign 1.0
    pause 0.3
    "taupe_02.png"
    xalign 0.5 yalign 1.0
    pause 0.3
    "taupe_03.png"
    xalign 0.5 yalign 1.0
    pause 0.3
    "taupe_04.png"
    xalign 0.5 yalign 1.0
    pause 1.0

screen taupe_sort:

    add "taupe_sorti"
screen taupe_lab:

    imagebutton:                        # Taupe
        idle "taupe_01.png"
        hovered [Show("taupe_sort")]
        unhovered [Hide("taupe_sort")]
        xalign 0.5 yalign 1.0
        action [Hide("taupe_sort"),Hide("taupe_lab",transition=dissolve), Jump("labyrinthe_minijeu")]
