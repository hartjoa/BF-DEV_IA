from abc import abstractmethod
from models.aquatic_organism import AquaticOrganism
import random

class Fish(AquaticOrganism):
    def __init__(self, name, gender):
        super().__init__()
        self.name = name
        self.gender = "F" if gender and gender[0].upper() == "F" else "M"
    
    @abstractmethod
    def eat(self, food):
        pass

    def mate(self, other):
        print(f"*** {self.name} is trying to mate with {other.name}")
        if type(self) == type(other) and self.gender != other.gender:
            print("*** A baby fish is born! Welcome to:")
            baby_fish = type(self)(f"baby-{random.randint(1, 1_000_000)}", "M" if random.random() < .5 else "F")
            print(baby_fish)
            return baby_fish
        else:
            print("*** Hmm... Didn't work this time...")
            return None