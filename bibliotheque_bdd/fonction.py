# AJOUT DES LIVRES 
def add_livres(cursor,cnx,nom_livre,auteur_livre):
    add_livre = (
        "INSERT INTO livres (nom_livre,auteur_livre)"
        "VALUES (%s,%s)"     
    )
    data_livre = (nom_livre,auteur_livre,)

    try:
          cursor.execute(add_livre,data_livre)
          print("Le livre a etait ajouter")
          cnx.commit()
    except Exception as e:
          cnx.rollback() # Annuler si quelque chose ne va pas
          print(f"ERREUR: Échec de l'ajout du livre ou de la validation : {e}")

#compter le nb de livre 
def count_livre(cursor):
     sql = "SELECT COUNT(id_livre) AS nb_livre FROM livres"
     cursor.execute(sql)
     resultat = cursor.fetchone()
     nombre_livre = resultat[0]
     return nombre_livre

#pour savoir si le livre est existe deja dans la bdd
def existe_livre(cursor,nom_livre):
     query = "SELECT nom_livre FROM livres WHERE nom_livre = %s"
     cursor.execute(query,(nom_livre,))
     resultat = cursor.fetchone()
     return resultat is not None

def show_livre(cursor):
     query = "SELECT nom_livre, auteur_livre FROM livres"
     cursor.execute(query)
     resultat = cursor.fetchall()
     return resultat
  