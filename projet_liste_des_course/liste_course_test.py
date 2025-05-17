tab_ingredient = []
nb_ingredient = 0
nb_iteration = 0;
ingredient_trouver = False;

print("Tu dois taper : ")
print(" 1 - ajouter un ingredient")
print(" 2- supprimer un ingredient")
print("3 quitter l'application")

nb_saisie = int(input("Quel est ton nb"))
# EN CAS D'ERREUR DE SAISIE 
while nb_saisie!= 1 and nb_saisie!=2 and nb_saisie!=3 : 
    print("erreur")
    print("1-Pour ajouter un ingredient")
    print("2 pour supprimer un ingredient")
    print("3 pour quitter ")
    nb_saisie = int(input("Quel est ton nb "))

# AJOUTER UN INGREDIENT
while nb_saisie == 1:
    ingredient = str(input("Saisie ton ingredient ")).lower().strip()
    tab_ingredient.append(ingredient)
    nb_ingredient =  nb_ingredient+1

    #Cela permet d'inserer un nombre
    if nb_ingredient>0  :
         print("1 - ajouter un nouvelle ingredient") 
         print("2 supprimer")
         print("3 - Quitter")
         nb_saisie = int(input("Quel est ton nb "))

# Supprimer un ingredient 
while nb_saisie == 2:

    #aucun ingredient 
    if nb_ingredient == 0:
          print("Si tu veux supprimer un ingredient il faut que tu en ai un ");

          ingredient = str(input("Saisie ton ingredient ")).lower().strip()
          tab_ingredient.append(ingredient)
          nb_ingredient =  nb_ingredient+1

#     print(tab_ingredient)
#     print(nb_ingredient)
    #
    ingredient_supprimer = str(input("Ingredient à supprimer ")).lower().strip()

    #boucle pour voir chaque ingredient 
    for item in tab_ingredient:
     #     print("mes ingredient",item)
         nb_iteration +=1

         if item == ingredient_supprimer:
              print("L'ingredient existe")
              nb_iteration= nb_iteration -1
              print("Le nb iteration",nb_iteration)
          #     print("Le nb iteration",nb_iteration)
              tab_ingredient.pop(nb_iteration)
              #renitialisation de la variable
              nb_iteration = 0
              ingredient_trouver = True;
              break

    # CONDITION AU CAS OU L'INGREDIENT EXITE PAS  
    if ingredient_trouver == False:
         print("L'ingredient existe pas") 


    #Permet a l'utilisateur de choisir le nb 
    if nb_ingredient > 0  :
         nb_saisie = int(input("Quel est ton nb "))




print("nombre iteration ", nb_iteration)
print("Ingredient  ", tab_ingredient)