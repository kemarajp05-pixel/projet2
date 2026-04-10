from fltk import *
from math import *
       
def click():
    ev= attend_ev()
    typeEv = type_ev(ev)
    if typeEv == "ClicGauche":
        x = abscisse(ev)
        y = ordonnee(ev)
        return (x, y)

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

def angle(position, click, sol):
    x, y = vect(position, click)
    norme_v = norme(x,y)
    sol1 = (click[0],sol)
    x1, y1 = vect(sol1, click)
    norme_s = norme(x1,y1)
    return asin(norme_s/norme_v)
    #à refaire

            
            