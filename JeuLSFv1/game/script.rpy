#Ce code s'exécute avec les autres fichiers du même dossier et avec le logiciel Ren'Py.

label start:
    show screen menuShow
#############################################################################################################################
#############################################################################################################################    
    label Didacticiel:  
    label Blackscreen1:
    show BlackScreen at sizeBackground
    jump OliveauSeau
    label LieuDeDepart:
    show LieuDeDepart at sizeBackground with slowDissolve
    play music "<loop 0.0>/audio/ForetBruitOiseau.mp3"
    "Comme à votre habitude, vous vous baladez dans la forêt. Le soleil brille comme toujours, mais cette fois-ci, vous sentez une légère brise tout à fait différente..."
    label Perdu1:
    show Perdu1 at sizeBackground with slowDissolve
    "Pour passer les dialogues, cliquez sur l'écran ou appuyer sur entrée."
    "Vous pouvez vous déplacer grâce aux liens sur l'écran"
    "Pour le bon fonctionnement du jeu, lorsqu'une vidéo se met en route, ne cliquez pas."
    show screen Perdu1ToPerdu2 with slowDissolve
    jump WaitingScreen

    label Perdu2:
    scene Perdu2 at sizeBackground with slowDissolve
    show screen Perdu2ToPerdu3 with slowDissolve
    jump WaitingScreen
    
    label Perdu3:
    scene Perdu3 at sizeBackground with slowDissolve
    show screen Perdu3ToPerdu4 with slowDissolve
    jump WaitingScreen
    
    label Perdu4:
    scene Perdu4 at sizeBackground with slowDissolve
    show screen Perdu4ToArriveForetFees with slowDissolve
    jump WaitingScreen
#############################################################################################################################
    label WaitingScreen:
        window hide
        $ renpy.pause(1.0)
        jump WaitingScreen
#############################################################################################################################
    label ArriveForetFees:
    #IntroLabel
    $ minimap.append(ArriveForetFees)
    scene ArriveForetFees at sizeBackground with slowDissolve
    show screen ArriveForetFeesLink with slowDissolve
    jump WaitingScreen
    #
#############################################################################################################################
    label ClairiereDOliveauIntro:
    label OliveauLSF:
    scene ClairiereDOliveau at sizeBackground with slowDissolve
    $ renpy.movie_cutscene("Videos/oliveau_eau.webm")
    "Qu’a-t-il dit?"
    menu:
        "Eau":
            jump TransitionNiveau3
        "Aidez-moi":
            jump OliveauLSFL
        "Manger":
            jump OliveauLSFL
        "Bonjour":
            jump OliveauLSFL
    
    label TransitionNiveau3:
    "Vous avez passé la première épreuve de compréhension de la langue des signes, le jeu va donc s’adapter à votre niveau."
    menu:
        "Continuer":
            jump Niveau3
        "Annuler":
            jump OliveauLSFL

    label OliveauLSFL:
    $ renpy.movie_cutscene("Videos/oliveau_eau_LSF.webm")
    "Qu’a-t-il dit?"
    menu:
        "Bonjour":
            jump TransitionNiveau2
        "Aidez-moi":
            jump OliveauSeau
        "Eau":
            jump OliveauSeau
        "Manger":
            jump OliveauSeau

    label TransitionNiveau2:
    "Vous avez passé la première épreuve de compréhension de la langue des signes, le jeu va donc s’adapter à votre niveau."
    menu:
        "Continuer":
            jump Niveau2
        "Annuler":
            jump OliveauSeau
    
    label OliveauSeau:
    $ inventaire.append(seau)
    show seau at Tinventaire onlayer overlay
    "Vous allez chercher de l'eau pour l'arbre qui avait de toute évidence très soif"
    $ avancement[0]="niveau1"
    jump Niveau1
