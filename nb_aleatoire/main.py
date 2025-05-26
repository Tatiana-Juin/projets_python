import random

nb_vie = 5

#randint utiliser pour generer un nb aleatoire qui est un entier 
nb_aleatoire = random.randint(1, 10)
# print(nb_aleatoire)

nb_utilisateur = int(input("entrer un nombre entre 1 et 10 ? "))


while nb_aleatoire != nb_utilisateur:
    nb_vie = nb_vie -1 
    print("ton nombre de vie est de : ",nb_vie)

    if nb_vie == 0 :
        print("Tu as perdu")
        break  

    if nb_utilisateur > nb_aleatoire :
        print("Ton nombre est trop grand") 
    else:
        print("Ton nombre est trop petit ")

   

    nb_utilisateur = int(input("entrer un nombre entre 1 et 10 ? "))
        

if nb_vie != 0:
    print("felicitations tu as trouver le nombre ", nb_aleatoire, " il te rester " ,nb_vie," vie ") 