from tkinter import *

# tableau pour la liste des taches 
tab_task=[]
# Stocker les label,button  pour pouvoir les supprimer et ajouter a chaque entre
task_widgets = {}

def add_task(task_entry):
    # Pour le convertir en chaine 
    task = task_entry.get().strip()
    if task.strip():
        # recupere la longueur 
        index = len(tab_task)
        # ajoute au tableau 
        tab_task.append(task)
    #    affiche la tache sur chaque ligne c'est pour ca row = index +1 pour que cela passe a la ligne 
        label_task = Label(frame,text=task,font=("Arial",15),bg="black",fg="white")
        label_task.grid(row=index +1,column=0,padx=5,pady=5)
         # Pour le bouton supprimer index +1 pour que le bouton soit  la ligne  idx = index caapturer la valeur de l'index 
        btn_delete = Button(frame,text="Supprimer",font=("Arial",12),bg="white",fg="black", command=lambda idx= index: delete_task(idx))
        btn_delete.grid(row=index +1,column = 1,padx=5,pady=5)

        #On enregistre dans un dictionnaire 
        task_widgets[index] = (label_task, btn_delete)
        # Pour supprimer l'element qui est dans le champs input 
        task_entry.delete(0, END)
# Fonction de suppression
def delete_task(index):
    print(f"Cela fonctionne {tab_task[index]}")
    # Boucle sur le diction 
    for widget in task_widgets[index]:
        # Supprime l'element du dictionnaire
        widget.destroy()
    # Remplace la valeur par None donc elle n'est pas totalement supprimer 
    tab_task[index] = None
    

#IDEE POUR SUPPRIMER IL SUFFIT DE RECUPERER L'INDEX DU BOUTON ET DE FAIRE REMOVE ET C'EST BON 

# CONFIGURATION DE LA PREMIERE FENETRE 
window = Tk()
window.title("Application de liste des taches ")
window.geometry("400x400")
window.config(background="black")

# Titre 
title = Label(window,text="Liste des tâches",font=("Arial",17),bg="black",fg="white")
title.pack(pady=(20,5))

# Frame left
frame=Frame(window,bg="black")
frame.pack(pady=10)

# Pour saisir du text 
task = Entry(frame,font=("Arial",15),bg="white",fg="black")
# pady = haut et bas , padx => gauche et droite 
task.grid(row=0,column=0,padx=5,pady=5)


btn_add_task = Button(frame,text="Ajout",font=("Arial",13), bg="white",fg="black", command=lambda:add_task(task))
btn_add_task.grid(row=0,column=1,padx=5,pady=5)


window.mainloop()