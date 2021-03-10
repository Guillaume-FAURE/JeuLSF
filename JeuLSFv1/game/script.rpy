#Ce code s'exécute avec les autres fichiers du même dossier et avec le logiciel Ren'Py.

label start:
    show screen menuShow
#############################################################################################################################
#############################################################################################################################    
    label Didacticiel:  
    label Blackscreen1:
    show BlackScreen at sizeBackground
    "Comme à votre habitude, vous vous baladez dans la forêt. Le soleil brille comme toujours, mais cette fois-ci, vous sentez une légère brise tout à fait différente..."
    "pause"
    show rubis at inventaire
    show rubis at achievement
    "pause"
    label Perdu1:
    show Perdu1 at sizeBackground with slowDissolve
    #play music "audio/Mushishi.mp3"
    show screen Perdu1ToPerdu2
    jump WaitingScreen
    
    label Perdu2:
    scene Perdu2 at sizeBackground with slowDissolve
    show screen Perdu2ToPerdu3
    jump WaitingScreen
    
    label Perdu3:
    scene Perdu3 at sizeBackground with slowDissolve
    show screen Perdu3ToPerdu4
    jump WaitingScreen
    
    label Perdu4:
    scene Perdu4 at sizeBackground with slowDissolve
    show screen Perdu4ToArriveForetFees
    jump WaitingScreen
#############################################################################################################################
    label WaitingScreen:
        window hide
        $ renpy.pause(1.0)
        jump WaitingScreen
