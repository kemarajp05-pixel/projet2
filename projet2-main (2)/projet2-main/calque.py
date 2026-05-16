# Calque - gestion des événements
from fltk import *
from modèle import *


def attendre_clic(personnage):
    """
    Attend un clic de l'utilisateur.
    - Clic gauche : met à jour la vitesse du personnage et renvoie (clic_pos, False)
    - Clic droit  : valide le saut et renvoie (clic_pos, True)
    """
    ev = attend_ev()
    typeEv = type_ev(ev)
    x = abscisse(ev)
    y = ordonnee(ev)
    clic_pos = (x, y)

    if typeEv == "ClicGauche":
        clic_vers_vitesse(personnage, clic_pos)
        return clic_pos, False

    if typeEv == "ClicDroit":
        clic_vers_vitesse(personnage, clic_pos)
        return clic_pos, True

    return None, None


def bouge(personnage, lst_blocs, rafraichir_ecran, objectif, ymax=600, xmax=600):
    """
    Anime le mouton pas par pas jusqu'à ce qu'il soit au repos.
    Renvoie True si victoire, False sinon.
    """
    en_mouvement = True
    while en_mouvement:
        en_mouvement = pas(personnage, lst_blocs, ymax, xmax)
        rafraichir_ecran(personnage, lst_blocs, objectif)
        mise_a_jour()
        if victoire(personnage, objectif):
            return True
    return False

