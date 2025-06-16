
filename="journal_bord.txt"
saisi_user = str(input("Ecris dans ton journal de bord ")).strip()

with open(filename,'a',encoding='utf-8') as file:
    file.write(saisi_user)

print(f"Du texte a etait ajouter au journal de bord {filename}")
