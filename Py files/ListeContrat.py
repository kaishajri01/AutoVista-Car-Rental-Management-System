from Contrat import Contrat
from Controle import *
from ListeClient import *
from Parc import *
from Voiture import *
from Client import *

class ListeContrat:
    
    def __init__(self,parc,listeclient):
        self.listecont=[]
        self.listevoit=parc
        self.listeclient=listeclient
    
    
    #AJOUT
    def ajout_contrat(self,cin,matr,dat,duree):
        if len(self.listecont)==0:
            nb=10000
        else:
            nb=str(int(self.listecont[len(self.listecont)-1].numero)+1)
        montant=str(int(self.listevoit[indice_matricule(matr,self.listevoit)].prix)*int(duree))
        self.listevoit[indice_matricule(matr,self.listevoit)].etat="Louée"
        c1=Contrat(cin,matr,dat,duree,0)
        c1.montant=montant
        c1.numero=str(nb)
        nb=int(nb)+1
        self.listecont.append(c1)
         
    #AFFICHE
    def affiche_contrat(self):
        for i in self.listecont:
            print(i)

    
    #SUPRESSION
    def supprimer_contrat(self,num):
            for i in range(len(self.listecont)):
                if self.listecont[i].numero==num:
                    self.listecont.pop(i)
                    return

    #MODIFICATION

    def modifier_date(self,num,nouv_date):
            self.listecont[indice_contrat(num,self.listecont)].date=nouv_date

    def modifier_duree(self,num,nouv_duree):
            self.listecont[indice_contrat(num,self.listecont)].duree=nouv_duree
    
    def modifier_payer(self,num):
            self.listecont[indice_contrat(num,self.listecont)].montant= str(int(self.listevoit[indice_matricule(self.listecont[indice_contrat(num,self.listecont)].matr,self.listevoit)].prix)*int(self.listecont[indice_contrat(num,self.listecont)].duree))
    

    #RECHERCHE
    def recherche_contrat_matr(self,matr):
        l=[]
        for i in self.listecont:
            if i.matr==matr:
                l.append(i)
        return l

    def recherche_contrat_cin(self,cin):
        l=[]
        for i in self.listecont:
            if i.cin==cin:
                l.append(i)
        return l

    def recherche_contrat_datee(self,date):
        l=[]
        for i in self.listecont:
            if i.date==date:
                l.append(i)
        return l


    def recherche_contrat_duree(self,duree):
        l=[]
        for i in self.listecont:
            if i.duree==duree:
                l.append(i)
        return l

    def recherche_contrat_date(self,d1,d2):
        l=[]
        for i in self.listecont:
            if entre_deux_date(i.date,d1,d2):
                l.append(i)
        return l


            