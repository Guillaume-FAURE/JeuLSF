#Python:
init python:
    class Sign:
        def __init__(self, name, image):
            self.name = name
            self.image = image


#Definition character/image
define m = Character("Monika", who_color="#e5a6e5")
define pp = Character("[nom]", color="#da1219")
define mpetit = Character(kind=m, what_size=18)
define moutline = Character(kind=m,what_color="#ffffff", what_outlines=[(3,"#e5a6e5", 0, 0)])
define mcentre = Character(kind=m, what_xalign=0.5, what_textalign=0.5, what_layout='subtitle')
define narrator = Character(what_bold=True)
image monika = "monika.webp"
image monika rotated = Transform ("monika.webp", rotate=10)
image monika rotatel = Transform ("monika.webp", rotate=-10)
image red solidexample = Solid("#ff0000", xysize=(200, 200), pos=(0.5, 0.5))
image red text = Text("bonjour", size=30, pos=(0.5,0.5))
#image test composite = Composite((300,600),(50, 50), "#ff0000", pos=(0.5, 0.5), Text("bonjour",size=30, pos=(0.5, 0.5)))
define fastfade = Fade(0.2, 0, 0, color="#000")
image alphabet = "alphabet LSF.png"

image magicpow:
    "images/monika.webp"
    linear 0.1 zoom 1.05
    linear 0.1 zoom 0.5
    repeat

image monika anime:
    "monika.webp"
    zoom 1.4
    around (700, 1350)
    angle -9
    radius 500
    parallel:
        linear .7 angle 11
        linear .7 angle -9
    parallel:
        linear .7 rotate 10
        linear .7 rotate -10
    repeat

transform alpha_control:
    anchor (.5, .5)
    parallel:
        zoom 0
        linear .5 zoom .75
        pause 2
        linear 1.0 zoom 4.0

    parallel:
        xpos 0.0 ypos .6
        linear 1.5 xpos 1.0
        linear 1.0 xpos .5 ypos .2

    pause .5
    repeat

image alpha_controls:
    "images/Images tutorial/spotlight.png"
    anchor (.5, .5)
    parallel:
        zoom 0
        linear .5 zoom .5
        pause 2.5
        linear 1.0 zoom 4.0

    parallel:
        xpos 0.0 ypos .6
        linear 1.5 xpos 1.0
        linear 1.0 xpos .5 ypos .2
        linear .5 xpos .5 ypos .5

    pause .5
    repeat

define alpha_example = AlphaDissolve("alpha_controls", delay=4)

transform mouvement:
    xpos .5 ypos .5
    zoom 0
    linear 2.0 zoom 0.5
    linear .2 xalign .5 yalign .5
    block:
        linear .5 xalign 0.0 yalign 0.0
        linear .5 xalign 0.0 yalign 1.0
        linear .5 xalign 1.0 yalign 1.0
        linear .5 xalign 1.0 yalign 0.0
        linear .5 xalign .5 yalign .5
        repeat

transform vibration:
    linear 0.1 zoom 0.95
    linear 0.1 zoom 1.05
    repeat