#############################################################################################################################
    label ArriveForetFees:
    scene ArriveForetFees at sizeBackground with slowDissolve

    $ minimap.append(ArriveForetFees)
    $ minimap.append(Gouffre)
    $ minimap.append(ArbreABonbons)
    $ minimap.append(FondDuGouffre)
    $ minimap.append(Bibliotheque)
    $ minimap.append(Labyrinthe)
    $ minimap.append(ClairiereDOliveau)
    $ minimap.append(Lac)
    $ minimap.append(Cuisine)
    $ minimap.append(NidDeLOiseau)
    $ minimap.append(PorteDuRoyaumeDesFees)
    $ minimap.append(LieuDuVol)
    $ minimap.append(PseudoLabyrinthe)
    $ minimap.append(FalaiseAvecLierre)
    $ minimap.append(PiegeDeLAlchimiste)
    show screen ArriveForetFeesToGouffre
    show screen ArriveForetFeesToClairiereDOliveau
    jump WaitingScreen
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
    $ minimap.append(ClairiereDOliveau)
    show screen oliveau
    if avancement[0] != "null" and avancement[0] != "Q2":
        show screen ClairiereDOliveauToPorteDuRoyaumeDesFees
    show screen ClairiereDOliveauToArriveForetFees
    show screen ClairiereDOliveauToLac
    show screen ClairiereDOliveauToLieuDuVol
    jump WaitingScreen

    label Oliveau:
    if avancement[0]=="null":
        jump IntroOliveau
    elif avancement[0]=="Q2":
        jump Q2
    elif avancement[0]=="LieuDuVolComplete":
        jump LieuDuVolComplete
    elif avancement[0]== "RenvoyeParGarde":
        jump RenvoyeParGarde
    elif avancement[0]== "AVuLOiseau":
        jump AVuLOiseau
    elif avancement[0]== "FioleObtenu":
        jump FioleObtenu
    elif avancement[0]== "ApprisSort":
        jump ApprisSort
    elif avancement[0]== "EnfantBonbon":
        jump EnfantBonbon
    elif avancement[0]== "ObtenuBouleDeCristal":
        jump ObtenuBouleDeCristal
    elif avancement[0]== "BesoinApprendreCompter":
        jump BesoinApprendreCompter    
    
    label IntroOliveau:
    hide screen ClairiereDOliveauToArriveForetFees
    hide screen ClairiereDOliveauToLac
    hide screen ClairiereDOliveauToLieuDuVol
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

    label R11:
    o "Eh bien non.. C’est un prénom plutôt commun dans le royaume des fées.. Tu devrais faire attention cela dit, ta gentillesse te sera rendue, qu’elle soit positive ou négative."
    $ avancement[0]="Q2"
    jump Q2
    
    label R12:
    o "C’est un plaisir de parler à quelqu’un de si agréable! Sache que pour ta gentillesse, tu seras récompensé dans la forêt des fées!"
    $ avancement[0]="Q2"
    jump Q2
    
    label R13:
    o "Tu souhaites peut-être en savoir plus sur ces lieux. Tu es ici dans la forêt des fées."
    $ avancement[0]="Q2"
    jump Q2

    label Q2:
    hide screen ClairiereDOliveauToArriveForetFees
    hide screen ClairiereDOliveauToLac
    hide screen ClairiereDOliveauToLieuDuVol
    o "Est-ce qu’il y a quelque chose d'autre que tu souhaites savoir?"
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
            jump ClairiereDOliveau
    
    label R21:
    o "Oui, et elles sont aussi jolies que dans ton imagination. En revanche, elles ne parlent pas ta langue. Elles ne communiquent qu’en langue des signes française. Pour mieux les connaître, il te faut donc apprendre les bases de cette langue. Les arbres t’aideront."
    jump ClairiereDOliveau

    label R22:
    o "Je suis un serviteur de sa majesté la Reine des fées."
    jump ClairiereDOliveau

    label R23:
    o "Il te faut demander l’aide de la Reine des fées pour rentrer dans ton monde. Tu la trouveras facilement."
    pp "Où est-elle?"
    #Oliveau t'indique la direction
    o "Elle est dans le royaume des fées, prend ce chemin pour en atteindre la porte."
    $ avancement[0] = "ConnaisDirectionRoyaumeFees"
    jump ClairiereDOliveau

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
    jump ClairiereDOliveau

    label RenvoyeParGarde:
    #(on garde les options de choix précédentes et on en ajoute  au fur et à mesure)
    #Si le joueur demande plus de 10 fois l’aide d’Oliveau: Enfant ignorant
    hide screen ClairiereDOliveauToArriveForetFees
    hide screen ClairiereDOliveauToLac
    hide screen ClairiereDOliveauToLieuDuVol
    hide screen ClairiereDOliveauToPorteDuRoyaumeDesFees
    o "Est-ce qu’il y a quelque chose que tu souhaites savoir?"
    menu:
        "Parmis les lettres que l’on m’a signées, il y en a une que j’ai mal comprise":
            jump R24
        "On m’a renvoyé une fois à la porte, que faire? ":
            o "Trouve une fée à aider, elle t’en sera reconnaissante et t’apprendras des signes"
    jump ClairiereDOliveau

    label LieuDuVolComplete:
    hide screen ClairiereDOliveauToArriveForetFees
    hide screen ClairiereDOliveauToLac
    hide screen ClairiereDOliveauToLieuDuVol
    hide screen ClairiereDOliveauToPorteDuRoyaumeDesFees
    o "Est-ce qu’il y a quelque chose que tu souhaites savoir?"
    menu:
        "Parmis les lettres que l’on m’a signées, il y en a une que j’ai mal comprise":
            jump R24
        "J’ai aidé la fée, elle m’a donné quelques lettres en échange, mais je n’en vois plus.. Comment puis-je aller plus loin dans la forêt?":
            o "Les fées ne seront pas les seules à t’aider, trouve un autre être magique et il t’apprendra le vrai pouvoir de la langue des signes"
    jump ClairiereDOliveau

    label FioleObtenu:
    hide screen ClairiereDOliveauToArriveForetFees
    hide screen ClairiereDOliveauToLac
    hide screen ClairiereDOliveauToLieuDuVol
    hide screen ClairiereDOliveauToPorteDuRoyaumeDesFees
    $ avancement[3]="PossibiliteApprendreKAME"
    o "Est-ce qu’il y a quelque chose que tu souhaites savoir?"
    menu:
        "Parmis les lettres que l’on m’a signées, il y en a une que j’ai mal comprise":
            jump R24
        "J’ai rencontré une fée alchimiste et j’ai récupéré une potion. Que faire maintenant?":
            o "Il me semble que l’oiseau use d’un objet particulier en cas de besoin."
            o "Tu as appris de nouvelles lettres n’est-ce pas? Appelle-le donc!"
    #Utilisation du sifflet
    jump ClairiereDOliveau

    label ApprisSort:
    hide screen ClairiereDOliveauToArriveForetFees
    hide screen ClairiereDOliveauToLac
    hide screen ClairiereDOliveauToLieuDuVol
    hide screen ClairiereDOliveauToPorteDuRoyaumeDesFees
    o "Est-ce qu’il y a quelque chose que tu souhaites savoir?"
    menu:
        "Parmis les lettres que l’on m’a signées, il y en a une que j’ai mal comprise":
            jump R24
        "Tous les chemins semblent à présent bloqués, je ne sais où aller?":
            o "Il me semble que l’Oiseau t’as montré quelques tours, pourquoi ne pas les utiliser?"
    jump ClairiereDOliveau

    label EnfantBonbon:
    hide screen ClairiereDOliveauToArriveForetFees
    hide screen ClairiereDOliveauToLac
    hide screen ClairiereDOliveauToPorteDuRoyaumeDesFees
    hide screen ClairiereDOliveauToLieuDuVol
    $ avancement[3]="PossibiliteApprendrePIF"
    o "Est-ce qu’il y a quelque chose que tu souhaites savoir?"
    menu:
        "Parmis les lettres que l’on m’a signées, il y en a une que j’ai mal comprise":
            jump R24
        "J’ai rencontré un enfant fée et j’ai récupéré des sucreries. Que faire maintenant?":
            o "Il me semble que l’oiseau use d’un objet particulier en cas de besoin. Tu as appris de nouvelles lettres n’est-ce pas? Appelle-le donc!"
    #Utilisation du sifflet
    jump ClairiereDOliveau

    label ObtenuBouleDeCristal:
    hide screen ClairiereDOliveauToArriveForetFees
    hide screen ClairiereDOliveauToLac
    hide screen ClairiereDOliveauToLieuDuVol
    hide screen ClairiereDOliveauToPorteDuRoyaumeDesFees
    $ avancement[3]="PossibiliteApprendreJUNQ"
    o "Est-ce qu’il y a quelque chose que tu souhaites savoir?"
    menu:
        "Parmis les lettres que l’on m’a signées, il y en a une que j’ai mal comprise":
            jump R24
        "J’ai rencontré la fée bibliothécaire et j’ai récupéré une boule de cristal. Que faire maintenant?":
            o "Il me semble que l’oiseau use d’un objet particulier en cas de besoin. Tu as appris de nouvelles lettres n’est-ce pas? Appelle-le donc!"
    #Utilisation du sifflet
    jump ClairiereDOliveau

    label BesoinApprendreCompter:
    hide screen ClairiereDOliveauToArriveForetFees
    hide screen ClairiereDOliveauToLac
    hide screen ClairiereDOliveauToLieuDuVol
    hide screen ClairiereDOliveauToPorteDuRoyaumeDesFees
    o "Est-ce qu’il y a quelque chose que tu souhaites savoir?"
    menu:
        "Parmis les lettres que l’on m’a signées, il y en a une que j’ai mal comprise":
            jump R24
        "Peux-tu m’apprendre à compter?":
            #incrustation video chiffre
            python:
                dico.append(Zero)
                dico.append(Un)
                dico.append(Deux)
                dico.append(Trois)
                dico.append(Quatre)
                dico.append(Cinq)
                dico.append(Six)
                dico.append(Sept)
                dico.append(Huit)
                dico.append(Neuf)
            o "Y a-t-il un chiffre que tu n’as pas compris?"
            python:
                chiffre = renpy.input("Laquelle?")
                chiffre = chiffre.strip() or "?"
            $ i=0
            while i < (len(dico)):
                if lettre == dico[i].name:
                    #oliveau refait le chiffre
                    jump PlanDeTravail
    jump ClairiereDOliveau
    
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
        show screen LieuDuVolToClairiereDOliveau
        show screen LieuDuVolToPseudoLabyrinthe
        show screen LieuDuVolToFalaiseAvecLierre
        jump WaitingScreen
