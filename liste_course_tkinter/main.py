from tkinter import *

window = Tk()
window.title("Liste des courses ")
window.geometry("600x600")
window.config(background="black")

# TITRE DE LA PAGE 
title_page = Label(window,text="Liste des courses",font=("Arial",20),fg="white",bg="black")
title_page.pack(pady=15)

# POUR SAISIR DES INGREDIENT 
label_product = Label(window,text="Saisie ton ingredient",font=("Arial",15),fg="white",bg="black")
label_product.pack(pady=15)

# SAISIE UTILISATEUR
entry_product = Entry(window,font=("Arial",13),fg="black",bg="white")
entry_product.pack(pady=4)

# Bouton pour ajout 
btn_add = Button(window,text="Ajout",font=("Arial",13),fg="black",bg="white")
btn_add.pack(pady=5)

window.mainloop()