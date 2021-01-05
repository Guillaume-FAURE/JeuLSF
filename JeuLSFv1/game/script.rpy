label start:
    show screen minimapShow
#############################################################################################################################
#############################################################################################################################    
    label Didacticiel:
    label Blackscreen1:
    scene BlackScreen
    "Comme à votre habitude, vous vous baladez dans la forêt. Le soleil brille comme toujours, mais cette fois-ci, vous sentez une légère brise tout à fait différente..."
#############################################################################################################################
    label ArriveForetFees:
    $ minimap.append(ArriveForetFees)
    scene ISalle1 with slowDissolve
    #inclure des imagemap pour aller dans le gouffre ou dans la foret avec oliveau comme daprès le script
#############################################################################################################################
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
#############################################################################################################################
#############################################################################################################################
    label Niveau1:
    label ClairiereDOliveau:
    if avancement[0]=="null":
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
        label Q1:
        menu:
            "Ok, cool. C’est un peu nul comme nom non? Ta mère ne manquait pas d’imagination...":
                jump R11
            "Enchanté Oliveau! Dis-m’en plus sur cette forêt! Qu'a-t-elle de si spécial?":
                jump R12
            "Bonjour.":
                jump R13
    elif avancement[0]=="LieuDuVolComplete":
        o "Est-ce qu’il y a quelque chose que tu souhaites savoir?"
        menu:
            "Les fées existent vraiment?":
                jump R21
            "Qui es-tu?":
                jump R22
            "Comment rentrer chez moi?":
                jump R23
            "Parmis les lettres que l’on m’a signées, il y en a une que j’ai mal comprise":
                jump R24
            "J’ai aidé la fée, elle m’a donné quelques lettres en échange, mais je n’en vois plus.. Comment puis-je aller plus loin dans la forêt?":
                jump R26

    elif avancement[0]== "RenvoyeParGarde":
        jump RenvoyeParGarde
    elif avancement[0]== "AVuLOiseau":
        jump AVuLoiseau
    elif avancement[0]== "FioleObtenu":
        jump FioleObtenu

    label R11:
    o "Eh bien non.. C’est un prénom plutôt commun dans le royaume des fées.. Tu devrais faire attention cela dit, ta gentillesse te sera rendue, qu’elle soit positive ou négative."
    jump Q2
    
    label R12:
    o "C’est un plaisir de parler à quelqu’un de si agréable! Sache que pour ta gentillesse, tu seras récompensé dans la forêt des fées!"
    jump Q2
    
    label R13:
    o "Tu souhaites peut-être en savoir plus sur ces lieux. Tu es ici dans la forêt des fées."
    jump Q2

    label Q2:
    o "Est-ce qu’il y a quelque chose que tu souhaites savoir?"
    menu:
        "Les fées existent vraiment?":
            jump R21
        "Qui es-tu?":
            jump R22
        "Comment rentrer chez moi?":
            jump R23
        "Parmis les lettres que l’on m’a signées, il y en a une que j’ai mal comprise":
            jump R24
        "Merci pour tout Oliveau, je m’en vais de ce pas.":
            jump R25
    
    label R21:
    o "Oui, et elles sont aussi jolies que dans ton imagination. En revanche, elles ne parlent pas ta langue. Elles ne communiquent qu’en langue des signes française. Pour mieux les connaître, il te faut donc apprendre les bases de cette langue. Les arbres t’aideront."
    jump Q2

    label R22:
    o "Je suis un serviteur de sa majesté la Reine des fées."
    jump Q2

    label R23:
    o "Il te faut demander l’aide de la Reine des fées pour rentrer dans ton monde. Tu la trouveras facilement."
    pp "Où est-elle?"
    #Oliveau t'indique la direction
    o "Elle est dans le royaume des fées, prend ce chemin pour en atteindre la porte."
    $ avancement[0] = "ConnaisDirectionRoyaumeFees"
    jump Q2

    label R24:
    o "Laquelle?"
    python:
        lettre = renpy.input("Laquelle?")
        lettre = lettre.strip() or "?"
    $ i=0
    while i < (len(dico)):
        if lettre == dico[i].name:
            "Tu connais cette lettre"
            jump Q2
        $ i=i+1
    "Tu ne connais pas encore cette lettre, les fées t’en donneront d'autres en échange de ton aide."
    jump Q2

    label R25:
    if avancement[0] == "ConnaisDirectionRoyaumeFees":
        jump PorteDuRoyaumeDesFees
    else:
        pp "Qu'est ce que je fais maintenant... Je ferais mieux de retourner parler à Oliveau pour en apprendre plus..."
        jump Q2

    label R26:
    o "Les fées ne seront pas les seules à t’aider, trouve un autre être magique et il t’apprendra le vrai pouvoir de la langue des signes"
    jump DevantLeLac

    label RenvoyeParGarde:
    #(on garde les options de choix précédentes et on en ajoute  au fur et à mesure)
    #Si le joueur demande plus de 10 fois l’aide d’Oliveau: Enfant ignorant
    pp "On m’a renvoyé une fois à la porte, que faire? "
    o "Trouve une fée à aider, elle t’en sera reconnaissante et t’apprendras des signes"
    jump LieuDuVol

    label AVuLOiseau:
    pp "Tous les chemins semblent à présent bloqués, je ne sais où aller?"
    o "Il me semble que l’Oiseau t’as montré quelques tours, pourquoi ne pas les utiliser?"
    jump Falaise

    label FioleObtenu:
    $ avancement[3]="PossibiliteApprendreKAME"
    pp "J’ai rencontré une fée alchimiste et j’ai récupéré une potion. Que faire maintenant?"
    o "Il me semble que l’oiseau use d’un objet particulier en cas de besoin. 
    o "Tu as appris de nouvelles lettres n’est-ce pas? Appelle-le donc!"
    #Utilisation du sifflet
