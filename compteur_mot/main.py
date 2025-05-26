

#demande a l'utilisateur de saisir du texte 
texte_utilisateur = str(input("Saisie ton texte : ")).strip()

#convertir la liste de caractere en mot 
mots = texte_utilisateur.split()
# variable pour connaitre le nb de mot 
nb_mot = len(mots)
#affiche le nombre de mot 
print(f"le nombre de mot est de {nb_mot}")


