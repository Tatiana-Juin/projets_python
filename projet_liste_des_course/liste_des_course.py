
tabIngredient = []
nbIngredient = 0

print("Tu dois taper : ")
print(" 1 - ajouter un ingredient")
print(" 2- supprimer un ingredient")
print("3 quitter l'application")

nbSaisie = int(input("Quel est ton nb"))
# EN CAS D'ERREUR DE SAISIE 
while nbSaisie!= 1 and nbSaisie!=2 and nbSaisie!=3 : 
    print("erreur")
    print("1-Pour ajouter un ingredient")
    print("2 pour supprimer un ingredient")
    print("3 pour quitter ")
    nbSaisie = int(input("Quel est ton nb"))

# AJOUTER UN INGREDIENT
while nbSaisie == 1:
    ingredient = str(input("Saisie ton ingredient ")).lower().strip()
    tabIngredient.append(ingredient)
    nbIngredient =  nbIngredient+1
    #Cela permet d'inserer des nombre 
    if tabIngredient !=0 :
         print("1 - ajouter un nouvelle ingredient") 
         print("2 supprimer")
         print("3 - Quitter")
         nbSaisie = int(input("Quel est ton nb"))

# Supprimer un ingredient 
while nbSaisie == 2:
    #aucun ingredient 
    if nbIngredient == 0:
          print("Si tu veux supprimer un ingredient il faut que tu en ai un ");

          ingredient = str(input("Saisie ton ingredient ")).lower().strip()
          tabIngredient.append(ingredient)
          nbIngredient =  nbIngredient+1

    print(tabIngredient)
    print(nbIngredient)

    
    for item in tabIngredient:
         print("mes ingredient",item)
        
    
    #Permet a l'utilisateur de choisir le nb 
    if tabIngredient !=0 :
         nbSaisie = int(input("Quel est ton nb"))
    



print("Ma liste d'ingredient ", tabIngredient)
