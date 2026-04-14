from fltk import *
from modelisation import *
from calque import *
from modèle import *

YMAX = 800

personnage = {
    "position": (450, 800),
    "vitesse": (0, 0),
    "gravité": (0, 10), 
    "temps": 0.2        
}


if __name__ == "__main__":
    cree_fenetre(900, 900)
    game = True  
    while game:
        rafraichir_ecran(YMAX, personnage["position"])
        click_droit = False
        while not click_droit:
            clic_pos, click_droit = click()
            v_cible = vect(personnage["position"], clic_pos)
            if vect_max(v_cible):
                clic_pos, v_cible = vect_cor(personnage["position"], v_cible)
            personnage["vitesse"] = v_cible
            rafraichir_ecran(YMAX, personnage["position"])
            vect_aff(personnage["position"], clic_pos)
            mise_a_jour()
        bouge(personnage, YMAX, rafraichir_ecran)
    attend_fermeture()
    
