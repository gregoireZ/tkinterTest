from Tkinter import *
fenetre1 = Tk() # instance de la classe TK
texte1 = Label(fenetre1, text="Coucou !", fg='red')
texte1.pack() # taille ajustee
bouton1 = Button(fenetre1, text='Quitter', command = fenetre1.destroy)
bouton1.pack()
fenetre1.mainloop() # demarrage du receptionnaire d'evenements
