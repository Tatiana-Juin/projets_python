import time
import os

def clear_console():
    # Commande pour effacer la console (dépend du système d'exploitation)
    os.system('cls' if os.name == 'nt' else 'clear')

duree_saisie = int(input("Saisie une duree "))
print(duree_saisie)