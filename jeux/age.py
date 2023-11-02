import time
import sys
from tkinter import*
class Jeu:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("image_fantome")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.tk, width=171, height=188, highlightthickness=20)
        self.canvas.pack()
        self.tk.update()
        self.hauteur_canevas = 500
        self.largeur_canevas = 500
        self.ap = PhotoImage(file="fantome.gif")
        larg = self.ap.width()
        haut = self.ap.height()
        self.canvas.create_image(171, 188, image=self.ap, anchor='nw')
                
az = input('age : ')
a = float(az)
if a >110:
    print("Impossible d'exister et tu as menti,ou alors tu es un revenant!")
    ae = input('Donne ton vrai age !!!!!!!!!!!! : ')
    aa = float(ae)
    if aa < 5:
        print('Bébé! Et menteur avec ça!!!')
    if aa >5 and aa < 15:
        print("C'est paaaaas bieeeen de mentiiiiiiir !!!!!(ton réprobateur)")
    if aa >14 and aa <111:
        print("Gros menteur")
    if aa >110:
        print("FANTOME!!!!!!")
        print("AU SECOUUUUUUURS")
        print("J'hallucine!!!!!")
        print()
        print()
        print()
        print("                      ________")
        print("           _____     /        \\     _____")
        print("           \\    \\   /  .    .  \\   /    /")
        print("            \\    \\  |          |  /    /")
        print("             \\    \\ |          | /    / ")
        print("              \\    \\|          |/    /")  
        print("               \\    |          |    /")
        print("                \\   |          |   /")
        print("                 \\  |          |  /")
        print("                  \\ |          | /")
        print("                   \\|          |/")
        print("                    |          |")
        print("                   /           \\")
        print("                  /             \\")
        print("                 /               \\")
        print("                /   __   __   __  \\")
        print("               /___/  \\_/  \\_/  \\__\\")
        time.sleep(10)

if a >0 and a <=2.5:
    print('bébé !')
if a >2.5 and a <=5:
    print('Grandis vite !')
if a >5 and a <=13:
    print('bien,tu est assez jeune')
if a >13 and a <=18:
    print('Passe bien ton brevet et ton bac !')
if a >18 and a <=30:
    print('Tu as l\'age qu\'il faut')
if a >30 and a <=110:
    print('Tu est trop vieux de %s années.' % (a - 30))
