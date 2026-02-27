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
        reponse.raise_for_status();
        donnees = reponse.json()
        # Cette ligne déclenche une erreur si le Pokémon n'existe pas (Erreur 404)
        resultat_recherche.configure(state="normal")
        # supprime s'il a deja du contenus dans la barre de recherche 
        resultat_recherche.delete("0.0", "end")

        # recupere les information du pokemon 
        nom = donnees["name"]
        poids = donnees["weight"] / 10
        taille = donnees["height"] / 10
        identifiant = donnees["id"]
       

        # on créer l'objet pour CTK 
        resultat_recherche.configure(state="normal")
        resultat_recherche.delete("0.0", "end")

        # Insertion du nom 
        resultat_recherche.insert("insert", f"--- {nom} ---")
       
        resultat_recherche.insert("insert", f"\n\nID : #{identifiant}\nPoids : {poids} kg\nTaille : {taille} m")
        resultat_recherche.configure(state="disabled")

    except:
        resultat_recherche.configure(state="normal")
        resultat_recherche.delete("0.0", "end")
        resultat_recherche.insert("insert", "⚠️ Erreur : Pokémon introuvable.")
        resultat_recherche.configure(state="disabled")

# FONCTION POUR FAIRE SWITCHER LES PAGE 
def changer_page(nom_page):
    # pour faire disparaitre les frames 
    frame_page_type.pack_forget()
    frame_page_recherche.pack_forget()

    if nom_page=="type":
        frame_page_type.pack(pady=5)
    elif nom_page =="rechercher":
        frame_page_recherche.pack(pady=5)

app = customtkinter.CTk()
app.title("Pokedex")
app.geometry("1000x1000")

# label pour le nom de application 
title_page = customtkinter.CTkLabel(app,text="POKEDEX",font=("Arial", 24, "bold"))
title_page.pack(pady=5)

# -----------MENU DE NAVIGATION --------------------------------------------------
# creation de la barre lateral
navigation_frame = customtkinter.CTkFrame(app,width=300,corner_radius=0)
navigation_frame.pack(pady=3)


btn_type = customtkinter.CTkButton(navigation_frame,text="Type",fg_color="black")
# lambda => parce que l'on peut passer des parametre a la fonction 
btn_type.configure(command=lambda: changer_page("type"))
btn_type.pack(pady=3)

btn_recherche = customtkinter.CTkButton(navigation_frame,text="Recherche",fg_color="black")
btn_recherche.configure(command=lambda: changer_page("rechercher"))
btn_recherche.pack(pady=3)

frame_page_type = customtkinter.CTkFrame(app, fg_color="transparent")
frame_page_recherche = customtkinter.CTkFrame(app, fg_color="transparent")

# -------------------TYPE DE POKEMON --------------------------
title_type = customtkinter.CTkLabel(frame_page_type,text="Choisi un type de pokemon ",font=("Arial", 14,"bold"))
title_type.pack(pady=3)
# Pour les type de pokemon 
menu_types = customtkinter.CTkOptionMenu(frame_page_type,values=mes_types, command=selection_type)
menu_types.pack(pady=3)

# Création de la zone de texte disabled => empeche l'ecriture a l'interrieur de la zone 
resultat_box = customtkinter.CTkTextbox(frame_page_type,width=300,height=200, state="disabled")
resultat_box.pack(pady=3)

# ---------------------------------RECHERCHE---------------------------------------
title_recherche = customtkinter.CTkLabel(frame_page_recherche,text="Recherche un pokemon",font=("Arial", 14,"bold"))
title_recherche.pack(pady=3)

# saisir les information 
saisie_nom_pokemon = customtkinter.CTkEntry(frame_page_recherche, placeholder_text="chercher un pokemon",width=300)
saisie_nom_pokemon.pack(pady=3)

btnValidation = customtkinter.CTkButton(frame_page_recherche,text="rechercher",command=chercher_pokemon)
btnValidation.pack(pady=3)

# resultat de la recherche de Pokemon 
label_result = customtkinter.CTkLabel(frame_page_recherche, text="Fiche Pokémon :", font=("Arial", 14))
label_result.pack(pady=3)
resultat_recherche = customtkinter.CTkTextbox(frame_page_recherche,width=300,height=200, state="disabled")
resultat_recherche.pack(pady=3)


app.mainloop()