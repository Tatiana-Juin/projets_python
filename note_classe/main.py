import json
# variable pour la moyenne et le nombre_eleves initialiser a 0 
nombre_eleves = 0
moyenne = 0;

# nom du fichier 
filename = "data.json"

# Pour lire le fichier 
with open(filename,'r',encoding='utf-8') as file:
      loaded_data=json.load(file)

# Boucle pour parourir les données des eleves 
for eleve in loaded_data['eleves']:
    # pour additionner chaque moyenne 
    moyenne = moyenne + eleve['moyenne']
    # pour connaitre le nombre de moyenne 
    nombre_eleves +=1
# formule pour calculer la moyenne de la classe 
moyenne_classe = moyenne / nombre_eleves

print(f"La moyenne de la classe est de {moyenne_classe}")