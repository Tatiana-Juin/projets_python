# main.py
import connexion_bdd
import fonction
import mysql.connector

# Appeler la fonction pour obtenir le dictionnaire de configuration
config = connexion_bdd.connexionBdd() 

# Le reste de votre code de connexion reste le même
try:
    cnx = mysql.connector.connect(**config)
    print("Connexion à la base de données réussie !")

except mysql.connector.Error as err:
    if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Quelque chose ne va pas avec votre nom d'utilisateur ou mot de passe")
    elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
        print("La base de données n'existe pas")
    else:
        print(err)
finally:
    # Toujours fermer la connexion
    if 'cnx' in locals() and cnx.is_connected():
        cnx.close()
        print("Connexion MySQL fermée.")