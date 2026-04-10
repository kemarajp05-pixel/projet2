from fltk import *
from calque import *

def aff_mouton(position):
    x, y= position
    rectangle(x ,y ,x+50 ,y+50 , "black", "black")

def vect_aff(position, click):
    #à compléter 

def affiche_sol(ymax):
    largeur = largeur_fenetre() 
    ligne(0, ymax, largeur, ymax, couleur="black", epaisseur=3)