#############################################################################################################################
#############################################################################################################################
    label Niveau1:
    label ClairiereDOliveau:
    #IntroLabel
    if avancement[0]=="null":
        jump ClairiereDOliveauIntro
    stop music
    play music "<loop 0.0>/audio/Oliveau.mp3"
    $ minimap.append(ClairiereDOliveau)
    scene ClairiereDOliveau at sizeBackground with slowDissolve
    show screen ClairiereDOliveauLink with slowDissolve
    jump WaitingScreen
    #

    label Oliveau:
    stop music
    play music "<loop 0.0>/audio/Cuisine.mp3"
    $ achEnfantIgnorant += 1
    if achEnfantIgnorant==10:
        show achEnfantIgnorant at Tachievement onlayer overlay
        $ achievements.append(Secret_EnfantIgnorant)
        $ achEnfantIgnorant +=1
    if avancement[0]=="niveau1":
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
    elif avancement[0]== "SaitCompter"
    
    label IntroOliveau:
    o "Quel est ton nom?"
    python:
        nom = renpy.input("Quel est ton nom?")
        nom = nom.strip() or "Anonyme"
    o "Bienvenue dans cette forêt pas tout à fait ordinaire [nom], Je me fait appeler Oliveau"
    $ renpy.movie_cutscene("Videos/oliveau_oliveau_LSF.webm")
    stop music
    play music "<loop 0.0>/audio/Oliveau.mp3"
    if achOLIVEAU==0:
        show achOLIVEAU at Tachievement onlayer overlay
        $ achievements.append(Lettre_OLIVEAU)
        $ achOLIVEAU +=1
    python:
        dico.append(O)
        dico.append(L)
        dico.append(I)
        dico.append(V)
        dico.append(E)
        dico.append(A)
        dico.append(U)
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
    o "Elle est dans le royaume des fées, prend ce chemin pour en atteindre la porte."
    $ avancement[0] = "ConnaisDirectionRoyaumeFees"
    show LinkHoverE at indication
    jump ClairiereDOliveau
   
    label R24:
    python:
        lettre = renpy.input("Laquelle?")
        lettre = lettre.strip() or "?"
    $ i=0
    while i < (len(dico)):
        if lettre == dico[i].name:
            o "Tu connais cette lettre"
            jump Q2
        $ i=i+1
    o "Tu ne connais pas encore cette lettre, les fées t’en donneront d'autres en échange de ton aide."
    jump ClairiereDOliveau

    label RenvoyeParGarde:
    o "Est-ce qu’il y a quelque chose que tu souhaites savoir?"
    menu:
        "Parmis les lettres que l’on m’a signées, il y en a une que j’ai mal comprise":
            jump R24
        "On m’a renvoyé une fois à la porte, que faire? ":
            o "Trouve une fée à aider, elle t’en sera reconnaissante et t’apprendras des signes"
    jump ClairiereDOliveau

    label LieuDuVolComplete:
    o "Est-ce qu’il y a quelque chose que tu souhaites savoir?"
    menu:
        "Parmis les lettres que l’on m’a signées, il y en a une que j’ai mal comprise":
            jump R24
        "J’ai aidé la fée, elle m’a donné quelques lettres en échange, mais je n’en vois plus.. Comment puis-je aller plus loin dans la forêt?":
            o "Les fées ne seront pas les seules à t’aider, trouve un autre être magique et il t’apprendra le vrai pouvoir de la langue des signes"
    jump ClairiereDOliveau

    label FioleObtenu:
    $ avancement[3]="PossibiliteApprendreKAME"
    o "Est-ce qu’il y a quelque chose que tu souhaites savoir?"
    menu:
        "Parmis les lettres que l’on m’a signées, il y en a une que j’ai mal comprise":
            jump R24
        "J’ai rencontré une fée alchimiste et j’ai récupéré une potion. Que faire maintenant?":
            o "Il me semble que l’oiseau use d’un objet particulier en cas de besoin."
            o "Tu as appris de nouvelles lettres n’est-ce pas? Appelle-le donc!"
    show sifflet at Tinventaire
    jump ClairiereDOliveau

    label ApprisSort:
    o "Est-ce qu’il y a quelque chose que tu souhaites savoir?"
    menu:
        "Parmis les lettres que l’on m’a signées, il y en a une que j’ai mal comprise":
            jump R24
        "Tous les chemins semblent à présent bloqués, je ne sais où aller?":
            o "Il me semble que l’Oiseau t’as montré quelques tours, pourquoi ne pas les utiliser?"
    jump ClairiereDOliveau

    label EnfantBonbon:
    $ avancement[3]="PossibiliteApprendrePIF"
    o "Est-ce qu’il y a quelque chose que tu souhaites savoir?"
    menu:
        "Parmis les lettres que l’on m’a signées, il y en a une que j’ai mal comprise":
            jump R24
        "J’ai rencontré un enfant fée et j’ai récupéré des sucreries. Que faire maintenant?":
            o "Il me semble que l’oiseau use d’un objet particulier en cas de besoin. Tu as appris de nouvelles lettres n’est-ce pas? Appelle-le donc!"
    show sifflet at Tinventaire
    jump ClairiereDOliveau

    label ObtenuBouleDeCristal:
    $ avancement[3]="PossibiliteApprendreJUNQ"
    o "Est-ce qu’il y a quelque chose que tu souhaites savoir?"
    menu:
        "Parmis les lettres que l’on m’a signées, il y en a une que j’ai mal comprise":
            jump R24
        "J’ai rencontré la fée bibliothécaire et j’ai récupéré une boule de cristal. Que faire maintenant?":
            o "Il me semble que l’oiseau use d’un objet particulier en cas de besoin. Tu as appris de nouvelles lettres n’est-ce pas? Appelle-le donc!"
    show sifflet at Tinventaire
    jump ClairiereDOliveau

    label BesoinApprendreCompter:
    o "Est-ce qu’il y a quelque chose que tu souhaites savoir?"
    menu:
        "Parmis les lettres que l’on m’a signées, il y en a une que j’ai mal comprise":
            jump R24
        "Peux-tu m’apprendre à compter?":
            $ renpy.movie_cutscene("Videos/oliveau_1_LSF.webm")
            $ renpy.movie_cutscene("Videos/oliveau_2_LSF.webm")
            $ renpy.movie_cutscene("Videos/oliveau_3_LSF.webm")
            $ renpy.movie_cutscene("Videos/oliveau_4_LSF.webm")
            $ renpy.movie_cutscene("Videos/oliveau_5_LSF.webm")
            $ renpy.movie_cutscene("Videos/oliveau_6_LSF.webm")
            $ renpy.movie_cutscene("Videos/oliveau_7_LSF.webm")
            $ renpy.movie_cutscene("Videos/oliveau_8_LSF.webm")
            $ renpy.movie_cutscene("Videos/oliveau_9_LSF.webm")
            $ renpy.movie_cutscene("Videos/oliveau_10_LSF.webm")
            $ renpy.movie_cutscene("Videos/oliveau_11_LSF.webm")
            $ renpy.movie_cutscene("Videos/oliveau_12_LSF.webm")
            $ renpy.movie_cutscene("Videos/oliveau_13_LSF.webm")
            $ renpy.movie_cutscene("Videos/oliveau_14_LSF.webm")
            $ renpy.movie_cutscene("Videos/oliveau_15_LSF.webm")
            $ renpy.movie_cutscene("Videos/oliveau_16_LSF.webm")
            $ renpy.movie_cutscene("Videos/oliveau_17_LSF.webm")
            $ renpy.movie_cutscene("Videos/oliveau_18_LSF.webm")
            $ renpy.movie_cutscene("Videos/oliveau_19_LSF.webm")
            $ renpy.movie_cutscene("Videos/oliveau_20_LSF.webm")
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
                dico.append(Dix)
                dico.append(Onze)
                dico.append(Douze)
                dico.append(Treize)
                dico.append(Quatorze)
                dico.append(Quinze)
                dico.append(Seize)
                dico.append(DixSept)
                dico.append(DixHuit)
                dico.append(DixNeuf)
                dico.append(Vingt)
            if achCompter==0:
                show achCompter at Tachievement onlayer overlay
                $ achievements.append(Histoire_Compter)
                $ achCompter +=1
            $ avancement[0]="SaitCompter"
            jump Oliveau
    
    label SaitCompter:
    o "Tu as besoin de quelque chose ?"
    menu:
        "Parmi les lettres et les chiffres que l'on m'a signée il y en a uns que j'ai mal compris...":
            python:
                lettre = renpy.input("Lequel? (merci d'écrire la lettre en majuscule)")
                lettre = chiffre.strip() or "?"
            $ i=0
            while i < (len(dico)):
                if lettre == dico[i].name:
                    $ renpy.movie_cutscene(i.video)
            jump ClairiereDOliveau
        "Je n'ai besoin de rien":
            jump ClairiereDOliveau
        
            
    
    
