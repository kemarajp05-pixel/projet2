from fltk import *

# Variable globale pour stocker le skin choisi
skin_selectionne = "mouton_blanc_acc.png"

def aff_acc():
    """ Affiche l'écran d'accueil principal """
    efface_tout()
    # Fond et sol
    rectangle(0, 0, 900, 900, "#87CEEB", "#87CEEB")
    rectangle(0, 860, 900, 900, "green", "green", epaisseur=2)
    
    # Titre
    image(150, 20, "titre_acc.png", largeur=600, hauteur=200, ancrage='nw')
    
    # Bouton OPTION (Haut à droite)
    rectangle(750, 20, 880, 70, "black", remplissage="lightgray")
    texte(815, 45, "OPTION", "black", taille=15, ancrage="center")
    
    # Affichage du mouton actuel au centre
    image(450, 600, skin_selectionne, largeur=320, hauteur=300, ancrage='center')
    
    mise_a_jour()
    gerer_clic_accueil()

def menu_options():
    """ Écran de sélection des skins """
    efface_tout()
    rectangle(0, 0, 900, 900, "#2F4F4F", "#2F4F4F")
    texte(450, 50, "CHOISIS TON SKIN", "white", taille=30, ancrage="center")
    
    # Liste des skins : (x, y, fichier)
    skins = [
        (150, 250, "mouton_pharaon.png"),
        (450, 250, "mouton_campagnard.png"),
        (750, 250, "mouton_graffeur.png"),
        (450, 500, "mouton_blanc_acc.png")
    ]
    
    for x, y, img in skins:
        rectangle(x-60, y-60, x+60, y+60, "white")
        image(x, y, img, largeur=100, hauteur=100, ancrage='center')
        
    mise_a_jour()
    gerer_clic_options(skins)

def gerer_clic_accueil():
    global skin_selectionne
    # Utilisation du nom exact : attend_ev()
    ev = attend_ev() 
    tev = type_ev(ev)
    
    if tev == "Quitte":
        return
    elif tev == "ClicGauche":
        x, y = abscisse(ev), ordonnee(ev)
        # Clic sur bouton OPTION
        if 750 <= x <= 880 and 20 <= y <= 70:
            menu_options()
        else:
            # Relance l'écoute si clic ailleurs
            aff_acc()

def gerer_clic_options(skins):
    global skin_selectionne
    ev = attend_ev()
    tev = type_ev(ev)
    
    if tev == "Quitte":
        return
    elif tev == "ClicGauche":
        x_clic, y_clic = abscisse(ev), ordonnee(ev)
        for x, y, img in skins:
            if x-60 <= x_clic <= x+60 and y-60 <= y_clic <= y+60:
                skin_selectionne = img
                aff_acc() # Retour à l'accueil
                return
        menu_options() # Relance l'écoute si clic à côté

# --- LANCEMENT ---
cree_fenetre(900, 900)
aff_acc()
ferme_fenetre()
