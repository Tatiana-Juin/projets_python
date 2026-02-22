import customtkinter
import requests

# POUR RECUPERER TOUS ELS TYPES DE POKEMON 
def get_types():
    url = "https://pokeapi.co/api/v2/type"
    # envoie la requete 
    reponse = requests.get(url)
    # recupére le json 
    donnees = reponse.json()
    # créer une liste vide 
    liste_types = [];

    # boucle pour ajouter chaque element a la liste 
    for item in donnees['results']:
        nom_type = item['name']
        if nom_type != "unknown" and nom_type != "shadow":
            liste_types.append(nom_type)
        
    # print(donnees)
    return liste_types

# APPELLE DE LA FONCTION 
mes_types = get_types()
# Pour choisir les pokemon a afficher selon leurs type 
def selection_type(choix):
    
    url = f"https://pokeapi.co/api/v2/type/{choix}"
    reponse = requests.get(url);
    donnees = reponse.json();

    liste_pokemon = donnees['pokemon'];

    # Pour deverouiller le mode ecriture  - les pokemon peuvent s'afficher a l'interrieur 
    resultat_box.configure(state="normal")
    # Affiche le nom du premier pokemon 
    # print(liste_pokemon[0]['pokemon']['name'])

    # supprimer les element de la box
    resultat_box.delete("0.0", "end")
    for pokemon_data in liste_pokemon:
        nom_pokemon = pokemon_data['pokemon']["name"]
        resultat_box.insert("insert", nom_pokemon + "\n")
    
    resultat_box.configure(state="disabled") # On ferme le cadenas 🔒

# pour chercher un pokemon 
def chercher_pokemon():
    # pour recuperer les information saisie est les mettre en minuscule 
    recherche = saisie_nom_pokemon.get().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{recherche}"
    # On utilise try catch pour eviter que l'utilisateur ne fasse planter le code si il saisie le nom d'un pokemon qui existe pas 
    try:

        reponse = requests.get(url)
        donnees = reponse.json()
        resultat_recherche.configure(state="normal")

        resultat_recherche.delete("0.0", "end")
        nom = donnees["name"]
        poids = donnees["weight"] / 10
        taille = donnees["height"] / 10
        identifiant = donnees["id"]
        resultat_recherche.insert("insert",f"Nom : {nom} \n id {identifiant} \n poids : {poids} \n Taille {taille}")

        resultat_recherche.configure(state="disabled")
    except:
        resultat_recherche.configure(state="normal")
        resultat_recherche.delete("0.0", "end")
        resultat_recherche.insert("insert", "⚠️ Erreur : Pokémon introuvable.")
        resultat_recherche.configure(state="disabled")
    


app = customtkinter.CTk()
app.title("Pokedex")
app.geometry("600x600")

menu_types = customtkinter.CTkOptionMenu(app,values=mes_types, command=selection_type)
menu_types.grid(row=1,column=0,padx=20,pady=20)

# Création de la zone de texte disabled => empeche l'ecriture a l'interrieur de la zone 
resultat_box = customtkinter.CTkTextbox(app,width=300,height=200, state="disabled")
resultat_box.grid(row=2,column=0,padx=20,pady=20);

# saisir les information 
saisie_nom_pokemon = customtkinter.CTkEntry(app, placeholder_text="chercher un pokemon",width=300)
saisie_nom_pokemon.grid(row=3,column=0,padx=20,pady=20)
btnValidation = customtkinter.CTkButton(app,text="Rechercher",command=chercher_pokemon)
btnValidation.grid(row=3,column=1);

# resultat de la recherche de Pokemon 
resultat_recherche = customtkinter.CTkTextbox(app,width=300,height=100, state="disabled")
resultat_recherche.grid(row=4,column=0,padx=20,pady=20);




app.mainloop()