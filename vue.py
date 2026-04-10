from fltk import *
cree_fenetre(900,900)

def aff_acc():
    rectangle(0, 0,900,900, "#87CEEB", "#87CEEB")
    rectangle(0, 860,900,900, "green", "green", epaisseur=2)
    image(141.5,20,"titre_acc.png",largeur=600, hauteur=400, ancrage='nw')
    image(450,622,"mouton_noir_acc.png",largeur=360, hauteur=300, ancrage='nw')
    image(141.5,20,"mouton_pharaon.png",largeur=50, hauteur=50, ancrage='nw')
    image(141.5,20,"mouton_campagnard.png",largeur=50, hauteur=50, ancrage='nw')
    image(141.5,20,"mouton_graffeur.png",largeur=50, hauteur=50, ancrage='nw')
    image(150,605,"mouton_blanc_acc.png",largeur=320, hauteur=300, ancrage='nw')
    image(141.5,20,"mouton_apiculteur.png",largeur=50, hauteur=50, ancrage='nw')
    
    #texte(300, 150, "Saute Mouton", "purple", taille=40, ancrage="center")
    #mode de jeu(solo ou duo)
    #parametre
    
    #fond ecran acceuil
aff_acc()
attend_fermeture()