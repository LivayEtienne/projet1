from comptebancaire import CompteBancaire

class CompteEpargne(CompteBancaire):
    def __init__(self, num_compte, titulaire, solde, taux_interets):
        super().__init__(num_compte, titulaire, solde)
        self.taux_interets = taux_interets

    def calcul_interet(self):
        interet = self.solde * (self.taux_interets/100)
        return interet
    def afficher_interet(self):
        interet = self.calcul_interet()
        self.solde += interet
        print(f"Solde avec interet {self.solde}")