#############################################################################################################################
    label PorteDuRoyaumeDesFees:
    stop music
    play music "<loop 0.0>/audio/ForetBruitOiseau.mp3"
    #IntroLabel
    $ minimap.append(PorteDuRoyaumeDesFees)
    scene PorteDuRoyaumeDesFees at sizeBackground with slowDissolve
    #

    $ renpy.movie_cutscene("Videos/garde_tes.webm")
    $ avancement[0]= "RenvoyeParGarde"
    jump ClairiereDOliveau
#############################################################################################################################
    label LieuDuVol:
    stop music
    play music "<loop 0.0>/audio/Foret.mp3"
    #IntroLabel
    scene LieuDuVol at sizeBackground with slowDissolve
    show screen LieuDuVolLink with slowDissolve
    jump WaitingScreen
    #   

    label Fee:
    if avancement[1]=="null":
        $ minimap.append(LieuDuVol)
        $ renpy.movie_cutscene("Videos/Lettre_V_LSF.webm")
        $ renpy.movie_cutscene("Videos/Lettre_O_LSF.webm")
        $ renpy.movie_cutscene("Videos/Lettre_L_LSF.webm")
        if achV==0:
            show achV at Tachievement onlayer overlay
            $ achievements.append(Lettre_V)
            $ achV +=1
        jump miniJeuPoursuite
        $ avancement[1]= "ObjetRecupere"
        jump LieuDuVol
    elif avancement[1]=="ObjetRecupere":
        "Tiens une lettre de remerciement"
        $ inventaire.append(LettreDeRemerciement)
        $ renpy.movie_cutscene("Videos/Lettre_C_LSF.webm")
        $ renpy.movie_cutscene("Videos/Lettre_H_LSF.webm")
        $ renpy.movie_cutscene("Videos/Lettre_W_LSF.webm")
        $ renpy.movie_cutscene("Videos/Lettre_Y_LSF.webm")
        $ renpy.movie_cutscene("Videos/Lettre_Z_LSF.webm")
        if achCHWYZ==0:
            show achCHWYZ at Tachievement onlayer overlay
            $ achievements.append(Lettre_CHWYZ)
            $ achCHWYZ +=1
        python:
            dico.append(C)
            dico.append(H)
            dico.append(W)
            dico.append(Y)
            dico.append(Z)
            avancement[0]= "LieuDuVolComplete"
        show screen LieuDuVolLink
        jump WaitingScreen

    label miniJeuPoursuite:
    stop music
    play music "<loop 0.0>/audio/ForetBruitOiseau.mp3"
    scene LieuDuVol at sizeBackground with slowDissolve

    pp "Oh ! Qu'est ce que c'est ?"

    show screen papier
    pp 'Hum...'

    pp "Ce schéma devait lui servir à retrouver son chemin. Si j'arrive à le dechiffrer, je trouverai où il se cache."

    "A l'aide du papier, trouvez le bon chemin menant à la cachette du voleur."

    label JeuPapier:

        show screen papier
        call screen papierJeu



    label Arrivee:

        hide screen papier
        hide screen papierJeu

        pp "Je pense qu'il doit se cacher ici !"

        scene CabaneDuVoleur at sizeBackground with slowDissolve

        pp "Oui c'est ici !"


    label CulDeSac:

        hide screen papier
        hide screen papierJeu


        pp 'Peut-être par là !'
        
        scene CulDeSac at sizeBackground with slowDissolve

        pp "Non... Ce n'est pas le bon chemin."

        jump JeuPapier
#############################################################################################################################
    label Lac:
    stop music
    play music "<loop 0.0>/audio/ForetBruitOiseau.mp3"
    #IntroLabel
    $ PossibiliteJUNQ=1
    $ minimap.append(Lac)
    scene Lac at sizeBackground with slowDissolve
    show screen LacLink with slowDissolve
    jump WaitingScreen
    #
