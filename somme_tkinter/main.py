






from tkinter import *

#FONCTION POUR AJOUTER UNE SOMME 
def addition():
    #   messagebox.showinfo("info","bouton cliU2")
    # RECUPERER LE DEUX VALEUR DES NB 
    nb1 = int(nb1_entry.get())
    nb2 = int(nb2_entry.get())
    result_calcule = nb1 + nb2
    # print(result_calcule)
    # return result
    labl_result = Label(window,text=f"Resultat du calcule {nb1} + {nb2} = {result_calcule}",font=("Arial",15),bg="black",fg="white")
    labl_result.pack(pady=5)

# CONSTRUCTION DE LA FENETRE 
window = Tk()
window.title("Calculatrice de somme ")
window.geometry("600x600")
window.config(background="black")

# TITRE DE LA PAGE 
label_title_page = Label(window,text="Calcule les sommes",fg="white",bg="black",font=("Arial",20))
label_title_page.pack(pady=5)

#LABEL POUR 1ER NB
label_nb1 = Label(window, text="Entre le premier nombre",font=("Arial",13),bg="black",fg="white" )
label_nb1.pack(pady=5)
# PREMIER NOMBRE SAISIE POUR LE CALCULE
nb1_entry = Entry(window,font=("Arial",15),bg="white",fg="black")
nb1_entry.pack(pady=5)

#LABEL POUR SECOND NB 
label_nb2 = Label(window,text="Entre un deuxieme nb ",font=("Arial",13),fg="white",bg="black")
label_nb2.pack(pady=5)
# POUR SAISIR LE DEUXIEME NB 
nb2_entry = Entry(window,font=("Arial",15), bg="white",fg="black")
nb2_entry.pack(pady=5)

# BOUTON
btn_result = Button(window,text="Calcule",font=("Arial",15),bg="white",fg="black", command=addition)
btn_result.pack(pady=5)

window.mainloop()
