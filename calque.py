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
    xp, yp = position
    xc, yc = click
    vx = xc - xp
    vy = yc - yp
    return (vx, vy)

def norme(x, y):
    return sqrt(x**2 + y**2)

def vect_max(vect):
    x, y = vect
    if norme(x,y)>100:
        return True
    return False

def vect_cor(position, vect1):
    x, y = position
    x2, y2 = vect1
    norme1 = norme(x2, y2)
    x2 = 100 * (x2/norme1)
    y2 = 100 * (y2/norme1)
    x1 = x + x2
    y1 = y + y2
    return (x1, y1)

def bouge(position, vect, grav, temps):
    x, y = position
    x1, y1 = vect
    xg, yg = grav
    pas = 1
    while pas > 0:
        x = x + pas * x1
        y = y + pas * y1
        x1 = x1 + pas * xg
        y1 = y1 + pas * yg
        pas = pas - temps
    return (x,y)

def angle(position, click, sol):
    x, y = vect(position, click)
    norme_v = norme(x,y)
    sol1 = (click[0],sol)
    x1, y1 = vect(sol1, click)
    norme_s = norme(x1,y1)
    return asin(norme_s/norme_v)
    #à refaire, pas complet

            
            