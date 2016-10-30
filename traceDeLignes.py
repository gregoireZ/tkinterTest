from tkinter import *
from random import randrange

# --- definition des fonctions gestionnaires d evenements
def drawline():
    "Trace d une ligne dans le canevas canevas1"
    global x1, y1, x2, y2, col
    canevas1.create_line(x1, y1,x2,y2, width=2, fill=col)

    # modification des coordonnees pour les droites suivantes
    y2, y1 = y2+10, y1 - 10

def changeColor():
    "Changement aleatoire de la couleur du trace"
    global col
    pal=['purple', 'cyan', 'maroon', 'green', 'red', 'blue', 'orange', 'yellow']