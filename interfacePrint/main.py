import string
from tkinter import *
 

# INITIALIZATION OF GLOABL MESSAGE
FENETRE_PRINTER_INFO = "Controle de l'environnement d'impression"


fenetre = Tk()

label = Label(fenetre, text = FENETRE_PRINTER_INFO)
label.pack()

fenetre['bg']='grey'

# frame printer
framePrinter = Frame(fenetre, borderwidth=2, relief=GROOVE)
framePrinter.pack(side=BOTTOM, padx=25, pady=25)
Label(framePrinter, text="INTERFACE D'IMPRIMANTE").pack(padx=25, pady=1)

# Ajout de labels


def alert():
    showinfo("alerte", "Bravo!")

menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alert)
menu1.add_command(label="Editer", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Couper", command=alert)
menu2.add_command(label="Copier", command=alert)
menu2.add_command(label="Coller", command=alert)
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)

fenetre.mainloop()