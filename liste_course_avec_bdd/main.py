# main.py
import connexion_bdd
import fonction
import mysql.connector

config = connexion_bdd.connexionBdd() 

try:
    cnx = mysql.connector.connect(**config)
    print("Connexion à la base de données réussie !")
    cursor = cnx.cursor()

    nb_ingredient = 0;

    # MENU
    print("Tu dois taper :");
    print("1 - inserer un ingredient");
    print("2 - Supprimer un ingredient");
    print("3 - Quitter l'application");
    
    nb_saisie = int(input("Quel est ton nombre"));

    while nb_saisie != 3:
        # AJOUT
        if nb_saisie == 1:
             # POUR SAISIR UN INGREDIENT
            nb_produit = fonction.count_ingredient(cursor)
            #aucun ingredient
            if nb_produit == 0:
                ingredient_saisie = str(input("Quel est ton ingredient ?  ")).lower().strip()
                fonction.ajout_produit(cursor, cnx,ingredient_saisie)
               
            else:
                print("plusieurs")
                ingredient_saisie = str(input("Quel est ton ingredient ?  ")).lower().strip()
                existe = fonction.produit_exist(cursor,ingredient_saisie)
                
                if(existe == True):
                    print("Cela existe")
                else:
                    print("Cela n'existe pas ")
        elif nb_saisie ==2:
            nb_saisie = int(input("Quel est ton nombre"));
            print("Supprimer")


        print("Tu dois taper :");
        print("1 - inserer un ingredient");
        print("2 - Supprimer un ingredient");
        print("3 - Quitter l'application");
    
        nb_saisie = int(input("Quel est ton nombre"));

    

except mysql.connector.Error as err:

    if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Quelque chose ne va pas avec votre nom d'utilisateur ou mot de passe")

    elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
        print("La base de données n'existe pas")
    else:
        print(f"Erreur MySQL: {err}") # Afficher l'erreur MySQL réelle

except Exception as e:
    print(f"Une erreur inattendue est survenue: {e}") # Capturer toute autre erreur générale
finally:
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
        print("Curseur MySQL fermé.")
    if 'cnx' in locals() and cnx.is_connected():
        cnx.close()
        print("Connexion MySQL fermée.")