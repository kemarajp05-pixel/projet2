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

def clic_vers_vitesse(personnage, clic):
    personnage["est_colle"] = False
    x, y = personnage["position"]
    xc, yc = clic
    vx = xc - x
    vy = yc - y
    norme = sqrt(vx**2 + vy**2)
    if norme > vmax:
        vx = vmax * vx / norme
        vy = vmax * vy / norme
    personnage["vitesse"] = (vx, vy)


#def pas(personnage, lst_blocs):
#     personnage['vy'] += g*delta #gravité deplacement
#     personnage['x'] += personnage['vx']*delta
#     personnage['y'] += personnage['vy']*delta
#     if collision(personnage, lst_blocs):
#         choc(personnage, lst_blocs)
#     sol(personnage, ymax)
#---------------------------------------------------------------------
#def pas(personnage, lst_blocs):
#     gx, gy = gravite
#     x, y = personnage["position"]
#     vx, vy = personnage["vitesse"]
# 
#     position_avant = personnage["position"]
#     vitesse_avant = personnage["vitesse"]
# 
#     vx += pas * gx
#     vy += pas * gy
#     x  += pas * vx
#     y  += pas * vy
# 
#     personnage["position"] = (x, y)
#     personnage["vitesse"]  = (vx, vy)
# 
#     bloc = collision(personnage, lst_blocs)
#     if bloc:
#         choc(personnage, bloc)
# 
#     sol(personnage, ymax, xmax)
# 
#     return (personnage["position"] != position_avant or
#             personnage["vitesse"]  != vitesse_avant)
    
# def pas(personnage,lst_blocs):
#     x, y = personnage["position"]
#     vx, vy = personnage["vitesse"]
#     gx, gy = gravite
#     
#     nv_x = x + pas * vx
#     nv_y = y + pas * vy
#     
#     nv_vx = vx + pas * gx
#     nv_vy = vy + pas * gy
#     if nv_x < 0:
#         nvb_x = 0
#     elif nv_x > 900:
#         nv_x = 900
#     
#     if nv_y >= y_sol:
#         nv_y = y_sol
#         nv_vx,nv_vy = 0,0
#         
#     position_av = (x, y)
#     
#     personnage["position"] = (nv_x, nv_y)
#     personnage["vitesse"] = (nv_vx, nv_vy)
# 
#     bloc_touche = collision(personnage,lst_blocs)
#     if bloc_touche:
#         personnage["position"] = position_av # On recule
#         choc(personnage, bloc_touche)
# 
#     return (personnage["position"] != position_av or 
#             personnage["vitesse"] != (0,0))

# def un_pas_de_jeu(personnage, lst_blocs):
#     """
#     fonction pour redessiner l'écran à chaque pas.
#     """
#     x, y = personnage["position"]
#     vx, vy = personnage["vitesse"]
#     gx, gy = gravite
#     delta = 0.5
#     en_mouvement = True
#     while en_mouvement:
#         x = x + delta * vx
#         y = y + delta * vy
#         if y < 0:
#             y = 0
#             vy = 0
#             
#         if x < 0:
#             x = 0
#             vx = -vx * 0.5
#             
#         if x > 900 - 30:  
#             x = 900 - 30
#             vx = -vx * 0.5
#             
#         vx = vx + delta * gx
#         vy = vy + delta * gy 
#         if y >= y_sol:
#             y = y_sol
#             vx, vy = 0, 0
#             en_mouvement = False
#         for bloc in lst_blocs:
#             x1, y1, x2, y2 = bloc
#             bx_min, bx_max = min(x1, x2), max(x1, x2)
#             by_min, by_max = min(y1, y2), max(y1, y2)
#             if (x < bx_max and x + 30 > bx_min and 
#                 y < by_max and y + 40 > by_min):  
#                 if vy > 0:
#                     y = by_min - 40
#                 vx, vy = 0, 0
#                 en_mouvement = False
#                 
#         personnage["position"] = (x, y)
#         personnage["vitesse"] = (vx, vy)
#         rafraichir_ecran(personnage, lst_blocs, objectif)
#         mise_a_jour()
# #         delta = 1 - personnage["temps"]
# #         if delta < 0:
# #             vx, vy = 0, 0
#     return (x, y)

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

