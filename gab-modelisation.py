# Les Yeux (Affichage)
from fltk import *
from modèle import *


# def aff_mouton(personnage):
#     x, y = personnage["position"]
# #     texte(x, y, "🐑", couleur="black", taille=30, ancrage="nw")
#     chemin_skin = personnage["skin"]
#     image(x, y, chemin_skin, largeur=largeur, hauteur=hauteur, ancrage="nw")
#     #rectangle(x+17, y+5, (x + largeur)-14, (y + hauteur)-4, couleur="blue", remplissage="", epaisseur=2)
#     rectangle(x, y, (x + largeur), (y + hauteur), couleur="blue", remplissage="", epaisseur=2)

def aff_mouton(personnage):
    x, y = personnage["position"]
    chemin_skin = personnage["skin"] 
    image(x-15, y -((50 - hauteur) // 2), chemin_skin,
          largeur=70, hauteur=50, ancrage="nw")
    #rectangle(x, y, (x + largeur), (y + hauteur), couleur="blue", remplissage="", epaisseur=2)

def aff_objectif(objectif):
    x1, y1, x2, y2 = objectif
    rectangle(x1, y1, x2, y2, couleur="gold", remplissage="yellow")
    texte((x1+x2)//2, (y1+y2)//2, "🚪", taille=20, ancrage="center")


def vect_aff(position, clic_pos):
    x, y = position
    x1, y1 = clic_pos
    distance = math.sqrt((x1 - x)**2 + (y1 - y)**2)
    if distance > 1:
        ligne(x, y, x1, y1,"red", 4)
        fleche(x, y, x1, y1,"red", 6)


def affiche_sol(ymax):
    largeur = largeur_fenetre()
    #ligne(0, ymax, largeur, ymax, couleur="black", epaisseur=3)


# def aff_plateforme(lst_blocs):
#     for bloc in lst_blocs:
#         x1, y1, x2, y2 = bloc
#         rectangle(x1, y1, x2, y2, couleur="black", remplissage="brown")

def aff_plateforme(lst_blocs):
    images_blocs = {
        "colle" : "images/bloc_colle.png",
        "glace" : "images/bloc_glace.png",
        "vert": "images/bloc_vert.png",
        "teleporteur" : "images/teleporteur.png",
        "derapage" : "images/bloc_derapage.png",
        "elastique" : "images/bloc_elastique.png",
        "amorti" : "images/bloc_amorti.png",
        }
    for bloc in lst_blocs:
        x1, y1, x2, y2, type_bloc, angle_bloc = bloc
        ax = min(x1-32, x2)
        ay = min(y1, y2)
        larg_bloc = max(x1, x2+32) - ax
        haut_bloc = max(y1, y2) - ay
        chemin_image = images_blocs.get(type_bloc)
        image(ax-61, ay-3, chemin_image, 
              largeur=larg_bloc+123 , hauteur=haut_bloc+5, ancrage='nw',angle=angle_bloc)
        #rectangle(x1, y1, x2, y2, couleur='red', remplissage='')

# def aff_plateforme(lst_blocs):
#     images_blocs = {
#         "colle" : "images/bloc_colle.png",
#         "glace" : "images/bloc_glace.png",
#         "vert": "images/bloc_vert.png",
#         "teleporteur" : "images/teleporteur.png"
#         }
#     for bloc in lst_blocs:
# 
#         x1, y1, x2, y2, type_bloc, angle_bloc = bloc
# 
#         ax = min(x1, x2)
#         ay = min(y1, y2)
# 
#         larg_bloc = abs(x1 - x2)
#         haut_bloc = abs(y1 - y2)
#         chemin_image = images_blocs.get(type_bloc)  
#         image(ax, ay, chemin_image, 
#               largeur=larg_bloc, hauteur=haut_bloc, ancrage='nw', angle=angle_bloc)
#         rectangle(x1, y1, x2, y2, couleur='red', remplissage='')
        
def rafraichir_ecran(personnage, lst_blocs, objectif, menu_ouvert = False):
    efface_tout()
    rectangle(0, 0, XMAX, 620, couleur="#87CEEB", remplissage="#87CEEB")
    affiche_sol(YMAX)
    aff_plateforme(lst_blocs)
    aff_objectif(objectif)
#     aff_mouton(personnage["position"])
    aff_mouton(personnage)
    aff_boutons_solver(menu_ouvert)

def aff_boutons_solver(menu_ouvert):
    rectangle(5, 5, 115, 45, couleur="white", remplissage="#4A4A4A", epaisseur=2)
    texte(60, 25, "OPTIONS", "white", taille=12, ancrage="center")
    if menu_ouvert:
        rectangle(0, 0, 120, 600, couleur="black", remplissage="#222222")
        texte(60, 80, "SOLVERS", "white", taille=14, ancrage="center")

        rectangle(10, 120, 110, 160, couleur="white", remplissage="#3F3F3F")
        texte(60, 140, "NAÏF", "white", taille=10, ancrage="center")

        rectangle(10, 180, 110, 220, couleur="white", remplissage="#3F3F3F")
        texte(60, 200, "OPTIMAL", "white", taille=10, ancrage="center")

        rectangle(10, 240, 110, 280, couleur="white", remplissage="#3F3F3F")
        texte(60, 260, "GREEDY", "white", taille=10, ancrage="center")

        rectangle(10, 540, 110, 580, couleur="white", remplissage="#3F3F3F")
        texte(60, 560, "ACCUEIL", "white", taille=12, ancrage="center")
        
        texte(60, 590, "clic pour fermer", "gray", taille=8, ancrage="center")
        
        