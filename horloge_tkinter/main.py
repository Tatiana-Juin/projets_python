import customtkinter
import datetime
class HorlogeFrame(customtkinter.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        # Pour recuperer la date actuel 
        date_actuel = datetime.datetime.now()
        format_date = date_actuel.strftime("%d-%m-%Y  ")

        # pour afficher le texte 
        self.label_date = customtkinter.CTkLabel(self,text=format_date)
        self.label_date.grid(row=0,column=0,padx=(0,10),pady=(10,0),sticky="n")

        # POUR AFFICHER L'HEURE
        self.label_heure = customtkinter.CTkLabel(self,text="")
        self.label_heure.grid(row=1,column=0,padx=(0,10),pady=(10,0))

        self.maj_heure()
    
    # FONCTION POUR METTRE A JOURS L'HEURE 
    def maj_heure(self):
        heure_date_actuel = datetime.datetime.now()
        heure_actuel = heure_date_actuel.strftime("%H:%M:%S")
        # pour que le texte soit egale a l'ehure actuel 
        self.label_heure.configure(text=heure_actuel)
        # toute les seconde cela appelle la fonction et met a jours le texte 
        self.label_heure.after(1000,self.maj_heure)
        
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Horloge")
        self.geometry("400x400")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        
        # APPELLE DE Horloge Frame 
        self.label_frame = HorlogeFrame(self)
        self.label_frame.grid(row=0,column=0,padx=(0,10),pady=(10,0),sticky="n")
    

app = App()
app.mainloop()