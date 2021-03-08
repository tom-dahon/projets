import turtle as t
from random import *
from pile import Pile

def arbre_branche(t, regle, niveau, taille, angle, pile):
    """ Interpreteur de règle exemple "F[+FX]F[-FX]F" """
    if niveau == 0:
        t.forward(taille)
    else:
        for r in regle:
            
            if r == "F":
                
                arbre_branche(t, regle, niveau-1, taille*0.6, angle, pile)
                t.pencolor(91, 120//niveau, 17) 
            elif r == "+":
                
                angle = randint(10, 45)
                t.left(angle)
                n = random()
                
                if n < 1:
                    t.circle(1)
                    x = random()
                    
                    if x < 1:
                        #regle += "F"
                        arbre_branche(t, regle, niveau-1, taille*0.6, angle, pile)
                        
            elif r == "-":
                
                angle = randint(10, 45)
                t.right(angle)
                n = random()
                if n < 1:
                    x = random()
                    if x < 1:
                        #regle += "F"
                        arbre_branche(t, regle, niveau-1, taille*0.6, angle, pile)
                    else:
                        t.circle(1)
            elif r == "[":
                position = t.position()
                direction = t.heading()
                pile.empile((position, direction))
            elif r == "]":
                s = pile.depile()
                t.setposition(s[0])
                t.setheading(s[1])
            elif r == "X":
                # t.dot()
                x = random()
                if x < 0.8:
                    #regle += "F"
                    arbre_branche(t, regle, niveau-1, taille/3, angle, pile)
            
                
def main():
    win = t.Screen()
    win.setup(800, 600)
    t.speed(0)
    t.left(90)
    t.up()
    t.back(250)
    t.colormode(255)
    t.color(91, 60, 17)
    t.pensize(1)
    t.down()
    
    #koch = "F-F++F-FF-F++F-F"
    regle = "F[+FX]F[-FX]F"
    angle = 90
    pile = Pile()
    arbre_branche(t, regle, 5, 80, angle, pile)
    
    win.exitonclick()
    
main()