from tkinter import *

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


btn_add_task = Button(frame,text="Ajout",font=("Arial",13), bg="white",fg="black")
btn_add_task.grid(row=0,column=1,padx=5,pady=5)


window.mainloop()