#############################################################################################################################
    label NidDeLOiseau:
    stop music
    play music "<loop 0.0>/audio/ForetBruitOiseau.mp3"
    #IntroLabel
    $ minimap.append(NidDeLOiseau)
    scene NidDeLOiseau at sizeBackground with slowDissolve
    show screen NidDeLOiseauLink with slowDissolve
    jump WaitingScreen
    #
    label Bird:
    stop music
    play music "<loop 0.0>/audio/ForetBruitOiseau.mp3"
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
    $ renpy.movie_cutscene("Videos/oiseau_qui.webm")
    jump Bird
    label R32:
    b "Oh tu n’es pas d’ici, je suis un oiseau. Mais pas un rouge-gorges ou un pigeon, non, un vrai oiseau."
    b "Et dans mon immense bonté je t’apprendrais à survivre, piètre mammifère, dans cette forêt."
    b "Refait ces gestes après moi, ils signifient D-O-Y et t’aideront à faire pousser les plantes."
    $ renpy.movie_cutscene("Videos/oiseau_DOY_LSF.webm")
    if achD==0:
            show achD at Tachievement onlayer overlay
            $ achievements.append(Lettre_D)
            $ achD +=1
    python:
        dico.append(D)
        dico.append(Y)
    $ magie.append(DOY)
    if achDOY==0:
        show achDOY at Tachievement onlayer overlay
        $ achievements.append(Sort_DOY)
        $ achDOY +=1
    jump Sifflet
    label R33:
    menu:
        "Rendre la plume à l'oiseau":
            b "Pour ta bonté, je vais t’apprendre un sort." 
            b "Refait ces gestes après moi, ils signifient D-O-Y et t’aideront à faire pousser les plantes."
    $ renpy.movie_cutscene("Videos/oiseau_DOY_LSF.webm")
    if achD==0:
            show achD at Tachievement onlayer overlay
            $ achievements.append(Lettre_D)
            $ achD +=1
    python:
        dico.append(D)
        dico.append(Y)
    $ magie.append(DOY)
    if achDOY==0:
        show achDOY at Tachievement onlayer overlay
        $ achievements.append(Sort_DOY)
        $ achDOY +=1
    jump Sifflet
    label R34:
    
    jump Sifflet
    label R35:
    b "Dans mon immense bonté je t’apprendrais à survivre, piètre mammifère, dans cette forêt."
    b "Refait ces gestes après moi, ils signifient D-O-Y et t’aideront à faire pousser les plantes."
    $ renpy.movie_cutscene("Videos/oiseau_DOY_LSF.webm")
    if achD==0:
            show achD at Tachievement onlayer overlay
            $ achievements.append(Lettre_D)
            $ achD +=1
    python:
        dico.append(D)
        dico.append(Y)
    $ magie.append(DOY)
    if achDOY==0:
        show achDOY at Tachievement onlayer overlay
        $ achievements.append(Sort_DOY)
        $ achDOY +=1
    jump Sifflet

    label Sifflet:
    b "Je ne peux pas encore t’apprendre d’autres sorts, ta connaissance en langue des signes est... Trop primitive."
    b "Appelle-moi avec ce sifflet"
    $ renpy.movie_cutscene("Videos/oiseau_sifflet_LSF.webm")
    if achS==0:
            show achS at Tachievement onlayer overlay
            $ achievements.append(Lettre_S)
            $ achS +=1
    python:
        dico.append(S)
        dico.append(I)
        dico.append(F)
        dico.append(L)
        dico.append(T)
    b "Pour quand tu seras moins bête."
    python:
        inventaire.append(Sifflet)
    if achMagie==0:
            show achMagie at Tachievement onlayer overlay
            $ achievements.append(Histoire_Magie)
            $ achMagie +=1
    $ avancement[0]="ApprisSort"
    jump NidDeLOiseau
#############################################################################################################################
    label Falaise:
    stop music
    play music "<loop 0.0>/audio/ForetBruitOiseau.mp3"
    #IntroLabel Sans lierre
    if falaiseLierre ==0:
        $ PossibiliteDOY=1
        $ minimap.append(Falaise)
        scene Falaise at sizeBackground with slowDissolve
        show screen FalaiseLink with slowDissolve
        jump WaitingScreen
    #IntroLabel Avec lierre
    elif falaiseLierre ==1:
        scene FalaiseLierre at sizeBackground with slowDissolve
        show screen FalaiseLink with slowDissolve
        jump WaitingScreen
    #
    label DessusDeLaFalaise:
    stop music
    play music "<loop 0.0>/audio/ForetBruitOiseau.mp3"
    scene DessusDeLaFalaise at sizeBackground with slowDissolve
    show screen DessusDeLaFalaiseLink with slowDissolve
    jump WaitingScreen

    label alchimiste:
    if avancement[2]=="null":
        $ renpy.movie_cutscene("Videos/alchimiste_besoin.webm")
        pp "{k=4}.....{/k}"
        $ renpy.movie_cutscene("Videos/alchimiste_SOS_LSF.webm")
        jump miniJeuFiole
    elif avancement[2]=="FioleObtenu":
        $ avancement[0]="FioleObtenu"
        menu:
            "Donner la fiole à la fée":
                $ gentillesse += 2
                $ renpy.movie_cutscene("Videos/achimiste_merci.webm")
                $ renpy.movie_cutscene("Videos/alchimiste_FIOLE_LSF.webm")
                if achF==0:
                    show achF at Tachievement onlayer overlay
                    $ achievements.append(Lettre_F)
                    $ achF +=1
                jump Falaise
            "Partir avec la fiole":
                $ gentillesse -= 3
                $ renpy.movie_cutscene("Videos/alchimiste_NON.webm")
                $ renpy.movie_cutscene("Videos/alchimiste_FIOLE_LSF.webm")
                if achF==0:
                    show achF at Tachievement onlayer overlay
                    $ achievements.append(Lettre_F)
                    $ achF +=1
                jump Falaise

    label miniJeuFiole:
    label jeuFiole_lancement:
        show screen lancementjeufiole
        "Appuie sur le chaudron pour lancer le mini-jeu !"
        jump jeuFiole_lancement

    label jeuFiole_init:
        $tab,ordre,video,coeur = jeuFiole_initVar()
        jump jeuFiole_loop

    label jeuFiole_loop:
        $ renpy.movie_cutscene(video[0])
        "Appuie pour relancer la video"
        jump jeuFiole_loop

    label jeuFiole_valider:
        $tab,ordre = jeuFiole_majtab(tab,ordre)
        "Oui, bravo"
        $renpy.jump(jeuFiole_fin(ordre))

    label jeuFiole_echec:
        $coeur-=1
        "Raté, regarde plus attentivement la vidéo"
        $renpy.jump(jeuFiole_nul(coeur))

    label jeuFiole_fingagner:
        hide screen jeufiole
        "Super, on a fini la potion grâce a ton aide"
        jump jeuFiole_fini

    label jeuFiole_finperdu:
        hide screen jeufiole
        "Tu t'es trompé trop de fois, essaye de réviser un peu ton alphabet puis relance le mini-jeu !"
        jump jeuFiole_lancement

    label jeuFiole_fini:
        $ renpy.movie_cutscene("Videos/oliveau_1_LSF.webm")
        $ renpy.movie_cutscene("Videos/oliveau_1_LSF.webm")
        if achMN==0:
            show achMN at Tachievement onlayer overlay
            $ achievements.append(Lettre_MN)
            $ achMN +=1
        python:
            dico.append(M)
            dico.append(N)
        $ avancement[2]="FioleObtenu"
        jump DessusDeLaFalaise
   
