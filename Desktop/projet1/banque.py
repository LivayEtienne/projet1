from comptebancaire import CompteBancaire

class Banque:
    def __init__(self):
        self.compte = []

    def ajouter_compte(self, c):
        self.compte.append(c)

    def afficher_compte(self):
        if not self.compte:
              print("Pas de compte")
        else:
             for compte in self.compte:
                  print(compte)
    
    def supprimer_compte(self, compte):
         if self.compte:
              self.compte.remove(compte)
