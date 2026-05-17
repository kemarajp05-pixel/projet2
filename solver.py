from modèle import pas, victoire, creer_personnage, collision
from collections import deque
import copy
import math
import random


def bloc_sous_pieds(perso, lst_blocs):
    x, y = perso["position"]
    largeur_mouton = 40 
    hauteur_mouton = 40 
    
    for bloc in lst_blocs:
        x1, y1, x2, y2, type_bloc, angle_bloc = bloc
        bx_min, bx_max = min(x1, x2), max(x1, x2)
        by_min, by_max = min(y1, y2), max(y1, y2)
        if (x < bx_max and x + largeur_mouton > bx_min and 
            y + hauteur_mouton >= by_min and y < by_max):
            return type_bloc   
    return "vide"


def simuler_saut(perso_actuel, vx, vy, lst_blocs, objectif):
    p_test = copy.deepcopy(perso_actuel)
    p_test["vitesse"] = (vx, vy)
    p_test["est_colle"] = False
    compteur_securite = 0
    compteur_arret = 0
    touche_objectif = False 
    while compteur_arret < 2 and compteur_securite < 1000 and not touche_objectif:
        a_bouge = pas(p_test, lst_blocs)
        if not a_bouge:
            compteur_arret += 1
        else:
            compteur_arret = 0    
        if victoire(p_test, objectif):
            touche_objectif = True     
        compteur_securite += 1  
    return p_test

def calculer_distance(perso, objectif):
    x, y = perso["position"]
    ox = (objectif[0] + objectif[2]) / 2
    oy = (objectif[1] + objectif[3]) / 2
    return math.sqrt((x - ox) ** 2 + (y - oy) ** 2)


def creer_cle_etat(perso):
    x, y = perso["position"]
    vx, vy = perso["vitesse"]
    est_colle = perso.get("est_colle", False)
    return (int(x // 10), int(y // 10), int(vx // 5), int(vy // 5), est_colle)


def generer_sauts():
    sauts = []
    for vx in range(-20, 21, 5):
        for vy in range(-25, 1, 5):
            sauts.append((vx, vy))
    return sauts


def extraire_distance(element):
    """ Renvoie la distance (le premier élément du tuple) pour le tri. """
    return element[0]


# SOLVER NAÏF 
def backtracking_recursif(perso, lst_blocs, objectif, visite, profondeur):
    if victoire(perso, objectif):
        return []
    if profondeur <= 0:
        return None
    type_sol = bloc_sous_pieds(perso, lst_blocs) 
    if type_sol in ["glace", "elastique", "derapage"]: 
        return None

    cle = creer_cle_etat(perso)
    if cle in visite:
        return None

    visite.add(cle)
    sauts_possibles = generer_sauts()
    random.shuffle(sauts_possibles)
    resultat_final = None

    i = 0
    while i < len(sauts_possibles) and resultat_final is None:
        vx, vy = sauts_possibles[i]
        p_apres = simuler_saut(perso, vx, vy, lst_blocs, objectif)
        if p_apres is not None:
            if victoire(p_apres, objectif):
                resultat_final = [(vx, vy)]
            else:
                res = backtracking_recursif(p_apres, lst_blocs, objectif, visite, profondeur - 1)
                if res is not None:
                    resultat_final = [(vx, vy)] + res
        i += 1
    return resultat_final


# SOLVER OPTIMAL
def solver_optimal(perso_depart, lst_blocs, objectif):
    file_attente = deque([(perso_depart, [])])
    visite = set()
    solution = None

    while len(file_attente) > 0 and solution is None:
        p_actuel, chemin = file_attente.popleft()
        if victoire(p_actuel, objectif):
            solution = chemin
        else:
            type_sol = bloc_sous_pieds(p_actuel, lst_blocs)
            if type_sol not in ["glace", "elastique", "derapage"]: 
                cle = creer_cle_etat(p_actuel)
            
                if cle not in visite:
                    visite.add(cle)
                    sauts = generer_sauts()
                
                    for vx, vy in sauts:
                        if solution is None:
                            p_suivant = simuler_saut(p_actuel, vx, vy, lst_blocs, objectif)
                            if p_suivant is not None:
                                if victoire(p_suivant, objectif):
                                    solution = chemin + [(vx, vy)]
                                else:
                                    file_attente.append((p_suivant, chemin + [(vx, vy)]))

    return solution


# SOLVER GREEDY
def solver_greedy_recursif(perso, lst_blocs, objectif, visite, profondeur):
    if victoire(perso, objectif):
        return []
    if profondeur <= 0:
        return None
    type_sol = bloc_sous_pieds(perso, lst_blocs)
    if type_sol in ["glace", "elastique", "derapage"]: 
        return None

    cle = creer_cle_etat(perso)
    if cle in visite:
        return None

    visite.add(cle)
    choix = []
    for vx, vy in generer_sauts():
        p_suivant = simuler_saut(perso, vx, vy, lst_blocs, objectif)
        if p_suivant is not None:
            distance = calculer_distance(p_suivant, objectif)
            choix.append((distance, vx, vy, p_suivant))

    choix.sort(key=extraire_distance)
    resultat_final = None
    i = 0
    while i < len(choix) and resultat_final is None:
        dist, vx, vy, p_suivant = choix[i]
        res = solver_greedy_recursif(p_suivant, lst_blocs, objectif, visite, profondeur - 1)
        
        if res is not None:
            resultat_final = [(vx, vy)] + res
        i += 1
    return resultat_final


# FONCTIONS DE LANCEMENT
def resoudre_naif(perso, blocs, obj):
    return backtracking_recursif(perso, blocs, obj, set(), profondeur=8)


def resoudre_optimal(perso, blocs, obj):
    return solver_optimal(perso, blocs, obj)


def resoudre_greedy(perso, blocs, obj):
    return solver_greedy_recursif(perso, blocs, obj, set(), profondeur=8)


