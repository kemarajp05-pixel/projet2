from fltk import *
from calque import *

def aff_mouton(position):
    x, y = position
    texte(x-40, y-40, "🐑", couleur="black", taille=40)

def vect_aff(position, click):
    x, y = position
    x1, y1 = click
    vect1 = vect(position, click)
    if vect_max(vect1):
        x2, y2 = vect1
        norme1 = norme(x2, y2)
        x2 = 100 * (x2/norme1)
        y2 = 100 * (y2/norme1)
        x1 = x + x2
        y1 = y + y2
    ligne(x, y, x1, y1,"red", 4)
    fleche(x, y, x1, y1,"red", 6)

def affiche_sol(ymax):
    largeur = largeur_fenetre() 
    ligne(0, ymax, largeur, ymax, couleur="black", epaisseur=3)
    
