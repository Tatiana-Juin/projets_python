import customtkinter
import time

class MinuteurFrame(customtkinter.CTkFrame):
     def __init__(self,master):
        super().__init__(master)


# FENETRE PRINCIPALE 
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.title("Horloge")
        self.geometry("700x500")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)


app =App()
app.mainloop()