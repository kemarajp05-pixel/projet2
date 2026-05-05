from fltk import *
cree_fenetre(900,900)

def aff_acc():
    rectangle(0, 0,900,900, "#87CEEB", "#87CEEB")
    rectangle(0, 860,900,900, "green", "green", epaisseur=2)
    image(141.5,20,"images/titre_acc.png",largeur=600, hauteur=400, ancrage='nw')
    image(450,622,"images/mouton_noir_acc.png",largeur=360, hauteur=300, ancrage='nw')
    image(141.5,20,"images/mouton_pharaon.png",largeur=50, hauteur=50, ancrage='nw')
    image(141.5,20,"images/mouton_campagnard.png",largeur=50, hauteur=50, ancrage='nw')
    image(141.5,20,"images/mouton_graffeur.png",largeur=50, hauteur=50, ancrage='nw')
    image(150,605,"images/mouton_blanc_acc.png",largeur=320, hauteur=300, ancrage='nw')
    image(141.5,20,"images/mouton_apiculteur.png",largeur=50, hauteur=50, ancrage='nw')
    
    #texte(300, 150, "Saute Mouton", "purple", taille=40, ancrage="center")
    #mode de jeu(solo ou duo)

    

# def click():
#     ev= attend_ev()
#     typeEv = type_ev(ev)
#     x = abscisse(ev)
#     y = ordonnee(ev)
#     if typeEv == "ClicGauche":
#         return (x, y)
    
               
def bouton_parametre():
    rectangle(740,30,885,75, "grey", "#87CEEB")
    texte(812.5, 37.5, "OPTIONS", "white", taille=20, ancrage="n")
    

def aff_options():
    efface_tout()
    # Fond et séparation
    rectangle(0, 0, 900, 900, "#87CEEB", "#87CEEB")
    rectangle(500, 0, 900, 900, "#2F4F4F", "#2F4F4F")
    rectangle(150,620,350,900,"black","#2F4F4F")
    
    rectangle(150,380,350,620, "white")
 #   image(85, 355, "images/mouton_blanc.png", largeur=320, hauteur=300, ancrage='nw')
    
    texte(700, 35, "MENU DES SKINS", "white", taille=30, ancrage="n")
    # Taille cadre blanc: largeur=180, hauteur=220
    
    # MOUTON NOIR
    rectangle(510, 120, 690, 340, "white", epaisseur=2) 
    image(470, 90, "images/mouton_noir.png", largeur=250, hauteur=280, ancrage='nw')
    
    # MOUTON APICULTEUR
    rectangle(705, 120, 885, 340, "white", epaisseur=2)
    image(715, 100, "images/mouton_apiculteur.png", largeur=165, hauteur=255, ancrage='nw')
    
    # MOUTON GRAFFEUR
    rectangle(510, 360, 690, 580, "white", epaisseur=2)
    image(512.5, 370, "images/mouton_graffeur.png", largeur=170, hauteur=220, ancrage='nw')
    
    # MOUTON PHARAON
    rectangle(705, 360, 885, 580, "white", epaisseur=2)
    image(690, 340, "images/mouton_pharaon.png", largeur=180, hauteur=260, ancrage='nw')
    
    # MOUTON CAMPAGNARD
    rectangle(510, 600, 690, 820, "white", epaisseur=2)
    image(505, 595, "images/mouton_campagnard.png", largeur=175, hauteur=240, ancrage='nw')

    mise_a_jour()






attend_fermeture()


#----------------------------------------------------------------------------------------


# TODO
# def options / def aff_options / faire nuage_acc / redimensionner tous les moutons
# finir aff_acc / def bouton_parametre a terminer --> donc def click


#----------------------------------------------------------------------------------------