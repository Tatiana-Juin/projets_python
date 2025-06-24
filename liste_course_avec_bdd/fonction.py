








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
        print(f" Exécution réussie pour {data_produit[0]}")
        
        cnx.commit() # Ceci enregistre les modifications
        # print("DEBUG: Modifications validées dans la base de données !")
    except Exception as e:
        cnx.rollback() # Annuler si quelque chose ne va pas
        print(f"ERREUR: Échec de l'ajout du produit ou de la validation : {e}")

#FONCTION POUR COMPTER LE NB DE PRODUIS 
def count_ingredient(cursor):
    cursor.execute("SELECT COUNT(id_produit) as nb_produit FROM produits")
    resultat = cursor.fetchone()
    #Le resultat est un tuple 
    nombre_produits = resultat[0]
    return nombre_produits

# FONCTION POUR SAVOIR SI LE PRODUIT EXISTE DEJA DANS LA BDD 
def produit_exist(cursor,nom_produit):
    query = "SELECT nom_produit FROM produits WHERE nom_produit= %s"
    cursor.execute(query,(nom_produit,))
    resultat = cursor.fetchone()
    return  resultat is not None


# FONCTION POUR SUPPRIMER UN PRODUIT 
def delete_produit(cursor,cnx,nom_produit_supprimer):
    sql = "DELETE FROM produits WHERE nom_produit = %s "
    cursor.execute(sql,(nom_produit_supprimer,))
    cnx.commit()
    print("Supprimer")

# POUR VOIR TOUS LES PRODUIT QUI SONT PRESENT DANS LA BDD
def show_produit(cursor):
    sql = "SELECT nom_produit FROM produits"
    # quand on utilise execute et qu'il n'y a pas de parametre autre que cursor on utilise une chaine de caractere 
    cursor.execute(sql)
    resultat = cursor.fetchall()
    return resultat