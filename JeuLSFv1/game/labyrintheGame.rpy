init python:
    dico_lab_vid ={"1":".avi","2":".avi","3":".avi","4":".avi","5":".avi","6":".avi","7":".avi","8":".avi","9":".avi","A":".avi","B":".avi",
    "C":".avi","D":".avi","E":".avi","F":".avi","G":".avi","H":".avi","I":".avi",
    "J":".avi","K":".avi","M":".avi","N":".avi","O":".avi","P":".avi","Q":".avi","R":".avi","S":".avi","T":".avi","U":".avi","V":".avi",
    "W":".avi","X":".avi","Y":".avi","Z":".avi"}
    Choix_laby = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N",
    "O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    def random_code_lab():
        a_lab= renpy.random.randint(0,len(Choix_laby)-1)
        b_lab= renpy.random.randint(0,len(Choix_laby)-1)
        c_lab= renpy.random.randint(0,len(Choix_laby)-1)
        d_lab= renpy.random.randint(0,len(Choix_laby)-1)
        return (a_lab,b_lab,c_lab,d_lab)

    class Code_laby():
        def __init__(self):
            self.a_laby = 0
            self.b_laby = 0
            self.c_laby = 0
            self.d_laby = 0
            self.sum_code = ""

        def nouv_code(self):
            (a_l, b_l,c_l, d_l) = random_code_lab()
            self.a_laby = a_l
            self.b_laby = b_l
            self.c_laby = c_l
            self.d_laby = d_l
            self.sum_code = Choix_laby[self.a_laby] + Choix_laby[self.b_laby] + Choix_laby[self.c_laby] + Choix_laby[self.d_laby]

        def verif(code):
            return (self.sum_code == code)

    class Bon_chem():
        def __init__(self):
            self.n_laby = 0
            self.a_laby = 0
            self.b_laby = 0
            self.c_laby = 0

        def nouv_code(self,n):
            if n == 2:
                self.n_laby = renpy.random.randint(1,2)
                self.a_laby = renpy.random.randint(0,len(Choix_laby)-1)
                self.b_laby = renpy.random.randint(0,len(Choix_laby)-1)
            else:
                self.n_laby = renpy.random.randint(1,3)
                self.a_laby = renpy.random.randint(0,len(Choix_laby)-1)
                self.b_laby = renpy.random.randint(0,len(Choix_laby)-1)
                self.c_laby = renpy.random.randint(0,len(Choix_laby)-1)
