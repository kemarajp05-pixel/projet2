from fltk import *
from modèle import *
from modelisation import *
from calque import *

lst_blocs = [
    (100, 480, 250, 500), 
    (320, 400, 470, 420),  
    (100, 320, 250, 340),  
]

objectif = (480, 250, 520, 300)

personnage = creer_personnage(285, 450)

if __name__ == "__main__":
    cree_fenetre(XMAX, 600)
    game = True
    victoire_atteinte = False

    while game and not victoire_atteinte:
        # Affichage initial
        rafraichir_ecran(personnage, lst_blocs, objectif)
        mise_a_jour()

        # Phase de visée : clic gauche pour viser, clic droit pour tirer
        clic_pos = personnage["position"]  # flèche par défaut sur le mouton
        valide = False
        while not valide:
            pos, valide = attendre_clic(personnage)
            if pos is not None:
                clic_pos = pos
            rafraichir_ecran(personnage, lst_blocs, objectif)
            if clic_pos != personnage["position"]:
                vect_aff(personnage["position"], clic_pos)
            mise_a_jour()

        # Phase de saut
        victoire_atteinte = bouge(personnage, lst_blocs,
                                  rafraichir_ecran, objectif, YMAX, XMAX)

    if victoire_atteinte:
        rafraichir_ecran(personnage, lst_blocs, objectif)
        texte(XMAX // 2, 250, "Victoire ! 🎉",
              couleur="green", taille=40, ancrage="center")
        mise_a_jour()

    attend_fermeture()

