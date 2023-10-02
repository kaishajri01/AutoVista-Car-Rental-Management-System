class Voiture:
    def __init__(self,matricule,marque,couleur,date,prix):
        self.matricule=matricule
        self.marque=marque
        self.couleur=couleur
        self.etat="Disponible"
        self.date=date
        self.prix=prix
    
    def __str__(self):
        return "{} : {} | {} | {} | {} | {} |".format(self.matricule,self.marque,self.couleur,self.etat,self.date,self.prix)
        
    