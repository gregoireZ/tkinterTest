from Tkinter import *
from random import randrange

# --- definition des fonctions gestionnaires d evenements
def drawline():
    "Trace d une ligne dans le canevas canevas1"
    global x1, y1, x2, y2, col
    canevas1.create_line(x1, y1,x2,y2, width=2, fill=col)

    # modification des coordonnees pour les droites suivantes
    y2, y1 = y2+5, y1 +5

def changeColor():
    "Changement aleatoire de la couleur du trace"
    global col
    pal=['purple', 'cyan', 'maroon', 'green', 'red', 'blue', 'orange', 'yellow']
    c = randrange(8) # genere un nombre aleatoire de 0 a 7
    col = pal[c]

#---------Programme principal---------
x1,y1,x2,y2 = 10,10,190,10  #coordonnees de la ligne
col = 'dark green'  #couleur de la ligne

#Creation du widget pincipal
fen1 = Tk()
#creation des widgets esclaves
canevas1 = Canvas(fen1,bg='dark green',height=200,width=200)
canevas1.pack(side=LEFT)
bouton1 = Button(fen1, text='Quitter',command=fen1.quit) #quit : pour quitter la boucle mainloop (ca va alors appeler destroy et quitter la fenetre)
bouton1.pack(side=BOTTOM)
bouton2 = Button(fen1, text='Tracer une ligne',command=drawline)
bouton2.pack()
bouton3 = Button(fen1, text='Autre couleur',command = changeColor)
bouton3.pack()

fen1.mainloop()
fen1.destroy()