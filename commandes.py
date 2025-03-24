import os


class Commandes:
    def __init__(self):
        pass    
    
    def toutes_les_commandes(self):
        print("""\nVoici toutes les commandes disponibles !\n\nhelp -> Connaitre toutes les commandes existante.\necho -> Ecrire un message exemple: echo coucou.\ntime -> Afffiche le temps actuelle.\nwhoami -> Qui suis-je ?\najoke -> Lors de l'éxecution raconte une blague.\nclear -> Efface toutes les commandes précedentes.\nls -> Affiche tout le contenue du répertoire actuelle.\ncd -> Permet de se déplacer de répertoires en répertoires.\nexit -> Quitter le terminal.\n""")

    def ajoke(self):
        ahah = input("\nQuelle est le comble pour un neuille ? [jsp] : ")
        if ahah == "jsp":
            print("\nBah parce qu'il dit neuilleeeeee!!!!")
        else: 
            print("ERREUR! Ecrivez 'jsp'.")
            

    def quitter(self, terminal):
        return terminal.lower() == "exit"
    
    def aide(self, terminal):
        return terminal.lower() == "help"    

    def ecrire(self, texte):
        return texte
    
    def temps(self, terminal):
        return terminal.lower() == "time"

    def qui_je_suis(self, terminal):
        return terminal.lower() == "whoami"

    def blague(self, terminal):
        return terminal.lower() == "ajoke"

    def deplacement(self, terminal):
        return terminal.lower() == "cd"
    
    def effacer_terminal(self, terminal):
        return terminal.lower() == "clear"
    
    def afficher_fichiers_du_repertoire(self, terminal):
        return terminal.lower() == "ls"



#chat gpt
    def creer_repertoire(self, terminal):
        # Vérifie si la commande commence par mkdir
        if terminal.startswith("mkdir "):
            # Extraire le nom du répertoire
            nom_repertoire = terminal[6:].strip()
            if nom_repertoire:
                os.system(f"mkdir {nom_repertoire}")
                print(f"Répertoire '{nom_repertoire}' créé avec succès.")
            else:
                print("Erreur : aucun nom de répertoire spécifié.")
            return True
        return False

#chat gpt
    def supprimer_repertoire(self, terminal):
        if terminal.startswith("rmdir "):
            nom_repertoire = terminal[6:].strip()
            if nom_repertoire:
                os.system(f"rmdir {nom_repertoire}")
                print(f"Répertoire '{nom_repertoire}' supprimé avec succès.")
            else:
                print("Erreur : aucun nom de répertoire spécifié.")
            return True
        return False
    
#chat gpt
    def changer_repertoire(self, terminal):
        if terminal.startswith("cd "):
            chemin_repertoire = terminal[3:].strip()
            try:
                os.chdir(chemin_repertoire)
                print(f"Répertoire courant changé en '{chemin_repertoire}'.")
            except FileNotFoundError:
                print(f"Erreur : Le répertoire '{chemin_repertoire}' n'existe pas.")
            except NotADirectoryError:
                print(f"Erreur : '{chemin_repertoire}' n'est pas un répertoire.")
            except PermissionError:
                print(f"Erreur : Permission refusée pour accéder à '{chemin_repertoire}'.")
            return True
        return False



    