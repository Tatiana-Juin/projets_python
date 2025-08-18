# REFELXION

- time utiliser les seconde il faut faire une conversion vers les minutes et  les heures 
time.time()

temps_total_en_secondes = minutes * 60
temps_total_en_secondes = heures * 3600



self.total_secondes = (heure_int * 3600) + (minute_int * 60)

## CALCULE POUR L'AFFICHAGE 
- heure = nb_total_seconde / 3600
- minute restante = (total_seconde %3600) // 60 
- seconde_restante = total_seconde % 60  

## EN PAS OUBLIER 
- faire **condition** pour appeller la bonne conversion si le champs heure est vide alors on appelle minute_seconde

si champs heure est vide alors : 
    minute_seconde
sinon 
    total_seconde 

# REFLEXION 
````
    if  (heure and not heure.isdigit()) or not minute.isdigit() or int(minute) > 59 or (int(minute) == 0 and heure =="")  or ((int(minute)heure=="0"):
````

si  (heure and not heure.isdigit()) ou minute n'est pas un chiffre  
    message erreur cela doit etre un chiffre 
else: 
    si minute > 59 ou (minute ==0 and heure=="") ou (minute ===0 and heure =="0")



