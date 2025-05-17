tab_ingredient = [];
nb_ingredient = 0;

print("Tu dois taper :");
print("1 - inserer un ingredient");
print("2 - Supprimer un ingredient");
print("3 - Quitter l'application");

nb_saisie = int(input("Quel est ton nombre"));

while nb_saisie != 3:
    if nb_saisie ==1:
        ingredient = str(input("Quel est ton ingredient ? ")).lower().strip();

        #si l'ingredient est dans le tableau
        if ingredient in tab_ingredient:
            print("cette ingredient qui est ", ingredient, "existe deja")
        else:
            tab_ingredient.append(ingredient)
            nb_ingredient +=1
            print("l'ingredient : ", ingredient," a ajouter ajouter avec succès")

    #SUPPRESSION
    elif nb_saisie ==2:
        if nb_ingredient ==0:
            print("Il n'y a aucun ingredient dans ta liste de course . Je ne peut pas supprimer d'ingredient");
        else:
            ingredient_supprimer = str(input("Ingredient a supprimer : ")).lower().strip()
            
            #si l'ingredient est dans le tableau 
            if ingredient_supprimer in tab_ingredient:
                tab_ingredient.remove(ingredient_supprimer)
                nb_ingredient -=1
                print("L'ingredient ", ingredient_supprimer, " a bien était supprimer")
            else:
                print("L'ingredient saisie n'ai pas dans ta liste des course")            

    print("Tu dois taper :");
    print("1 - inserer un ingredient");
    print("2 - Supprimer un ingredient");
    print("3 - Quitter l'application");
    nb_saisie = int(input("Quel est ton nombre"));

#Si il clique sur 3 
print("L'application est terminer")
print("Ta liste des courses est :", tab_ingredient)