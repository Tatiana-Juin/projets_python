







# FICHIER POUR ECRIRE LES FONCTIONS 
def ajout_produit(cursor, cnx,ingredient_saisie): 
    add_produit = (
        "INSERT INTO produits"
        "(nom_produit)"
        "VALUES (%s)"
    )
    # Ceci DOIT être un tuple avec une virgule
    # data_produit = ("Poire",) 
    data_produit = (ingredient_saisie,)

    
    try:
        cursor.execute(add_produit, data_produit)
        print(f"DEBUG: Exécution réussie pour {data_produit[0]}")
        
        cnx.commit() # Ceci enregistre les modifications
        print("DEBUG: Modifications validées dans la base de données !")
    except Exception as e:
        cnx.rollback() # Annuler si quelque chose ne va pas
        print(f"ERREUR: Échec de l'ajout du produit ou de la validation : {e}")