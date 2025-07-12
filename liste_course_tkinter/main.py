




from tkinter import *

window = Tk()
window.title("Liste des courses ")
window.geometry("600x600")
window.config(background="black")

#TABLEAU POUR LES COURSE
tab_product = []
#DICTIONNAIRE POUR LES WIDGET 
product_widget = {} 

# FONCTION AJOUT DES PRODUITS

def add_product(entry_product):
    print("Ajout")


# REFRESH DES ELEMENTS VISUEL BOUTON + INGREDIENT 
def refresh():
    for widgets in product_widget.value():
        for widget in widgets:
            widget.destroy()
    
    product_widget.clear()
    # APPELLER FONCTION VIEW POUR TOUTES LES TACHES 

# TITRE DE LA PAGE 
title_page = Label(window,text="Liste des courses",font=("Arial", 20),fg="white", bg="black")
title_page.pack(pady=15)

frame = Frame(window,bg="black")
frame.pack(pady=10)

# POUR SAISIR DES INGREDIENT 
label_product = Label(frame,text="Saisie ton ingredient",font=("Arial",15),fg="white",bg="black")
label_product.grid(row=0,column=0,padx=5,pady=5)

# SAISIE UTILISATEUR
entry_product = Entry(frame,font=("Arial",13),fg="black",bg="white")
entry_product.grid(row = 1, column=0,padx=5,pady=5)

# Bouton pour ajout 
btn_add = Button(frame,text="Ajout",font=("Arial",13),fg="black",bg="white", command=lambda:add_product(entry_product))
btn_add.grid(row=1, column=1,padx=5,pady=5)

window.mainloop()