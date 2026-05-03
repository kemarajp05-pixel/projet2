from fltk import *
from modelisation import *
from calque import *
from modèle import *
   
# # # ne pas touché ca ca marche
#     (100, 480, 250, 500,"colle",0), 
#     (320, 400, 470, 420, "glace",0),  
#     (100, 320, 250, 340, "vert",0),
# #     #test vertgical
# #     (0, 120, 200, 500, "colle", 0), # Mur de colle tourné
# #     (0, 320, 20,480, "colle_vertical", 0)
# ]
# #(100, 480, 250, 500 , "colle"),
# #(x1 [gauche],y1 [haut],x2 [droit],y2[bas])
# 
# # objectif = (480, 250, 520, 300)

lst_blocs = [
    #sol NE PAS TOUCHER SVP
    (0, 600, 150, 620, "vert", 0),
    (150, 600, 300, 620, "vert", 0),
    (300, 600, 450, 620, "vert", 0),
    (450, 600, 600, 620, "vert", 0),
    (600, 600, 750, 620, "vert", 0),
    (750, 600, 900, 620, "vert", 0),
    
    #platefrome
    (100, 480, 250, 500, "vert", 0),  
    (320, 400, 470, 420, "colle", 0), 
    (550, 320, 700, 340, "glace", 0), 
    (400, 240, 550, 260, "vert", 0),  
    (650, 160, 800, 180, "colle", 0),
    (750, 590, 900, 610, "derapage", 0),
    (400, 550, 500, 570, "elastique", 0),
    (550, 450, 650, 470, "amorti", 0),
        
]
objectif = (820, 20, 870, 90)
personnage = creer_personnage(285, 562,"images/mouton_blanc.png" )


if __name__ == "__main__":
    cree_fenetre(900, 620) #a voir si on peut faire avec (770,770) car fenetre trop grande
    game = True  
    while game:
        rafraichir_ecran(personnage, lst_blocs, objectif)
        click_droit = False
        while not click_droit:
            clic_pos, click_droit = click()
            v_cible = vect(personnage["position"], clic_pos)
            if vect_max(v_cible):
                clic_pos, v_cible = vect_cor(personnage["position"], v_cible)
            personnage["vitesse"] = v_cible
            rafraichir_ecran(personnage, lst_blocs, objectif)
            vect_aff(personnage["position"], clic_pos)
            mise_a_jour()
        personnage["est_colle"] = False
        en_mouvement = True
        while en_mouvement:
            en_mouvement = pas(personnage, lst_blocs)
            rafraichir_ecran(personnage, lst_blocs, objectif)
            if victoire(personnage, objectif):
                texte(XMAX // 2, 250, "Victoire ! 🎉",
                      couleur="green", taille=40, ancrage="center")
                game = False
                en_mouvement = False
            mise_a_jour()
    attend_fermeture()
    
