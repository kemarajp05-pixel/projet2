from fltk import *
from modelisation import *
from calque import *
from modèle import *

YMAX = 800

personnage = {
    "position": (450, 600),
    "vitesse": (0, 0),
    "gravité": (0, 10), 
    "temps": 0.2        
}

def rafraichir_ecran():
    """
    Fonction qui redessine tout le niveau
    """
    efface_tout()
    affiche_sol(YMAX)
    aff_mouton(personnage["position"])

if __name__ == "__main__":
    cree_fenetre(900, 900)
    game = True  
    while game:
        rafraichir_ecran()
        click_droit = False
        while not click_droit:
            clic_pos, click_droit = click()
            v_cible = vect(personnage["position"], clic_pos)
            personnage["vitesse"] = v_cible
            rafraichir_ecran()
            vect_aff(personnage["position"], clic_pos)
            mise_a_jour()
        bouge(personnage, YMAX)
    attend_fermeture()
    