#############################################################################################################################
    label Lac:
    show screen LacToClairiereDOliveau
    show screen LacToNidDeLOiseau
    jump WaitingScreen
    #Un bateau est posé sur les rives du lac. En cliquant dessus on arrive sur une petite ile au milieu du lac avec un immense arbre dessus.
    #imagemap de bateau pour aller au nid de l'oiseau
#############################################################################################################################
    label NidDeLOiseau:
    show screen NidDeLOiseauToLac
    show screen bird
    jump WaitingScreen
    label Bird:
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
    jump Bird
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
    $ avancement[0]="ApprisSort"
    jump NidDeLOiseau
#############################################################################################################################
    label Falaise:
    show screen FalaiseAvecLierreToPiegeDeLAlchimiste
    show screen FalaiseAvecLierreToLieuDuVol
    jump WaitingScreen
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
        $ avancement[2]="FioleObtenu"
        jump DessusDeLaFalaise
    elif avancement[2]=="FioleObtenu":
        $ avancement[0]="FioleObtenu"
        menu:
            "Donner la fiole à la fée":
                $ gentillesse += 2
                #Video Fee :Merci. Prends cette fiole. F-I-O-L-E
                jump Falaise
            "Partir avec la fiole":
                $ gentillesse -= 3
                #Video Fee :NON! Rend-moi cette F-I-O-L-E!
                #Fee en larme
                jump Falaise
