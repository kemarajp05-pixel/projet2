from fltk import *
from modelisation import *
from calque import *
from modèle import *

personnage= {
    "position": (450,600),
    "vitesse": (0,0),
    "gravité": (0,10),
    "temps": 0.1
    }
game = True

if __name__ == "__main__":
    cree_fenetre(900,900)
    affiche_sol(ymax)
    while game:
        aff_mouton(personnage["position"])
        click1 = click()
        personnage["vitesse"] = vect_aff(personnage["position"], click1)
        personnage["position"] = bouge(personnage["position"], personnage["vitesse"], personnage["gravité"], personnage["temps"])
    attend_fermeture()
    
