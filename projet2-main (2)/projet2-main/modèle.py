# Cerveau (physique) - sans fltk et sans print
from math import sqrt

# Constantes
VMAX = 15        # vitesse maximale que le joueur peut donner
GRAVITE = (0, 1) # vecteur gravité
PAS = 0.5        # pas de la simulation
LARGEUR = 30     # largeur du personnage en pixels
HAUTEUR = 40     # hauteur du personnage en pixels


def creer_personnage(x, y):
    return {
        "position": (x, y),
        "vitesse": (0, 0)
    }


def clic_vers_vitesse(personnage, clic):
    """
    Donne au personnage la vitesse définie par le vecteur entre sa position
    et le clic, dans la limite de VMAX.
    """
    x, y = personnage["position"]
    xc, yc = clic
    vx = xc - x
    vy = yc - y
    norme = sqrt(vx**2 + vy**2)
    if norme > VMAX:
        vx = VMAX * vx / norme
        vy = VMAX * vy / norme
    personnage["vitesse"] = (vx, vy)


def collision(personnage, lst_blocs):
    """
    Renvoie le bloc avec lequel le personnage est en collision, ou None.
    Un bloc est un tuple (x1, y1, x2, y2).
    """
    x, y = personnage["position"]
    for bloc in lst_blocs:
        bx, by, bx2, by2 = bloc
        if (x < bx2 and x + LARGEUR > bx and
                y < by2 and y + HAUTEUR > by):
            return bloc
    return None


def cote_collision(personnage, bloc):
    """
    Détermine par quel côté le personnage entre en collision avec le bloc.
    Renvoie 'dessus', 'dessous', 'gauche' ou 'droite'.
    """
    vx, vy = personnage["vitesse"]
    x, y = personnage["position"]
    bx, by, bx2, by2 = bloc

    candidats = []
    if vy > 0:
        candidats.append(('dessus',  (y + HAUTEUR) - by))
    if vy < 0:
        candidats.append(('dessous', by2 - y))
    if vx > 0:
        candidats.append(('gauche',  (x + LARGEUR) - bx))
    if vx < 0:
        candidats.append(('droite',  bx2 - x))

    if not candidats:
        return 'dessus'

    return min(candidats, key=lambda c: c[1])[0]


def choc(personnage, bloc):
    """
    Choc mou : replace le personnage sur le bord du bloc et annule la vitesse.
    """
    x, y = personnage["position"]
    bx, by, bx2, by2 = bloc
    cote = cote_collision(personnage, bloc)

    if cote == 'dessus':
        personnage["position"] = (x, by - HAUTEUR)
    elif cote == 'dessous':
        personnage["position"] = (x, by2)
    elif cote == 'gauche':
        personnage["position"] = (bx - LARGEUR, y)
    elif cote == 'droite':
        personnage["position"] = (bx2, y)

    personnage["vitesse"] = (0, 0)


def sol(personnage, ymax, xmax):
    """
    Gère les bords de l'écran, renvoie True si une modification a eu lieu.
    """
    x, y = personnage["position"]
    vx, vy = personnage["vitesse"]
    modifie = False

    if y + HAUTEUR >= ymax:
        y = ymax - HAUTEUR
        vx, vy = 0, 0
        modifie = True
    if y < 0:
        y = 0
        vy = 0
        modifie = True
    if x < 0:
        x = 0
        vx = 0
        modifie = True
    if x + LARGEUR > xmax:
        x = xmax - LARGEUR
        vx = 0
        modifie = True

    personnage["position"] = (x, y)
    personnage["vitesse"] = (vx, vy)
    return modifie


def pas(personnage, lst_blocs, ymax=600, xmax=600):
    """
    Réalise un pas élémentaire de la simulation.
    Renvoie True si la position ou vitesse a changé (mouton encore en mouvement).
    """
    gx, gy = GRAVITE
    x, y = personnage["position"]
    vx, vy = personnage["vitesse"]

    pos_avant = personnage["position"]
    vit_avant = personnage["vitesse"]

    vx += PAS * gx
    vy += PAS * gy
    x  += PAS * vx
    y  += PAS * vy

    personnage["position"] = (x, y)
    personnage["vitesse"]  = (vx, vy)

    bloc = collision(personnage, lst_blocs)
    if bloc:
        choc(personnage, bloc)

    sol(personnage, ymax, xmax)

    return (personnage["position"] != pos_avant or
            personnage["vitesse"]  != vit_avant)


def victoire(personnage, objectif):
    """
    Renvoie True si le personnage a atteint l'objectif.
    objectif = (x1, y1, x2, y2)
    """
    x, y = personnage["position"]
    ox1, oy1, ox2, oy2 = objectif
    return (x < ox2 and x + LARGEUR > ox1 and
            y < oy2 and y + HAUTEUR > oy1)

