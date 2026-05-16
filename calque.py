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
    fonction qurafraichir_ecran()i vérifie si le vecteur dépasse un certain seuil ici 20
    """
    x, y = vect
    if norme(x,y)>40:
        return True
    return False

def vect_cor(position, vect1, echelle):
    """
    corrige le vecteur à l'echelle
    """
    x, y = position
    x2, y2 = vect1
    norme1 = norme(x2, y2)
    x2 = echelle * (x2/norme1)
    y2 = echelle * (y2/norme1)
    x1 = x + x2
    y1 = y + y2
    return (x1, y1), (x2, y2)


       
            