#############################################################################################################################
    label PorteDuRoyaumeDesFees:
    "(LSF) Garde: Qui es-tu ? Tu n’es pas une fée, vas-t’en!"
    $ avancement[0]= "RenvoyeParGarde"
    jump ClairiereDOliveau
#############################################################################################################################
    label LieuDuVol:
    if avancement[1]=="null":
        $ minimap.append(LieuDuVol)
        #Fée: On m’a volé quelque chose... V-O-L
        #POURSUITE (mini-jeu)
        $ avancement[1]= "ObjetRecupere"
        jump LieuDuVol
    elif avancement[1]=="ObjetRecupere":
        #la Fée donne une lettre de remerciement
        #Video de la fee qui fait les lettres CHWYZ
        python:
            dico.append(C)
            dico.append(H)
            dico.append(W)
            dico.append(Y)
            dico.append(Z)
            avancement[0]= "LieuDuVolComplete"
        jump ClairiereDOliveau
#############################################################################################################################
    label DevantLeLac:
    #Un bateau est posé sur les rives du lac. En cliquant dessus on arrive sur une petite ile au milieu du lac avec un immense arbre dessus.
    #imagemap de bateau pour aller au nid de l'oiseau
#############################################################################################################################
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
        "Rendre la plume à l'oiseau":
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
    $ avancement[0]="AVuLOiseau"
    jump ClairiereDOliveau
    #############################################################################################################################
    label Falaise:
    #Utilisation de DOY pour faire pousser du lierre
    label DessusDeLaFalaise:
    if avancement[2]=="null":
        #Video Fee AIDE MOI
        pp "{k=4}.....{/k}"
        #Video Fee SOS
        #Fee indique un sac rempli de fiole
        #LE CHAUDRON ET LES FIOLES (mini-jeu)
        #La fée fait des lettres en langue des signes, il faut verser la fiole correspondante dans le chaudron 
        #Il reste deux fioles “N” et “M”, la fée pointe la fiole “M” et signe le M puis pointe la fiole “N” et signe le “N” 
        python:
            dico.append(M)
            dico.append(N)
        avancement[2]=="FioleObtenu"
        jump DessusDeLaFalaise
    elif avancement[2]=="FioleObtenu":
        $avancement[0]="FioleObtenu"
        menu:
            "Donner la fiole à la fée":#+2 points de gentillesse
                #Video Fee :Merci. Prends cette fiole. F-I-O-L-E
                jump ClairiereDOliveau 
            "Partir avec la fiole":#-3 points de gentillesse
                #Video Fee :NON! Rend-moi cette F-I-O-L-E!
                #Fee en larme
                jump ClairiereDOliveau

    label DansLesAirs:
        b "Vous avez appelé le phœnix des hôtes de ces bois? Me voilà, le magnifique, le superbe Oiseau! Que puis-je faire pour toi?"
    if avancement[3]=="null":
        b "Attends, tu oses m'appeler alors que ton ignorance est inchangée? Quel toupet!"
        jump ClairiereDOliveau
    elif avancement[3]=="PossibiliteApprendreKAME":
        jump PossibiliteApprendreKAME


    label PossibiliteApprendreKAME:
        menu:
            "Ah bah c’est pas trop tôt! Dépêche toi de m’apprendre un nouveau sort! J’ai pas tout mon temps.":#-2 points de gentillesse
                b "Je ne saurais me rabaisser au niveau d’un être inférieur tel que toi. Il nous faut à chacun rester à sa place. Pour faire simple, je vaut mieux que toi." 
                b "Cela dit je vais t’apprendre un sort. Il faut au lion protéger la souris, ainsi, noblesse oblige, je me dois de te protéger."
                jump ApprentissageKAME
            "Bien le bonjour grand Oiseau! J’ose me présenter devant vous dans l’espoir d’apprendre, peut-être, un nouveau sort"#-1 point de gentillesse
                b "Comme vous me flattez, vile créature. Il est facile pour toi d’admirer un être tel que moi, n’est-ce pas?"
                b "Je vais t’apprendre un nouveau sort afin de t’éclairer de ma perfection."

    "Fin de jeu"

    return