#############################################################################################################################
    label DansLesAirs:
    stop music
    play music "<loop 0.0>/audio/ForetBruitOiseau.mp3"
    #IntroLabel
    scene DansLesAirs at sizeBackground with slowDissolve
    show screen DansLesAirsLink with slowDissolve
    jump WaitingScreen
    #
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
    $ renpy.movie_cutscene("Videos/oiseau_KAME_LSF.webm")
    if achK==0:
        show achK at Tachievement onlayer overlay
        $ achievements.append(Lettre_K)
        $ achK +=1
    python:
        dico.append(K)
    b "Ce sort permet de voler. Il ne m’est évidemment d’aucune utilité, mais il me semble qu’une espèce comme la tienne en aurait plus que besoin. Bon courage, humain."
    #L'oiseau part
    $ magie.append(KAME)
    $ PossibiliteKAME=1
    if achKAME==0:
        show achKAME at Tachievement onlayer overlay
        $ achievements.append(Sort_KAME)
        $ achKAME +=1
    "Tu peux désormais voler dans la forêt, cela te permettra de te déplacer plus facilement sur la carte."
    $ avancement[0]="ApprisSort"

    label PossibiliteApprendrePIF:
    b "Le sort que je vais t’apprendre se dit PIF"
    $ renpy.movie_cutscene("Videos/oiseau_PIF_LSF.webm")
    if achP==0:
        show achP at Tachievement onlayer overlay
        $ achievements.append(Lettre_P)
        $ achP +=1
    $ dico.append(P)
    b "Ce sort permet de casser ce que l’on souhaite. C’est de lui que la plupart des fées tirent leur force."
    b "Pas moi, évidemment.Tu devrais en avoir besoin bientôt. Bon courage, humain."
    #l'oiseau part
    $ magie.append(PIF)
    if achPIF==0:
        show achPIF at Tachievement onlayer overlay
        $ achievements.append(Sort_PIF)
        $ achPIF +=1
    $ avancement[0]= "ApprisSort"
    jump ClairiereDOliveau

    label PossibiliteApprendreJUNQ:
    b "Le sort que je vais t’apprendre se dit JUNQ"
    #oiseau signe pas JUNQ??
    if achJ==0:
        show achJ at Tachievement onlayer overlay
        $ achievements.append(Lettre_J)
        $ achJ +=1
    $ dico.append(J)
    b " Ce sort permet de respirer dans l’eau." 
    b "Il te servira à traverser de longues étendues d’eau ou bien à aller chercher les trésors des fonds marins."
    b "Enfin, ceux dont je n’ai pas voulu. Bon courage, humain."
    $ magie.append(JUNQ)
    if achJUNQ==0:
        show achJUNQ at Tachievement onlayer overlay
        $ achievements.append(Sort_JUNQ)
        $ achJUNQ +=1
    $ avancement[0]= "ApprisSort"
    jump Lac
    
    label PossibiliteApprendreGREX:
    b "Le sort que je vais t'apprendre se dit GREX"
    #oiseau signe pas GREX??
    if achX==0:
        show achX at Tachievement onlayer overlay
        $ achievements.append(Lettre_X)
        $ achX +=1
    $ dico.append(X)
    b "Ce sort permet de creuser. Il te servira à retrouver des animaux de ton ordre comme les mulots et autres taupes." 
    b "Il y a sûrement des galeries que tu aimeras explorer là-bas. Bon courage, humain."
    $ magie.append(GREX)
    if achGREX==0:
        show achGREX at Tachievement onlayer overlay
        $ achievements.append(Sort_GREX)
        $ achGREX +=1
    $ avancement[0]= "ApprisSort"
    if achAlphabet==0:
        show achAlphabet at Tachievement onlayer overlay
        $ achievements.append(Histoire_Alphabet)
        $ achAlphabet +=1
    jump Labyrinthe
#############################################################################################################################
    label Gouffre:
    stop music
    play music "<loop 0.0>/audio/ForetBruitOiseau.mp3"
    #IntroLabel
    $ minimap.append(Gouffre)
    scene Gouffre at sizeBackground with slowDissolve
    show screen GouffreLink with slowDissolve
    jump WaitingScreen
    #
    $ PossibiliteKAME=2
    "On est dans un gouffre"
    "Vous avez traversé le gouffre en volant"
    jump WaitingScreen
#############################################################################################################################
    label ArbreABonbons:
    #IntroLabel
    $ minimap.append(ArbreABonbons)
    scene ArbreABonbons at sizeBackground with slowDissolve
    show screen ArbreABonbonsLink with slowDissolve
    jump WaitingScreen
    #
    label enfant:
    if avancement[4]=="null":
        jump EnfantQuiPleure
    elif avancement[4]=="ObtenuBonbons":
        jump ObtenuBonbons
    
    label EnfantQuiPleure:
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
    $ renpy.movie_cutscene("Videos/enfant_bonbon.webm")
    pp "..."
    $ renpy.movie_cutscene("Videos/enfant_Bonbon_LSF.webm")
    if achB==0:
        show achB at Tachievement onlayer overlay
        $ achievements.append(Lettre_B)
        $ achB +=1
    $ dico.append(B)
    #L’enfant pointe le doigt vers l’arbre et tend un sac de bonbons vides
    #Le joueur peut monter dans l’arbre
    jump MinijeuBonbons

    label ObtenuBonbons:
    menu:
        "Rendre les bonbons":
            $ gentillesse += 3
            $inventaire.append(Sucette)
            $ renpy.movie_cutscene("Videos/enfant_merci.webm")
            jump ArbreABonbons
        "Garder les bonbons":
            $ gentillesse -= 1
            $ renpy.movie_cutscene("Videos/enfant_mechant.webm")
            jump ArbreABonbons

    label MinijeuBonbons:
    scene bgArbreFeuillage
    show screen bonbonScreen
    "début"


    label jeuBonbon:
        "Trouvez six bonbons"
        $ renpy.jump(verif(bonbon1valeur, bonbon2valeur, bonbon3valeur, bonbon4valeur, bonbon5valeur, bonbon6valeur))


    label jeuBonbonFin:
        hide screen bonbonScreen
        "Vous avez trouvé tous les bonbons"
        $ avancement[4]="ObtenuBonbons"
        jump ArbreABonbons
