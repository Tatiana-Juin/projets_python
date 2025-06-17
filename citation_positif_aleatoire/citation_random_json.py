import json
import random

filename="citation.json"

with open(filename, 'r', encoding="utf-8") as file:
    loaded_citation = json.load(file)

#On doit avoir accèes a la clé citations pour choisir aleatoirement 
liste_citation = loaded_citation['citations']

citation_choisie = random.choice(liste_citation)

print(citation_choisie)
