#sans fltk et sans print
import math
from calque import *
vmax = 15
gravité = (0, 1)
delta = 0.5
largeur = 40
hauteur = 40
XMAX = 900
YMAX = 600
# delta = 0.1
# g = 0.5 #(chute leger)
# f = 0.99
# ymax = 600
#sert à simuler les sauts, la gravité, et le résultat des collisions.
"""Tache 1 fini"""
"""tache 2"""
def creer_personnage(x, y, skin="images/mouton_blanc.png"):
    return {
        "position": (x, y),
        "vitesse": (0, 0),
        "skin": skin
    } 

def pas(personnage, lst_blocs):
    
    if personnage.get("est_colle",False):
        return False
    
    x_actuel, y_actuel = personnage["position"]
    vx, vy = personnage["vitesse"]
    gx, gy = gravité
    
    nv_vx = vx + delta * gx
    nv_vy = vy + delta * gy
    
    nv_x = x_actuel + delta * nv_vx
    nv_y = y_actuel + delta * nv_vy
    
    if nv_x < 0:
        nv_x = 0
        nv_vx = 0
    elif nv_x > XMAX - largeur:
        nv_x = XMAX - largeur
        nv_vx = 0
        
    if nv_y > YMAX - hauteur:
        nv_y = YMAX - hauteur
        nv_vx, nv_vy = 0, 0
        personnage["est_colle"] = False
        
    personnage["position"] = (nv_x, nv_y)
    personnage["vitesse"] = (nv_vx, nv_vy)
    
    bloc_touche = collision(personnage, lst_blocs)
    if bloc_touche is not None:
        choc(personnage, bloc_touche)
        
    return personnage["position"] != (x_actuel, y_actuel) or personnage["vitesse"] != (0, 0)

def collision(personnage, lst_blocs):
    x, y = personnage["position"]
    bloc_nonprio= None
    for bloc in lst_blocs:
        x1, y1, x2, y2, type_bloc, angle_bloc = bloc
        bx_min, bx_max = min(x1, x2), max(x1, x2)
        by_min, by_max = min(y1, y2), max(y1, y2)
        
        if (x < bx_max and x + largeur > bx_min and
            y < by_max and y + hauteur > by_min):
            
            if type_bloc == "elastique":
                return bloc
            
            if bloc_nonprio is None:
                bloc_nonprio = bloc
            
    return bloc_nonprio

def choc(personnage, bloc_touche):
    x, y = personnage["position"]
    vx, vy = personnage["vitesse"]
    x1, y1, x2, y2, type_bloc, angle_bloc = bloc_touche 
    
    bx_min, bx_max = min(x1, x2), max(x1, x2)
    by_min, by_max = min(y1, y2), max(y1, y2)

    if vy > 0:
        dist_v = (y + hauteur) - by_min # Choc par le haut du bloc
        bord_v = "HAUT"
    else:
        dist_v = by_max - y
        bord_v = "BAS"

    if vx > 0:
        dist_h = (x + largeur) - bx_min
        bord_h = "GAUCHE"
    else:
        dist_h = bx_max - x
        bord_h = "DROITE"

    if dist_v < dist_h:
        if bord_v == "HAUT":
            y = by_min - hauteur
        else:
            y = by_max
    else:
        if bord_h == "GAUCHE":
            x = bx_min - largeur
        else:
            x = bx_max
            
    if type_bloc == "derapage":
        if dist_v < dist_h:
            vy = 0
            vx = vx * 0.9
            if vx < 1:
                vx = 0
        else:     
            vx = 0
            
    elif type_bloc == "elastique":
        if dist_v < dist_h:
            if -1 < vy < 1:
                vy = 0
            else:
                vy = -vy
        else:
            if -1 < vx < 1:
                vx = 0
            else:
                vx = -vx
            
    elif type_bloc == "amorti":
        if dist_v < dist_h:
            if -1 < vy < 1:
                vy = 0
            else:
                vy = -vy * 0.3
        else:
            if -1 < vx < 1:
                vx = 0
            else:
                vx = -vx * 0.3
            
    elif type_bloc == "glace":
        if dist_v < dist_h:
            vy = 0
        else:
            vx = 0
            
    elif type_bloc == "colle":
        vx , vy = 0,0
        personnage["est_colle"] = True
    else:
        vx, vy = 0,0
        
    personnage["position"] = (x, y)
    personnage["vitesse"] = (vx, vy)
    
# def sol(personnage, ymax):
#     if personnage['y'] + personnage['hauteur'] > ymax:
#         personnage['y'] = ymax - personnage['hauteur']
#         personnage['vy'] = 0

def victoire(personnage, objectif):
    x, y = personnage["position"]
    ox1, oy1, ox2, oy2 = objectif
    bx_min, bx_max = min(ox1, ox2), max(ox1, ox2)
    by_min, by_max = min(oy1, oy2), max(oy1, oy2)
    return (x < bx_max and x + largeur > bx_min and
            y < by_max and y + hauteur > by_min)
    
    

