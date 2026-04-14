from fltk import *
from calque import *

def aff_mouton(position):
    x, y = position
    texte(x-40, y-40, "🐑", couleur="black", taille=40)


def vect_aff(position, click):
    x, y = position
    x1, y1 = click
    ligne(x, y, x1, y1,"red", 4)
    fleche(x, y, x1, y1,"red", 6)


def affiche_sol(ymax):
    largeur = largeur_fenetre() 
    ligne(0, ymax, largeur, ymax, couleur="black", epaisseur=3)


def rafraichir_ecran(YMAX, mouton):
    efface_tout()
    affiche_sol(YMAX)
    aff_mouton(mouton)
    
