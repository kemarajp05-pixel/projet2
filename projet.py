from fltk import *
from modelisation import *
from calque import *

personnage= {
    "position": (0,0),
    "vitesse": (0,0)
    }

if __name__ == "__main__":
    cree_fenetre(900,900)
    aff_mouton(personnage["position"])
    vect()
    attend_fermeture()