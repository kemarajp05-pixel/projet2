from fltk import *
from modelisation import *
from calque import *
from modèle import *
from vue import *
   
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
    #niv 1
    #(100, 480, 250, 500, "vert", 0), (320, 400, 470, 420, "vert", 0),(400, 240, 550, 260, "vert", 0),(650, 160, 800, 180, "vert", 0),
    #niv 2
    #(50, 480, 200, 500, "vert", 0), (50, 230, 200, 250, "colle", 0), (170, 320, 320, 340, "vert", 0), (400, 120, 550, 140, "colle", 0),(570, 200, 720, 220, "vert", 0), (320, 320, 470, 340, "glace", 0), (470, 320, 620, 340, "glace", 0), (620, 320, 770, 340, "glace", 0), (750, 280, 900, 300, "elastique", 0),
    #pseudo niv 3
    #(100, 480, 250, 500, "derapage", 0), (320, 400, 470, 420, "derapage", 0),(400, 240, 550, 260, "derapage", 0),(650, 160, 800, 180, "derapage", 0),
    #niv 4
    #(400, 550, 500, 570, "elastique", 0),(550, 450, 650, 470, "amorti", 0),(320, 400, 470, 420, "colle", 0),(150, 380, 300, 400, "vert", 0),(-130, 200, 20, 220, "colle", 0),(300, 200, 450, 220, "vert", 0),(620, 160, 770, 180, "vert", 0)
]
objectif = (820, 20, 870, 90)
personnage = creer_personnage(285, 562,"images/mouton_blanc.png" )


if __name__ == "__main__":
    cree_fenetre(900, 620) #a voir si on peut faire avec (770,770) car fenetre trop grande
    #aff_acc()
    #bouton_parametre()
    game = True  
    while game:
        rafraichir_ecran(personnage, lst_blocs, objectif)
        click_droit = False
        while not click_droit:
            clic_pos, click_droit = click()
            xp, yp = personnage["position"]
            xp += 20
            v_cible = vect((xp,yp), clic_pos)
            clic_pos1 = clic_pos
            if vect_max(v_cible):
                clic_pos1, v_cible1 = vect_cor((xp,yp), v_cible, 40)
                clic_pos, v_cible = vect_cor((xp,yp), v_cible, 20)
            personnage["vitesse"] = v_cible
            rafraichir_ecran(personnage, lst_blocs, objectif)
            vect_aff((xp,yp), clic_pos1)
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
    
