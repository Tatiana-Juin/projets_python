








import time


# VREFICATION QUE L'UTILISATEUR N'A PAS SAISIE AUTRE CHOSE QUE UN NOMBRE  

try:
    seconde_saisie = int(input("Saisie une duree  en seconde "))


    # VERRIFICATION PAR RAPPORT AU NB SAISIE 
    if seconde_saisie < 0:
        print("erreur ton nombre de seconde doit etre positif ")
    else:
        # BOUCLE POUR QUE CELA S'ARRETE S'ARRETE QUAND LE NB EST EGALE A 0
        while seconde_saisie > 0: 
            print(seconde_saisie)
            # PERMET DE FAIRE UNE PAUSE D'UNE SECONDE AVANT D'AFFICHER LE NB SUIVANT 
            time.sleep(1)
            seconde_saisie = seconde_saisie -1
            
            if seconde_saisie == 0: 
                print("Fin du compte a rebour")
           

except Exception as e:
    print( f"On a une erreur  : {e}")