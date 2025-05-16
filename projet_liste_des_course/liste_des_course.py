
tab_ingredient = []
#pour trouver index de l'element du tableau
nb_iteration = 0;
#pour savoir si l'ingredient a etait trouver 
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
  
    #cela ajoute obligatoirement l'element 

    #Si tab_ingredient n'a aucun element  : on met not car dans une condition tab_ingredient sans not est egale a True c'est pour cela qu'on met not 
    if not tab_ingredient:
         tab_ingredient.append(ingredient)

    elif ingredient in tab_ingredient :
         print("Tu as deja inserer cette ingredient ")
    else:
        tab_ingredient.append(ingredient)
        print("Ingrédient inséré.")

    #Cela permet d'inserer un nombre Superieur a 0 : si la liste d'ingredient n'est pas vide 
    if tab_ingredient :
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


    
    ingredient_supprimer = str(input("Ingredient à supprimer ")).lower().strip()

    #boucle pour voir chaque ingredient 
    for item in tab_ingredient:
     
         nb_iteration +=1
         
         if item == ingredient_supprimer:
              nb_iteration= nb_iteration -1
          
              tab_ingredient.pop(nb_iteration)
              #renitialisation de la variable
              nb_iteration = 0
              ingredient_trouver = True;
              break
         
    # CONDITION AU CAS OU L'INGREDIENT EXITE PAS  
    if ingredient_trouver == False:
         print("L'ingredient existe pas") 
     
    
    #Permet a l'utilisateur de choisir le nb 
    if tab_ingredient  :
         nb_saisie = int(input("Quel est ton nb "))
    



print("Ingredient  ", tab_ingredient)