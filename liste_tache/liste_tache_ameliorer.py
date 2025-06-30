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
frame_left=Frame(window,bg="black",bd=1,relief=SUNKEN)

task = Entry(frame_left,font=("Arial",15),bg="white",fg="black")
task.pack()

frame_left.pack()

window.mainloop()