############################################################################################################################
    label FondDuGouffre:
    #IntroLabel
    $ PossibiliteGREX=1
    if porteGouffre==0:
        $ PossibilitePIF=1
    $ minimap.append(FondDuGouffre)
    scene FondDuGouffre at sizeBackground with slowDissolve
    show screen FondDuGouffreLink with slowDissolve
    jump WaitingScreen
    #
############################################################################################################################
    label Bibliotheque:
    #IntroLabel
    $ PossibiliteKAME=0
    $ minimap.append(Bibliotheque)
    scene Bibliotheque at sizeBackground with slowDissolve
    show screen BibliothequeLink with slowDissolve
    stop music
    play music "<loop 0.0>/audio/Bibliotheque.mp3"
    #
    if avancement[5]=="null":
        #Une fée bibliothécaire qui semble avoir des milliers d’années est assise derrière un immense bureau dans la bibliothèque
        #Le bibliothécaire tend un bout de papier avec trois références bibliographiques dessus et indique la bibliothèque
        $ renpy.movie_cutscene("Videos/bibliothecaire_amene_LSF.webm")
        jump MinijeuBibliotheque
    elif avancement[5]=="ObtenuReference":
        jump ObtenuReference
    
    label MinijeuBibliotheque:
    # ----- DEBUT JEU BIBLIOTHEQUE -----
    label jeuBiblio_init:
        $rep,repV,tab,coeur=jeuBiblio_initVar()
        jump jeuBiblio_loop

    label jeuBiblio_loop:
        show screen jeubiblio with slowDissolve
        "Clique sur les boules de cristal pour voir leurs mots associés puis valide si c'est un mot recherché !"
    jump jeuBiblio_loop

    # -début vérification réussite/échec-
    label jeuBiblio_valider1:
        $repV[0]=1
        $rep[0][1]="jeuBiblio_MotValider.png"
        $renpy.jump(jeuBiblio_validation(repV))

    label jeuBiblio_valider2:
        $repV[1]=1
        $rep[1][1]="jeuBiblio_MotValider.png"
        $renpy.jump(jeuBiblio_validation(repV))

    label jeuBiblio_valider3:
        $repV[2]=1
        $rep[2][1]="jeuBiblio_MotValider.png"
        $renpy.jump(jeuBiblio_validation(repV))

    label jeuBiblio_echec:
        $coeur-=1
        $renpy.jump(jeuBiblio_echec(coeur))
    # -fin vérification réussite/échec-

    # -début lancement vidéo des boules de cristal-

    label jeuBiblio_video0:
        $ renpy.movie_cutscene(tab[0][3])
        $ renpy.movie_cutscene(tab[0][4])
        $ renpy.movie_cutscene(tab[0][5])
        jump jeuBiblio_loop

    label jeuBiblio_video1:
        $ renpy.movie_cutscene(tab[1][3])
        $ renpy.movie_cutscene(tab[1][4])
        $ renpy.movie_cutscene(tab[1][5])
        jump jeuBiblio_loop

    label jeuBiblio_video2:
        $ renpy.movie_cutscene(tab[2][3])
        $ renpy.movie_cutscene(tab[2][4])
        $ renpy.movie_cutscene(tab[2][5])
        jump jeuBiblio_loop

    label jeuBiblio_video3:
        $ renpy.movie_cutscene(tab[3][3])
        $ renpy.movie_cutscene(tab[3][4])
        $ renpy.movie_cutscene(tab[3][5])
        jump jeuBiblio_loop

    label jeuBiblio_video4:
        $ renpy.movie_cutscene(tab[4][3])
        $ renpy.movie_cutscene(tab[4][4])
        $ renpy.movie_cutscene(tab[4][5])
        jump jeuBiblio_loop

    label jeuBiblio_video5:
        $ renpy.movie_cutscene(tab[5][3])
        $ renpy.movie_cutscene(tab[5][4])
        $ renpy.movie_cutscene(tab[5][5])
        jump jeuBiblio_loop

    label jeuBiblio_video6:
        $ renpy.movie_cutscene(tab[6][3])
        $ renpy.movie_cutscene(tab[6][4])
        $ renpy.movie_cutscene(tab[6][5])
        jump jeuBiblio_loop

    label jeuBiblio_video7:
        $ renpy.movie_cutscene(tab[7][3])
        $ renpy.movie_cutscene(tab[7][4])
        $ renpy.movie_cutscene(tab[7][5])
        jump jeuBiblio_loop

    label jeuBiblio_video8:
        $ renpy.movie_cutscene(tab[8][3])
        $ renpy.movie_cutscene(tab[8][4])
        $ renpy.movie_cutscene(tab[8][5])
        jump jeuBiblio_loop

    label jeuBiblio_video9:
        $ renpy.movie_cutscene(tab[9][3])
        $ renpy.movie_cutscene(tab[9][4])
        $ renpy.movie_cutscene(tab[9][5])
        jump jeuBiblio_loop

    label jeuBiblio_video10:
        $ renpy.movie_cutscene(tab[10][3])
        $ renpy.movie_cutscene(tab[10][4])
        $ renpy.movie_cutscene(tab[10][5])
        jump jeuBiblio_loop

    label jeuBiblio_video11:
        $ renpy.movie_cutscene(tab[11][3])
        $ renpy.movie_cutscene(tab[11][4])
        $ renpy.movie_cutscene(tab[11][5])
        jump jeuBiblio_loop

    label jeuBiblio_video12:
        $ renpy.movie_cutscene(tab[12][3])
        $ renpy.movie_cutscene(tab[12][4])
        $ renpy.movie_cutscene(tab[12][5])
        jump jeuBiblio_loop

    label jeuBiblio_video13:
        $ renpy.movie_cutscene(tab[13][3])
        $ renpy.movie_cutscene(tab[13][4])
        $ renpy.movie_cutscene(tab[13][5])
        jump jeuBiblio_loop

    label jeuBiblio_video14:
        $ renpy.movie_cutscene(tab[14][3])
        $ renpy.movie_cutscene(tab[14][4])
        $ renpy.movie_cutscene(tab[14][5])
        jump jeuBiblio_loop

    label jeuBiblio_video15:
        $ renpy.movie_cutscene(tab[15][3])
        $ renpy.movie_cutscene(tab[15][4])
        $ renpy.movie_cutscene(tab[15][5])
        jump jeuBiblio_loop

    label jeuBiblio_video16:
        $ renpy.movie_cutscene(tab[16][3])
        $ renpy.movie_cutscene(tab[16][4])
        $ renpy.movie_cutscene(tab[16][5])
        jump jeuBiblio_loop

    label jeuBiblio_video17:
        $ renpy.movie_cutscene(tab[17][3])
        $ renpy.movie_cutscene(tab[17][4])
        $ renpy.movie_cutscene(tab[17][5])
        jump jeuBiblio_loop

    label jeuBiblio_video18:
        $ renpy.movie_cutscene(tab[18][3])
        $ renpy.movie_cutscene(tab[18][4])
        $ renpy.movie_cutscene(tab[18][5])
        jump jeuBiblio_loop

    label jeuBiblio_video19:
        $ renpy.movie_cutscene(tab[19][3])
        $ renpy.movie_cutscene(tab[19][4])
        $ renpy.movie_cutscene(tab[19][5])

    label jeuBiblio_video20:
        $ renpy.movie_cutscene(tab[20][3])
        $ renpy.movie_cutscene(tab[20][4])
        $ renpy.movie_cutscene(tab[20][5])
        jump jeuBiblio_loop
    # -fin lancement vidéo des boules de cristal-

    # -début des fins du jeu-
    label jeuBiblio_fingagner:
        hide screen jeubiblio with slowDissolve
        "Bravo ! Tu as réussi"
        jump Bibliotheque

    label jeuBiblio_finperdu:
        hide screen jeubiblio with slowDissolve
        "Raté. Essaye de réviser grâce a Oliveau avant de rejouer"
        jump MinijeuBibliotheque

    # -fin des fins du jeu-

    # ----- FIN JEU BIBLIOTHEQUE -----


    
    label ObtenuReference:
    $ renpy.movie_cutscene("Videos/bibliothecaire_merci.webm")
    if achBIBLIOTHEQUE==0:
        show achBIBLIOTHEQUE at Tachievement onlayer overlay
        $ achievements.append(Lettre_BIBLIOTHEQUE)
        $ achBIBLIOTHEQUE +=1
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
    label FondDuLac:
    #IntroLabel
    $ PossibiliteKAME=0
    scene FondDuLac at sizeBackground with slowDissolve
    show screen FondDuLacLink with slowDissolve
    jump WaitingScreen
    #
    #on trouve une porte sculptée dans le corail.
    jump Cuisine
