from fltk import *

def vect():
    click = True
    while click:
        ev= donne_ev()
        typeEv = type_ev(ev)
        if typeEv == "Motion":
            x= abscisse(ev)
            y= ordonnee(ev)
            print(x, y)
        if typeEv == "ClicGauche":
            click = False
        mise_a_jour()
        
def vect1():
    ev= donne_ev()
    typeEv = type_ev(ev)
    if typeEv == "Motion":
        x= abscisse(ev)
        y= ordonnee(ev)
        print(x, y)
    if typeEv == "ClicGauche":
        click = False
            
            