from Tkinter import *

def carre(x,y):
    "Trace d'un carre de cote a"
    canevas.create_rectangle(x,y,x+20,y+20,fill='black')

def damier():
    "Dessiner un damier"
    cc = []
    for i in range(5):
        if (i % 2 == 0):
            x=40*i
        else:
            x=20+40*i
        for j in range(5):
            if (j % 2 == 0):
                y = 40 * j
            else:
                y = 20 + 40 * j
            cc.append([x,y])

    #on trace les carres
    i=0
    while i<len(cc):
        el = cc[i]
        carre(el[0],el[1])
        i+=1

######## Programme principal #########

fen = Tk()
canevas = Canvas(fen,width=600,height=600,bg='ivory')
canevas.pack(side=TOP,padx=5,pady=5) #padx : nombre de pixels a reserver a gauche et a droite du widget
b1 = Button(fen,text='Damier', command=damier)
b1.pack(side=BOTTOM,padx=3,pady=3)
#b2 = Button(fen,text='Dessin visage', command=figure_2)
#b2.pack(side=RIGHT,padx=3,pady=3)
fen.mainloop()


