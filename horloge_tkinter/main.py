import customtkinter
import datetime
from PIL import Image
class HorlogeFrame(customtkinter.CTkFrame):
    def __init__(self,master):
        super().__init__(master,fg_color="#F9F9F9")

        # Pour recuperer la date actuel 
        date_actuel = datetime.datetime.now()
        format_date = date_actuel.strftime("%d-%m-%Y  ")

        # pour afficher le texte 
        self.label_date = customtkinter.CTkLabel(self,text=format_date,font=("Arial",25))
        self.label_date.grid(row=0,column=0,padx=(0,10),pady=(10,0),sticky="n")

        # POUR AFFICHER L'HEURE
        self.label_heure = customtkinter.CTkLabel(self,text="",text_color="purple",font=("Arial",40,"bold"))
        self.label_heure.grid(row=1,column=0,padx=(0,10),pady=(10,0))

        # POUR L'IMAGE 
        my_image = customtkinter.CTkImage(Image.open("images/manette.jpg"),size=(600,300) )
        my_label = customtkinter.CTkLabel(self,text="",image=my_image)
        my_label.grid(row=2,column=0,padx=(0,10),pady=(10,0))

        self.maj_heure()

    # FONCTION POUR METTRE A JOURS L'HEURE 
    def maj_heure(self):
        heure_date_actuel = datetime.datetime.now()
        heure_actuel = heure_date_actuel.strftime("%H:%M:%S")
        
        # pour que le texte soit egale a l'ehure actuel 
        self.label_heure.configure(text=heure_actuel)
        # toute les seconde cela appelle la fonction et met a jours le texte 
        self.label_heure.after(1000,self.maj_heure)


# FENETRE PRINCIPALE 
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Horloge")
        self.geometry("700x500")
        # changer la couleur de fond 
        self.configure(fg_color="#F9F9F9")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

        # APPELLE DE Horloge Frame 
        self.label_frame = HorlogeFrame(self)
        self.label_frame.grid(row=0,column=0,padx=(0,10),pady=(10,0),sticky="n")

        # self.image_horloge = ImageApp(self)
        # self.image_horloge.grid(row=1,column=0,padx=(0,10),pady=(10,0))
    

app = App()
app.mainloop()