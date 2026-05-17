from fltk import *
from modelisation import *
from calque import *
from modèle import *
from vue import *
from solver import *
from time import sleep


NIVEAU_1_BLOCS = [
    (0, 600, 150, 620, "vert", 0),
    (150, 600, 300, 620, "vert", 0),
    (300, 600, 450, 620, "vert", 0),
    (450, 600, 600, 620, "vert", 0),
    (600, 600, 750, 620, "vert", 0),
    (750, 600, 900, 620, "vert", 0),
    (100, 480, 250, 500, "colle", 0), 
    (320, 400, 470, 420, "glace", 0),  
    (100, 320, 250, 340, "vert", 0)
]
NIVEAU_1_OBJECTIF = (480, 250, 520, 300)

NIVEAU_2_BLOCS = [
    (0, 600, 150, 620, "vert", 0),
    (150, 600, 300, 620, "vert", 0),
    (300, 600, 450, 620, "vert", 0),
    (450, 600, 600, 620, "vert", 0),
    (600, 600, 750, 620, "vert", 0),
    (750, 600, 900, 620, "vert", 0),

    (100, 480, 250, 500, "vert", 0),  
    (320, 400, 470, 420, "colle", 0), 
    (550, 320, 700, 340, "glace", 0), 
    (400, 240, 550, 260, "vert", 0),  
    (650, 160, 800, 180, "colle", 0),
    (750, 590, 900, 610, "derapage", 0),
    (400, 550, 500, 570, "elastique", 0),
    (550, 450, 650, 470, "amorti", 0),
]
NIVEAU_2_OBJECTIF = (820, 20, 870, 90)

personnage = creer_personnage(285, 562,"images/mouton_blanc.png" )

def animer_solution(personnage, lst_blocs, objectif, liste_sauts):
    points_trajectoire = []
    victoire_atteinte = False
    i = 0
    while i < len(liste_sauts) and not victoire_atteinte:
        vx, vy = liste_sauts[i]
        personnage["vitesse"] = (vx, vy)
        personnage["est_colle"] = False
        compteur_arret = 0
        while compteur_arret < 2 and not victoire_atteinte:
            a_bouge = pas(personnage, lst_blocs)
            if not a_bouge:
                compteur_arret += 1
            else:
                compteur_arret = 0
                
            px, py = personnage["position"]
            points_trajectoire.append((px, py))
            if victoire(personnage, objectif):
                x1, y1, x2, y2 = objectif
                personnage["position"] = ((x1+x2)//2 - 20, (y1+y2)//2 - 20)
                personnage["vitesse"] = (0, 0)
                personnage["est_colle"] = True 
                victoire_atteinte = True
            else:
                sleep(0.01)
                
            rafraichir_ecran(personnage, lst_blocs, objectif, menu_ouvert=False)
            for pt_x, pt_y in points_trajectoire:
                cercle(pt_x, pt_y, 3, couleur="red", remplissage="red")
            mise_a_jour()    
        i += 1
            

if __name__ == "__main__":
    cree_fenetre(900, 620) #a voir si on peut faire avec (770,770) car fenetre trop grande
    appli_active = True
    while appli_active:
        
        mon_skin = gerer_accueil()
        if mon_skin is None:
            appli_active = False
            game = False
        else:
            choix = choisir_niveau()
            if choix is None:
                appli_active = False
                game = False
            else:
                if choix == 1:
                    lst_blocs = NIVEAU_1_BLOCS
                    objectif = NIVEAU_1_OBJECTIF
                    personnage = creer_personnage(170, 280, mon_skin)
                else:
                    lst_blocs = NIVEAU_2_BLOCS
                    objectif = NIVEAU_2_OBJECTIF
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
                        if res_clic == "ACCUEIL":
                            en_phase_visee = False
                            game = False
                        else :
                            if res_clic[0] <= 120:
                                cx, cy = res_clic 
                                if cy > 45 and menu_ouvert:
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

                    elif est_droit and visee_figee :
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
                    appli_active = False

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
                        appli_active = False
                    mise_a_jour()
                    sleep(0.01)
ferme_fenetre()
    
