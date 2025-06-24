# main.py
import connexion_bdd
import fonction
import mysql.connector

config = connexion_bdd.connexionBdd() 

try:
    cnx = mysql.connector.connect(**config)
    print("Connexion à la base de données réussie !")
    cursor = cnx.cursor()

    # nb_ingredient = 0;

    # MENU
    print("Tu dois taper :");
    print("1 - inserer un ingredient");
    print("2 - Supprimer un ingredient");
    print("3 - Quitter l'application");
    
    nb_saisie = int(input("Quel est ton nombre ? "));

    while nb_saisie != 3:
        # AJOUT
        if nb_saisie == 1:
             # POUR SAISIR UN INGREDIENT
            nb_produit = fonction.count_ingredient(cursor)

            #aucun ingredient on peut ajouter l'ingredient
            if nb_produit == 0:
                ingredient_saisie = str(input("Quel est ton ingredient ?  ")).lower().strip()
                fonction.ajout_produit(cursor, cnx,ingredient_saisie)
            
            #verifie que l'ingredient n'existe pas dans la bdd     
            else:
                ingredient_saisie = str(input("Quel est ton ingredient ?  ")).lower().strip()
                existe = fonction.produit_exist(cursor,ingredient_saisie)

                # condition pour savoir si l'ingredient est deja present dans la liste des course ou si on peut l'ajouter 
                if(existe == True):
                    print("L'ingredient est éjà présent dans ta liste de course tu ne peut pas l'ajouter")
                else:
                    # print("Cela n'existe pas ")
                    fonction.ajout_produit(cursor, cnx,ingredient_saisie)
        elif nb_saisie ==2:

            # fonction pour savoir le nb de produit dans la bdd 
            nb_produit = fonction.count_ingredient(cursor)

            # Si il a aucun produit on a un message 
            if nb_produit ==0:
                print("Tu ne peut pas supprimer de produit car il en a pas dans labase de donnée")
            else:
                nom_produit_supprimer = str(input("Quel est le produit que tu veux supprimer ? ")).lower().strip()
               
            #    Appelle de la fonction pour sazvoir si le produit existe 
                existe = fonction.produit_exist(cursor,nom_produit_supprimer)
                if existe == True : 
                    # print("Le produit existe ")
                    supprimer_produit = fonction.delete_produit(cursor,cnx,nom_produit_supprimer)

                    affiche_produit = fonction.show_produit(cursor)
                    for ligne in affiche_produit:
                        print("La liste des produits : ")
                        print(ligne[0])

                    
                else:
                    print("Tu ne peut pas supprimer un produit qui n'existe pas dans la base de données ")
                    


        print("Tu dois taper :");
        print("1 - inserer un ingredient");
        print("2 - Supprimer un ingredient");
        print("3 - Quitter l'application");
    
        nb_saisie = int(input("Quel est ton nombre ? "));

    

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