#############################################################################################################################
    label Cuisine:
    #IntroLabel
    $ PossibliteKAME=0
    $ minimap.append(Cuisine)
    scene Cuisine at sizeBackground with slowDissolve
    show screen CuisineLink with slowDissolve
    stop music
    play music "<loop 0.0>/audio/Cuisine.mp3"
    jump WaitingScreen
    #
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

    #mini-jeu
    label PlanDeTravail:
        scene décor_cuisine
        with dissolve

        pause(1.0)
        # pour rouge:#711616
        show cuisine with dissolve

        pause(2.5)

        hide cuisine with dissolve

        scene décor_cuisine with dissolve

        "Ce mini-jeu est en deux parties: la préparation et la cuisson du gateau."
        "La préparation consiste simplement à mettre les bon ingrédients au bon nombre dans le chaudron."
        "La cuisson est un petit jeu de rythme ou il vous faut toucher 10 flammes pour cuire le gateau."
        jump kitch

    label kitch:
        scene décor_cuisine with dissolve
        $ gat = Gateau()
        $ choix_sirop = 0
        #n= [n_oeufs*5, n_farine, n_levure, n_beurre, n_lait]
        "J'ai besoin de [gat.n_ingr[0]] oeufs (par paquets de 5), [gat.n_ingr[1]] sachets de farine, [gat.n_ingr[2]] sachets de levure, [gat.n_ingr[3]] mottes de beurre, [gat.n_ingr[4]] L de lait, [gat.n_ingr[5]] morceaux de sucre (par paquets de 5)."
        "Et n'oublie pas, un soupcon d'eau de rose par gentilesse, et méfie toi de l'arsenic."

        scene fond_minijeu_cuisine
        with dissolve

        call screen ingred

    label cuisson:
        scene fond_minijeu_cuisine with dissolve
        show barre_flamme at pos_flamme
        show screen timeup_cuisson
        show screen le_feu_cuisson
        show screen marmite_cuisson
        python:
            hits = 0
            misses = 0
            t = time.time()
            manager = SpriteManager(update=sprites_update, event=sprites_event)
            sprite = "flamme.png"
            targets = set(1000+i for i in xrange(-30, 30))
            sprites = []
            td = 0
            for i in xrange(100):
                td += renpy.random.random() + 0.5
                sprites.append(Four("flamme.png", 15, td, 50))
            renpy.show_screen("show_vars")
            renpy.show("_", what=manager, zorder=1)
            while True:
                result = ui.interact()

    label cuire_gateau:
        scene fond_minijeu_cuisine with dissolve
        call screen cuisinefour with dissolve

    label ingredients_gateau:
        scene décor_cuisine with dissolve
        "J'ai dis que j'ai besoin de [gat.n_ingr[0]] oeufs (par paquets de 5), [gat.n_ingr[1]] sachets de farine, [gat.n_ingr[2]] sachets de levure, [gat.n_ingr[3]] mottes de beurre, [gat.n_ingr[4]] L de lait, [gat.n_ingr[5]] morceaux de sucre (par paquets de 5)."
        "Et n'oublie pas, un soupcon d'eau de rose par gentilesse, et méfie toi de l'arsenic."
        scene fond_minijeu_cuisine with dissolve
        call screen ingred with dissolve



    label echec_jeu_four:
        scene décor_cuisine
        with dissolve

        "Ce n'est pas ce que j'ai demandé!"
        "Tu vas devoir recommencer!"

        jump kitch

    label fin_minijeu_cuisine:

        scene décor_cuisine with dissolve
        show gateau at right
        if choix_sirop == 1:
            "Merci d'avoir mis du sirop du rose!"
            "Tu gagne 2 points de gentillesse!"
            $ gentillesse += 2
        elif choix_sirop == 2:
            "Tu veux m'empoisonner avec l'arsenic!!"
            "Je te retire 3 points de gentillesse!"
            $ gentillesse -= 3

    "Merci beaucoup, tu peux continuer"
    #Cuisinière: (pointe le joueur du doigt) G-A-T-E-A-U
    $ dico.append(G)
    #le joueur repart avec une part de gateau
    $ avancement[3]="PossibiliteApprendreGREX"    
