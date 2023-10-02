
class Contrat:

    def __init__(self,cin,matr,date,duree,montant):
        self.numero=str(0)
        self.cin=cin
        self.matr=matr
        self.date=date
        self.duree=duree
        self.montant=montant
    
    def __str__(self):
        return "{} : {} | {} | {} | {} | {}$ |".format(Contrat.nb,self.cin,self.matr,self.date,self.duree,self.montant)
        
        