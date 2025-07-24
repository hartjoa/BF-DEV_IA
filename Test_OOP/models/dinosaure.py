import random

class Dinosaure():
    def __init__(self, nom, age, sante = 80, stress = 30, faim = 0):
        self.nom = nom    # nom du dino (uique pour chaque occupant du parc)
        self.age = age    # age du dino
        self.sante = sante # pourcentage de sante. 80% par défaut
        self.stress = stress # niveau de stress. 30% par défaut
        self.faim = faim  # niveau de faim. 0% par défaut

    def mange(self, unites: int):
        print(f"{self.nom} mange {unites} unité(s) de nourriture")
        self.faim -= unites * 5
        if self.faim < 0:
            # La faim doit restze comprise entre 0 et 100
            self.faim = 0

    def attaque(self, autre: "Dinosaure"):
        print(f"{self.nom} veut attaquer {autre.nom}")
        succes = False   # Flag de succès de l'attaque
        if isinstance(self, Carnivore):
            # L'attaquant est un carnivore
            if isinstance(autre, Herbivore):
                # Carnivore vs Herbivore: l'attaque réussit toujours
                succes = True
            elif isinstance(autre, Carnivore):
                # Carnivore vs Carnivore: l'attaque réussit si la santé de l'attaquant
                # est supérieure au stress de l'attaqué
                succes = self.sante > autre.stress
        elif isinstance(self, Herbivore):
            # L'attaquant est un herbivore
            if isinstance(autre, Herbivore):
                # Herbivore vs Herbivore: l'attaque réussit une fois sur deux
                succes = random.random() < .5
            elif isinstance(autre, Carnivore):
                # Herbivore vs Carnivore: l'attaque rate toujours
                succes = False
        if success:
            # Succès de l'attaque
            print("L'attaque a réussi")
            # Le niveau de stress de l'attaquant diminue
            self.stress -= 20 if self.stress > 20 else 0
            # Le niveau de stress de l'attaqué augmente
            autre.stress += 30 if autre.stress < 70 else 100
            # Le niveau de santé de l'attaqué diminue
            autre.sante -= 25 if autre.sante > 25 else 0
        else:
            print("L'attaque n'a pas réussi")
            

            
    def fuir(self, etat_enclos: int) -> bool:
        """
        Tentative de fuite d'un dinosaure. Renvoie un booléen spécifiant si la fuite 
        a réussi ou pas

        Args:
            etat_enclos (int): etat de solidité de l'enclos

        Returns:
            bool: True si la fuite réussit, sinon False
        """
        print(f"{self.nom} essaie de fuir")
        if etat_enclos < 40:
            # enclos en mauvais etat: la fuite réussit
            return True
        print("L'enclos est en trop bon état...")
        return False

    def detruire(self):
        print(f"{self.nom} sacage sa cage!")
        self.stress -= 20 if self.stress > 20 else 0

    def __str__(self) -> str:
        """
        Renvoie un string reprenant touds les éléments sur l'état du dinosaure
        Returns:
            str: Etat du dino
        """
        return f"{self.nom} ({self.age} ans): {self.__class__.__name__}. Santé: {self.sante}%, Stress: {self.stress}%, Faim: {self.faim}%"