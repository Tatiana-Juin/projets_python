import customtkinter

class HorlogeFrame(customtkinter.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        self.label_heure = customtkinter.CTkLabel(self,text="texte")
        self.label_heure.grid(row=0,column=0,padx=(0,10),pady=(10,0),sticky="n")

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