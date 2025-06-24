import connexion_bdd
import fonction
import mysql.connector

# Appelle de la fonction connexion bdd du module conenxion_bdd
config = connexion_bdd.connexion_bdd() 
try:
    cnx= mysql.connector.connect(**config)
    print("Connexion a la bdd")
    cursor = cnx.cursor()

    print("Tu dois taper :");
    print("1 - Ajouter un livre ");
    print("2 - Voir les livres ");
    print("3 - supprimer un livre");
    print("4 - Quitter l'application");

    nb_saisie = int(input("Quel est ton nombre ? "));

    while nb_saisie != 4:
        #Ajout 
        if nb_saisie == 1: 
            # print("Ajout")
            nom_livre = str(input("Quel est le nom du livre ? ")).lower().strip()
            auteur_livre = str(input("Quel est l'auteur du livre ? ")).lower().strip()
            # Pour savoir le nb de livre qu'il y a dans la bibliotheque
            nb_livre = fonction.count_livre(cursor)

            # S'il n'y a pas de livre on ajoute
            if nb_livre == 0:
                fonction.add_livres(cursor,cnx,nom_livre,auteur_livre)
            else:
                # sinon on verifie que le livre n'est pas deja present dans la bibliotheque 
                existe = fonction.existe_livre(cursor,nom_livre)

                if existe == True: 
                    print("Le livre est deja dans la bibliothéque ")
                else:
                    fonction.add_livres(cursor,cnx,nom_livre,auteur_livre)
                
        
        # VOIR LES LIVRES 
        elif nb_saisie ==2:
            # print("Tous les livres")
            nb_livre = fonction.count_livre(cursor)
            
            if nb_livre == 0:
                print("Il n'y a aucun livre dans ta bibliotheque ")
            else:
                print("Tous les livres qui sont dans la bibliotheque : ")
                livres = fonction.show_livre(cursor)
                for ligne in livres: 
                    print(f"Nom du livre : {ligne[0]} auteur: {ligne[1]}")

        # SUPPRIMER UN LIVRE
        elif nb_saisie == 3 : 
            # compte le nb de livre qu'il y a dans ta bdd 
            nb_livre = fonction.count_livre(cursor)

            # s'il n'y a aucun livre cela affiche un message erreur 
            if nb_livre == 0:
                print("Tu ne peut pas supprimer de lire car tu en a pas dans ta bibliotheque ")
            else:
                # Si il a des livre on demander le nom du livre 
                nom_supprimer = str(input("Quel est le nom du livre a supprimer ? ")).lower().strip()
                # On verifie si le livre est dans la bdd
                existe = fonction.existe_livre(cursor,nom_supprimer)
                # S'il est present dans la bdd on le supprime 
                if existe == True : 
                    supprimer = fonction.delete_livre(cursor,cnx,nom_supprimer)
                else:
                    # sinon on affiche un message d'erreur 
                    print("Le livre que tu souhaite supprimer n'est pas dans ta bibliotheque ")

        # Pour eviter les boucle infini 
        print("Tu dois taper :");
        print("1 - Ajouter un livre ");
        print("2 - Voir les livres ");
        print("3 - supprimer un livre");
        print("4 - Quitter l'application");

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