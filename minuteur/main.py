import customtkinter
import time


class MinuteurFrame(customtkinter.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        
        self.visible_input = True;

        self.label_text=customtkinter.CTkLabel(self,text="Minuteur",font=("Arial",15))
        self.label_text.grid(row=0,column=0,padx=(0,10),pady=(10,0),sticky="n")

        # HEURE
        self.heure = customtkinter.CTkEntry(self,font=("Arial",12),text_color="white")
        self.heure.grid(row=1,column=0,padx=(0,10),pady=(10,0))
        self.label_heure=customtkinter.CTkLabel(self,text="h",font=("Arial",15))
        self.label_heure.grid(row=1,column=1,padx=(0,10),pady=(10,0))

        # MINUTE
        self.minute = customtkinter.CTkEntry(self,font=("Arial",12),text_color="white")
        self.minute.grid(row=1,column=2,padx=(0,10),pady=(10,0))
        self.label_minute=customtkinter.CTkLabel(self,text="m",font=("Arial",15))
        self.label_minute.grid(row=1,column=3,padx=(0,10),pady=(10,0))

        # CREATION DU LABEL QUE L'ON APPELLE DANS LA FONCTION PLUS BAS POUR MODIFIER LE TEXTE PAR RAPPORT A CE QUE A ENTRER L'UTILISATEUR 
        self.label_error = customtkinter.CTkLabel(self, font=("Arial",15),text_color="red",text="")
        # self.label_error.grid(row=2,column=0,padx=(0,10),pady=(10,0))
        self.label_error.grid(row=2, column=0, columnspan=6, pady=(10, 0), sticky="w")

        self.btn = customtkinter.CTkButton(self,text="Démarrer",font=("Arial",15),command=self.verif)
        self.btn.grid(row=1,column=5,padx=(0,10),pady=(10,0))

    # METHODE DE LA CLASSE POUR VERIFIER QUE C'EST UN NOMBRE 
    def verif(self):
            # recupere heure et minute  en chaine de caractere 
            heure = self.heure.get()
            minute = self.minute.get()
            # int_heure = int(heure) if heure else 0
            # pour verifier que les champs soit des nombre 
            if  (heure and not heure.isdigit()) or not minute.isdigit() or int(minute) > 59 or int(minute) == 0 :
                self.label_error.configure(text="Erreur tu dois saisir un chiffre ou le nombre doit etre différents de 0 ")
                self.heure.delete(0,'end')
                self.minute.delete(0,'end')
               
            else:
                # supprime le message d'erreur 
                self.label_error.configure(text="")
                self.toggle_input()

    # FONCTION POUR FAIRE APPARAITRE ET DISPARAITRE LE CHAMPS 
    def toggle_input(self):

        # Si le champs est visible 
        if  self.visible_input:
            self.heure.grid_forget()
            self.label_heure.grid_forget()
            self.minute.grid_forget()
            self.label_minute.grid_forget()
            # APPELLE DE LA METHODE POUR AFFICHER L'HEURE
            self.show()
            #changer la valeur du bouton en reset
            self.btn.configure(text="Pause")
        else:
            self.btn.configure(text="relancer")
            
        self.visible_input = not self.visible_input

    # FONCTION POUR AFFICHER LES MINUTES 
    def show(self):
       
        # recupere les heure et minutes
        self.show_heure = self.heure.get()
        self.show_minute = self.minute.get()
        self.label_show_heure = customtkinter.CTkLabel(self,text=self.show_heure,font=("Arial",15))
        self.label_show_heure.grid(row=1,column=0,padx=(0,10),pady=(10,0))
        self.label_show_minute = customtkinter.CTkLabel(self,text=self.show_minute,font=("Arial",15))
        self.label_show_minute.grid(row=1,column=1,padx=(0,10),pady=(10,0))

        self.conversion()
    
    # FONCTION POUR LA CONVERSION POUR AFFICHER LES MINUTES ET HEURE 
    def conversion(self):
      
        # Pour dire que le nombre est soit un nb  ou 0 
        heure_int = int(self.show_heure) if self.show_heure else 0
        minute_int = int(self.show_minute)
        self.total_seconde = (heure_int *3600) + (minute_int * 60)
        # POUR AFFICHER LE MINUTEUR 
        self.start_compt() 

        
    # FONCTION POUR AFFICHER LE MINUTEUR 
    def  start_compt(self):
        if self.total_seconde > 0:
            # fait la conversion en minute 
            heures = self.total_seconde //3600
            minute_restante = (self.total_seconde % 3600) //60
            seconde = self.total_seconde % 60

            print(heures, " h ",minute_restante," m ", seconde," s")
            

            # Decrementer le compteur 
            self.total_seconde -=1;

            # Relance la fonction toute les secondes 
            self.after(1000,self.start_compt)
        else:
            print("FIN")



# FENETRE PRINCIPALE 
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # apparence par defaut 
        customtkinter.set_appearance_mode("dark") 
        customtkinter.set_default_color_theme("dark-blue")
        self.title("Minuteur")
        self.geometry("700x500")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

        self.label_frame = MinuteurFrame(self)
        self.label_frame.grid(row=0,column=0,padx=(0,10),pady=(10,0),sticky="n")

        

        
app =App()
app.mainloop()