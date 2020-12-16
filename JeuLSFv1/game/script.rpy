label start:
    $ minimap = []
    $ salle1 = Room("Salle1","Salle1.png", 60, 60)
    $ salle2 = Room("Salle2","Salle2.png", 400, 230)
    show screen minimapShow

    label Salle1:
    $ minimap.append(salle1)
    scene ISalle1

    m "après ce message ce sera la salle 2"
    label Salle2:
    $ minimap.append(salle2)
    scene ISalle2

    "pause"

    return