# def collision(personnage, lst_blocs):
#     x, y = personnage["position"]
#     for (c1, c2) in lst_blocs:
#         bx_min, bx_max = min(c1[0], c2[0]), max(c1[0], c2[0])
#         by_min, by_max = min(c1[1], c2[1]), max(c1[1], c2[1])
#         if (x < bx_max and x + largeur > bx_min and
#             y < by_max and y + hauteur > by_min):
#             return (c1, c2)
#     return None

def collision(personnage, lst_blocs):
    x, y = personnage["position"]
    for bloc in lst_blocs:
        x1, y1, x2, y2, type_bloc, angle_bloc = bloc
        bx_min, bx_max = min(x1, x2), max(x1, x2)
        by_min, by_max = min(y1, y2), max(y1, y2)
        
        if (x < bx_max and x + largeur > bx_min and
            y < by_max and y + hauteur > by_min):
            return bloc
            
    return None



# def choc(personnage, lst_blocs):
#     personnage["vitesse"] = (0,0)
#     #A voir si on peut l'améliorer
#     # récupérerfonction collision le bloc avec
#     #lequel le personnage est en collision
#     #S’il n’y en a pas, on s’arrête là.

# def choc(personnage, bloc_touche):
# 
#     x, y = personnage["position"]
#     vx, vy = personnage["vitesse"]
#     x1, y1, x2, y2 = bloc_touche
#     by_min = min(y1, y2)
#     
#     if vy > 0:
#         y = by_min - hauteur
#         
#     personnage["position"] = (x, y)
#     personnage["vitesse"] = (0, 0)

# def choc(personnage, bloc_touche):
#     x, y = personnage["position"]
#     vx, vy = personnage["vitesse"]
#     x1, y1, x2, y2 = bloc_touche
#     
#     bx_min, bx_max = min(x1, x2), max(x1, x2)
#     by_min, by_max = min(y1, y2), max(y1, y2)
#     
#     rentre_x = 9999
#     rentre_y = 9999
#     
#     if vx > 0:
#         rentre_x = (x + largeur) - bx_min
#     elif vx < 0:
#         rentre_x = bx_max - x
#         
#     if vy > 0:
#         rentre_y = (y + hauteur) - by_min
#     elif vy < 0:
#         rentre_y = by_max - y
#         
#     if rentre_x < rentre_y:
#         if vx > 0:
#             x = bx_min - largeur
#         elif vx < 0:
#             x = bx_max
#         vx = -vx * 0.8 # moins 20% de sa vitesse suit au choc
#     else:
#         if vy > 0:
#             y = by_min - hauteur
#         elif vy < 0:
#             y = by_max
#         vy = -vy * 0.8
#             
#     personnage["position"] = (x, y)
#     personnage["vitesse"] = (0, 0)
"""
def choc(personnage, bloc_touche):
    x, y = personnage["position"]
    vx, vy = personnage["vitesse"]
    x1, y1, x2, y2, type_bloc, angle_bloc= bloc_touche
    
    bx_min, bx_max = min(x1, x2), max(x1, x2)
    by_min, by_max = min(y1, y2), max(y1, y2)

    if vy > 0:
        dist_v = (y + hauteur) - by_min  # Choc par le haut du bloc
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
    
    if type_bloc == "elastique":
        rebond = 1.4  
        if dist_v < dist_h:
            vy = -vy * rebond 
        else:
            vx = -vx * rebond
            
    if type_bloc == "glace":
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
"""
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
            vy = -vy
        else:
            vx = -vx
            
    elif type_bloc == "amorti":
        if dist_v < dist_h:
            vy = -vy * 0.5
        else:
            vx = -vx * 0.5
            
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
    
    

