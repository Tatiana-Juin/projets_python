from tkinter import * 

tab_tache = []
def ajout_tache(tache_entry):
    
    tache_saisie = tache_entry.get()
    # Pour ignorer les champs vide 
    if tache_saisie.strip(): 
        tab_tache.append(tache_saisie)
        label_entry = Label(frame,text=tache_saisie,font=("Helvetica",15),bg="#ffeeee",fg="black")
        label_entry.pack(pady=(10,0))
        
        tache_entry.delete(0, END)
   
window = Tk()
window.title("Liste des taches ")
window.geometry("720x480")
window.config(background="#ffeeee")

frame = Frame(window,bg="#ffeeee")

label_titre = Label(frame,text="Liste des tâches",font=("Helvetica",20), bg="#ffeeee",fg="red")
label_titre.pack()

#Pour que l'utilisateur saisie une tache 
tache_entry = Entry(frame,font=("Helvetica",17),fg="black")
tache_entry.pack(pady=(10,0))

#on utilise command = lambda: => quand ne fonction a des argument 
btn_entry = Button(frame,text="Ajouter une tache",font=("Helvetica",15),bg="pink",fg="black",command=lambda:ajout_tache(tache_entry))
btn_entry.pack(pady=(15,0))


#pady => marge => haut et bas 
frame.pack(pady=(20,0))

window.mainloop()