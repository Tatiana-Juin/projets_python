import customtkinter
import time


class MinuteurFrame(customtkinter.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        

        self.label_text=customtkinter.CTkLabel(self,text="Entrer un nombre",font=("Arial",15))
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
        self.label_error.grid(row=2,column=0,padx=(0,10),pady=(10,0))

        self.btn = customtkinter.CTkButton(self,text="Envoyer",font=("Arial",15),command=self.verif)
        self.btn.grid(row=1,column=5,padx=(0,10),pady=(10,0))

    # METHODE DE LA CLASSE POUR VERIFIER QUE C'EST UN NOMBRE 
    def verif(self):
            heure = self.heure.get()
            minute = self.minute.get()
            if not heure.isdigit() or not minute.isdigit():
                self.label_error.configure(text="Tu dois saisir un chiffre")
                self.heure.delete(0,'end')
                self.minute.delete(0,'end')
               
            else:
                # supprime le message d'erreur 
                self.label_error.configure(text="")

    
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