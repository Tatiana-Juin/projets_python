








import time
import os

def clear_console():
    # Commande pour effacer la console (dépend du système d'exploitation)
    os.system('cls' if os.name == 'nt' else 'clear')

# VREFICATION QUE L'UTILISATEUR N'A PAS SAISIE AUTRE CHOSE QUE UN NOMBRE  

try:
    seconde_saisie = int(input("Saisie une duree  en seconde "))
    # print(seconde_saisie)

    # VERRIFICATION PAR RAPPORT AU NB SAISIE 
    if seconde_saisie < 0:
        print("erreur ton nombre de seconde doit etre positif ")
    else:
        # print("Super ton nb est superieur a 0")
        while seconde_saisie > 0: 
            print(seconde_saisie)
            time.sleep(1)
            seconde_saisie = seconde_saisie -1
            
        if seconde_saisie == 0: 
            print("Fin du compte a rebour")
           

except Exception as e:
    print( f"On a une erreur  : {e}")