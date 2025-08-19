import customtkinter
import time


class MinuteurFrame(customtkinter.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        
        # VARIABLE POUR SAVOIR SI LE MINUTEUR EST LANCER, EN PAUSE,ET POUR GARDER L'IODENTIFIANT DU TIMER POUR L'ETAT DE PAUSE 
        self.visible_input = True;
        self.is_start = False
        self.is_paused = False
        self.id_timer = None

        self.label_text=customtkinter.CTkLabel(self,text="Minuteur",font=("Arial",15))
        self.label_text.grid(row=0,column=0,padx=(0,10),pady=(10,0),sticky="n")
        # HEURE
        self.heure = customtkinter.CTkEntry(self,font=("Arial",12),text_color="white")
        self.label_heure=customtkinter.CTkLabel(self,text="h",font=("Arial",15))
        self.minute = customtkinter.CTkEntry(self,font=("Arial",12),text_color="white")
        self.label_minute=customtkinter.CTkLabel(self,text="m",font=("Arial",15))
        self.label_error = customtkinter.CTkLabel(self, font=("Arial",15),text_color="red",text="")
        self.btn = customtkinter.CTkButton(self,text="Démarrer",font=("Arial",15),command=self.toggle_input)

        self.show_input()

    def show_input(self):

        
        self.heure.grid(row=1,column=0,padx=(0,10),pady=(10,0))
        
        self.label_heure.grid(row=1,column=1,padx=(0,10),pady=(10,0))

        # MINUTE
        
        self.minute.grid(row=1,column=2,padx=(0,10),pady=(10,0))
        
        self.label_minute.grid(row=1,column=3,padx=(0,10),pady=(10,0))

        # CREATION DU LABEL QUE L'ON APPELLE DANS LA FONCTION PLUS BAS POUR MODIFIER LE TEXTE PAR RAPPORT A CE QUE A ENTRER L'UTILISATEUR 
        
        # self.label_error.grid(row=2,column=0,padx=(0,10),pady=(10,0))
        self.label_error.grid(row=2, column=0, columnspan=6, pady=(10, 0), sticky="w")

        
        self.btn.grid(row=1,column=5,padx=(0,10),pady=(10,0))

    # METHODE DE LA CLASSE POUR VERIFIER QUE C'EST UN NOMBRE 
    def verif(self):
            # recupere heure et minute  en chaine de caractere 
            heure = self.heure.get()
            minute = self.minute.get()
            # int_heure = int(heure) if heure else 0
            # pour verifier que les champs soit des nombre 
            if  (heure and not heure.isdigit()) or not minute.isdigit() or int(minute) > 59 or (int(minute) == 0 and heure =="") or ( int(minute) == 0 and  heure=="0"):
                self.label_error.configure(text="Erreur tu dois saisir un chiffre  ")
                self.heure.delete(0,'end')
                self.minute.delete(0,'end')
               
            else:
                # supprime le message d'erreur 
                self.label_error.configure(text="")
                # self.toggle_input()
                self.start()

    # FONCTION POUR LANCER LES BONNE 
    def toggle_input(self):

        if not self.is_start and not self.is_paused:
            self.verif()
        elif self.is_start and not self.is_paused:
            self.pause()
        elif self.is_paused:
            self.resume()

    # FONCTION POUR RECUPERER  LES MINUTES ,HEURE ET SECONDE ET CACHER LES ENTRER
    def start(self):
       
        # recupere les heure et minutes
        self.show_heure = self.heure.get()
        self.show_minute = self.minute.get()

        # cacher les entrer
        self.heure.grid_forget()
        self.label_heure.grid_forget()
        self.minute.grid_forget()
        self.label_minute.grid_forget()


        self.label_show_heure = customtkinter.CTkLabel(self,text="",font=("Arial",15))
        self.label_show_heure.grid(row=1,column=0,padx=(0,10),pady=(10,0))

        self.label_show_minute = customtkinter.CTkLabel(self,text="",font=("Arial",15))
        self.label_show_minute.grid(row=1,column=1,padx=(0,10),pady=(10,0))

        # POUR LES SECONDE 
        self.label_show_seconde  = customtkinter.CTkLabel(self,text="",font=("Arial",15))
        self.label_show_seconde.grid(row=1,column=2,padx=(0,10),pady=(10,0))

        self.conversion()

        self.is_start = True
        self.is_paused = False
        self.btn.configure(text="Pause")
    
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

        if self.total_seconde >= 0:
            # fait la conversion en minute 
            heures = self.total_seconde //3600
            minute_restante = (self.total_seconde % 3600) //60
            seconde = self.total_seconde % 60

            # POUR AFFICHER LE MINUTEUR 
            self.label_show_heure.configure(text=heures)
            self.label_show_minute.configure(text=minute_restante)
            self.label_show_seconde.configure(text=seconde)
            

            # Decrementer le compteur 
            self.total_seconde -=1;

            # Relance la fonction toute les secondes 
            self.id_timer = self.after(1000,self.start_compt)
            
        else:
            self.label_show_heure.configure(text="")

            self.label_show_minute.configure(text="")
            self.label_show_seconde.configure(text="Fin")

            # Texte ajouter
            self.is_start = False
            self.btn.grid_forget()
            self.reset()
    
    # STOPER LE MINUTEUR 
    def stop_timer(self):
        if self.id_timer:
            self.after_cancel(self.id_timer)
            self.id_timer = None

    # FONCTION POUR AFFICHER LE BOUTON RENITIALISER 
    def reset(self):
        self.btn_reset = customtkinter.CTkButton(self,text="Reset",font=("Arial",15),command=self.reset_timer)
        self.btn_reset.grid(row=1,column=6,padx=(0,10),pady=(10,0))
        

    def reset_timer(self):
        self.stop_timer()
        self.show_input()
        self.label_show_heure.configure(text="")
        self.label_show_minute.configure(text="")
        self.label_show_seconde.configure(text="")
        self.heure.delete(0,'end')
        self.minute.delete(0,'end')
        self.btn.configure(text="Démarrer")
        #  sert a verifier si un objet btn reset possède un attribut donc existe 
        if hasattr(self,'btn_reset'):
            self.btn_reset.grid_forget()
            del self.btn_reset
        
        self.is_start = False
        self.is_paused=False


    # METHODE POUR EFFECTUER LA PAUSE 
    def pause(self):
        # RECUPERE ID 
        self.stop_timer()
        self.is_paused = True
        self.btn.configure(text="Relancer")
        self.reset()

    # METHODE POUR RELANCER APRES LA PAUSE 
    def resume(self):
        self.is_paused = False
        self.start_compt()
        
        self.btn.configure(text="Pause")

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