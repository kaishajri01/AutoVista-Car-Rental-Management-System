class Client:
    def __init__(self,cin,nom,prenom,age,adresse,mail,tlf):
        self.cin=cin
        self.nom=nom
        self.prenom=prenom
        self.age=age
        self.adresse=adresse
        self.mail=mail
        self.tlf=tlf
    def __str__(self):
        return "{} : {} | {} | {} | {} | {} | {} |".format(self.cin,self.nom,self.prenom,self.age,self.adresse,self.mail,self.tlf)
        