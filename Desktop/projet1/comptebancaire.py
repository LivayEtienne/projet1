class CompteBancaire:

    def __init__(self, num_compte, titulaire, solde):
        self.num_compte = num_compte
        self.titulaire = titulaire
        self.solde = solde
    
    def affiche(self):
        print(f"Numero_compte {self.num_compte}, Titulaire: {self.titulaire}, Solde: {self.solde}")

    def ajouter_solde(self, montant):
        if(montant <= 0):
            print(f"Montant entrer invalide")

        else:
            self.solde += montant
            print(f"Votre solde actuel apres ajout du montant de {montant} est de : {self.solde}")
    
    def retirer_argent(self, montant):
        if(self.solde < montant):
            print(f"Retrait impossible votre solde est de: {self.solde}")

        elif(montant < 0):
            print("Invalide")
        
        else:
            self.solde -= montant
            print(f"Vous avez fais une retrait de {montant}")

    def consulter_solde(self):
        print(f"Votre montant actuel est de: {self.solde}")

