label start:
    $ minimap = []
    $ salle1 = Room("Salle1","Salle1.png", 60, 60)
    $ salle2 = Room("Salle2","Salle2.png", 400, 230)

    label Salle1:
    $ minimap.append(salle1)
    scene Salle1
    show screen minimapShow

    m "après ce message ce sera la salle 2"
    label Salle2:
    $ minimap.append(salle2)
    scene Salle2

    "pause"

    return
