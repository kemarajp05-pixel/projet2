from fltk import *
from modelisation import *
from calque import *

personnage= {
    "position": (450,800),
    "vitesse": (0,0)
    }
sol = 800

if __name__ == "__main__":
    cree_fenetre(900,900)
    position=personnage["position"]
    aff_mouton(position)
    click = click()
    print(angle(position, click, sol))
    vect_aff(position, click)
    attend_fermeture()