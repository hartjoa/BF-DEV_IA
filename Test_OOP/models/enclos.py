from models.diplodocus import Diplodocus
from models.triceratops import Triceratops
from models.spinosaure import Spinosaure
from models.iguanodon import Iguanodon
from models.t_rex import TRex
from models.velociraptor import Velociraptor

import random
import os

"""
Cette classe représente un enclos susceptible de contenir des dinosaures
"""
class Enclos:
    def __init__(self, nom, capacite = 5):
        self.nom = nom
        self.dinosaures = [] # liste des dinosaures présents dans l'enclos
        self.etat = 100      # pourcentage de résistance. Au départ à 100 (enclos neuf)
        self.jour = 0        # compteur de jours d'activité de l'enclos
        self.unites_alimentaires = 0
        self.capacite = capacite # Nombre de dinosaures max. 5 par défaut.
    
    def ajouter(self, dino: "Dinosaure") -> None:
        """
        Ajoute un dinosaure à la liste des occupants de l'enclos s'il reste de la place
        Sinon renvoie une exception
        Args:
            dino (Dinosaure): Le dinosaure à ajouter
        """
        if len(self.dinosaures) < self.capacite:
            self.dinosaures.append(dino)
        else:
            raise Exception("Impossible d'ajouter un dinosaure. L'enclos est plein")

    def retirer(self, nom: str) -> None:
        """
        Cherche si l'enclos contient un dino portant le nom donné
        Le retire de la liste et renvoie True s'il est trouvé
        Sinon renvoie False
        Args:
            nom (str): Le nom du dinosaure à supprimer
        """
        dinos = [dino for dino in self.dinosaures if dino.nom == nom]
        # liste des dinosaures de l'enclos portant ce nom (1 ou 0 élément)
        if dinos:
            self.dinosaures.remove(dinos[0])
            return True
        else:
            return False
    
    def montre_statut(self) -> None:
        """
        Affiche l'état de l'enclos
       
        """
        print(f"\n=== Statut de l'enclos '{self.nom}' ===")
        print("Nombre de jours de fonctionnement:", self.jour)
        print("Etat de solidité:", self.etat, "%")
        print("Nombre d'unités alimentaires dans la mangeoire:", self.unites_alimentaires)
        print(f"Nombre de dinosaures: {len(self.dinosaures)}/{self.capacite}")
        for dino in self.dinosaures:
            print(dino)
        
    def ajouter_nourriture(self, unites: int) -> None:
        """
        Ajoute la quantité spécifiée d'unités alimentaires à la mangeoire de l'enclos

        Args:
            unites (int): nombre d'unités
        """
        self.unites_alimentaires += unites
    
    def reparer(self) -> None:
        """
        Augmente de 10 % l'état de solidité de l'enclos
        """
        if self.etat == 100:
            print("Aucune réparation nécessaire")
        else:
            print("Etat de solidité avant réparation:", self.etat, "%")
            self.etat += 10 if self.etat < 90 else 100
            print("Etat de solidité après réparation:", self.etat, "%")
        
    def jour_passe(self) -> None:
        """
        Simule une journée dans l'enclos:
        """
        # En début de journée, la faim de tous les dinos augmente
        for dino in self.dinosaures:
            dino.faim += 15 if dino.faim < 85 else 100
        
        # Les dinos se nourrissent
        for dino in self.dinosaures:
            if dino.faim > 30:
                print(f"{dino.nom} a faim!")
                if self.unites_alimentaires > 0:
                    quantite = self.unites_alimentaires // len(self.dinosaures)
                    if quantite < 1:
                        quantite = self.unites_alimentaires
                    dino.mange(quantite)
                    self.unites_alimentaires -= quantite
                else:
                    print("Alerte! Plus rien à manger!")

        # Les dinos ont des comportements en fonction de leur stress:
        # (stress < 20 : aucun comportement)
        for dino in [dino for dino in self.dinosaures if 20 < dino.stress <= 30]:
            # stress entre 20 et 30: détruire l'enclos
            dino.detruire()
            self.etat -= 20 if self.etat > 20 else 0

        for dino in [dino for dino in self.dinosaures if 30 < dino.stress <= 80]:
            # stress entre 30 et 80: attaquer un autre dinosaure
            proie = random.choice([proie for proie in self.dinosaures if proie != dino])
            dino.attaque(proie)
                
        for dino in [dino for dino in self.dinosaures if dino.stress > 80]:
            # stress supérieur à 80: fuir
            if dino.fuir(self.etat):
                print(f"Alerte!! Un dinosaure s'est échappé, c'est {dino.nom}")
                self.dinosaures.remove(dino)
                
        # En fin de journée, le stress de tous les dinos augmente
        for dino in self.dinosaures:
            dino.stress += 10 if dino.stress < 90 else 100
        
        # le compteur de jours est augmenté
        self.jour += 1

    def menu(self) -> None:
        """
        Propose un menu d'options d'actions relatives à cet enclos.
        Reçois une commande de l'utilisateur et exécute l'action correspondante
        """
        stop = False
        while not stop:
            os.system('cls' if os.name=='nt' else 'clear')
            print(f"Options valides pour l'enclos '{self.nom}'")
            print("[1] - Voir le statut de l'enclos")
            print("[2] - Réparer l'enclos")
            print("[3] - Ajouter nourriture")
            print("[4] - Ajouter dinosaure")
            print("[5] - Supprimer dinosaure")
            print("[6] - Simuler passage d'un jour")
            print("[7] - Quitter ce menu")
            
            choix = None
            while not choix:
                try:
                    choix = int(input("Option choisie: "))
                    if choix < 1 or choix > 7:
                        print("Choisissez une option entre 1 et 7")
                except ValueError:
                    print("Veuillez entrer un nombre entier uniquement")
            
            os.system('cls' if os.name=='nt' else 'clear')
            match choix:
                case 1:
                    self.montre_statut()
                case 2:
                    self.reparer()
                case 3:
                    quantite = None
                    while not quantite:
                        try:
                            quantite = int(input("Combien d'unités de nourriture voulez-vous ajouter? "))
                            if quantite < 0:
                                print("Veuillez entrer un nombre positif")
                        except ValueError:
                            print("Veuillez entrer un nombre entier uniquement")
                    self.ajouter_nourriture(quantite)
                case 4:
                    nom = input("Nom du dinosaure à ajouter? ")
                    age = None
                    while not age:
                        try:
                            age = int(input("Age du dinosaure? "))
                            if age < 0:
                                print("Veuillez entrer un nombre positif")
                        except ValueError:
                            print("Veuillez entrer un nombre entier uniquement")
                    os.system('cls' if os.name=='nt' else 'clear')
                    print("Espèces de dinosaures:")
                    print("[1] - Diplodocus (H)")
                    print("[2] - Iguanodon (H)")
                    print("[3] - Tricératops (H)")
                    print("[4] - T-Rex (C)")
                    print("[5] - Spinosaure (C)")
                    print("[6] - Velociraptor (C)")
                    id_espece = None
                    while not id_espece or id_espece < 1 or id_espece > 6:
                        try:
                            id_espece = int(input("Espèce du dinosaure? "))
                            if id_espece < 1 or id_espece > 6:
                                print("Veuillez entrer un nombre entre 1 et 6")
                        except ValueError:
                            print("Veuillez entrer un nombre entier uniquement")

                    match id_espece:
                        case 1:
                            espece = Diplodocus
                        case 2:
                            espece = Iguanodon
                        case 3:
                            espece = Triceratops
                        case 4:
                            espece = TRex
                        case 5:
                            espece = Spinosaure
                        case 6:
                            espece = Velociraptor
                    self.ajouter(espece(nom, age))
                case 5:
                    nom = input("Nom du dinosaure à supprimer? ")
                    if self.retirer(nom):
                        print(f"{nom} a bien été retiré de l'enclos")
                    else:
                        print(f"Aucun dinosaure appelé {nom} dans l'enclos")
                case 6:
                    print("Un jour passe...")
                    self.jour_passe()
                case 7:
                    print("Fin de gestion de l'enclos.")
                    stop = True
            
            print("\nPressez [Enter] pour retourner au menu de l'enclos")
            _ = input()


