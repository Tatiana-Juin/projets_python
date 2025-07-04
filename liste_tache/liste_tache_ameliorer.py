from tkinter import *

# tableau pour la liste des taches 
tab_task=[]
# Stocker les label,button  pour pouvoir les supprimer et ajouter a chaque entre
task_widgets = {}

def add_task(task_entry):
    # Pour le convertir en chaine 
    task = task_entry.get().strip()
    if task.strip():
        
        # ajoute au tableau 
        tab_task.append(task)
    
        # Pour supprimer l'element qui est dans le champs input 
        task_entry.delete(0, END)
        # mettre a jours l'affichage 
        refresh_task()
      #   view_task()
        
    
# Fonction de suppression
def delete_task(index):
#    Supprime la tache du tableau
   tab_task.pop(index)
#    mettre a jour l'affichage avec les bonne ligne 
   refresh_task()

# FONCTION POUR VOIR TOUS LES ELEMENTS 
def view_task():
        # Pour afficher les elements 
        for index, task in enumerate(tab_task):
            label_task = Label(frame,text=task,font=("Arial",15),bg="black",fg="white")
            label_task.grid(row=index +1,column=0,padx=5,pady=5)

            btn_delete = Button(frame,text="Supprimer",font=("Arial",12),bg="white",fg="black", command=lambda idx= index: delete_task(idx))
            btn_delete.grid(row=index +1,column = 1,padx=5,pady=5)

            # Pour ajouter dans le dictionnaire le label et bouton a la ligne demander 
            task_widgets[index] = (label_task,btn_delete)
                
# FONCTION POUR REFRESH , RAFRAICHIR LES ELEMENTS DU TUPLE 
def refresh_task():
    #  pour recuperer tous les element du dictionnaire sans les index 
     for widgets in task_widgets.values():
        #   wigets est un tuple ou il a labbel et bouton . Cette ligne parcours chacun des deux widget comme for widget in (label, bouton)
          for widget in widgets:
            #    supprime le widget de l'ecran
               widget.destroy()
    #  vide complementement le dictionnaire
     task_widgets.clear()

    #  reafiche les elements du dictionnaire avec leurs nouveau index si necessaire 
     view_task()



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