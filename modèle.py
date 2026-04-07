#sans fltk et sans print
import math
# position = (x,y)
# v = (Vx,Vy)
# g = (gx,gy)
# 0 < δ ≤ 1
# x = x + δ × vx
# vx = vx + δ × gx
# y = y + δ × vy
# vy = vy + δ × gy
delta = 0.1
g = 0.5 #(chute leger)
f = 0.99
ymax = 600
#sert à simuler les sauts, la gravité, et le résultat des collisions.

def pas(personnage, lst_blocs):
    personnage['vy'] += g*delta #gravité deplacement
    personnage['x'] += personnage['vx']*delta
    personnage['y'] += personnage['vy']*delta
    if collision(personnage, lst_blocs):
        choc(personnage, lst_blocs)
    sol(personnage, ymax)


def collision(personnage, lst_blocs):
    for bloc in lst_blocs:
        if (personnage['x'] < bloc['x'] + bloc['largeur'] and personnage['x'] + personnage['largeur'] > bloc['x'] and
            personnage['y'] < bloc['y'] + bloc['hauteur'] and personnage['y'] + personnage['hauteur'] > bloc['y']):
            return True
    return False

def choc(personnage, lst_blocs):
    personnage['vy'] = 0 #annnule la vitesse vertical si touche bloc (sol)
    personnage['y'] -= 1 #pour pas qu'il soit littéralement dans le bloc on remonte le personnage légérement

def sol(personnage, ymax):
    if personnage['y'] + personnage['hauteur'] > ymax:
        personnage['y'] = ymax - personnage['hauteur']
        personnage['vy'] = 0
    
    

