







# FICHIER POUR ECRIRE LES FONCTIONS 
#FONCTION POUR AJOUTER UN INGREDIENT 
def ajout_produit(cursor, cnx,ingredient_saisie): 
    #REQUETE
    add_produit = (
        "INSERT INTO produits"
        "(nom_produit)"
        "VALUES (%s)"
    )
    # Ceci DOIT être un tuple avec une virgule
    # (ingredient_saisie,) => cela doit etre un tuple 
    data_produit = (ingredient_saisie,)

    
    try:
        cursor.execute(add_produit, data_produit)
        print(f"DEBUG: Exécution réussie pour {data_produit[0]}")
        
        cnx.commit() # Ceci enregistre les modifications
        print("DEBUG: Modifications validées dans la base de données !")
    except Exception as e:
        cnx.rollback() # Annuler si quelque chose ne va pas
        print(f"ERREUR: Échec de l'ajout du produit ou de la validation : {e}")

#FONCTION POUR COMPTER LE NB INGREDIENT 
def count_ingredient(cursor):
    cursor.execute("SELECT COUNT(id_produit) as nb_produit FROM produits")
    resultat = cursor.fetchone()
    #Le resultat est un tuple 
    nombre_produits = resultat[0]
    return nombre_produits

def produit_exist(cursor,nom_produit):
    query = "SELECT nom_produit FROM produits WHERE nom_produit= %s"
    cursor.execute(query,(nom_produit,))
    resultat = cursor.fetchone()
    return  resultat is not None