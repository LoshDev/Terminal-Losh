from commandes import *
import time
from datetime import datetime
import fade
import os 

cmd = Commandes()
c = datetime.now()
temps_actuelle = c.strftime('%H:%M:%S')


class Login:
    def __init__(self):
        pass

    def question(self):
        self.user = input("Quelle est votre user : ")
        self.ordinateur = input("Quelle est le nom de votre ordinateur : ")
    
    def bienvenue(self):
        print("\nBienvenue dans votre Terminal "+ self.user +" !\n")
    
    def terminal(self):
        while True:
            invite = self.user + "@" + self.ordinateur + " $~ "
            colored_invite = fade.brazil(invite).strip() 
            terminal = input(colored_invite)

            if cmd.quitter(terminal):
                time.sleep(2)
                print("\nDéconnexion !")
                break
            elif cmd.aide(terminal):
                time.sleep(0.5)
                cmd.toutes_les_commandes()
            elif terminal.startswith("echo "):
                texte = terminal[5:]
                print(cmd.ecrire(texte))
            elif cmd.temps(terminal):
                print("Il est", temps_actuelle)
            elif cmd.qui_je_suis(terminal):
                print(self.ordinateur+"/"+self.user+"\n")
            elif cmd.blague(terminal):
                cmd.ajoke()
            elif cmd.effacer_terminal(terminal):
                os.system("cls")
            elif cmd.afficher_fichiers_du_repertoire(terminal):
                os.system("dir")              
            elif cmd.creer_repertoire(terminal):
                pass
            elif cmd.supprimer_repertoire(terminal): 
                pass
            elif cmd.changer_repertoire(terminal): 
                pass

            else:
                print(f"Commande non reconue : '{terminal}'\nSi vous avez besoin d'aide taper 'help' !")