#############################################################################################################################
    label DansLesAirs:
        b "Vous avez appelé le phœnix des hôtes de ces bois? Me voilà, le magnifique, le superbe Oiseau! Que puis-je faire pour toi?"
    if avancement[3]=="null":
        b "Attends, tu oses m'appeler alors que ton ignorance est inchangée? Quel toupet!"
        jump ClairiereDOliveau
    elif avancement[3]=="PossibiliteApprendreKAME":
        jump PossibiliteApprendreKAME
    elif avancement[3]=="PossibiliteApprendrePIF":
        jump PossibiliteApprendrePIF
    elif avancement[3]=="PossibiliteApprendreJUNQ":
        jump PossibiliteApprendreJUNQ
    elif avancement[3]=="PossibiliteApprendreGREX":
        jump PossibiliteApprendreGREX


    label PossibiliteApprendreKAME:
        menu:
            "Ah bah c’est pas trop tôt! Dépêche toi de m’apprendre un nouveau sort! J’ai pas tout mon temps.":
                $ gentillesse -= 2
                b "Je ne saurais me rabaisser au niveau d’un être inférieur tel que toi. Il nous faut à chacun rester à sa place. Pour faire simple, je vaut mieux que toi." 
                b "Cela dit je vais t’apprendre un sort. Il faut au lion protéger la souris, ainsi, noblesse oblige, je me dois de te protéger."
                jump ApprentissageKAME
            "Bien le bonjour grand Oiseau! J’ose me présenter devant vous dans l’espoir d’apprendre, peut-être, un nouveau sort":
                $ gentillesse -= 1
                b "Comme vous me flattez, vile créature. Il est facile pour toi d’admirer un être tel que moi, n’est-ce pas?"
                b "Je vais t’apprendre un nouveau sort afin de t’éclairer de ma perfection."
                jump ApprentissageKAME
            "Bonjour Oiseau! Je t’appelle pour apprendre un nouveau sort!":
                b "Bonjour, humain. Je te pense capable de comprendre une infime partie de mon intellect, je vais donc t’enseigner un nouveau sort."
                jump ApprentissageKAME
    
    label ApprentissageKAME:
    b "Le sort que je vais t’apprendre se dit KAME"
    #Video de l'oiseau signant KAME
    python:
        dico.append(K)
    #L'oiseau vole sans battre des ailes
    b "Ce sort, comme tu le vois, permet de voler. Il ne m’est évidemment d’aucune utilité, mais il me semble qu’une espèce comme la tienne en aurait plus que besoin. Bon courage, humain."
    #L'oiseau part
    $ magie.append(KAME)
    "Tu peux désormais voler dans la forêt, cela te permettra de te déplacer plus facilement sur la carte."
    #Possibilité de se téléporter
    $ avancement[0]="ApprisSort"

    label PossibiliteApprendrePIF:
    b "Le sort que je vais t’apprendre se dit PIF" #oiseau signe PIF
    #l'oiseau casse le rocher
    b "Ce sort, comme tu le vois, permet de casser ce que l’on souhaite. C’est de lui que la plupart des fées tirent leur force."
    b "Pas moi, évidemment.Tu devrais en avoir besoin bientôt. Bon courage, humain."
    #l'oiseau part
    $ magie.append(PIF)
    $ avancement[0]= "ApprisSort"
    jump ClairiereDOliveau

    label PossibiliteApprendreJUNQ:
    b "Le sort que je vais t’apprendre se dit JUNQ"
    $ dico.append(J)
    b " Ce sort, comme tu le vois, permet de respirer dans l’eau." 
    b "Il te servira à traverser de longues étendues d’eau ou bien à aller chercher les trésors des fonds marins."
    b "Enfin, ceux dont je n’ai pas voulu. Bon courage, humain."
    $ magie.append(JUNQ)
    $ avancement[0]= "ApprisSort"
    jump Lac
    
    label PossibiliteApprendreGREX:
    b "Le sort que je vais t'apprendre se dit GREX"
    $ dico.append(X)
    b "Ce sort, comme tu le vois, permet de creuser. Il te servira à retrouver des animaux de ton ordre comme les mulots et autres taupes." 
    b "Il y a sûrement des galeries que tu aimeras explorer là-bas. Bon courage, humain."
    $ magie.append(GREX)
    $ avancement[0]= "ApprisSort"
    jump Labyrinthe
