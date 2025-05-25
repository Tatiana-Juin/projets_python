
"""
LISTE DES COURSE EN UTILISANT MATCH CASE
"""

# FONCTION POUR GERER LES INGREDIENT 

def gerer_ingredient():
    #tableau
    tab_ingredient = []
    # variable pour savoir si le programme est en cour - boolean
    programme_actif = True

    nb_ingredient = 0;

    print("Bienvenue sur ta liste des course ")
    print("----------------------------------")

    #TANT QUE LE PROGRAMME EST EN COUR DONC
    while programme_actif:
        print("Veuillez faire un choix en entrant un nombre")
        print("1 - Ajouter un ingredient ")
        print("2 - Supprimer un ingredient ")
        print("3 - Quitter et voir la liste des courses")

        #NB QUE L'UTILISATEUR VA SAISIR 
        nb_saisie = int(input("Quel est ton nombre"))

        match nb_saisie:

            case 1:
                ingredient = str(input("Quel est ton ingredient ? ")).lower().strip();
                
                #POUR VOIR SI L'INGREDIENT EST DEJA PRESENT DANS LA LISTE DES COURSES 
                 #si l'ingredient est dans le tableau
                if ingredient in tab_ingredient:
                    print("cette ingredient qui est ", ingredient, "existe deja")
                else:
                    tab_ingredient.append(ingredient)
                    nb_ingredient +=1
                    print("l'ingredient : ", ingredient," a ajouter ajouter avec succès")
            
            #supprimer
            case 2:
                if nb_ingredient == 0:
                    print("Je ne peut pas supprimer d'ingredient car il en a aucun dans ta liste de course")
                else:
                    ingredient_supprimer = str(input("Ingredient a supprimer : ")).lower().strip()

                    #verification que l'ingredient est dans le tableau 
                    if ingredient_supprimer in tab_ingredient:
                        tab_ingredient.remove(ingredient_supprimer)
                        nb_ingredient -=1
                        print("L'ingredient ", ingredient_supprimer, " a bien était supprimer")
                    else:
                        print("L'ingredient saisie n'ai pas dans ta liste des course") 
            
            #Arreter le programme 
            case 3:
                print("Arret du programme")
                programme_actif = False
                print(tab_ingredient)
            
            #erreur de l'utilisateur 
            case _:
                print("Tu dois taper 1 pour ajouter un ingredient, 2 pour en supprimer ou 3 pour quitter l'application")

#appelle de la fonction 
if __name__ == "__main__":
    gerer_ingredient()