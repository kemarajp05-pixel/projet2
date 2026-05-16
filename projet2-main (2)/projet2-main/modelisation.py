# Les Yeux (Affichage)
from fltk import *
from modèle import LARGEUR, HAUTEUR

YMAX = 500
XMAX = 600


def aff_mouton(position):
    x, y = position
    texte(x, y, "🐑", couleur="black", taille=30, ancrage="nw")


def aff_objectif(objectif):
    x1, y1, x2, y2 = objectif
    rectangle(x1, y1, x2, y2, couleur="gold", remplissage="yellow")
    texte((x1+x2)//2, (y1+y2)//2, "🚪", taille=20, ancrage="center")


def vect_aff(position, clic_pos):
    x, y = position
    x1, y1 = clic_pos
    ligne(x + LARGEUR//2, y + HAUTEUR//2,
          x1, y1, "red", 3)
    fleche(x + LARGEUR//2, y + HAUTEUR//2,
           x1, y1, "red", 5)


def affiche_sol(ymax):
    largeur = largeur_fenetre()
    ligne(0, ymax, largeur, ymax, couleur="black", epaisseur=3)


def aff_plateforme(lst_blocs):
    for bloc in lst_blocs:
        x1, y1, x2, y2 = bloc
        rectangle(x1, y1, x2, y2, couleur="black", remplissage="brown")


def rafraichir_ecran(personnage, lst_blocs, objectif):
    efface_tout()
    affiche_sol(YMAX)
    aff_plateforme(lst_blocs)
    aff_objectif(objectif)
    aff_mouton(personnage["position"])

