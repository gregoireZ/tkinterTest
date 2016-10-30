from tkinter import *
fenetre1 = TK() # instance de la classe TK
texte1 = Label(fenetre1, text="Coucou !", fg='red')
texte1.pack() # taille ajustée
bouton1 = Button(fenetre1, text='Quitter', command = fenetre1.destroy) # pas appel à la méthode
bouton1.pack()
fenetre1.mainloop() # démarrage du réceptionnaire d'événements