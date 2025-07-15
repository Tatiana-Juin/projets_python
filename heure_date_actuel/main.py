
import datetime
#pour recuperer la date et l'heure actuel 
heure_date_actuel = datetime.datetime.now()

#format de la date 
format_date= heure_date_actuel.strftime("%d-%m-%Y %H:%M:%S ")
print(format_date)