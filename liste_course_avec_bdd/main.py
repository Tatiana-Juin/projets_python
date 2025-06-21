# main.py
import connexion_bdd
import fonction
import mysql.connector

config = connexion_bdd.connexionBdd() 

try:
    cnx = mysql.connector.connect(**config)
    print("Connexion à la base de données réussie !")
    cursor = cnx.cursor()

    # Appeler la fonction avec l'ordre (cursor, cnx)
    fonction.ajout_produit(cursor, cnx) 

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