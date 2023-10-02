
from Voiture import *
from Controle import *

class Parc:
    def __init__(self):
        self.parc=[]
    
    #AJOUT
    def ajout_voiture(self,matr,marq,coul,achat,prix):
        p1=Voiture(matr,marq,coul,achat,prix)
        self.parc.append(p1)


    #AFFICHAGE  
    def affiche_voiture(self):
        for i in self.parc:
            print(i)

    #SUPRESSION
    def supprimer_mat(self,mat):
            for i in range(len(self.parc)):
                if self.parc[i].matricule==mat:
                    self.parc.pop(i)
                    return

    def supprimer_marq(self,marq):
        i=0
        j=len(self.parc)
        while i<j:
            if self.parc[i].marque==marq:
                self.parc.pop(i)
                j=len(self.parc)
                i=0
            else:
                i+=1

    def supprimer_agee(self):
        i=0
        j=len(self.parc)
        while i<j:
            if int(age_voit(self.parc[i].date))>3650:
                self.parc.pop(i)
                j=len(self.parc)
                i=0
            else:
                i+=1

    #MODIFICATION
    def modif_prix_voit(self,matr,nouveau_prix):
            self.parc[indice_matricule(matr,self.parc)].prix=nouveau_prix

    def modif_couleur_voit(self,matr,nouveau_couleur):
            self.parc[indice_matricule(matr,self.parc)].couleur=nouveau_couleur

    #AFFICHAGE
    def afficher(self):
        if len(self.parc)==0:
            print("Le Garage est Vide !")
        else:
            for i in self.parc:
                print(i)

    #RECHERCHE
    def recherche_matr(self,matr):
            l=[]
            l.append(self.parc[indice_matricule(matr,self.parc)])
            return l

    def recherche_marq(self,marq):
        l=[]
        for i in self.parc:
            if i.marque==marq:
                l.append(i)
        return l


    def recherche_coul(self,coul):
        l=[]
        for i in self.parc:
            if i.couleur==coul:
                l.append(i)
        return l


    def recherche_dispo(self):
        l=[]
        for i in self.parc:
            if i.etat=="Disponible":
                l.append(i)
        return l


    def recherche_louee(self):
        l=[]
        for i in self.parc:
            if i.etat=="Louée":
                l.append(i)
        return l
 

    def recherche_louee_entre_date(self,d1,d2):
        l=[]
        for i in self.parc:
            if entre_deux_date(i.date,d1,d2):
                l.append(i)
        return l
 