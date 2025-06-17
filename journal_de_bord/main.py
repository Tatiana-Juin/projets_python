import os 

filename="journal_bord.txt"
date_saisie = str(input("Saisie la date d'ecriture de ton texte ")).strip()
saisi_user = str(input("Ecris dans ton journal de bord ")).strip()

#verifie si le fichier existe si ce n'est pas le cas on ne passe pas a la ligne mais si'il existe le texte sera  a  la ligne  
if not os.path.exists(filename):
    text_journal=f"{date_saisie} : {saisi_user}"
    
else:
    text_journal = f"\n{date_saisie}  : {saisi_user}"
    

#a permet d'ajouter du etxte et de ne pas ecraser els donner quand il a une nouvelle entrer 
with open(filename,'a',encoding='utf-8') as file:
    file.write(text_journal)
    # file.write(ajout_text)

print(f"Du texte a etait ajouter au journal de bord {filename}")
