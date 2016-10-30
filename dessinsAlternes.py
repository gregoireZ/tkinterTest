from Tkinter import *

def cercle(x,y,r,col='black'):
    "Trace d'un cercle de centre (x,y) et de rayon r"
    canevas.create_oval(x-r,y-r,x+r,y+r,outline=col)

def figure_1():
    "Dessiner une cible"
    #Effacer d'abord tout dessin preexistant
    canevas.delete(ALL)
    #tracer les 2 lignes
    canevas.create_line(100,0,100,200,fill='blue')
    canevas.create_line(0, 100, 200, 100, fill='blue')
    #tracer plusieurs cercles concentriques
    rayon=15
    while rayon<100:
        cercle(100,100,rayon)
        rayon+=15

def figure_2():
    "dessiner un visage"
    canevas.delete(ALL)
    #on met les caracteristiques de chaque cercle dans une liste de listes
    cc = [[100,100,80,'red'],           #visage
          [70,70,15,'blue'],            #yeux
          [130,70,15,'blue'],
          [70,70,5,'black'],
          [130,70,5,'black'],
          [44,115,20,'red'],            #joues
          [156, 115, 20, 'red'],
          [100, 95, 15, 'purple'],      #nez
          [100, 145, 20, 'purple']]     #bouche
    #on trace les cercles
    i=0
    while i<len(cc):
        el = cc[i]
        cercle(el[0],el[1],el[2],el[3])
        i+=1

######## Programme principal #########

fen = Tk()
canevas = Canvas(fen,width=200,height=200,bg='ivory')
canevas.pack(side=TOP,padx=5,pady=5) #padx : nombre de pixels a reserver a gauche et a droite du widget
b1 = Button(fen,text='Dessin cible', command=figure_1)
b1.pack(side=LEFT,padx=3,pady=3)
b2 = Button(fen,text='Dessin visage', command=figure_2)
b2.pack(side=RIGHT,padx=3,pady=3)
fen.mainloop()


