import customtkinter
import datetime
class HorlogeFrame(customtkinter.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        # Pour recuperer la date actuel 
        heure_date_actuel = datetime.datetime.now()
        format_date = heure_date_actuel.strftime("%d-%m-%Y  ")
        # Pour récuperer l'ehure actuel 
        format_heure = heure_date_actuel.strftime("%H:%M:%S")

        # pour afficher le texte 
        self.label_date = customtkinter.CTkLabel(self,text=format_date)
        self.label_date.grid(row=0,column=0,padx=(0,10),pady=(10,0),sticky="n")
        # pour l'heure
        self.label_heure = customtkinter.CTkLabel(self,text=format_heure)
        self.label_heure.grid(row=1,column=0,padx=(0,10),pady=(10,0))

        

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Horloge")
        self.geometry("400x400")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

        self.label_frame = HorlogeFrame(self)
        self.label_frame.grid(row=0,column=0,padx=(0,10),pady=(10,0),sticky="n")

app = App()
app.mainloop()