from fltk import *
       
def vect():
    ev= attend_ev()
    typeEv = type_ev(ev)
    if typeEv == "ClicGauche":
        x= abscisse(ev)
        y= ordonnee(ev)
        return x, y
            
            