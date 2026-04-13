from fltk import *
from modelisation import *
from calque import *

# Paramètres du niveau
YMAX = 800

personnage = {
    "position": (450, 600),
    "vitesse": (0, 0),
    "gravité": (0, 10), # Accélération vers le bas
    "temps": 0.2        # Delta
}

def rafraichir_ecran():
    """Fonction qui redessine tout le niveau"""
    efface_tout()
    affiche_sol(YMAX)
    aff_mouton(personnage["position"])

if __name__ == "__main__":
    cree_fenetre(900, 900)
    game = True
    
    while game:
        rafraichir_ecran()
        
        # Phase de visée (Clic Gauche)
        click_droit = False
        while not click_droit:
            clic_pos, click_droit = click()
            
            # On recalcule la vitesse à chaque clic gauche
            v_cible = vect(personnage["position"], clic_pos)
            # On stocke le vecteur vitesse (pas la position cible)
            personnage["vitesse"] = v_cible
            
            rafraichir_ecran()
            # On affiche la flèche de prévisualisation
            vect_aff(personnage["position"], clic_pos)
            mise_a_jour()
        
        # Phase de saut (après Clic Droit)
        # On lance la simulation physique animée
        bouge(personnage, YMAX, rafraichir_ecran)
        
    attend_fermeture()