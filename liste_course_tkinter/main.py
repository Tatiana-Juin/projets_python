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
    # RECUPERE LES DONNES SAISIE EN CHAINE DE CARACTERE 
    # print("Ajout")
    product = entry_product.get().strip()
    # La chaine n'est pas vide 
    if product.strip():
        # ajoute dans le tableau 
        tab_product.append(product)
        # vide le champs de saisie 
        entry_product.delete(0,END)
        # appelle la fonction refresh
        refresh()

def delete_product(index):

    tab_product.pop(index)
    refresh()

def view_product():
    # Pour que ca commence a partir de la deuxieme ligne 
    row_offset = 2
    for index,product in enumerate(tab_product):
        
        name_product = Label(frame,text=product,font=("Arial",13),bg="black",fg="white")
        name_product.grid(row = index +1 + row_offset, column=0,padx=5,pady=5)

        button_delete = Button(frame,text="Supprimer", font=("Arial",13) , bg="white",fg="black",command=lambda idx = index:delete_product(idx))
        button_delete.grid(row=index+1 + row_offset, column=1,padx=5,pady=5)
        product_widget[index] = (name_product,button_delete)


# REFRESH DES ELEMENTS VISUEL BOUTON + INGREDIENT 
def refresh():
    for widgets in product_widget.values():
        for widget in widgets:
            widget.destroy()
    
    product_widget.clear()
    # APPELLER FONCTION VIEW POUR TOUTES LES TACHES 
    view_product()

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