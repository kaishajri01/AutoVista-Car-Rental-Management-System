from ListeContrat import *
from Parc import *
from ListeClient import *


class Agence:
    def __init__(self):
        self.ListeClient=ListeClient()
        self.Parc=Parc()
        self.ListeContrat=ListeContrat(self.Parc.parc,self.ListeClient.liste)
