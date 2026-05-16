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

    

# def click():
#     ev= attend_ev()
#     typeEv = type_ev(ev)
#     x = abscisse(ev)
#     y = ordonnee(ev)
#     if typeEv == "ClicGauche":
#         return (x, y)
    
               
# def bouton_parametre():
#     image(735,25,"options_acc.png",largeur=150, hauteur=50, ancrage='nw')
#     image(735,25,"nuage_options_acc.png",largeur=150, hauteur=50, ancrage='nw')
#     rectangle(740,30,885,75, "black", epaisseur=1)
#     #nuage_options_acc.png a faire
    

def aff_options():
    efface_tout()
    rectangle(0,0,900,900, "#87CEEB", "#87CEEB")
    rectangle(500,0,900,900, "#2F4F4F", "#2F4F4F")
    image(100,355,"mouton_blanc.png",largeur=320, hauteur=300, ancrage='nw')
    texte(700, 35, "MENU DES SKINS", "white", taille=30, ancrage="n")
    
    rectangle(525,135,680,300, "white", "#2F4F4F", epaisseur=1)#noir
    image(430,110,"mouton_noir.png",largeur=320, hauteur=300, ancrage='nw')
    
    rectangle(650,0,650,900, "#2F4F4F", "#2F4F4F", epaisseur=1)#apiculteur
    image(685,125,"mouton_apiculteur.png",largeur=225, hauteur=275, ancrage='nw')
    
    rectangle(650,0,650,900, "#2F4F4F", "#2F4F4F", epaisseur=1)#graffeur
    image(430,355,"mouton_graffeur.png",largeur=225, hauteur=275, ancrage='nw')
    
    rectangle(650,0,650,900, "#2F4F4F", "#2F4F4F", epaisseur=1)#pharaon
    image(100,355,"mouton_pharaon.png",largeur=320, hauteur=300, ancrage='nw')
    
    rectangle(650,0,650,900, "#2F4F4F", "#2F4F4F", epaisseur=1)#campagnard
    image(100,355,"mouton_campagnard.png",largeur=320, hauteur=300, ancrage='nw')

def options():
    if 740 <= x <= 885 and 30 <= y <= 75 and a==0:
        mise_a_jour()
        aff_options()
        pass

aff_options()
#aff_acc()
#bouton_parametre()

attend_fermeture()


#----------------------------------------------------------------------------------------


# TODO
# def options / def aff_options / faire nuage_acc / redimensionner tous les moutons
# finir aff_acc / def bouton_parametre a terminer --> donc def click


#----------------------------------------------------------------------------------------