#############################################################################################################################
    label Gouffre:
    scene Gouffre at sizeBackground with slowDissolve
    show screen GouffreToArbreABonbons
    show screen GouffreToArriveForetFees
    show screen GouffreToFondDuGouffre
    #Possibilite d'utiliser KAME.
    "On est dans un gouffre"
    "Vous avez traversé le gouffre en volant"
    jump WaitingScreen
#############################################################################################################################
    label ArbreABonbons:
    $ minimap.append(ArbreABonbons)
    
    if avancement[4]=="null":
        jump EnfantQuiPleure
    elif avancement[4]=="ObtenuBonbons":
        jump ObtenuBonbons
    
    label EnfantQuiPleure:
    #un enfant qui pleure
    menu:
        "Que se passe t-il jeune fée ?":
            $ gentillesse += 1
            jump bonbon
        "Hey, viens, ne pleure pas, fais moi plutôt un câlin, shhh, tout va bien. Raconte-moi tes tourments.": 
            $ gentillesse += 3
            jump bonbon
        "Rooh, même les enfants-fées pleurent tout le temps?":
            jump bonbon
    label bonbon:
    #enfant dit bonbon en LSF
    pp "..."
    #enfant dit B-O-N-B-O-N
    $ dico.append(B)
    #L’enfant pointe le doigt vers l’arbre et tend un sac de bonbons vides
    #Le joueur peut monter dans l’arbre
    jump MinijeuBonbons

    label ObtenuBonbons:
    menu:
        "Rendre les bonbons":
            $ gentillesse += 3
            $inventaire.append(Sucette)
            #enfant dit merci
            jump ClairiereDOliveau
        "Garder les bonbons":
            $ gentillesse -= 1
            #enfant pleure
            jump ClairiereDOliveau

    label MinijeuBonbons:
    #retrouver bonbons dans l'arbre
    $ avancement[4]="ObtenuBonbons"
    jump ArbreABonbons
