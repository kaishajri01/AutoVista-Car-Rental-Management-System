from Client import *
from Controle import *

class ListeClient:
    def __init__(self):
        self.liste=[]

    #AJOUT
    def ajout_client(self,cin,nom,prenom,age,adresse,mail,tlf):
        c1=Client(cin,nom,prenom,age,adresse,mail,tlf)
        self.liste.append(c1)

    #AFFICHAGE
    def affiche_client(self):
        for i in self.liste:
            print(i)

    #SUPRESSION
    def suprrimer_client(self,cin):
            for i in range(len(self.liste)):
                if self.liste[i].cin==cin:
                    self.liste.pop(i)
                    return

    #MODIFIER
    def modif_adresse_client(self,cin,nouvelle_adresse):
            self.liste[indice_cin(cin,self.liste)].adresse=nouvelle_adresse

    def modif_tlf_client(self,cin,nouveau_tlf):
            self.liste[indice_cin(cin,self.liste)].tlf=nouveau_tlf

    def modif_mail_client(self,cin,nouveau_mail):
            self.liste[indice_cin(cin,self.liste)].mail=nouveau_mail

    #RECHERCHE
    def recherche_cin(self,cin):
        l=[]
        l.append(self.liste[indice_cin(cin,self.liste)])
        return l