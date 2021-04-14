init python:
    config.screen_width=1280
    config.screen_height=800
    import time
    import pygame
    MOUSEBUTTONDOWN=pygame.MOUSEBUTTONDOWN

    class Four(object):
        def __init__(self, sprite, speed, delay, ypos=0):
            self.sprite = sprite
            self.speed = speed
            self.delay = delay
            self.show = manager.create(sprite)
            self.show.x = 0
            self.show.y = ypos
            self.moving = False

        def update(self):
            if store.t + self.delay < time.time():
                self.moving = True
                self.x = self.x + self.speed
            else:
                pass

        @property
        def x(self):
            return self.show.x
        @x.setter
        def x(self, value):
            self.show.x = value

        @property
        def y(self):
            return self.show.y
        @y.setter
        def y(self, value):
            self.show.y = value

    def sprites_update(st):
        for sprite in sprites[:]:
            sprite.update()
            if sprite.x > config.screen_width:
                sprite.show.destroy()
                sprites.remove(sprite)
                store.misses += 1
                renpy.restart_interaction()
            if store.misses > 5:
                renpy.hide_screen("show_vars")
                renpy.hide_screen("le_feu_cuisson")
                renpy.hide_screen("marmite_cuisson")
                renpy.hide("_")
                renpy.hide("barre_flamme")
                renpy.jump("echec_jeu_four")
        return 0.05

    def sprites_event(ev, x, y, st):
        if ev.type == MOUSEBUTTONDOWN:
            if ev.button == 1:
                hit = False
                for sprite in sprites[:]:
                    if sprite.moving:
                        if int(sprite.x) in store.targets:
                            store.hits += 1
                            hit = True
                            sprite.show.destroy()
                            sprites.remove(sprite)
                            break
                if not hit:
                    store.misses += 1
                if store.misses > 5:
                    renpy.hide_screen("show_vars")
                    renpy.hide_screen("le_feu_cuisson")
                    renpy.hide_screen("marmite_cuisson")
                    renpy.hide("_")
                    renpy.hide("barre_flamme")
                    renpy.jump("echec_jeu_four")
                if store.hits > 10:
                    renpy.hide_screen("show_vars")
                    renpy.hide_screen("le_feu_cuisson")
                    renpy.hide_screen("marmite_cuisson")
                    renpy.hide("_")
                    renpy.hide("barre_flamme")
                    renpy.jump("fin_minijeu_cuisine")
                renpy.restart_interaction()


    #renvoie un tuple avec en 1. nombre de chaque ingrédients du gateau 2.
    def creer_list_ingr():
        l=[]
        n_oeufs = renpy.random.randint(2, 4)
        n_farine = renpy.random.randint(1, 9)
        n_levure = renpy.random.randint(1, 9)
        n_beurre = renpy.random.randint(1, 9)
        n_lait = renpy.random.randint(1, 9)
        n_sucre = renpy.random.randint(2, 4)
        #n_oeufs = renpy.random.randint(1, 1)
        #n_farine = renpy.random.randint(1, 1)
        #n_levure = renpy.random.randint(1, 1)
        #n_beurre = renpy.random.randint(1, 1)
        #n_lait = renpy.random.randint(1, 1)
        #n_sucre = renpy.random.randint(1, 1)
        n= [n_oeufs*5, n_farine, n_levure, n_beurre, n_lait, n_sucre*5]
        for i in range (n_oeufs):
            l.append("oeufs")
        for i in range (n_farine):
            l.append("farine")
        for i in range (n_levure):
            l.append("levure")
        for i in range(n_beurre):
            l.append("beurre")
        for i in range(n_lait):
            l.append("lait")
        for i in range(n_sucre):
            l.append("sucre")
        return (n,l)

#le gateau à préparer
    class Gateau:
        def __init__(self):
            (a,b) = creer_list_ingr()
            self.n_ingr = a
            self.ingredients = b
            self.n_oeufs = 0
            self.n_farine = 0
            self.n_levure = 0
            self.n_beurre = 0
            self.n_lait = 0
            self.n_sucre = 0

        def remove_ingredient(self, ing):
            (self.ingredients).remove(ing)
            if ing == "oeufs":
                self.n_oeufs += 5
            if ing == "farine":
                self.n_farine += 1
            if ing == "levure":
                self.n_levure += 1
            if ing == "beurre":
                self.n_beurre += 1
            if ing == "lait":
                self.n_lait += 1
            if ing == "sucre":
                self.n_sucre += 5
            renpy.restart_interaction()

        def echec_ingr(self):
            (self.ingredients).append("oups")

        def check(self, ing):
            return (ing in self.ingredients)
