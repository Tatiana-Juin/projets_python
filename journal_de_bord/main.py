
filename="journal_bord.txt"
saisi_user = str(input("Ecris dans ton journal de bord ")).strip()
ajout_text = f"\n {saisi_user}"
#a permet d'ajouter du etxte et de ne pas ecraser els donner quand il a une nouvelle entrer 
with open(filename,'a',encoding='utf-8') as file:
    
    file.write(ajout_text)

print(f"Du texte a etait ajouter au journal de bord {filename}")
