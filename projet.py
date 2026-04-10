from fltk import *
from modelisation import *
from calque import *
from modèle import *

personnage= {
    "position": (450,600),
    "vitesse": (0,0)
    }

if __name__ == "__main__":
    cree_fenetre(900,900)
    affiche_sol(ymax)
    position = personnage["position"]
    aff_mouton(position)
    click = click()
    vect_aff(position, click)
    attend_fermeture()
    
