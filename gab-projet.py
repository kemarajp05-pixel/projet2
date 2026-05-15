from fltk import *
from modelisation import *
from calque import *
from modèle import *
from vue import *
from solver import *
from time import sleep
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

def animer_solution(personnage, lst_blocs, objectif, liste_sauts):
    for vx, vy in liste_sauts:
        personnage["vitesse"] = (vx, vy)
        personnage["est_colle"] = False
        en_mouvement = True
        while en_mouvement:
            en_mouvement = pas(personnage, lst_blocs)
            rafraichir_ecran(personnage, lst_blocs, objectif)
            mise_a_jour()
            sleep(0.01)

if __name__ == "__main__":
    cree_fenetre(900, 620) #a voir si on peut faire avec (770,770) car fenetre trop grande
    
    mon_skin = gerer_accueil()
    if mon_skin:
        personnage = creer_personnage(285, 562, mon_skin)
        game = True
        menu_ouvert = False
    
    while game:                
        visee_figee = False
        en_phase_visee = True
        clic_pos = personnage["position"] 

        while en_phase_visee and game:
            ev = donne_ev()
            res_clic, est_droit, menu_ouvert = click(ev, menu_ouvert)
            sx, sy = position_souris()

            if not visee_figee:
                clic_pos = (sx, sy)
                
            if res_clic is not None:
                if not est_droit:
                    if res_clic[0] <= 120:
                        if res_clic[1] > 45 and menu_ouvert:
                            cx, cy = res_clic
                            solution = None
                            if 120 <= cy <= 160: 
                                solution = resoudre_naif(personnage, lst_blocs, objectif)
                            elif 180 <= cy <= 220: 
                                solution = resoudre_optimal(personnage, lst_blocs, objectif)
                            elif 240 <= cy <= 280: 
                                solution = resoudre_greedy(personnage, lst_blocs, objectif)
                            
                            if solution:
                                animer_solution(personnage, lst_blocs, objectif, solution)
                                menu_ouvert = False
                                en_phase_visee = False 
                    
                    else:
                        if menu_ouvert:
                            menu_ouvert = False
                        else:
                            visee_figee = True 

                elif est_droit:
                    if visee_figee:
                        en_phase_visee = False 

            v_cible = vect(personnage["position"], clic_pos)
            if vect_max(v_cible):
                pos_cor, v_cible = vect_cor(personnage["position"], v_cible)
                aff_x, aff_y = pos_cor
            else:
                aff_x, aff_y = clic_pos
            
            personnage["vitesse"] = v_cible
            rafraichir_ecran(personnage, lst_blocs, objectif, menu_ouvert)
            
            if (aff_x, aff_y) != personnage["position"]:
                vect_aff(personnage["position"], (aff_x, aff_y))
            
            mise_a_jour()
            
            if type_ev(ev) == "Quitte":
                game = False
                en_phase_visee = False

        if game:
            personnage["est_colle"] = False
            en_mouvement = True
            while en_mouvement and game:
                en_mouvement = pas(personnage, lst_blocs)
                rafraichir_ecran(personnage, lst_blocs, objectif, menu_ouvert)
                
                if victoire(personnage, objectif):
                    texte(450, 250, "Victoire ! 🎉", couleur="green", taille=40, ancrage="center")
                    mise_a_jour()
                    sleep(2)
                    game = False
                    en_mouvement = False
                
                ev_m = donne_ev()
                if type_ev(ev_m) == "Quitte":
                    game = False
                    en_mouvement = False
                mise_a_jour()
                sleep(0.01)
attend_fermeture()
    