############################################################################################################################
    label FondDuGouffre:
    scene FondDuGouffre at sizeBackground with slowDissolve
    show screen FondDuGouffreToGouffre
    show screen FondDuGouffreToBibliotheque
    show screen FondDuGouffreToLabyrinthe
    jump WaitingScreen
    #Utilisation du sort PIF, porte se découvre
############################################################################################################################
    label Bibliotheque:
    $ minimap.append(Bibliotheque)
    show screen BibliothequeToFondDuGouffre
    if avancement[5]=="null":
        #Une fée bibliothécaire qui semble avoir des milliers d’années est assise derrière un immense bureau dans la bibliothèque
        #Le bibliothécaire tend un bout de papier avec trois références bibliographiques dessus et indique la bibliothèque
        #Si le joueur reparle au bibliothécaire: -A-M-È-N-E s’il te plait
        jump MinijeuBibliotheque
    elif avancement[5]=="ObtenuReference":
        jump ObtenuReference
    
    label MinijeuBibliotheque:
    #Les étagères sont remplies de boules de cristal 
    #Les références sont composées de 3 lettres chacune. 
    #Chaque boule fait 3 lettres (il y en a autant que possible, rangées dans l’ordre alphabétique). 
    
    label ObtenuReference:
    #Le joueur doit retrouver les trois boules correspondant à ses références et les ramène au bibliothécaire pour les valider.
    #Bibliothécaire: Merci, B-I-B-L-I-O-T-H-È-Q-U-E
    $ dico.append(T)
    $ dico.append(Q)
    $ avancement[0]="ObtenuBouleDeCristal"
    menu:
        "Lui rendre ses livres": 
            $ gentillesse += 1
            $ inventaire.append(BouleDeCristal)
        "Partir avec ses livres": 
            $ gentillesse -= 1
            "Vous avez fait tomber 2 boules de cristal dans la précipitation"
    jump WaitingScreen
#############################################################################################################################
    label SurLac:
    show screen LacToCuisine
    #Utilisation JUNQ
    jump FondDuLac
#############################################################################################################################
    label FondDuLac:
    #on trouve une porte sculptée dans le corail.
    jump Cuisine
#############################################################################################################################
    label Cuisine:
    #Cuisinière: 2 tomates
    #Le joueur peut donner les tomates à la cuisinière (en choisissant le nombre)
    #Cuisinière: 12 carottes
    #Le joueur peut donner les carottes à la cuisinière (en choisissant le nombre)
    #Cuisinière: 10 asperges
    #Le joueur peut donner les asperges à la cuisinière (en choisissant le nombre)
    #Cuisinière: 16 poivrons
    #Le joueur peut donner les poivrons à la cuisinière (en choisissant le nombre)

    #Si le joueur rate, à quelconque moment:
     #   La fée fait non de la tête.
    #Une photo d’Oliveau est affichée au fond de la cuisine, la fée le désigne 
    #Cuisinière: O-L-I-V-E-A-U
    #Si le joueur réussit le tout: on lance le mini-jeu
    $ avancement[0]="BesoinApprendreCompter"
    jump ClairiereDOliveau
#############################################################################################################################
    label PlanDeTravail:
    #mini-jeu
    #Cuisinière: (pointe le joueur du doigt) G-A-T-E-A-U
    $ dico.append(G)
    #le joueur repart avec une part de gateau
    $ avancement[3]="PossibiliteApprendreGREX"
#############################################################################################################################
    label Labyrinthe:

    "Fin de jeu"

    return
