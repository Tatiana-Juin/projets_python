class Banque():

    # constructeur 
    def __init__(self,nom,pay):
        self.nom = nom
       
        self.pay = pay
    
    def presentation(self):
        print(f"Ma banque est {self.nom} . Il est dans le pay {self.pay}")
    

class Compte(Banque):

    def __init__(self,nom,pay,numero):
        super().__init__(nom,pay)
        self.numero = numero
    
    def presentation(self):
        super().presentation()
        print(f"Le numero du compte de la personne est {self.numero}")

compte1 = Compte(nom="Banque populaire",pay="France",numero=52536)

compte1.presentation()