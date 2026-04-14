from fltk import *
from math import *

def click():
    ev= attend_ev()
    typeEv = type_ev(ev)
    x = abscisse(ev)
    y = ordonnee(ev)
    if typeEv == "ClicGauche":
        return (x, y), False
    if typeEv == "ClicDroit":
        return (x, y), True


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
    fonction qurafraichir_ecran()i vérifie si le vecteur dépasse un certain seuil ici 100
    """
    x, y = vect
    if norme(x,y)>50:
        return True
    return False

def vect_cor(position, vect1):
    """
    corrige le vecteur si vect_max est dépassé
    """
    x, y = position
    x2, y2 = vect1
    norme1 = norme(x2, y2)
    x2 = 75 * (x2/norme1)
    y2 = 75 * (y2/norme1)
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


def bouge(personnage, y_sol, rafraichir_ecran):
    """
    fonction pour redessiner l'écran à chaque pas.
    """
    x, y = personnage["position"]
    vx, vy = personnage["vitesse"]
    gx, gy = personnage["gravité"]
    delta = 1
    en_mouvement = True
    while en_mouvement:
        x = x + delta * vx
        y = y + delta * vy
        vx = vx + delta * gx
        vy = vy + delta * gy 
        if y >= y_sol:
            y = y_sol
            vx, vy = 0, 0
            en_mouvement = False
        if x < 0:
            x = 0
        if x > 900:
            x = 900
        personnage["position"] = (x, y)
        personnage["vitesse"] = (vx, vy)
        rafraichir_ecran(y_sol, personnage["position"])
        mise_a_jour()
        delta = 1 - personnage["temps"]
        if delta < 0:
            vx, vy = 0, 0
    return (x, y)           
            
