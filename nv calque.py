from fltk import *
from math import *

def click():
    ev = attend_ev()
    typeEv = type_ev(ev)
    if ev is None: return (0, 0), False
    x = abscisse(ev)
    y = ordonnee(ev)
    if typeEv == "ClicGauche":
        return (x, y), False
    if typeEv == "ClicDroit":
        return (x, y), True
    return (x, y), False

def vect(position, click):
    xp, yp = position
    xc, yc = click
    return (xc - xp, yc - yp)

def norme(x, y):
    return sqrt(x**2 + y**2)

def vect_max(v):
    return norme(v[0], v[1]) > 100

def vect_cor(position, v1):
    x, y = position
    vx, vy = v1
    n = norme(vx, vy)
    # On ramène le vecteur à une norme de 100
    vx_corr = 100 * (vx / n)
    vy_corr = 100 * (vy / n)
    return (x + vx_corr, y + vy_corr)

def bouge(personnage, y_sol, affichage_callback):
    """
    Simule le mouvement complet. 
    affichage_callback est une fonction pour redessiner l'écran à chaque pas.
    """
    x, y = personnage["position"]
    vx, vy = personnage["vitesse"]
    gx, gy = personnage["gravité"]
    delta = personnage["temps"]
    
    en_mouvement = True
    while en_mouvement:
        # --- PHYSIQUE : Vos équations ---
        # 1. Mise à jour position
        x = x + delta * vx
        y = y + delta * vy
        
        # 2. Mise à jour vitesse
        vx = vx + delta * gx
        vy = vy + delta * gy
        
        # --- GESTION DU SOL (Collision simple) ---
        if y >= y_sol:
            y = y_sol
            vx, vy = 0, 0
            en_mouvement = False
        
        # Mise à jour des données du personnage
        personnage["position"] = (x, y)
        personnage["vitesse"] = (vx, vy)
        
        # --- ANIMATION ---
        affichage_callback() # Appelle la fonction de dessin
        mise_a_jour()
        sleep(0.01) # Petit délai pour voir l'animation
        
    return (x, y)