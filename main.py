#modules
from commandes import *
from login import *
#variables 
login = Login()
commandes = Commandes()
#fonctions
def main():
    login.question()
    login.bienvenue()
    login.terminal()
#les appeles de fonctions 
main()
