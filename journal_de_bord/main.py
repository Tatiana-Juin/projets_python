
filename="journal_bord.txt"
saisi_user = str(input("Ecris dans ton journal de bord ")).strip()
ajout_text = f"\n {saisi_user}"

with open(filename,'a',encoding='utf-8') as file:
    
    file.write(ajout_text)

print(f"Du texte a etait ajouter au journal de bord {filename}")
