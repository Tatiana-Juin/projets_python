from tkinter import *

# tableau pour la liste des taches 
tab_task=[]

def add_task(task_entry):
    # curent_row = 0
    task = task_entry.get()
    if task.strip():
        tab_task.append(task)
        task_entry.delete(0, END)
        # On fait cette ligne pour incrementer la row en recuperant l'index . start = 1 dit que la boucle commence a 1 fonction de enumerate
        for index,task in enumerate(tab_task,start=1):
            label_task = Label(frame,text=task,font=("Arial",15),bg="black",fg="white")
            label_task.grid(row=index,column=0,padx=5,pady=5)
            # Pour le bouton supprimer 
            btn_delete = Button(frame,text="Supprimer",font=("Arial",12),bg="white",fg="black", command=lambda:delete_task(task_entry))
            btn_delete.grid(row=index,column = 1,padx=5,pady=5)

def delete_task(task_entry):
    print("Cela fonctionne")

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