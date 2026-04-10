from fltk import *
from modelisation import *
from calque import *
from modèle import *

personnage= {
    "position": (100,100),
    "vitesse": (0,0)
    }

if __name__ == "__main__":
    cree_fenetre(900,900)
    affiche_sol(ymax)
    aff_mouton(personnage["position"])
    print(click())
    attend_fermeture()
    
