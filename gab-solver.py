from modèle import pas, victoire, creer_personnage
from collections import deque
import copy
import math


def simuler_saut(perso_actuel, vx, vy, lst_blocs):
    p_test = copy.deepcopy(perso_actuel)
    p_test["vitesse"] = (vx, vy)
    p_test["est_colle"] = False
    en_mouvement = True
    compteur_securite = 0
    while en_mouvement and compteur_securite < 1000:
        en_mouvement = pas(p_test, lst_blocs)
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
    return (int(x // 10), int(y // 10), int(vx // 5), int(vy // 5), perso["est_colle"])


def generer_sauts():
    sauts = []
    for vx in range(-20, 21, 5):
        for vy in range(-25, 1, 5):
            sauts.append((vx, vy))
    return sauts


def extraire_distance(element):
    """ Renvoie la distance (le premier élément du tuple) pour le tri. """
    return element[0]


# SOLVER NAÏF (DFS)
def backtracking_recursif(perso, lst_blocs, objectif, visite, profondeur):
    if victoire(perso, objectif):
        return []
    if profondeur <= 0:
        return None

    cle = creer_cle_etat(perso)
    if cle in visite:
        return None

    visite.add(cle)
    sauts_possibles = generer_sauts()
    resultat_final = None

    i = 0
    while i < len(sauts_possibles) and resultat_final is None:
        vx, vy = sauts_possibles[i]
        p_apres = simuler_saut(perso, vx, vy, lst_blocs)
        res = backtracking_recursif(p_apres, lst_blocs, objectif, visite, profondeur - 1)
        
        if res is not None:
            resultat_final = [(vx, vy)] + res
        i += 1

    visite.remove(cle)
    return resultat_final


# 2. SOLVER OPTIMAL (BFS)
def solver_optimal(perso_depart, lst_blocs, objectif):
    file_attente = deque([(perso_depart, [])])
    visite = set()
    solution = None

    while len(file_attente) > 0 and solution is None:
        p_actuel, chemin = file_attente.popleft()
        if victoire(p_actuel, objectif):
            solution = chemin
        else:
            cle = creer_cle_etat(p_actuel)
            
            if cle not in visite:
                visite.add(cle)
                sauts = generer_sauts()
                
                for vx, vy in sauts:
                    p_suivant = simuler_saut(p_actuel, vx, vy, lst_blocs)
                    file_attente.append((p_suivant, chemin + [(vx, vy)]))

    return solution


# 3. SOLVER GREEDY (HEURISTIQUE)
def solver_greedy_recursif(perso, lst_blocs, objectif, visite, profondeur):
    if victoire(perso, objectif):
        return []
    if profondeur <= 0:
        return None

    cle = creer_cle_etat(perso)
    if cle in visite:
        return None

    visite.add(cle)
    choix = []
    for vx, vy in generer_sauts():
        p_suivant = simuler_saut(perso, vx, vy, lst_blocs)
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

    visite.remove(cle)
    return resultat_final


# FONCTIONS DE LANCEMENT
def resoudre_naif(perso, blocs, obj):
    return backtracking_recursif(perso, blocs, obj, set(), profondeur=8)


def resoudre_optimal(perso, blocs, obj):
    return solver_optimal(perso, blocs, obj)


def resoudre_greedy(perso, blocs, obj):
    return solver_greedy_recursif(perso, blocs, obj, set(), profondeur=8)


