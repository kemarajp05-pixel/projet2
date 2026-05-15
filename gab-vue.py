from fltk import *

SKINS = [
        ("Blanc", "images/mouton_blanc.png"),
        ("Noir", "images/mouton_noir.png"),
        ("Pharaon", "images/mouton_pharaon.png"),
        ("Graffeur", "images/mouton_graffeur.png"),
        ("Campagnard", "images/mouton_campagnard.png"),
        ("Apiculteur", "images/mouton_apiculteur.png")
        ]

menu = {
        "ouvert": False,
        "skin_actuel": "images/mouton_blanc.png",
        "nom_skin": "Blanc"
       }

def aff_acc():
    image(0, 0, "images/fond_ecran_acc.jpg", largeur=900, hauteur=600, ancrage='nw')
    image(141.5, -75, "images/titre_acc.png", largeur=600, hauteur=400, ancrage='nw')
    image(525, 332, "images/mouton_noir_acc.png", largeur=360, hauteur=300, ancrage='nw')
    image(85, 305, "images/mouton_blanc_acc.png", largeur=320, hauteur=300, ancrage='nw')

    texte(450, 265, "JOUER", "white", taille=40, ancrage="n")

    x_m, y_m = 750, 35
    texte(x_m, y_m, f"SKIN : {menu['nom_skin']} ▼", "white", taille=15, ancrage="center")
    
    if menu["ouvert"]:
        nb_skins = len(SKINS)
        rectangle(640, 60, 880, 60 + (nb_skins * 50), 
                  couleur=None, remplissage="#2F2F2F")

        for i, (nom, chemin) in enumerate(SKINS):
            y_opt = y_m + 55 + (i * 50)
            if nom == menu["nom_skin"]:
                couleur_texte = "yellow"
            else:
                couleur_texte = "white"

            image(x_m - 60, y_opt, chemin, 
                  largeur=45, hauteur=35, 
                  ancrage="center")
            texte(x_m - 30, y_opt, nom, 
                  couleur=couleur_texte, 
                  taille=12, 
                  ancrage="w")

def gerer_accueil():
    en_attente = True
    while en_attente:
        efface_tout()
        aff_acc()
        mise_a_jour()
        ev = attend_ev()
        tev = type_ev(ev)
        
        if tev == "Quitte":
            return None     
        if tev == "ClicGauche":
            x, y = abscisse(ev), ordonnee(ev)

            if 380 <= x <= 520 and 265 <= y <= 315:
                en_attente = False 
            elif 650 <= x <= 850 and 15 <= y <= 60:
                menu["ouvert"] = not menu["ouvert"]
            elif menu["ouvert"]:
                depart_y = 60
                if 640 <= x <= 880:
                    i_clique = (y - depart_y) // 50
                    if 0 <= i_clique < len(SKINS):
                        idx = int(i_clique)
                        menu["skin_actuel"] = SKINS[idx][1]
                        menu["nom_skin"] = SKINS[idx][0]
                        menu["ouvert"] = False

    return menu["skin_actuel"]
