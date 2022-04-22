from sqlite3 import Row
import string
from tkinter import *
from turtle import right
 
temperatureValue = 25; 
humiditeValue = 25; 

# INITIALIZATION OF GLOABL MESSAGE
FENETRE_PRINTER_INFO = "Controle de l'environnement d'impression"

# INITIALIZATION OF FRAME MENU
fenetre = Tk()
label = Label(fenetre, text = FENETRE_PRINTER_INFO)
label.pack()
fenetre['bg']='grey'

# frame printer
framePrinter = Frame(fenetre, borderwidth=2, relief=GROOVE)
framePrinter.pack(side=BOTTOM, padx=25, pady=25)
Label(framePrinter, text="INTERFACE D'IMPRIMANTE").pack(padx=25, pady=1)

    # frame data -- température
temperatureMessage = str("TEMPERATURE : ") + str(temperatureValue) + str("°C")
temperature = Frame(framePrinter, borderwidth=2, relief=GROOVE)
temperature.place(x=25, y=5)
Label(temperature, text=temperatureMessage).pack(padx=25, pady=1)

    # frame data -- humidité
humiditeMessage = str("HUMIDITE : ") + str(humiditeValue) + str("%HR")
temperature = Frame(framePrinter, borderwidth=2, relief=GROOVE)
temperature.place(x=10, y=100)
Label(temperature, text=humiditeMessage).pack(padx=25, pady=1)





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