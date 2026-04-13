from fltk import *
from math import *
from modelisation import *
       
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
    fonction qui vérifie si le vecteur dépasse un certain seuil ici 100
    """
    x, y = vect
    if norme(x,y)>100:
        return True
    return False

def vect_cor(position, vect1):
    """
    corrige le vecteur si vect_max est dépassé
    """
    x, y = position
    x2, y2 = vect1
    norme1 = norme(x2, y2)
    x2 = 100 * (x2/norme1)
    y2 = 100 * (y2/norme1)
    x1 = x + x2
    y1 = y + y2
    return (x1, y1)


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


def bouge(personnage, y_sol, affichage_callback):
    """
    fonction pour redessiner l'écran à chaque pas.
    """
    x, y = personnage["position"]
    vx, vy = personnage["vitesse"]
    gx, gy = personnage["gravité"]
    delta = personnage["temps"]
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
        personnage["position"] = (x, y)
        personnage["vitesse"] = (vx, vy)
        affichage_callback()
        mise_a_jour()
    return (x, y)           
            