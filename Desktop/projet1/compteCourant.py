from comptebancaire import CompteBancaire

class CompteCourant(CompteBancaire):
    def __init__(self, num_compte, titulaire, solde, frais):
        super().__init__(num_compte, titulaire, solde)
        self.frais = frais

    def calcul_frais(self):
        if self.solde < self.frais:
            print(f"Solde est insuffisant pour en deduire frais: {self.solde}")
        else:
            self.solde -= self.frais
            print(f"Vous avez une frais de {self.frais} reste {self.solde}")

    def afficher_frais(self):
        print(f"frais: {self.frais}, solde restant: {self.solde}")
