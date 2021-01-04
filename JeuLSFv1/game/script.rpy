label start:
    show screen minimapShow

    label Didacticiel:
    label Blackscreen1:
    scene BlackScreen
    "Comme à votre habitude, vous vous baladez dans la forêt. Le soleil brille comme toujours, mais cette fois-ci, vous sentez une légère brise tout à fait différente..."

    label ArriveForetFees:
    $ minimap.append(ArriveForetFees)
    scene ISalle1 with slowDissolve
    #inclure des imagemap pour aller dans le gouffre ou dans la foret avec oliveau comme daprès le script
    label ClairiereDOliveauIntro:
    #Possibilité d’aller à différents endroits en vain.
    #Imagemap Oliveau vers label OliveauParle
    label OliveauLSF:
    #Inclure video de Oliveau qui parle en LSF (EAU) (voir FaceRig)
    "Qu’a-t-il dit?"
    menu:
        "Eau":
            jump TransitionNiveau3
        "Choix2":
            jump OliveauLSFL
        "Choix3":
            jump OliveauLSFL
        "Choix4":
            jump OliveauLSFL
    
    label TransitionNiveau3:
    "Vous avez passé la première épreuve de compréhension de la langue des signes, le jeu va donc s’adapter à votre niveau."
    menu:
        "Continuer":
            jump Niveau3
        "Annuler":
            jump OliveauLSFL

    label OliveauLSFL:
    #Inclure video de Oliveau E-A-U
        "Qu’a-t-il dit?"
    menu:
        "Eau":
            jump TransitionNiveau2
        "Choix2":
            jump OliveauSeau
        "Choix3":
            jump OliveauSeau
        "Choix4":
            jump OliveauSeau

    label TransitionNiveau2:
    "Vous avez passé la première épreuve de compréhension de la langue des signes, le jeu va donc s’adapter à votre niveau."
    menu:
        "Continuer":
            jump Niveau2
        "Annuler":
            jump OliveauSeau
    
    label OliveauSeau:
    #Oliveau te tend un sceau et te montre le lac, tu vas chercher de l’eau et tu passes niveau 1.
    #Obtention seau dans inventaire
    "Vous allez chercher de l'eau pour l'arbre qui avait de toute évidence très soif"
    label Niveau1:
    label ClairiereDOliveau:
    if avancement[2]=="null":
        $ minimap.append(ClairiereDOliveau)
        o "Quel est ton nom?"
        python:
            nom = renpy.input("Quel est ton nom?")
            nom = nom.strip() or "Anonyme"
        o "Bienvenue dans cette forêt pas tout à fait ordinaire [nom], Je me fait appeler Oliveau"
        #Video Oliveau O-L-I-V-E-A-U LSF "O-L-I-V-E-A-U; O-L-I-V-E-A-U O L I V E A U"
        python:
            dico.append(O)
            dico.append(L)
            dico.append(I)
            dico.append(V)
            dico.append(E)
            dico.append(A)
            dico.append(U)
        #Succes Oliveau debloque
        label Question1:
        menu:
            "Ok, cool. C’est un peu nul comme nom non? Ta mère ne manquait pas d’imagination...":
                jump Reponse11
            "Enchanté Oliveau! Dis-m’en plus sur cette forêt! Qu'a-t-elle de si spécial?":
                jump Reponse12
            "Bonjour.":
                jump Reponse13
    elif avancement[2]=="LieuDuVolComplete":
        o "Est-ce qu’il y a quelque chose que tu souhaites savoir?"
        menu:
            "Les fées existent vraiment?":
                jump Reponse21
            "Qui es-tu?":
                jump Reponse22
            "Comment rentrer chez moi?":
                jump Reponse23
            "Parmis les lettres que l’on m’a signées, il y en a une que j’ai mal comprise":
                jump Reponse24LSF
            "J’ai aidé la fée, elle m’a donné quelques lettres en échange, mais je n’en vois plus.. Comment puis-je aller plus loin dans la forêt?":
                jump Reponse26

    label AideOliveau:
    pp "J’ai aidé la fée, elle m’a donné quelques lettres en échange, mais je n’en vois plus.. Comment puis-je aller plus loin dans la forêt?"
    o "Les fées ne seront pas les seules à t’aider, trouve un autre être magique et il t’apprendra le vrai pouvoir de la langue des signes"
    label Reponse11:
    o "Eh bien non.. C’est un prénom plutôt commun dans le royaume des fées.. Tu devrais faire attention cela dit, ta gentillesse te sera rendue, qu’elle soit positive ou négative."
    jump Question2
    label Reponse12:
    o "C’est un plaisir de parler à quelqu’un de si agréable! Sache que pour ta gentillesse, tu seras récompensé dans la forêt des fées!"
    jump Question2
    label Reponse13:
    o "Tu souhaites peut-être en savoir plus sur ces lieux. Tu es ici dans la forêt des fées."
    jump Question2

    label Question2:
    o "Est-ce qu’il y a quelque chose que tu souhaites savoir?"
    menu:
        "Les fées existent vraiment?":
            jump Reponse21
        "Qui es-tu?":
            jump Reponse22
        "Comment rentrer chez moi?":
            jump Reponse23
        "Parmis les lettres que l’on m’a signées, il y en a une que j’ai mal comprise":
            jump Reponse24LSF
        "Merci pour tout Oliveau, je m’en vais de ce pas.":
            jump Reponse25
    
    label Reponse21:
    o "Oui, et elles sont aussi jolies que dans ton imagination. En revanche, elles ne parlent pas ta langue. Elles ne communiquent qu’en langue des signes française. Pour mieux les connaître, il te faut donc apprendre les bases de cette langue. Les arbres t’aideront."
    jump Question2
    label Reponse22:
    o "Je suis un serviteur de sa majesté la Reine des fées."
    jump Question2
    label Reponse23:
    o "Il te faut demander l’aide de la Reine des fées pour rentrer dans ton monde. Tu la trouveras facilement."
    pp "Où est-elle?"
    #Oliveau t'indique la direction
    o "Elle est dans le royaume des fées, prend ce chemin pour en atteindre la porte."
    $ avancement[0] = "ConnaisDirectionRoyaumeFees"
    jump Question2
    label Reponse24LSF:
    o "Laquelle?"
    python:
        lettre = renpy.input("Laquelle?")
        lettre = lettre.strip() or "?"
    $ i=0
    while i < (len(dico)):
        if lettre == dico[i].name:
            "Tu connais cette lettre"
            jump Question2
        $ i=i+1
    "Tu ne connais pas encore cette lettre, les fées t’en donneront d'autres en échange de ton aide."
    jump Question2
    label Reponse25:
    if avancement[0] == "ConnaisDirectionRoyaumeFees":
        jump PorteDuRoyaumeDesFees
    else:
        pp "Qu'est ce que je fais maintenant... Je ferais mieux de retourner parler à Oliveau pour en apprendre plus..."
        jump Question2
    label Reponse26:
    o "Les fées ne seront pas les seules à t’aider, trouve un autre être magique et il t’apprendra le vrai pouvoir de la langue des signes"
    jump DevantLeLac
    label PorteDuRoyaumeDesFees:
    "(LSF) Garde: Qui es-tu ? Tu n’es pas une fée, vas-t’en!"
    jump ClairiereDOliveau
    #(on garde les options de choix précédentes et on en ajoute  au fur et à mesure)
    #Si le joueur demande plus de 10 fois l’aide d’Oliveau: Enfant ignorant
    pp "On m’a renvoyé une fois à la porte, que faire? "
    o "Trouve une fée à aider, elle t’en sera reconnaissante et t’apprendras des signes"
    jump LieuDuVol
    label LieuDuVol:
    if avancement[1]=="ObjetRecupere":
        #la Fée donne une lettre de remerciement
        #Video de la fee qui fait les lettres CHWYZ
        python:
            dico.append(C)
            dico.append(H)
            dico.append(W)
            dico.append(Y)
            dico.append(Z)
            avancement[2]= "LieuDuVolComplete"
        jump ClairiereDOliveau
    else:
        $ minimap.append(LieuDuVol)
        #Fée: On m’a volé quelque chose... V-O-L
        #POURSUITE (mini-jeu)
        $ avancement[1]= "ObjetRecupere"
        jump LieuDuVol
    label DevantLeLac:
    #Un bateau est posé sur les rives du lac. En cliquant dessus on arrive sur une petite ile au milieu du lac avec un immense arbre dessus.
    #imagemap de bateau pour aller au nid de l'oiseau
    label NidDeLOiseau:
    label Q3:
    menu:
        "Caresser":
            jump R31
        "...":
            jump R32
        "Arracher une plume de l’oiseau":
            jump R33
        "Faire chanter l'Oiseau":
            jump R34
        "Bonjour":
            jump R35

    label R31:
    #Video Oiseau LSF:As-tu cru que j’étais animal primitif?
    jump Q3
    label R32:
    b "Oh tu n’es pas d’ici, je suis un oiseau. Mais pas un rouge-gorges ou un pigeon, non, un vrai oiseau."
    b "Et dans mon immense bonté je t’apprendrais à survivre, piètre mammifère, dans cette forêt."
    b "Refait ces gestes après moi, ils signifient D-O-Y et t’aideront à faire pousser les plantes."
    #Video Oiseau DOY
    #Du lierre pousse autour des branches des arbres
    python:
        dico.append(D)
        dico.append(Y)
    jump Sifflet
    label R33:
    #Video Oiseau LSF: Rend la moi!
    menu:
        "Rendre la plume à l'oiseau"
    b "Pour ta bonté, je vais t’apprendre un sort." 
    b "Refait ces gestes après moi, ils signifient D-O-Y et t’aideront à faire pousser les plantes."
    #Video Oiseau DOY
    #Du lierre pousse autour des branches des arbres
    python:
        dico.append(D)
        dico.append(Y)
    jump Sifflet
    label R34:
    
    jump Sifflet
    label R35:
    b "Dans mon immense bonté je t’apprendrais à survivre, piètre mammifère, dans cette forêt."
    b "Refait ces gestes après moi, ils signifient D-O-Y et t’aideront à faire pousser les plantes."
    #Video Oiseau DOY
    #Du lierre pousse autour des branches des arbres
    python:
        dico.append(D)
        dico.append(Y)
    jump Sifflet

    label Sifflet:
    b "Je ne peux pas encore t’apprendre d’autres sorts, ta connaissance en langue des signes est... Trop primitive."
    b "Appelle-moi avec ce sifflet"
    #Video Oiseau SIFFLET
    python:
        dico.append(S)
        dico.append(I)
        dico.append(F)
        dico.append(L)
        dico.append(T)
    b "Pour quand tu seras moins bête."
    python:
        inventaire.append(Sifflet)
    #Onglet magie débloqué
    #Peut repartir et doit avoir l’idée de faire pousser le lierre devant la falaise
    "pause"

    return