#############################################################################################################################
    label Labyrinthe:
    $ PossibiliteKAME=0
    $ taille_labyrinthe= renpy.random.randint(5,10)    # nombre de salles du labyrinthe
    $ position_laby = 0                               # a quelle salle on en est
    $ cod_laby = Code_laby()
    $ chem_laby = Bon_chem()
    $ cod_laby.nouv_code()
    $ minimap.append(Labyrinthe)

    label labyrinthe_minijeu:
    scene gallerie porte at sizeBackground with slowDissolve
    "Vous arrivez au labyrinthe."
    call screen porte_gallerie with slowDissolve
    stop music
    play music "<loop 0.0>/audio/Labyrinthe.mp3"

    label transition_lab:                               # transition entre 2 salles
        $ position_laby += 1
        $ switch_laby = position_laby % 3

        "Cela semble correct. Continuons d'avancer."
        if position_laby == taille_labyrinthe:
            jump fin_laby
        elif switch_laby == 0:
            $ cod_laby.nouv_code()
            scene gallerie porte at sizeBackground with dissolve
            call screen porte_gallerie with dissolve
        elif switch_laby == 1:
            $ chem_laby.nouv_code(2)
            scene gallerie croisement 2 at sizeBackground with dissolve
            call screen carrefour_deux with dissolve
        else:
            $ chem_laby.nouv_code(3)
            scene gallerie croisement 3 at sizeBackground with dissolve
            call screen carrefour_trois with dissolve

    label entrer_code_laby:
        $ code_j_laby = renpy.input("Quel est le code?", length = 4)
        if code_j_laby == cod_laby.sum_code:
            jump transition_lab
        else:
            jump echec_porte_lab

    label echec_porte_lab:
        "Ca ne semble pas être le bon code..."
        "Réessayons!"
        call screen porte_gallerie with dissolve

    label video_fantome_deux:
        #"porte [chem_laby.n_laby]"
        if chem_laby.n_laby == 1:
            $ renpy.movie_cutscene(dico_lab_vid[Choix_laby[chem_laby.a_laby]])
        else:
            $ renpy.movie_cutscene(dico_lab_vid[Choix_laby[chem_laby.b_laby]])
        call screen carrefour_deux with dissolve

    label video_fantome_trois:
        #"porte [chem_laby.n_laby]"
        if chem_laby.n_laby == 1:
            $ renpy.movie_cutscene(dico_lab_vid[Choix_laby[chem_laby.a_laby]])
        elif chem_laby.n_laby == 2:
            $ renpy.movie_cutscene(dico_lab_vid[Choix_laby[chem_laby.b_laby]])
        else:
            $ renpy.movie_cutscene(dico_lab_vid[Choix_laby[chem_laby.c_laby]])
        call screen carrefour_trois with dissolve

    label video_fantome_porte:
        #$ renpy.say(None,cod_laby.sum_code)
        $ renpy.movie_cutscene(dico_lab_vid[Choix_laby[cod_laby.a_laby]])
        $ renpy.movie_cutscene(dico_lab_vid[Choix_laby[cod_laby.b_laby]])
        $ renpy.movie_cutscene(dico_lab_vid[Choix_laby[cod_laby.c_laby]])
        $ renpy.movie_cutscene(dico_lab_vid[Choix_laby[cod_laby.d_laby]])
        call screen porte_gallerie with dissolve

    label echec_lab:
        scene gallerie croisement 3 with dissolve
        "Il semble que c'était le mauvais chemin"
        "Cela fait des heures que vous errez dans des galeries toutes semblables."
        "Prenez la taupe pour retourner au début."
        call screen taupe_lab with dissolve

    label fin_laby:
        scene carte with dissolve
        "Vous êtes enfin sorti!"
        jump RoyaumeDesFees
#############################################################################################################################
    label RoyaumeDesFees:
    stop music
    play music "<loop 0.0>/audio/Denouement.mp3"
    if achNiveau1==0:
        show achNiveau1 at Tachievement onlayer overlay
        $ achievements.append(Histoire_Niveau1)
        $ achNiveau1 +=1
    "Alors c'est ça le royaume des fées!!"

    return
