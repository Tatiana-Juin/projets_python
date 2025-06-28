from tkinter import * 

window = Tk()
window.title("Liste des taches ")
window.geometry("720x480")
window.config(background="#ffeeee")

frame = Frame(window,bg="#ffeeee")

label_titre = Label(frame,text="Liste des taches",font=("Helvetica",20), bg="#ffeeee",fg="red")
label_titre.pack()
#pady => marge => haut et bas 
frame.pack(pady=(20,0))

window.mainloop()