from fltk import *
from math import *

def click(ev, menu_ouvert):
    if ev is None:
        return None, False, menu_ouvert
    
    typeEv = type_ev(ev)
    x, y = abscisse(ev), ordonnee(ev)
    
    if typeEv == "ClicGauche":
        if x <= 120 and y <= 45:
            return (x, y), False, not menu_ouvert
        if menu_ouvert and 10 <= x <= 110 and 540 <= y <= 580:
            return "ACCUEIL", False, menu_ouvert
        return (x, y), False, menu_ouvert
    
    if typeEv == "ClicDroit":
        return (x, y), True, menu_ouvert
    
    return None, False, menu_ouvert


def position_souris():
    return (abscisse_souris(),ordonnee_souris())

def vect(position, click):
    """
    calcule le vecteur en fonction du point du mouton(position) et du click
    """
    xp, yp = position
    xc, yc = click
    vx = xc - xp
    vy = yc - yp
    return (vx, vy)


def norme(x, y):
    return sqrt(x**2 + y**2)


def vect_max(vect):
    """
    fonction qurafraichir_ecran()i vérifie si le vecteur dépasse un certain seuil ici 25
    """
    x, y = vect
    if norme(x,y)>25:
        return True
    return False

def vect_cor(position, vect1):
    """
    corrige le vecteur si vect_max est dépassé
    """
    x, y = position
    x2, y2 = vect1
    norme1 = norme(x2, y2)
    x2 = 25 * (x2/norme1)
    y2 = 25 * (y2/norme1)
    x1 = x + x2
    y1 = y + y2
    return (x1, y1), (x2, y2)


def angle(position, click, sol):
    """
    à refaire pas complet
    """
    x, y = vect(position, click)
    norme_v = norme(x,y)
    sol1 = (click[0],sol)
    x1, y1 = vect(sol1, click)
    norme_s = norme(x1,y1)
    return asin(norme_s/norme_v)

       
            
