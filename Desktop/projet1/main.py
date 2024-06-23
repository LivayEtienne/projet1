from comptebancaire import CompteBancaire
from compteEpargne import CompteEpargne
from compteCourant import CompteCourant
from banque import Banque

def main():

    num_compte = int(input("Veillez entrer le num du compte: "))
    titulaire = int(input("Veillez entrer le titulaire: "))
    solde = int(input("Veillez entrer le solde actuel: "))

    compte = CompteBancaire(num_compte, titulaire, solde)
    nouveau_solde = int(input("Veillez entrer le montant à ajouter: "))
    compte.ajouter_solde(nouveau_solde)
    retrait = int(input("Veillez entrer le montant a retirer: "))
    compte.retirer_argent(retrait)
    compte.consulter_solde()

    interet = float(input("Veillez entrer l'interet: "))
    compte = CompteEpargne(num_compte, titulaire, solde, interet)
    compte.afficher_interet()

    frais = int(input("Veillez entrer le montant des frais: "))
    compte = CompteCourant(num_compte, titulaire, solde, frais)
    compte.afficher_frais()

    banque = Banque()
    coord = input("Voulez vous entrer les coordonnées du propriétaire 'o' pour continuer: ")  
    while(coord == 'o'):  
            numero_compte = int(input("Veillez entrer le num du compte: "))
            nom = input("Veillez entrer le nom du propriétire: ")
            somme = int(input("Veillez entrer la somme dans le compte: "))
            compte = CompteBancaire(numero_compte, nom, somme)
            banque.ajouter_compte(compte)

            print("Information compte: ")
            banque.afficher_compte()            
            coord = input("Voulez vous entrer les coordonnées du propriétaire 'o' pour continuer: ") 
            if(coord == 'n'):
                  print(f"Saisi terminer: ")              
main()
