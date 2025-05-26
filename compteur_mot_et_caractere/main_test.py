
#demande a l'utilisateur de saisir du texte 

texte_utilisateur = str(input("Saisie ton texte : ")).strip()

#convertir la liste de caractere en mot 
mots = texte_utilisateur.split()

nb_mot = len(mots)



print(f"le nombre de mot est de {nb_mot}")


caractere_seul =list(texte_utilisateur)
nb_caractere = len(caractere_seul)
print(f"Le nombre de caractere est de {nb_caractere}")