label start:
    python:
        nom = "???"

    scene salle 1

    "Page d'acceuil : {a=jump:lien}Lien{/a} ; {a=jump:intro}Intro{/a} ; {a=jump:option}Menu{/a} ; {a=jump:video}Video{/a} ; {a=jump:nvltest}Nvl{/a}
    ; {a=jump:diffecriture}Différentes écritures{/a} ; {a=jump:character}Character{/a} ; {a=jump:images}Images{/a} ; {a=jump:simpleTransition}Transitions simples{/a} ;
    {a=jump:advancedTransition}Transitions avancées{/a} ; {a=jump:button}Button{/a} ; {a=jump:screen}Screen{/a}"

    play music "music/largest-star.mp3"

    show monika

    m "Bonjour"

    show monika at right

    m "droite"

    transform sligthleft:
        xalign 0.25
        yalign 1.0

    transform sligthrigth:
        xalign 0.75
        yalign 1.0

    transform middle:
        xalign 0.5
        yalign 1.0

    define slowDissolve = Dissolve(1)

    show monika at middle with slowDissolve

    label lien:
    "ceci est un lien: {a=https://www.trefle.org} le site de l'association Trèfles pour en apprendre plus sur la langue des signes{/a}"
    "et cela peut permettre d'aller plus loin dans le jeu: {a=jump:Reponse1} lien{/a}"

    "Bienvenue dans le monde du Test1LSF"
    label intro:
    play music "music/largest-star.mp3" fadeout 1

    pp "Où suis-je?"

    m "Que veux-tu faire?"

    label option:
    menu:
        "Je veux savoir ce qui ce passe ici!":
            jump Option1

        "Je veux partir!":
            jump Option2

    label Option1:
        m "Tu es dans un Test pour apprendre à utiliser Ren'py"
        jump Reponse1

    label Option2:
        pp "Suicide"
        return
    label Reponse1:
        pp "Je suis dans un jeu..."
        m "Quel est ton nom?"

    python:
        nom = renpy.input("Quel est ton nom?")
        nom = nom.strip() or "Inconnu"

    m "Donc, tu t'appelles [nom]..."

    m "Maintenant, que veux tu faire?"

    menu:
        "Continuer":
            jump Option11
        "Arrêter":
            jump Option12

    label Option11:
        jump Reponse11
    label Option12:
        pp "Suicide"
        return
    label Reponse11:
    m "Alors on continue"
    stop music fadeout 1
    #python:
    #    renpy.movie_cutscene("video/video-absol2.webm")
    label video:
    image test = Movie(play="video/video-absol2.webm",pos=(10, 10), anchor=(0, 0))
    #screen test:
        #add "test"
        #textbutton "Start" action Start() xalign 0.5 yalign 0.5
    show test
    "stop"
    hide test
    image gif = Movie(play="video/giphy2.avi", pos=(10, 10), anchor=(0, 0))
    show gif
    "stop"
    hide gif

    label nvltest:
    define nvla = Character("Full", color="#123456", kind=nvl)
    nvla "Test 1"
    nvl clear
    nvla "test numero 2"

    "C'est fini après ce message..."

    label diffecriture:
    "Nuances de gris : {alpha=0}test d'écriture{/alpha}{alpha=.1}test d'écriture{/alpha}
    {alpha=.2}test d'écriture{/alpha}{alpha=.3}test d'écriture{/alpha}
    {alpha=.4}test d'écriture{/alpha}{alpha=.5}test d'écriture{/alpha}
    {alpha=.7}test d'écriture{/alpha}{alpha=.9}test d'écriture{/alpha}"
    "{cps=10}Différentes couleurs: {color=#ff5733}test{/color}{color=#ffc433}test{/color}{color=#f0ff33}test{/color}{color=#7aff33}test{/color}{color=#33ffa2}test{/color}{color=#33fff3}test{/color}{color=#3368ff}test{/color}{color=#9933ff}test{/color}{color=#ff33ca}test{/color}{color=#ff3339}test{/color}{/cps}"
    "Sans" "{k=4}you'll be burning in hell{/k}"
    "Possibilité d'utiliser space ou vspace pour ajouter des espaces horizontaux ou verticaux entre le texte"
    "Les commande p ou p=n permette faire apparaitre le reste du texte au click ou au bon d'un moment"
    "bonjour {p=0.5} je {p=0.5} suis {p=0.5} guillaume {p=0.5} au revoir"
    "le tag w fait la meme chose que p mais ne fait pas de retour {w=1} à la ligne"
    "ceci est un {nw}"
    extend "test"

    label character:
    mpetit "Ceci est la police 18"
    mpetit "Les différentes propriétés qui peuvent être données à un character sont le window_background, who_color, what_color (pour la police d'écriture), who_font, what_font, who_bold, what_italic (true or false), what_size"
    mpetit "le what_outlines (qui est en fait un tableau de couleur du type what_outlines=(1,couleur, 0, 0), premier nombre est la taille du outline, le deuxieme la couleur et le x et y offsets"
    moutline "Ceci est un test aussi"
    extend ", what_outlines peut aussi permettre de faire une ombre pour le texte avec les parametres approprié (0,couleur, x, x)"
    mpetit "what_xalign et what_textalign permettent de placer le texte"
    mcentre "texte centré"
    mpetit "what_prefix et what_suffix permettent de mettre une suite de charactère au début et à la fin de chaque prise de parole d'un character"
    mpetit "kind permet de copier les propriétés d'un autre character et de changer seulement un truc (facilite la vie)"
    narrator "il existe un character spécial, narrator, des changement de ce personnage change toutes les prises de parole sans nom"

    label images:
    mpetit "il est possible de définir une image et de lui donné des propriétés"
    show monika
    "image de base"
    show monika rotated
    "image tourné avec Transform et rotate"
    hide monika rotated
    extend " il est aussi possible de donner une taille à une couleur par exemple avec xysize"
    extend " avec la commande Text, il est meme possible d'afficher du texte comme une image"
    "Et il est bien évidemment possible de combiné Transform et Texte"
    "Il est aussi possible de faire des composites d'images"

    show red solidexample
    pause 1
    show red text
    pause 1
    "pause"

    label simpleTransition:
    show monika at middle with slowDissolve
    show monika rotated with fastfade
    show monika rotatel with fastfade
    show monika with pixellate
    "pause"
    show monika at right
    with move
    show monika at left
    with move
    hide monika with zoomout
    show monika rotated with zoomin
    hide monika rotated with moveoutleft
    show monika rotatel with moveinright
    hide monika rotatel with moveouttop
    "pause"
    label advancedTransition:
    "pause"
    scene alphabet with irisout
    pause 3
    scene salle 1
    show monika
    with irisin
    "pause"
    scene black with irisin
    show monika anime
    "pause"
    hide monika anime with moveoutbottom
    scene salle 1
    show monika at center
    with alpha_example
    "pause"
    scene black with irisin
    #show spotlight at mouvement
    show magic at mouvement:
        linear 0.1 zoom 0.95
        linear 0.1 zoom 1.05
        repeat
    label button:
    screen textstyle():
        frame:
            textbutton "Button 1":
                text_color "#fd2c07"
    label screen:
    show screen Button1

    "pause"
    hide screen Button1
    show screen magie
    "pause"
    "error"
    label dictionnary:
    $ dictionnary = []
    $ eau = Sign("eau", "images/monika.webp")
    $ magie = Sign("magie", "magicpow")
    show screen dictionnary
    $ dictionnary.append(eau)
    $ dictionnary.append(magie)
    "pause"


    return
